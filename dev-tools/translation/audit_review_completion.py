"""Check full-field editorial coverage and the separately reviewed UI/assets."""
import hashlib
from schema import ROOT, DATA, load, fields


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    reviewed={r['field'] for b in load(ROOT/'dev-tools/translation/editorial-review.json')['batches']
              for r in b['fields'] if not r.get('scope')}
    expected=set()
    for path in DATA.glob('*.en.json'):
        source=load(path)
        for doc in source['documents']:
            for address,_ in fields(doc,source['documentType']):
                expected.add('.'.join([source['collection'],doc['_id'],*address]))
    errors=sorted(expected-reviewed)
    ui=load(ROOT/'dev-tools/translation/interface-review.json')
    for path,key in [(ROOT.parent/'dnd-tomb-annihilation/lang/en.json','sourceSha256'),(ROOT/'lang/es.json','translationSha256')]:
        if digest(path)!=ui[key]: errors.append(f'UI review is stale: {path.name}')
    target=load(ROOT/'compendium/dnd-tomb-annihilation.adventures.json')
    image_count=0
    for name in ['handout-assets.json','atlas-assets.json']:
        manifest=load(ROOT/'dev-tools/translation'/name)
        pages=target['entries'][manifest['adventureId']]['journals'][manifest['journalId']]['pages']
        for asset in manifest['assets']:
            path=ROOT.parent.parent/asset['translation']
            if not path.is_file() or digest(path)!=asset['sha256']: errors.append(f'Asset changed or missing: {asset["pageId"]}')
            if pages[asset['pageId']].get('src')!=asset['translation']: errors.append(f'Asset mapping changed: {asset["pageId"]}')
        image_count+=len(manifest['assets'])
    for asset in load(ROOT/'dev-tools/translation/scene-image-review.json')['images']:
        path=ROOT.parent.parent/asset['source']
        if not path.is_file() or digest(path)!=asset['sha256']:
            errors.append(f'Scene image review is stale: {asset["source"]}')
    print(f'Full-field review: {len(expected & reviewed)}/{len(expected)}; UI keys: {ui["keys"]}; Spanish images: {image_count}; errors: {len(errors)}')
    for error in errors: print(error)
    return int(bool(errors))


if __name__=='__main__': raise SystemExit(main())
