"""Checks of the text-only profile against disposable commits."""
import json
import zipfile
import test_build_release as contract


class LightReleaseTests(contract.BuildReleaseTests):
    def configure_light(self):
        old = f"modules/{contract.MODULE_ID}/assets/map.jpg"
        source = "modules/dnd-tomb-annihilation/assets/map.webp"
        self.meta["title"] = "Test"
        self.write_json("module.json", self.meta)
        self.write_json("dev-tools/buildScripts/release-profile.json", {"variant": "text-only"})
        self.write_json("dev-tools/translation/handout-assets.json", {"assets": [{"translation": old, "source": source}]})
        self.write_json("dev-tools/translation/atlas-assets.json", {"assets": []})
        self.write_json("compendium/items.json", {"src": old, "text": "Texto @UUID[Actor.example]"})
        self.initial = self.commit()
        return old, source

    def test_light_uses_committed_mapping_and_preserves_text(self):
        old, source = self.configure_light()
        self.write_json("dev-tools/translation/handout-assets.json", {"assets": []})
        self.success("--allow-dirty", "--ref", self.initial)
        output = self.root / "dist"
        with zipfile.ZipFile(output / (contract.MODULE_ID + ".zip")) as archive:
            self.assertEqual(json.loads(archive.read(contract.MODULE_ID + "/compendium/items.json")),
                             {"src": source, "text": "Texto @UUID[Actor.example]"})
            manifest = archive.read(contract.MODULE_ID + "/module.json")
            self.assertEqual(manifest, (output / "module.json").read_bytes())
            self.assertTrue(json.loads(manifest)["title"].endswith("Solo texto"))
            self.assertIn(contract.MODULE_ID + "/README.en.md", archive.namelist())
            self.assertIn(contract.MODULE_ID + "/LICENSE.md", archive.namelist())
        first = (output / (contract.MODULE_ID + ".zip")).read_bytes()
        self.success("--allow-dirty", "--ref", self.initial)
        self.assertEqual(first, (output / (contract.MODULE_ID + ".zip")).read_bytes())

    def test_light_rejects_missing_replacement_coverage(self):
        self.configure_light()
        self.write_json("compendium/items.json", {"text": "No image"})
        self.commit()
        self.failure("Unexpected image coverage")

    def test_light_rejects_unresolved_translated_image(self):
        old, _ = self.configure_light()
        self.write_json("compendium/items.json", {"src": old, "text": f"<img src='{old}'>"})
        self.commit()
        self.failure("Unresolved translated image reference")
