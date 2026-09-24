import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec = importlib.util.spec_from_file_location('build_light', Path(__file__).resolve().parents[1] / 'dev-tools/build_light.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class LightReleaseTests(unittest.TestCase):
    def test_release_without_foundry_preserves_text_and_matches_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            module_id = 'translate-dnd5e-tomb-annihilation-es'
            old = f'modules/{module_id}/assets/map.jpg'
            original = 'modules/dnd-tomb-annihilation/assets/map.webp'
            files = {
                'module.json': {'id': module_id, 'version': '0.2.0', 'title': 'Test', 'esmodules': ['scripts/main.js']},
                'compendium/test.json': {'src': old, 'text': 'Texto español @UUID[Actor.example]'},
                'dev-tools/translation/handout-assets.json': {'assets': [{'translation': old, 'source': original}]},
                'dev-tools/translation/atlas-assets.json': {'assets': []},
            }
            for name, value in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(value), encoding='utf-8')
            (root / 'scripts').mkdir()
            (root / 'scripts/main.js').write_text('// test', encoding='utf-8')
            tracked = '\0'.join([*files, 'scripts/main.js', 'assets/map.jpg']).encode()
            with patch.object(builder, 'ROOT', root), patch.object(builder.subprocess, 'check_output', return_value=tracked):
                with self.assertRaises(ValueError):
                    builder.build(release_tag='v9.0.0')
                builder.build(release_tag='v0.2.0')
            manifest = (root / 'dist/module.json').read_bytes()
            with zipfile.ZipFile(root / f'dist/{module_id}.zip') as archive:
                self.assertEqual(archive.read(f'{module_id}/module.json'), manifest)
                self.assertFalse(any('/assets/' in name for name in archive.namelist()))
                pack = json.loads(archive.read(f'{module_id}/compendium/test.json'))
                self.assertEqual(pack, {'src': original, 'text': files['compendium/test.json']['text']})
            self.assertTrue(json.loads(manifest)['download'].endswith(f'/v0.2.0/{module_id}.zip'))


if __name__ == '__main__':
    unittest.main()
