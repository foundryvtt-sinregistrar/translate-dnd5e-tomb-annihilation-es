"""Extract visually checked atlas crops from the owner's Spanish PDF.

Only journal images are replaced. Scene geometry and backgrounds stay intact.
Map numbering differs between editions; correspondence uses locations/page IDs.
"""
import argparse
import hashlib
from pathlib import Path
from schema import ROOT, DATA, load, save

# Atlas page ID, one-based Spanish PDF page, crop rectangle in PDF points.
CROPS = [
 ('PKl5p0cr20zTmPRz',20,(58.9,41.3,542.8,698)),
 ('r5Eh6P1HR0ZW24oO',29,(53.3,28.8,530.4,358.5)),
 ('YmRoyFdlfhNOWyuD',40,(50.9,33.6,551.2,710.7)),
 ('XUYsTwbT6tsSUTmw',46,(62.2,34.3,539.3,364)),
 ('Tsw3so8kK5A7wwqA',54,(62.5,31.6,539.6,361.3)),
 ('25FfMlR6XrnCOuGq',59,(53.3,30.4,530.4,360)),
 ('UXVMbbWtM7MCGYfC',72,(62.3,26.4,539.4,356.1)),
 ('yc8PZb1Y4xuqn9xz',81,(38.2,27.6,542.3,711.7)),
 ('yB3e7XeNyEimnMC0',88,(62.4,29.9,539.5,359.6)),
 ('wkfRCgAXnTELXhPI',78,(61.5,27.5,539.4,357.7)),
 ('5z0tczTEyExEhEYK',42,(62.3,29.8,539.4,359.4)),
 ('qaFBKBCaEyFccKzu',49,(54.2,34,529.5,362.4)),
 ('KISG7F07e24PQgN4',56,(63.3,24.2,538.6,352.6)),
 ('tJo2EBVl28o8TE6F',62,(62.3,30,539.4,359.6)),
 ('WSz3AAZ8PqL1DU0s',52,(62.3,29.8,539.4,359.4)),
 ('ihK0q3Bjpk30776z',67,(54.5,26.2,529.4,354.4)),
 ('2rRmsqDGumFCTzNU',91,(53.3,27.7,530.4,357.4)),
 ('IDEcMjNikwfUZZjg',99,(51.9,41.9,531.8,693.2)),
 ('5cAG2DguKqeKo5nb',100,(60.4,41.4,540.3,692.7)),
 ('xgaQNLgIyhRamIy4',116,(55.5,41.3,546.2,707.2)),
 ('yQ0EIRd4IxCDKk55',62,(405,40,529,350)),
 ('4IDB4ojSh25tHivw',136,(62.3,28.2,539.4,357.9)),
 ('rZbTaXxLYqjcnEks',141,(53.3,29,530.4,358.7)),
 ('6Ksw6YQd0QhItwzb',150,(62.3,28.9,539.4,358.6)),
 ('AiHNVbBMeyjGOPGl',161,(53.3,27.7,530.4,357.4)),
 ('lgP6PrVZUf8aDcAi',172,(62.3,26.8,539.4,356.5)),
 ('QPsr5xJjgKyUI3qB',153,(50,60,290,294)),
 ('Evp7GVuey2T9UUVi',183,(53.3,22.2,530.4,351.9)),
]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    args=parser.parse_args()
    import pymupdf
    pdf=pymupdf.open(args.pdf)
    target_path=ROOT/'compendium/dnd-tomb-annihilation.adventures.json'
    target=load(target_path)
    pages=target['entries']['OQ0bB1QgjuxagwGI']['journals']['toaAtlas00000000']['pages']
    source=load(DATA/'dnd-tomb-annihilation.adventures.en.json')['documents'][0]
    original=next(j for j in source['journal'] if j['_id']=='toaAtlas00000000')
    originals={p['_id']:p for p in original['pages']}
    output=ROOT/'assets/atlas/es'
    output.mkdir(parents=True,exist_ok=True)
    records=[]
    for pid,number,box in CROPS:
        asset=output/f'{pid}.jpg'
        pdf[number-1].get_pixmap(dpi=240,clip=pymupdf.Rect(box),alpha=False).save(str(asset),jpg_quality=94)
        src='modules/'+ROOT.name+'/'+asset.relative_to(ROOT).as_posix()
        pages[pid]['src']=src
        records.append(dict(pageId=pid,pdfPage=number,cropPdfPoints=box,source=originals[pid]['src'],
            translation=src,sha256=hashlib.sha256(asset.read_bytes()).hexdigest()))
    save(target_path,target)
    save(ROOT/'dev-tools/translation/atlas-assets.json',dict(pdf=args.pdf.name,
        pdfSha256=hashlib.sha256(args.pdf.read_bytes()).hexdigest(),adventureId='OQ0bB1QgjuxagwGI',
        journalId='toaAtlas00000000',assets=records))
    print(f'Extracted {len(records)} atlas maps')

if __name__=='__main__': main()
