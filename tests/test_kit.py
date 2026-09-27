"""Offline integrity checks for the distributed kit, not external integrations."""
from pathlib import Path
import hashlib
import json
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class KitTests(unittest.TestCase):
    def test_skills_same_in_both_clients_and_manifest(self):
        manifest = json.loads((ROOT / 'skills/manifest.json').read_text(encoding='utf-8-sig'))
        self.assertEqual(len(manifest), 4)
        for name, digest in manifest.items():
            source = (ROOT / 'skills' / name / 'SKILL.md').read_bytes()
            self.assertEqual(hashlib.sha256(source).hexdigest(), digest)
            for client in ('.agents', '.claude'):
                self.assertEqual(source, (ROOT / client / 'skills' / name / 'SKILL.md').read_bytes())
            text = source.decode('utf-8')
            self.assertTrue(text.startswith('---\nname: ' + name + '\n'))
            self.assertRegex(text, r'(?m)^description: .+')

    def test_markdown_relative_links_exist(self):
        for path in ROOT.rglob('*.md'):
            if any(part in ('local', '.git') for part in path.relative_to(ROOT).parts):
                continue
            text = re.sub(r'```.*?```', '', path.read_text(encoding='utf-8'), flags=re.S)
            for match in re.finditer(r'\[[^\]]+\]\(([^)]+)\)', text):
                target = match.group(1).split('#')[0]
                if not target or '://' in target or target.startswith('mailto:'):
                    continue
                target = unquote(target.strip('<>'))
                self.assertTrue((path.parent / target).exists(), f'{path.relative_to(ROOT)} -> {target}')

    def test_vault_seed_links_resolve(self):
        notes = {p.stem for p in (ROOT / 'vault-template').glob('*.md')}
        self.assertEqual(len(notes), 7)
        for path in (ROOT / 'vault-template').glob('*.md'):
            for target in re.findall(r'\[\[([^\]|#]+)', path.read_text(encoding='utf-8')):
                self.assertIn(target, notes)

    def test_entrypoints_available_without_accounts(self):
        for name in ('README.md', 'AGENTS.md', 'CLAUDE.md', 'INICIO-IA.md', 'EMPEZA-AQUI.md'):
            self.assertGreater((ROOT / name).stat().st_size, 150)
        self.assertIn('/local/', (ROOT / '.gitignore').read_text())


if __name__ == '__main__':
    unittest.main()
