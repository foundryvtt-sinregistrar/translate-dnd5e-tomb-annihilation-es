"""Transform the committed Tomb archive without reading local source files."""
import json
from pathlib import Path
import subprocess
import stat
import zipfile


def transform_archive(root: Path, commit: str, archive_path: Path, meta: dict):
    replacements = {}
    prefix = meta["id"] + "/"
    private_prefix = f"modules/{meta['id']}/assets/"
    for name in ("handout-assets.json", "atlas-assets.json"):
        raw = subprocess.check_output(["git", "show", f"{commit}:dev-tools/translation/{name}"], cwd=root)
        for asset in json.loads(raw)["assets"]:
            translated, source = asset["translation"], asset["source"]
            if not translated.startswith(private_prefix) or not source.startswith("modules/dnd-tomb-annihilation/assets/"):
                raise ValueError("Unexpected image replacement path")
            if translated in replacements:
                raise ValueError("Duplicate image replacement")
            replacements[translated] = source
    seen = set()
    count = 0

    def restore(value):
        nonlocal count
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "src" and isinstance(child, str) and child in replacements:
                    seen.add(child)
                    value[key] = replacements[child]
                    count += 1
                else:
                    restore(child)
        elif isinstance(value, list):
            for child in value:
                restore(child)

    payload = {}
    with zipfile.ZipFile(archive_path) as archive:
        for entry in archive.infolist():
            if stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError("Symlink is not distributable")
            if entry.is_dir():
                continue
            if not entry.filename.startswith(prefix) or entry.filename in payload:
                raise ValueError("Invalid text-only archive member")
            data = archive.read(entry)
            if entry.filename.startswith(prefix + "compendium/") and entry.filename.endswith(".json"):
                value = json.loads(data)
                restore(value)
                data = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            payload[entry.filename] = data
    if not replacements or seen != set(replacements) or count != len(replacements):
        raise ValueError(f"Unexpected image coverage: {count}/{len(replacements)}")
    meta = dict(meta)
    if not meta["title"].endswith(" — Solo texto"):
        meta["title"] += " — Solo texto"
    meta["description"] = "Traducción textual al español; utiliza las imágenes del módulo oficial, que pueden contener texto inglés. Validación funcional integral pendiente."
    manifest = (json.dumps(meta, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    payload[prefix + "module.json"] = manifest
    for name, data in payload.items():
        if private_prefix.encode() in data:
            raise ValueError(f"Unresolved translated image reference in {name}")
    transformed = archive_path.with_suffix(".transformed.zip")
    with zipfile.ZipFile(transformed, "w") as archive:
        for name, data in sorted(payload.items()):
            entry = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data)
    transformed.replace(archive_path)
    print(f"Text-only: {count} official image paths restored")
    return manifest, meta
