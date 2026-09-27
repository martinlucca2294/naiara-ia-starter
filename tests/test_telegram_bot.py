"""Pruebas sin red ni credenciales reales: python -m unittest discover -s tests."""
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
import urllib.error

SPEC = importlib.util.spec_from_file_location("telegram_bot", Path(__file__).resolve().parents[1] / "scripts" / "telegram_bot.py")
bot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bot)


def update(uid, chat=123, text="hola", kind="private"):
    return {"update_id": uid, "message": {"chat": {"id": chat, "type": kind}, "from": {"id": chat, "is_bot": False}, "text": text, "date": 123456}}


class TelegramTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.state = {"chat_id": 123, "bot_id": 99, "offset": 0}
        self.me = {"id": 99, "is_bot": True, "username": "example_bot"}

    def tearDown(self):
        self.temp.cleanup()

    def test_wrong_chat_and_group_ignored(self):
        self.assertIsNone(bot.private_message(update(1, 456), 123))
        self.assertIsNone(bot.private_message(update(1, 123, kind="group"), 123))
        self.assertIsNotNone(bot.private_message(update(1), 123))

    def test_pair_requires_exact_code(self):
        api = Mock()
        api.call.side_effect = [self.me, {}, [update(1, 456, "/start"), update(2, 456, "/vincular wrong"), update(3, 123, "/vincular secretcode")]]
        with patch.object(bot.time, "monotonic", side_effect=[0, 1, 2]), patch("sys.stdout", new=io.StringIO()):
            result = bot.pair(api, self.directory, code="secretcode")
        self.assertEqual(result["chat_id"], 123)
        self.assertEqual(result["offset"], 4)
        self.assertNotIn("secretcode", (self.directory / "state.json").read_text())

    def test_pair_refuses_overwrite(self):
        bot.save_state(self.directory, self.state)
        api = Mock()
        with self.assertRaises(bot.BotError):
            bot.pair(api, self.directory)
        api.call.assert_not_called()

    def test_webhook_never_deleted(self):
        api = Mock()
        api.call.return_value = {"url": "https://example.test/existing"}
        with self.assertRaises(bot.BotError):
            bot.check_polling(api)
        api.call.assert_called_once_with("getWebhookInfo")

    def test_network_error_redacted_and_no_retry(self):
        token = "123:TEST_SECRET"
        api = bot.API(token)
        with patch.object(bot.urllib.request, "urlopen", side_effect=OSError("https://api.telegram.org/bot" + token)) as http:
            with self.assertRaises(bot.BotError) as caught:
                api.call("sendMessage", {"chat_id": 123, "text": "hola"})
        self.assertNotIn(token, str(caught.exception))
        self.assertNotIn("https://", str(caught.exception))
        http.assert_called_once()

    def test_conflict_redacted(self):
        error = urllib.error.HTTPError("secret-token-url", 409, "secret", {}, None)
        with patch.object(bot.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(bot.BotError) as caught:
                bot.API("123:fake").call("getUpdates")
        self.assertIn("409", str(caught.exception))
        self.assertNotIn("secret", str(caught.exception))

    def test_multipart_preserves_bytes(self):
        path = self.directory / 'foto .jpg'
        original = b"\xff\xd8\x00photo\xff\xd9"
        path.write_bytes(original)
        body, content_type = bot.multipart({"chat_id": 123}, path)
        self.assertIn(original, body)
        self.assertIn(b'name="document"; filename="foto_.jpg"', body)
        self.assertIn(b"Content-Type: image/jpeg", body)
        self.assertTrue(body.endswith(("--" + content_type.split("boundary=")[1] + "--\r\n").encode()))

    def test_send_only_registered_chat(self):
        bot.save_state(self.directory, self.state)
        api = Mock()
        api.call.side_effect = [self.me, {"message_id": 7}]
        with patch("sys.stdout", new=io.StringIO()):
            bot.send(api, self.directory, text="hola")
        self.assertEqual(api.call.call_args.args, ("sendMessage", {"chat_id": 123, "text": "hola"}))

    def test_wrong_bot_cannot_send(self):
        bot.save_state(self.directory, self.state)
        api = Mock()
        api.call.return_value = {"id": 88, "is_bot": True}
        with self.assertRaises(bot.BotError):
            bot.send(api, self.directory, text="hola")
        self.assertEqual(api.call.call_count, 1)

    def test_inbox_allowlist_and_dedup_without_outbound_messages(self):
        bot.save_state(self.directory, self.state)
        api = Mock()
        api.call.side_effect = [self.me, {}, [update(1, 456, "malicioso"), update(2, 123, "/idea una campaña"), update(2, 123, "/idea una campaña")]]
        with patch.object(bot.time, "monotonic", side_effect=[0, 1, 2, 99]), patch("sys.stdout", new=io.StringIO()):
            bot.inbox(api, self.directory, seconds=5)
        lines = (self.directory / "inbox.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0])["kind"], "idea")
        self.assertEqual(bot.read_state(self.directory)["offset"], 3)
        self.assertFalse(any(call.args[0].startswith("send") for call in api.call.call_args_list))

    def test_second_local_process_refused(self):
        with bot.local_lock(self.directory):
            with self.assertRaises(bot.BotError):
                with bot.local_lock(self.directory):
                    self.fail("No debería entrar")
        self.assertFalse((self.directory / "running.lock").exists())

    def test_no_token_in_argv(self):
        with patch("sys.stderr", new=io.StringIO()):
            with self.assertRaises(SystemExit):
                bot.main(["identify", "--token", "123:fake"])


if __name__ == "__main__":
    unittest.main()
