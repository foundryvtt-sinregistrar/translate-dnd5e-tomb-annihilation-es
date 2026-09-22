"""Apply explicit mappings to Adventure embedded documents and root packs."""
from schema import ROOT, load, save


def main():
    folder = ROOT / 'compendium'
    def pack(name): return load(folder / f'dnd-tomb-annihilation.{name}.json')
    actor = pack('actors')['mapping']
    item = pack('items')['mapping']
    table = pack('tables')['mapping']
    scene = {'name':'name', 'navigation':'navName'}
    for key in ['notes', 'drawings', 'tokens', 'levels']:
        scene[key] = {'path':key, 'converter':'toaSceneTextById'}
    scene['tokens'] = {'path':'tokens', 'converter':'toaSceneTokensById'}
    # Babele's built-in Region mapping handles nested behavior documents.
    journal = {'name':'name', 'pages':{'path':'pages','converter':'toaJournalPagesById'}}
    adventure = pack('adventures')
    adventure['mapping']['folders'] = {'path':'folders', 'converter':'toaFolderNamesById'}
    for key, kind, mapping in [('actors','Actor',actor), ('items','Item',item),
            ('journals','JournalEntry',journal), ('scenes','Scene',scene),
            ('tables','RollTable',table), ('macros','Macro',{'name':'name'})]:
        adventure['mapping'][key] = {'path':'journal' if key == 'journals' else key,
            'converter':'document', 'documentType':kind, 'cardinality':'many',
            'mapping':mapping}
    adventure['mapping']['actors'] = {'path':'actors', 'converter':'toaAdventureActorsById'}
    save(folder / 'dnd-tomb-annihilation.adventures.json', adventure)


if __name__ == '__main__': main()
