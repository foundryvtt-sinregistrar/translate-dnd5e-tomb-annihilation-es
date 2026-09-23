"""Audit local UUID targets and actor item commands without importing a world.

External packs and anchors require Foundry; they are counted, not certified.
Original broken references remain findings, separate from translation regressions.
"""
import re
from collections import Counter
from schema import ROOT, DATA, load, save, fields, get, COLLECTIONS
from item_links import actor_context, ITEM_LINK


def main():
    packs={}
    for path in DATA.glob('*.en.json'):
        source=load(path)
        packs[source['collection']]=(source,load(ROOT/'compendium'/path.name.replace('.en.json','.json')))
    adventure=packs['dnd-tomb-annihilation.adventures'][0]['documents'][0]
    world={kind:{d['_id']:d for d in adventure.get(group,[])} for group,kind in COLLECTIONS.items()}
    counts=Counter(); findings=[]
    def resolve_uuid(uuid):
        uuid,_,anchor=uuid.partition('#')
        if anchor: counts['anchorsRequiringRuntime']+=1
        parts=uuid.split('.')
        if parts[0]=='Compendium':
            collection='.'.join(parts[1:3])
            if collection not in packs: return None
            source,_=packs[collection]
            parts=parts[3:]
            if parts[0]==source['documentType']: parts=parts[1:]
            obj=next((d for d in source['documents'] if d['_id']==parts[0]),None)
            parts=parts[1:]
        elif parts[0] in world and len(parts)>1:
            obj=world[parts[0]].get(parts[1]); parts=parts[2:]
        else: return None
        child_groups={'Item':'items','ActiveEffect':'effects','JournalEntryPage':'pages','Token':'tokens','Region':'regions'}
        while obj is not None and len(parts)>=2:
            kind,id,*parts=parts
            if kind not in child_groups: return None
            obj=next((d for d in obj.get(child_groups[kind],[]) if d['_id']==id),None)
        return obj is not None
    for collection,(source,target) in packs.items():
        for doc in source['documents']:
            for path,english in fields(doc,source['documentType']):
                value=get(target['entries'][doc['_id']],path)
                key='.'.join([collection,doc['_id'],*path])
                actor=actor_context(doc,source['documentType'],path)
                for match in ITEM_LINK.finditer(value):
                    reference=match[1]
                    if not actor:
                        counts['itemCommandsWithoutActorContext']+=1
                        continue
                    matches=[i for i in actor.get('items',[]) if i['_id']==reference.lstrip('.') or i.get('name')==reference]
                    if len(matches)==1:
                        counts['resolvedItemCommands']+=1
                    else:
                        counts['unresolvedItemCommands']+=1
                        findings.append(dict(field=key,type='item',reference=reference,inOriginal=match[0] in english))
                for match in re.finditer(r'@(?:UUID|Embed)\[([^\]\s]+)',value):
                    reference=match[1]
                    result=resolve_uuid(reference)
                    if result is None: counts['externalOrContextualReferences']+=1
                    elif result: counts['resolvedLocalReferences']+=1
                    else:
                        counts['unresolvedLocalReferences']+=1
                        findings.append(dict(field=key,type='uuid',reference=reference,inOriginal=reference in english))
    report={'counts':dict(counts),'findings':findings}
    save(DATA/'link-audit.json',report)
    print(report['counts'])
    print('Translation regressions:',sum(not f['inOriginal'] for f in findings))
    return int(any(not f['inOriginal'] for f in findings))


if __name__=='__main__': raise SystemExit(main())
