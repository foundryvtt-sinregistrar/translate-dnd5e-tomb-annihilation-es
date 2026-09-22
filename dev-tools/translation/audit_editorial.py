"""Verify recorded English/Spanish editorial hashes, including partial scopes."""
import hashlib
from schema import ROOT, DATA, load, fields, get


def fragment(value, scope, language):
    if not scope:
        return value
    if scope['type'] == 'between-markers':
        marker = scope[language + 'StartInclusive']
        if value.count(marker) != 1:
            raise ValueError('Start marker is missing or ambiguous')
        value = value[value.index(marker):]
    elif scope['type'] != 'prefix-before-marker':
        raise ValueError('Unknown editorial scope')
    marker = scope[language + 'EndExclusive']
    if value.count(marker) != 1:
        raise ValueError('End marker is missing or ambiguous')
    return value.split(marker, 1)[0]


def main():
    sources, targets = {}, {}
    for path in DATA.glob('*.en.json'):
        source = load(path)
        target = load(ROOT / 'compendium' / path.name.replace('.en.json', '.json'))
        for doc in source['documents']:
            for address, english in fields(doc, source['documentType']):
                key = '.'.join([source['collection'], doc['_id'], *address])
                sources[key] = english
                targets[key] = get(target['entries'].get(doc['_id'], {}), address)
    errors, checked = [], 0
    for batch in load(ROOT / 'dev-tools/translation/editorial-review.json')['batches']:
        for record in batch['fields']:
            checked += 1
            for language, values in [('source', sources), ('translation', targets)]:
                try:
                    value = fragment(values[record['field']], record.get('scope'), language)
                    actual = hashlib.sha256(value.encode('utf8')).hexdigest()
                    if actual != record[language + 'Sha256']:
                        raise ValueError('Reviewed text changed')
                except (KeyError, TypeError, AttributeError, ValueError) as error:
                    errors.append(f"{batch['id']} {record['field']} ({language}): {error}")
    print(f'Editorial records: {checked}; errors: {len(errors)}')
    for error in errors:
        print(error)
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
