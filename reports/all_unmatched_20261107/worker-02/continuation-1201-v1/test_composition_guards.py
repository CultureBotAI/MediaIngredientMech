import unittest
from compose_owner_versions import compose


class CompositionGuards(unittest.TestCase):
    def test_retains_both_additions_and_rejected_source_text(self):
        raw={'synonym_text':'stock 1%','synonym_type':'EXACT_SYNONYM','source':'original'}
        base={'synonyms':[raw],'curation_history':[{'old':True}],'identifier':'CHEBI:1'}
        previous={**base,'synonyms':[raw,{'synonym_text':'salt','synonym_type':'EXACT_SYNONYM'}], 'curation_history':[{'old':True},{'prior':True}]}
        revision={**base,'synonyms':[{**raw,'synonym_type':'REJECTED_LABEL'}], 'curation_history':[{'old':True},{'new':True}]}
        result=compose(base,previous,revision)
        self.assertEqual(result['synonyms'][0],{**raw,'synonym_type':'REJECTED_LABEL'})
        self.assertEqual(result['synonyms'][1],previous['synonyms'][1])
        self.assertEqual(result['curation_history'],[{'old':True},{'prior':True},{'new':True}])
        self.assertEqual(base['synonyms'][0],raw)

    def test_conflicting_scalar_fails(self):
        with self.assertRaises(ValueError):compose({'id':1},{'id':2},{'id':3})

    def test_deleted_original_list_item_fails(self):
        with self.assertRaises(ValueError):compose({'history':[1]},{'history':[1,2]},{'history':[]})
        with self.assertRaises(ValueError):compose({'history':[1]},{'history':[1]},{'history':[]})

    def test_source_text_changed_fails(self):
        a={'synonym_text':'stock','synonym_type':'RAW_TEXT'}
        with self.assertRaises(ValueError):compose({'synonyms':[a]},{'synonyms':[a,{'new':1}]},{'synonyms':[{'synonym_text':'changed','synonym_type':'REJECTED_LABEL'}]})

    def test_conflicting_new_field_fails(self):
        with self.assertRaises(ValueError):compose({}, {'x':1}, {'x':2})


if __name__ == '__main__':unittest.main()
