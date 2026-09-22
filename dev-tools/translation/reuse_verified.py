"""Reuse exact English matches from existing local bilingual exports over MT drafts."""
from collections import defaultdict
from schema import *
def address_for(data,doc,key): return data['collection']+'.'+doc['_id']+'.'+'.'.join(key)
def main():
    memory = defaultdict(dict)
    for path in sorted((ROOT.parent/'translate-dnd5e-dm-2024-es/dev-tools/export/data').glob('*.reference.json')):
        source = load(path)
        name = source['collection'].rsplit('.', 1)[1]
        kind = {'equipment24':'Item', 'content24':'JournalEntry', 'tables24':'RollTable', 'actors24':'Actor', 'actors':'Actor'}[name]
        for pair in source['documents']:
            translated = dict(fields(pair['translated'], kind))
            for key, english in fields(pair['original'], kind):
                spanish = translated.get(key)
                if english.strip() and spanish and normalize(english) != normalize(spanish):
                    memory[normalize(english)][spanish] = source['collection']
    report = {'reused': [], 'ambiguous': [], 'pending': []}
    provenance = load(DATA/'mt-provenance.json') if (DATA/'mt-provenance.json').exists() else {}
    for path in sorted(DATA.glob('*.en.json')):
        data = load(path); kind = data['documentType']
        output = ROOT / 'compendium' / path.name.replace('.en.json', '.json')
        translation = load(output)
        for doc in data['documents']:
            entry = translation['entries'].setdefault(doc['_id'], {})
            for key, english in fields(doc, kind):
                if not english.strip(): continue
                if get(entry, key) is not None and address_for(data,doc,key) not in provenance.get('fields', {}): continue
                candidates = memory.get(normalize(english), {})
                adapted = {}
                for text, collection in candidates.items():
                    text = adapt(english, text)
                    if text is not None: adapted[text] = collection
                address = f"{data['collection']}.{doc['_id']}." + '.'.join(key)
                if len(adapted) == 1:
                    text, collection = next(iter(adapted.items()))
                    put(entry, key, text)
                    provenance.get('fields', {}).pop(address_for(data,doc,key), None)
                    report['reused'].append({'field': address, 'source': collection})
                elif adapted: report['ambiguous'].append(address)
                else: report['pending'].append({'field': address, 'english': english})
            if not entry: del translation['entries'][doc['_id']]
        save(output, translation)
    save(DATA / 'reuse-report.json', report)
    save(DATA/'mt-provenance.json', provenance)
    print({key:len(value) for key,value in report.items()})

if __name__ == '__main__': main()
