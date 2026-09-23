import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'dev-tools/translation'))
from reference_repairs import apply_reference_repairs

class ReferenceRepairTests(unittest.TestCase):
    def test_repairs_are_scoped_to_reviewed_field(self):
        rules={'field': [{'source':'@UUID[Actor.old]','translation':'@UUID[Actor.new]'}]}
        text='@UUID[Actor.old]{Nombre} [[/r 1d20]]'
        self.assertEqual(apply_reference_repairs(text,'other',rules),text)
        self.assertEqual(apply_reference_repairs(text,'field',rules),'@UUID[Actor.new]{Nombre} [[/r 1d20]]')

    def test_changed_source_invalidates_repair(self):
        with self.assertRaises(ValueError):
            apply_reference_repairs('@UUID[Actor.changed]','field',{'field':[{'source':'@UUID[Actor.old]','translation':'@UUID[Actor.new]'}]})
