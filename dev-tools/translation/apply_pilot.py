"""Apply reviewed pilot text to standalone and Adventure copies by source equality."""
from schema import *
import hashlib

PILOT = {
 'Bat': 'Murciélago',
 'Echolocation': 'Ecolocalización',
 'Keen Hearing': 'Oído agudo',
 "<p>The bat can't use its blindsight while deafened.</p>": '<p>El murciélago no puede usar su visión ciega mientras esté ensordecido.</p>',
 '<p>The bat has<strong> advantage </strong>on Wisdom (Perception) checks that rely on hearing.</p>': '<p>El murciélago tiene<strong> ventaja </strong>en las pruebas de Sabiduría (Percepción) que dependan del oído.</p>',
 '<p>The Bat attacks with its Bite.</p>': '<p>El murciélago ataca con su mordisco.</p>',
 '<p><em>Token artwork by <a href="https://www.forgotten-adventures.net/" target="_blank" rel="noopener">Forgotten Adventures</a>.</em></p>': '<p><em>Ilustración de la ficha de <a href="https://www.forgotten-adventures.net/" target="_blank" rel="noopener">Forgotten Adventures</a>.</em></p>',
 '<p>A ruby found in a chest at Firefinger.</p>': '<p>Un rubí encontrado en un cofre en el Dedo de Fuego.</p>',
 'No. Yuan-ti Malisons Returning': 'Cantidad de yuan-tis malison que regresan',
 '<p>@UUID[Actor.toaYuantiMal2000]{Yuan-ti Malison (Type 1)}</p>': '<p>@UUID[Actor.toaYuantiMal2000]{Yuan-ti malison (tipo 1)}</p>',
 '<p>@UUID[Actor.toaYuantiMal2000]{Yuan-ti Malison (Type 2)}</p>': '<p>@UUID[Actor.toaYuantiMal2000]{Yuan-ti malison (tipo 2)}</p>',
 '<p>@UUID[Actor.toaYuantiMal3000]{Yuan-ti Malison (Type 3)}</p>': '<p>@UUID[Actor.toaYuantiMal3000]{Yuan-ti malison (tipo 3)}</p>',
 'Ataaz Muhahah': 'Ataaz Muhahah',
 'Level 3: Vault of Reflection': 'Nivel 3: Bóveda del Reflejo',
 'Dwellers of the Forbidden City': 'Moradores de la Ciudad Prohibida'
}


def main():
    glossary = load(ROOT / 'dev-tools/translation/reviewed-segments.json')
    glossary.update(load(ROOT / 'dev-tools/translation/terminology.json'))
    glossary.update(PILOT)
    save(ROOT / 'dev-tools/translation/reviewed-segments.json', glossary)
    reviewed = []
    provenance = load(DATA / 'mt-provenance.json')
    for source_path in DATA.glob('*.en.json'):
        source = load(source_path)
        target = ROOT / 'compendium' / source_path.name.replace('.en.json', '.json')
        translation = load(target)
        for doc in source['documents']:
            entry = translation['entries'].setdefault(doc['_id'], {})
            for address, english in fields(doc, source['documentType']):
                if english not in glossary: continue
                spanish = glossary[english]
                put(entry, address, spanish)
                key = source['collection']+'.'+doc['_id']+'.'+'.'.join(address)
                provenance['fields'].pop(key, None)
                reviewed.append({'field':key,'sourceSha256':hashlib.sha256(english.encode()).hexdigest(),'translationSha256':hashlib.sha256(spanish.encode()).hexdigest()})
        if source['documentType'] == 'Adventure':
            key = ('journals', 'toaCh2AldaniBasi', 'pages', 'O3nw3YpRTmoj7v0W', 'text')
            spanish = '<p>Los ríos Soshenstar y Tath fluyen desde esta cuenca cenagosa de las tierras altas, una zona en la que se alimentan los dinosaurios y enjambres de insectos que pican. Las mesetas altas y las paredes del follaje denso circundan el pantano.</p><p>La cuenca recibe su nombre de los @UUID[Actor.kwmBntzfAVxY1CT1]{aldani}, una raza de hombres langosta (consulta el @UUID[JournalEntry.toaAppDMonstersA.JournalEntryPage.304auBV3HuY9dSM4]{apéndice D}). Muchos chultanos recuerdan cuentos infantiles sobre los misteriosos hombres langosta que vivían en los ríos y lagos de su patria. Ningún testigo fiable afirma haberse encontrado con un aldani desde hace décadas. Por eso, la mayoría de chultanos creen que los aldani han muerto. De hecho, los hombres langosta se refugiaron en los lagos recónditos de esta cuenca, donde llevan un siglo escondidos.</p><p>Cuando el cielo está despejado, se puede ver el @UUID[JournalEntry.toaCh2HeartofUbt]{Corazón de Ubtao} flotando sobre el pantano a una distancia de hasta 50 millas (tira [[/r 1d4]] cada día para determinar a cuántos hexágonos de distancia es visible a través de la niebla y la calima).</p>'
            put(translation['entries'][doc['_id']], key, spanish)
            address = source['collection']+'.'+doc['_id']+'.'+'.'.join(key)
            provenance['fields'].pop(address, None)
            reviewed.append({'field':address,'method':'pdf-es-adapted','pdfPage':52})
        save(target, translation)
    save(DATA / 'mt-provenance.json', provenance)
    save(DATA / 'reviewed-fields.json', reviewed)
    print('Reviewed fields:', len(reviewed))


if __name__ == '__main__': main()
