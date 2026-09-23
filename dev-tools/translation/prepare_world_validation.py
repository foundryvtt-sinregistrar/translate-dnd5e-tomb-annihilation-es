"""Build local expectations for validating the freshly imported Adventure."""
from schema import *
from audit_runtime import raw_path

source=load(DATA/'dnd-tomb-annihilation.adventures.en.json')['documents'][0]
translation=load(ROOT/'compendium/dnd-tomb-annihilation.adventures.json')['entries'][source['_id']]
checks=[]
for path,english in fields(source,'Adventure'):
    raw=raw_path('Adventure',path)
    if raw[0] not in COLLECTIONS and raw[0]!='folders': continue
    kind='Folder' if raw[0]=='folders' else COLLECTIONS[raw[0]]
    checks.append(dict(kind=kind,id=raw[1],path=raw[2:],expected=get(translation,path)))
manifest=load(ROOT/'dev-tools/translation/handout-assets.json')
for asset in manifest['assets']:
    checks.append(dict(kind='JournalEntry',id=manifest['journalId'],path=['pages',asset['pageId'],'src'],expected=asset['translation']))
save(DATA/'world-validation-expectations.json',dict(checks=checks,
    counts={kind:len(source.get(group,[])) for group,kind in COLLECTIONS.items() if source.get(group)},
    references=load(DATA/'link-audit.json')['findings']))
print('Prepared checks:',len(checks))
