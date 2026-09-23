"""Check actual Babele output against every translation field and source mechanics."""
from schema import *


def indexed_leaves(value, path=()):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in ['_stats','originalName','translated','hasTranslation']: continue
            if key == 'babele' and path and path[-1] == 'flags': continue
            yield from indexed_leaves(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            key = child.get('_id', index) if isinstance(child, dict) else index
            yield from indexed_leaves(child, path + (key,))
    else: yield path, value


def raw_path(kind, path):
    first, *rest = path
    rest = tuple(rest)
    if kind == 'Adventure':
        key = 'journal' if first == 'journals' else first
        if key == 'folders': return (key, *rest, 'name')
        if key in COLLECTIONS:
            return (key, rest[0], *raw_path(COLLECTIONS[key], rest[1:]))
    if kind == 'Actor' and first == 'items': return ('items', rest[0], *raw_path('Item', rest[1:]))
    if kind == 'Scene' and first == 'tokens' and len(rest)>1 and rest[1]=='delta':
        return ('tokens',rest[0],'delta',*raw_path('Actor',rest[2:]))
    aliases = {
      'Actor': {'biography':('system','details','biography','value'), 'biographyPublic':('system','details','biography','public'),
        'tokenName':('prototypeToken','name'), 'alignment':('system','details','alignment'),
        'creatureType':('system','details','type','custom'), 'creatureSubtype':('system','details','type','subtype'),
        'languages':('system','traits','languages','custom'), 'senses':('system','attributes','senses','special')},
      'Item': {'description':('system','description','value'),'descriptionChat':('system','description','chat'),
        'unidentifiedDescription':('system','unidentified','description'),'requirements':('system','requirements'),
        'activities':('system','activities'), 'advancement':('system','advancement')},
      'Scene': {'navigation':('navName',)}
    }
    if first in aliases.get(kind, {}): return aliases[kind][first] + rest
    if kind == 'JournalEntry' and first == 'pages' and len(rest)>1 and rest[1]=='text': return ('pages',rest[0],'text','content')
    if kind == 'Scene' and first == 'regions' and len(rest)>3 and rest[1]=='behaviors':
        key = rest[3]
        mapped = {'text':('system','text'), 'revealedDialog':('system','dialog','revealed'), 'unrevealedDialog':('system','dialog','unrevealed')}
        if key in mapped: return ('regions', *rest[:3], *mapped[key])
    return path


def main():
    report = {'checkedFields':0, 'fieldErrors':[], 'mechanicalErrors':[], 'missingDocuments':[]}
    handouts = load(ROOT / 'dev-tools/translation/handout-assets.json')
    for source_path in DATA.glob('*.en.json'):
        source = load(source_path)
        actual = load(DATA / source_path.name.replace('.en.json','.validated.json'))
        trans = load(ROOT / 'compendium' / source_path.name.replace('.en.json','.json'))
        lookup = {d['_id']:d for d in actual['documents']}
        raw = load(DATA / source_path.name.replace('.en.json','.translated.json'))
        raw_lookup = {d['_id']:d for d in raw['documents']}
        for doc in source['documents']:
            id = doc['_id']
            if id not in lookup:
                report['missingDocuments'].append([source['collection'],id]); continue
            actual_fields = dict(fields(lookup[id],source['documentType']))
            allowed = set()
            for path, english in fields(doc,source['documentType']):
                allowed.add(raw_path(source['documentType'],path))
                expected = get(trans['entries'][id],path)
                result = actual_fields.get(path)
                report['checkedFields'] += 1
                if (result.strip() if isinstance(result,str) else result) != (expected.strip() if isinstance(expected,str) else expected):
                    report['fieldErrors'].append([source['collection'],id,list(path)])
            leaves = dict(indexed_leaves(raw_lookup[id]))
            if source['documentType'] == 'Adventure' and id == handouts['adventureId']:
                for asset in handouts['assets']:
                    path = ('journal', handouts['journalId'], 'pages', asset['pageId'], 'src')
                    allowed.add(path)
                    if leaves.get(path) != asset['translation']:
                        report['fieldErrors'].append([source['collection'], id, list(path)])
            for path, value in indexed_leaves(doc):
                if path in allowed: continue
                if leaves.get(path) != value:
                    report['mechanicalErrors'].append({'collection':source['collection'],'id':id,'path':path,'source':value,'actual':leaves.get(path)})
    save(DATA/'runtime-audit.json',report)
    print({k:len(v) if isinstance(v,list) else v for k,v in report.items()})
    return int(any(report[k] for k in ['fieldErrors','mechanicalErrors','missingDocuments']))


if __name__ == '__main__': raise SystemExit(main())
