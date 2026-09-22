"""Audit coverage, markup, technical tokens, and numbers against original exports."""
from collections import Counter
from html.parser import HTMLParser
import json
import re
from schema import ROOT, DATA, load, save, fields, get, numbers, technical


class Markup(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(text)
    def handle_starttag(self, tag, attrs): self.tags.append(('start', tag, attrs))
    def handle_startendtag(self, tag, attrs): self.tags.append(('single', tag, attrs))
    def handle_endtag(self, tag): self.tags.append(('end', tag))


def main():
    report = {'packs':[], 'missing':[], 'syntax':[], 'markup':[], 'numbers':[], 'unchanged':[]}
    for path in sorted(DATA.glob('*.en.json')):
        source = load(path)
        trans = load(ROOT / 'compendium' / path.name.replace('.en.json', '.json'))
        total = translated = 0
        for doc in source['documents']:
            for address, english in fields(doc, source['documentType']):
                total += 1
                target = get(trans['entries'].get(doc['_id'], {}), address)
                key = [source['collection'], doc['_id'], *address]
                if not isinstance(target, str) or not target.strip():
                    report['missing'].append(key)
                    continue
                translated += 1
                if technical(english) != technical(target): report['syntax'].append(key)
                if Markup(english).tags != Markup(target).tags: report['markup'].append(key)
                if numbers(english) != numbers(target): report['numbers'].append({'path':key,'source':english,'translation':target})
                if english == target: report['unchanged'].append(key)
        report['packs'].append({'collection':source['collection'], 'fields':total,'translated':translated})
    save(DATA / 'translation-audit.json', report)
    print(json.dumps({k:len(v) if k!='packs' else v for k,v in report.items()},ensure_ascii=True,indent=2))
    return int(any(report[k] for k in ['missing','syntax','markup','numbers']))


if __name__ == '__main__': raise SystemExit(main())
