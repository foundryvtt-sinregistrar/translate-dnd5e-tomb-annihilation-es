"""Extract Spanish player handouts from the owner's local PDF (PyMuPDF).

Coordinates were checked visually on 100-dpi renders. Guide numbering follows
the English Foundry module, not the different ordering in the Spanish book.
"""
import argparse
import hashlib
from pathlib import Path
from schema import ROOT, DATA, load, save

# module number, PDF page (one-based), page ID, crop on the 100-dpi render
CROPS = [
 (1,244,'4tCpwoj4A71rw6Rx',(99,147,738,1010)),
 (2,245,'73pfOhi0uI8ImMlm',(0,88,750,520)),
 (3,246,'Da6RwTnohbRNNMPU',(73,88,824,505)),
 (4,246,'HqIM8px13pWr0aLv',(73,583,824,997)),
 (5,247,'siiN4Qhpk1ARBRh3',(0,88,750,505)),
 (6,247,'ciEZf8O0K3rnHhNs',(0,585,750,1020)),
 (7,248,'c93X1nruLP5dwoYI',(73,88,824,505)),
 (8,245,'Q2rWfVReK0dKbyPb',(0,583,750,1015)),
 (9,248,'RY1oSiH0powrtzd5',(73,585,824,1000)),
 (10,249,'lpN4JMJO4H5SLTiC',(0,88,750,516)),
 (12,250,'JhEjrKSGTbCelI3e',(85,96,751,999)),
 (13,251,'SLdBpcrK8dNlXkxp',(61,101,750,492)),
 (15,252,'MbunRtLHwATJIJCr',(83,102,758,457)),
 (17,253,'26wtZOCBLI1UWqpz',(73,102,709,501)),
 (18,253,'Pr5FPZyukQ9GQa6T',(70,577,719,922)),
 (19,254,'UW7u47h0ZKEnwYP0',(85,98,731,517)),
 (20,254,'A8cdWYcacokPLv2D',(82,579,730,998)),
 (21,255,'sctAPcZLR40PFy6s',(72,97,739,552)),
 (22,255,'FMGCsWGCPeGWfqgY',(72,623,739,971)),
]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    args=parser.parse_args()
    import pymupdf
    pdf=pymupdf.open(args.pdf)
    output=ROOT/'assets/handouts/es'
    output.mkdir(parents=True,exist_ok=True)
    target_path=ROOT/'compendium/dnd-tomb-annihilation.adventures.json'
    target=load(target_path)
    pages=target['entries']['OQ0bB1QgjuxagwGI']['journals']['toaAppEPlayerHan']['pages']
    source=load(DATA/'dnd-tomb-annihilation.adventures.en.json')
    journal=next(j for j in source['documents'][0]['journal'] if j['_id']=='toaAppEPlayerHan')
    originals={p['_id']:p for p in journal['pages']}
    records=[]
    for number,page_id,pid,box in CROPS:
        clip=pymupdf.Rect(*(v*72/100 for v in box))
        pixmap=pdf[page_id-1].get_pixmap(dpi=200,clip=clip,alpha=False)
        asset=output/f'handout-{number:02}.jpg'
        pixmap.save(str(asset),jpg_quality=92)
        src='modules/'+ROOT.name+'/'+asset.relative_to(ROOT).as_posix()
        pages[pid]['src']=src
        records.append(dict(number=number,pdfPage=page_id,pageId=pid,
            source=originals[pid]['src'],translation=src,
            cropAt100Dpi=box,sha256=hashlib.sha256(asset.read_bytes()).hexdigest()))
    save(target_path,target)
    save(ROOT/'dev-tools/translation/handout-assets.json',dict(
        pdf=args.pdf.name,pdfSha256=hashlib.sha256(args.pdf.read_bytes()).hexdigest(),
        journalId='toaAppEPlayerHan',adventureId='OQ0bB1QgjuxagwGI',
        unchangedHandouts=[11,14,16,23,24],assets=records))
    print(f'Extracted {len(records)} Spanish handouts')


if __name__=='__main__': main()
