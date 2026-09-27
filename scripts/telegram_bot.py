#!/usr/bin/env python3
"""Bot personal mínimo. Python >=3.10, biblioteca estándar, sin motor de IA."""
from __future__ import annotations

import argparse
import getpass
import json
import mimetypes
import os
from pathlib import Path
import re
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from contextlib import contextmanager

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / "local" / "telegram"


class BotError(Exception):
    """Error deliberadamente seguro para mostrar: nunca incluye URL ni token."""


class API:
    def __init__(self, token: str):
        if not re.fullmatch(r"[0-9]+:[A-Za-z0-9_-]+", token):
            raise BotError("El token no tiene el formato esperado. Revisalo en BotFather.")
        self._token = token

    def call(self, method, fields=None, file=None, timeout=40):
        fields = fields or {}
        if file is None:
            body = urllib.parse.urlencode(fields).encode()
            content_type = "application/x-www-form-urlencoded"
        else:
            body, content_type = multipart(fields, file)
        request = urllib.request.Request(
            "https://api.telegram.org/bot" + self._token + "/" + method,
            data=body, headers={"Content-Type": content_type}, method="POST",
        )
        # Una sola solicitud: un timeout durante sendMessage/sendDocument puede
        # ocurrir DESPUÉS del envío. No reintentamos automáticamente.
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = json.loads(response.read())
        except urllib.error.HTTPError as exc:
            if exc.code == 409:
                raise BotError("Conflicto 409: hay otro lector o un webhook. Detené el otro proceso; no se cambió la configuración.") from None
            raise BotError(f"Telegram rechazó la solicitud (HTTP {exc.code}). No se reintentó.") from None
        except (OSError, ValueError):
            raise BotError("No se pudo confirmar la respuesta. Si estabas enviando, mirá el chat antes de repetir: podría haberse enviado. No se reintentó.") from None
        if not isinstance(data, dict) or data.get("ok") is not True:
            raise BotError("Telegram no confirmó la operación. No se reintentó.")
        return data["result"]


def multipart(fields, path):
    path = Path(path)
    if not path.is_file():
        raise BotError("El archivo no existe o no es un archivo regular.")
    # Límite deliberado del ejemplo, no una promesa sobre el máximo de Telegram.
    if path.stat().st_size > 20 * 1024 * 1024:
        raise BotError("Este ejemplo admite archivos de hasta 20 MiB. Para un video grande, enviá un enlace revisado.")
    boundary = "naiara_" + secrets.token_hex(16)
    parts = []
    for key, value in fields.items():
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n'.encode())
    # Filename ASCII seguro; el archivo conserva su contenido original.
    filename = re.sub(r'[^A-Za-z0-9._-]', '_', path.name) or "archivo"
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="document"; filename="{filename}"\r\nContent-Type: {mime}\r\n\r\n'.encode())
    parts.extend([path.read_bytes(), f'\r\n--{boundary}--\r\n'.encode()])
    return b"".join(parts), "multipart/form-data; boundary=" + boundary


def save_state(directory, state):
    directory.mkdir(parents=True, exist_ok=True)
    temporary = directory / "state.tmp"
    temporary.write_text(json.dumps(state, indent=2), encoding="utf-8")
    temporary.replace(directory / "state.json")


def read_state(directory):
    try:
        state = json.loads((directory / "state.json").read_text(encoding="utf-8"))
        if not all(type(state.get(k)) is int for k in ("chat_id", "bot_id", "offset")) or state["chat_id"] <= 0:
            raise ValueError()
        return state
    except (OSError, ValueError):
        raise BotError("No hay un emparejamiento válido. Ejecutá primero pair.") from None


@contextmanager
def local_lock(directory):
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "running.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise BotError("Ya hay una ejecución local o quedó running.lock. Cerrá las otras ventanas. Sólo si no hay un proceso activo, borrá local/telegram/running.lock.") from None
    try:
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
        yield
    finally:
        path.unlink(missing_ok=True)


def check_polling(api):
    if api.call("getWebhookInfo").get("url"):
        raise BotError("Este bot ya tiene un webhook. No lo modificamos. Usá un bot nuevo o consultá a quien administra el existente.")


def identity(api):
    me = api.call("getMe")
    if not me.get("is_bot") or type(me.get("id")) is not int:
        raise BotError("La identidad recibida no corresponde a un bot válido.")
    return me


def private_message(update, chat_id=None):
    message = update.get("message", {})
    chat = message.get("chat", {})
    sender = message.get("from", {})
    if chat.get("type") != "private" or sender.get("is_bot") or sender.get("id") != chat.get("id"):
        return None
    if type(chat.get("id")) is not int or chat["id"] <= 0:
        return None
    if chat_id is not None and chat["id"] != chat_id:
        return None
    return message


def pair(api, directory, seconds=120, code=None):
    if (directory / "state.json").exists():
        raise BotError("Ya existe un emparejamiento. No se sobrescribió. Revisá la guía para cambiar de cuenta.")
    me = identity(api)
    check_polling(api)
    code = code or secrets.token_hex(8)
    phrase = "/vincular " + code
    print(f"Abrí el chat privado de @{me.get('username', '(ver BotFather)')} y enviá exactamente:\n{phrase}\nNo compartas este código. Esperando hasta {seconds} segundos...")
    deadline = time.monotonic() + seconds
    offset = 0
    while time.monotonic() < deadline:
        timeout = min(20, max(1, int(deadline - time.monotonic())))
        updates = api.call("getUpdates", {"offset": offset, "timeout": timeout, "allowed_updates": '["message"]'}, timeout=timeout + 10)
        for update in updates:
            offset = max(offset, update["update_id"] + 1)
            message = private_message(update)
            if message and message.get("text", "").strip() == phrase:
                state = {"chat_id": message["chat"]["id"], "bot_id": me["id"], "offset": offset}
                save_state(directory, state)
                print("Vinculación guardada localmente. No se guardó el token.")
                return state
    raise BotError("Se agotó el tiempo sin recibir tu código. Podés ejecutar pair de nuevo; generará otro código.")


def checked_state(api, directory):
    state = read_state(directory)
    if identity(api)["id"] != state["bot_id"]:
        raise BotError("El token corresponde a otro bot. Usá el token del bot emparejado.")
    return state


def send(api, directory, text=None, file=None):
    state = checked_state(api, directory)
    if file is None:
        if not text or len(text) > 4000:
            raise BotError("El texto debe contener entre 1 y 4000 caracteres.")
        result = api.call("sendMessage", {"chat_id": state["chat_id"], "text": text})
    else:
        result = api.call("sendDocument", {"chat_id": state["chat_id"]}, file=file, timeout=90)
    print(f"Telegram confirmó el envío. ID del mensaje: {result.get('message_id')}. No confirma lectura.")
    return result


def inbox(api, directory, seconds=60):
    state = checked_state(api, directory)
    check_polling(api)
    journal = directory / "inbox.jsonl"
    seen = set()
    if journal.exists():
        for line in journal.read_text(encoding="utf-8").splitlines():
            if line.strip():
                seen.add(json.loads(line)["update_id"])
    deadline = time.monotonic() + seconds
    print(f"Buzón activo hasta {seconds} segundos. Ctrl+C para terminar. No se ejecutan instrucciones recibidas.")
    while time.monotonic() < deadline:
        timeout = min(20, max(1, int(deadline - time.monotonic())))
        updates = api.call("getUpdates", {"offset": state["offset"], "timeout": timeout, "allowed_updates": '["message"]'}, timeout=timeout + 10)
        for update in updates:
            uid = update["update_id"]
            message = private_message(update, state["chat_id"])
            if message and isinstance(message.get("text"), str) and uid not in seen:
                text = message["text"]
                kind = "ayuda" if text == "/ayuda" else "estado" if text == "/estado" else "idea" if text.startswith("/idea ") else "nota"
                record = {"update_id": uid, "date": message.get("date"), "kind": kind, "text": text}
                with journal.open("a", encoding="utf-8") as output:
                    output.write(json.dumps(record, ensure_ascii=False) + "\n")
                    output.flush()
                    os.fsync(output.fileno())
                seen.add(uid)
                if kind == "ayuda":
                    print("/idea texto: guarda una idea; /estado: informa aquí; cualquier otro texto: nota. No hay respuestas automáticas en Telegram.")
                elif kind == "estado":
                    print("Buzón local activo. Sin motor de IA ni publicaciones automáticas.")
                else:
                    print("Idea o nota guardada en local/telegram/inbox.jsonl.")
            state["offset"] = max(state["offset"], uid + 1)
            save_state(directory, state)
    print("Buzón detenido.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("identify", help="Verificar el bot sin guardar token")
    sub.add_parser("pair", help="Vincular tu chat privado con código aleatorio")
    sub.add_parser("send-text").add_argument("text")
    sub.add_parser("send-file").add_argument("file", type=Path)
    receive = sub.add_parser("inbox")
    receive.add_argument("--seconds", type=int, default=60, choices=range(1, 301), metavar="1..300")
    args = parser.parse_args(argv)
    try:
        token = os.environ.get("NAIARA_TELEGRAM_TOKEN")
        if not token:
            if not sys.stdin.isatty():
                raise BotError("Abrí una terminal interactiva para pegar el token de forma oculta. No lo pases como argumento.")
            token = getpass.getpass("Token de BotFather (oculto; no se guarda): ")
        api = API(token.strip())
        with local_lock(LOCAL):
            if args.command == "identify":
                me = identity(api)
                print(f"Bot verificado: @{me.get('username')} (ID {me['id']}).")
            elif args.command == "pair":
                pair(api, LOCAL)
            elif args.command == "send-text":
                send(api, LOCAL, text=args.text)
            elif args.command == "send-file":
                send(api, LOCAL, file=args.file)
            else:
                inbox(api, LOCAL, seconds=args.seconds)
        return 0
    except KeyboardInterrupt:
        print("\nDetenido. Si interrumpiste un envío, comprobá el chat antes de repetir.")
        return 130
    except BotError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError):
        print("Error local o respuesta inesperada. No se muestran detalles sensibles. Revisá archivos y conexión antes de repetir.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
