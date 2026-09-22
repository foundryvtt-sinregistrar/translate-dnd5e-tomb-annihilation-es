"""Checks for Foundry syntax observed in the original adventure."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'dev-tools/translation'))
from generate_draft import pieces
from schema import technical


class FoundrySyntaxTests(unittest.TestCase):
    def test_lowercase_embed_is_never_sent_to_translation(self):
        token='@embed[Actor.toaWithers000000.Item.QIctyB0wXKBWOcNZ caption=false]'
        self.assertEqual(list(pieces(token)), [('literal',token)])
        self.assertEqual(technical(token), [token])

    def test_uuid_caption_is_translatable_but_destination_is_not(self):
        token='@UUID[JournalEntry.toaCh2HeartofUbt]{Heart of Ubtao}'
        parts=list(pieces(token))
        self.assertIn(('text','Heart of Ubtao'),parts)
        self.assertTrue(all('JournalEntry' not in value for kind,value in parts if kind=='text'))

    def test_roll_and_html_attributes_are_preserved(self):
        source='<p data-id="123">[[/r 1d4]]</p>'
        self.assertEqual(''.join(value for _,value in pieces(source)),source)
        self.assertFalse(any(kind=='text' for kind,_ in pieces(source)))


if __name__ == '__main__': unittest.main()
