"""Author the explicitly reviewed #1149 mapping-only decision; no role approval."""
import json
from pathlib import Path
import yaml
from mediaingredientmech.export.reviewed_sssom import read_sssom, row_sha256, digest

root = Path.cwd()
owner = 'data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml'
review = 'reviews/structured/20261108T024039Z-sodium-acetate-source-alias-scientific-review/review.yaml'
report = 'reports/kgm_unmapped_chemicals_20261107/sodium-acetate/'
readback = json.loads((root / report / 'scientific-review-inputs-v1/readback.json').read_text())
_, _, rows = read_sssom(root / 'mappings/ingredient_mappings.sssom.tsv')
selected = [r for r in rows if r['subject_id'] == 'MIM:Sodium_Acetate_Trihydrate']
assert selected == [readback['selected'][0]['row']]
assert digest(root / owner) == readback['owner_sha256']
scientific = yaml.safe_load((root / review).read_text())
assert scientific['scientific_review'] is True
assert next(a for a in scientific['assessments'] if a['assessment_id']=='all-six-row-tokens')['outcome']=='supported'
tokens = {
 'Na-acetate x 3 H2O': 'KEEP: sodium acetate with three waters; the exact same stoichiometric hydrate as CHEBI:32138, not anhydrous sodium acetate.',
 'Sodium acetate x 3 H2O': 'KEEP: explicit trihydrate stoichiometry matches the ChEBI formula and InChI with three waters.',
 'sodium acetate--water (1/3)': 'KEEP: inspected exact ChEBI:32138 synonym; 1:3 sodium acetate/water stoichiometry.',
 'Sodium acetate·3H2O': 'KEEP: equivalent explicit hydrate notation preserved from the prior duplicate; three waters remain part of identity.',
 'CAS:6131-90-4': 'KEEP: registry display alias for the trihydrate, corroborated by ChEBI, PubChem CID23665404 and MediaDive1315. Not an expandable uppercase CURIE.',
 'Na acetate x 3 H2O': 'KEEP: the exact MediaDive1315 source label is explicitly paired with CAS6131-90-4. ChEBI and PubChem independently corroborate the trihydrate; MediaDive\'s discrepant hydrogen count is not imported.',
}
assert set(tokens) == set(selected[0]['other'].split('|'))
paths = [review, review.replace('review.yaml','review.md'), report+'sources/mediadive-1315.json', report+'sources/chebi-32138.json', report+'sources/pubchem-cas6131-synonyms.json', report+'sources/manifest.json', report+'scientific-review-inputs-v1/readback.json', 'reports/sssom_completion_20260921/mapping_changes/issue1149-1151-kgm-source-corrections.json']
entry = {
 'mapping': selected[0], 'row_sha256': row_sha256(selected[0]),
 'owner_record': owner, 'owner_record_sha256': digest(root/owner), 'disposition': 'SUPPORTED',
 'reason': 'Fresh mapping-only review of the exact changed owner and complete six-token row (#1149), after receipt27 withdrew inherited approval. The explicit trihydrate identity and each remaining/new name are supported. No role, occurrence count, whole-record scientific status or other withheld mapping is approved; historical confidence and validation stamps are retained as provenance.',
 'identity_review': 'MediaDive1315 pairs its exact source name with CAS6131-90-4. ChEBI:32138 denotes sodium acetate trihydrate, formula C2H3O2.3H2O.Na, with three water components in the InChI; PubChemCID23665404 corroborates the CAS/name. This is database evidence for the same hydrate, not the anhydrous salt or a stock. The excess hydrogen in MediaDive automated formula is retained as a discrepancy and not copied. Full current row and all six tokens were assessed in the immutable scientific review.',
 'token_reviews': tokens, 'evidence_inputs': {p:digest(root/p) for p in paths}, 'resolved_negative_reviews': [],
}
target = root/'reports/sssom_completion_20260921/mapping_review/kgmicrobe-followup.json'
original = target.read_bytes(); doc=json.loads(original)
assert not any(d['mapping']['subject_id']==selected[0]['subject_id'] for d in doc['decisions'])
(root/report/'mapping-followup-before.json').write_bytes(original)
(root/report/'mapping-followup-decision.json').write_text(json.dumps(entry,indent=2,ensure_ascii=False)+'\n')
doc['scope'] += ' The exact #1149 sodium acetate trihydrate source-alias row has a fresh content-bound mapping-only review; no role approval.'
doc['decisions'].append(entry)
target.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n')
print('Added one exact mapping-only follow-up after explicit full-row scientific review')
