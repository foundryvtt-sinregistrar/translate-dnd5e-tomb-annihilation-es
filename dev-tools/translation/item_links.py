"""Resolve name-based actor item links against the original actor inventory.

Only an exact, unique source name can be replaced by its embedded item ID.
Missing and ambiguous source references are never guessed.
"""
import re
from copy import deepcopy

ITEM_LINK = re.compile(r'\[\[/item ([^\]\n]+)\]\]')


def actor_context(document, kind, address):
    if kind == 'Actor':
        return document
    if kind != 'Adventure' or not address:
        return None
    if address[0] == 'actors':
        return next((a for a in document.get('actors', []) if a['_id'] == address[1]), None)
    if address[0] == 'scenes' and len(address) > 5 and address[2] == 'tokens' and address[4] == 'delta':
        scene = next(s for s in document['scenes'] if s['_id'] == address[1])
        token = next(t for t in scene['tokens'] if t['_id'] == address[3])
        base = next((a for a in document.get('actors', []) if a['_id'] == token.get('actorId')), {})
        items = {i['_id']:deepcopy(i) for i in base.get('items', [])}
        for item in token.get('delta', {}).get('items', []):
            items.setdefault(item['_id'], {}).update(item)
        return {'items':list(items.values())}
    return None


def stabilize_item_links(text, actor):
    if not actor:
        return text
    def replace(match):
        name = match[1]
        if name.startswith('.'):
            return match[0]
        matches = [i for i in actor.get('items', []) if i.get('name') == name]
        if len(matches) != 1:
            return match[0]
        return '[[/item .' + matches[0]['_id'] + ']]'
    return ITEM_LINK.sub(replace, text)
