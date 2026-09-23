"""Build a text-only distribution without changing the full translation."""
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build():
    module = json.loads((ROOT / 'module.json').read_text(encoding='utf-8'))
    module_id = module['id']
    replacements = {}
    for name in ('handout-assets.json', 'atlas-assets.json'):
        manifest = json.loads((ROOT / 'dev-tools/translation' / name).read_text(encoding='utf-8'))
        for asset in manifest['assets']:
            replacements[asset['translation']] = asset['source']
            if not (ROOT.parent.parent / asset['source']).is_file():
                raise ValueError(f"Missing official image: {asset['source']}")
    seen = set()
    count = 0

    def restore(value):
        nonlocal count
        if isinstance(value, dict):
            for key, child in value.items():
                if key == 'src' and isinstance(child, str) and child in replacements:
                    seen.add(child)
                    value[key] = replacements[child]
                    count += 1
                else:
                    restore(child)
        elif isinstance(value, list):
            for child in value:
                restore(child)

    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    payload = {}
    for name in paths:
        if not name or name.split('/')[0] not in ('module.json', 'scripts', 'lang', 'compendium', 'CHANGELOG.md'):
            continue
        data = (ROOT / name).read_bytes()
        if name.startswith('compendium/') and name.endswith('.json'):
            value = json.loads(data)
            restore(value)
            data = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
        payload[name] = data
    if seen != set(replacements) or count != len(replacements):
        raise ValueError(f'Unexpected image coverage: {count}/{len(replacements)}')
    module['title'] += ' — Solo texto'
    module['description'] = 'Versión de prueba ligera: traducción textual al español; utiliza las imágenes del módulo oficial, que pueden contener texto inglés. Validación funcional integral pendiente.'
    payload['module.json'] = (json.dumps(module, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    payload['README.md'] = f'''# La tumba de la aniquilación — Solo texto

Versión de prueba {module['version']}. Variante ligera del mismo módulo;
no instalar junto con la variante completa como un módulo diferente.

Incluye los cinco compendios traducidos y 126 claves de interfaz. No incluye
imágenes, PDF, OCR ni exportaciones originales. Las 47 referencias a imágenes
españolas se han sustituido por las rutas del módulo oficial. Los rótulos
integrados en las imágenes originales permanecen en su idioma original.

## Instalación

Con Foundry detenido, extraer la carpeta del ZIP en Data/modules/.
Requiere Foundry 14.368, dnd5e 6.0.3, Babele 2.9.1 y el módulo oficial
dnd-tomb-annihilation 2.0.0 con sus dependencias. Activar español y los módulos.
Antes de importar, desactivar en Babele «Sync imported Adventure token names».

La instalación no cambia automáticamente documentos ya importados. Un mundo
importado con la variante completa puede conservar rutas a imágenes españolas;
para probar esta variante, utilizar una importación nueva en un mundo de prueba.

La revisión textual está cerrada; las pruebas funcionales no cubren todas las
automatizaciones de una partida. Esta variante no dispone de publicación remota.
'''.encode('utf-8')
    for name, data in payload.items():
        if f'modules/{module_id}/assets/'.encode() in data:
            raise ValueError(f'Unresolved translated image reference in {name}')
    for path in module['esmodules']:
        if path not in payload:
            raise ValueError(f'Missing script: {path}')
    output = ROOT / 'dist' / f'{module_id}-{module["version"]}-light.zip'
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            archive.writestr(f'{module_id}/{name}', data)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError('Invalid ZIP')
    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix('.zip.sha256').write_text(f'{digest}  {output.name}\n', encoding='ascii')
    print(f'{output.name}: {output.stat().st_size} bytes; {count} original image references restored; {len(payload)} files')


if __name__ == '__main__':
    build()
