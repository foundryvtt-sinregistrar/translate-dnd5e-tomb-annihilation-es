"""Verify exports and inventory every supported translation field."""
from collections import Counter
import hashlib
import json
from schema import ROOT, DATA, COLLECTIONS, fields, load, save


def main():
    manifest = load(DATA / 'toa-export-inventory.json')
    rows, catalog = [], []
    for pack in manifest['packs']:
        path = DATA / pack['filename']
        assert hashlib.sha256(path.read_bytes()).hexdigest() == pack['sha256'], path
        source = load(path)
        assert len(source['documents']) == pack['documents']
        assert len({d['_id'] for d in source['documents']}) == len(source['documents'])
        count, characters = 0, 0
        for doc in source['documents']:
            for address, text in fields(doc, source['documentType']):
                catalog.append({'collection': source['collection'], 'id': doc['_id'], 'path': address, 'source': text})
                count += 1
                characters += len(text)
        rows.append(f"| {source['collection']} | {len(source['documents'])} | {count} | {characters:,} |")
        if source['documentType'] == 'Adventure': adventure = source['documents'][0]
    save(DATA / 'translation-fields.json', catalog)
    report = ['# Inventario de Tomb of Annihilation', '',
        f"Exportación: {manifest['exportedAt']}. Foundry {manifest['foundry']}, dnd5e {manifest['system']['version']}, aventura {manifest['source']['version']}.", '',
        'Los cinco SHA-256 coinciden con el manifiesto. El exportador rechazó marcas de Babele y packs traducidos. Los originales permanecen excluidos de Git.', '',
        '| Pack | Documentos principales | Campos de texto | Caracteres |', '|---|---:|---:|---:|', *rows, '',
        '## Documentos incluidos en Adventure', '']
    for key in [*COLLECTIONS, 'folders']:
        report.append(f"- {key}: {len(adventure.get(key, []))}.")
    report += [f"- Páginas de diario: {sum(len(j['pages']) for j in adventure['journal'])}.", '',
        'El catálogo local `export/data/translation-fields.json` identifica cada campo por pack, documento y ruta. Incluye las copias anidadas de actores, objetos, escenas y diarios. No traduce comandos de macros, scripts de regiones, geometría, fórmulas ni valores mecánicos.', '',
        'La cobertura de campos no equivale a revisión lingüística. Los textos incrustados en imágenes requieren un tratamiento separado; se conservan los recursos oficiales.', '']
    (ROOT / 'dev-tools/translation/INVENTARIO.md').write_text('\n'.join(report), encoding='utf-8')
    print('\n'.join(rows))
    print('Unique fields',len(set(r['source'] for r in catalog)))


if __name__ == '__main__': main()
