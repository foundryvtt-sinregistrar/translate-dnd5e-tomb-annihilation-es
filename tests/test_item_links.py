import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'dev-tools/translation'))
from item_links import stabilize_item_links,actor_context


class ItemLinksTest(unittest.TestCase):
    def test_unique_reference_survives_renaming(self):
        actor={'items':[{'_id':'bite123','name':'Bite'}]}
        self.assertEqual(stabilize_item_links('[[/item Bite]]{Mordisco}',actor),'[[/item .bite123]]{Mordisco}')

    def test_missing_ambiguous_and_existing_ids_are_unchanged(self):
        actor={'items':[{'_id':'a','name':'Claw'},{'_id':'b','name':'Claw'}]}
        text='[[/item Claw]] [[/item Missing]] [[/item .a]] [[/damage 1d6]]'
        self.assertEqual(stabilize_item_links(text,actor),text)

    def test_scene_delta_resolves_base_inventory_and_renamed_overrides(self):
        adventure={'actors':[{'_id':'actor','items':[{'_id':'a','name':'Bite'},{'_id':'b','name':'Claw'}]}],
                   'scenes':[{'_id':'s','tokens':[{'_id':'t','actorId':'actor','delta':{'items':[{'_id':'b','name':'Tail'}]}}]}]}
        actor=actor_context(adventure,'Adventure',('scenes','s','tokens','t','delta','biography'))
        self.assertEqual(stabilize_item_links('[[/item Bite]] [[/item Tail]] [[/item Claw]]',actor),
                         '[[/item .a]] [[/item .b]] [[/item Claw]]')
