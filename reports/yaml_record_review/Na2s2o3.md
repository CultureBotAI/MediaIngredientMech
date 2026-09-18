# `data/ingredients/mapped/Na2s2o3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132112` sodium thiosulfate identity,
CAS-backed structure, duplicate merge, occurrence count, and final exact row
pass, but stale synonyms from the old unrelated ChEBI mapping plus malformed and
conditional raw labels still publish in final SSSOM, and the `ELECTRON_DONOR`
role is provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2s2o3.yaml`.
- Identifier and grounding: `identifier: CHEBI:132112` with
  `ontology_mapping.ontology_id: CHEBI:132112`, label `sodium thiosulfate`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 119 CultureMech recipe occurrences across 119 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2moo42h2o` through `Na2s2o3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:132112` as active
  `sodium thiosulfate`. A fresh PubChem lookup for CAS RN `7772-98-7` resolves
  to sodium thiosulfate with the stored formula and InChI.
- The 2026-04-18 remap correctly moved the record off unrelated `CHEBI:59168`
  and onto `CHEBI:132112`, but three exact synonyms from the old nonaethylene
  glycol target still remain active and still publish in final SSSOM.
- Major: final SSSOM also publishes malformed or conditional source labels:
  `NaS2O3`, `Na2S2SO3`, and `Na2S2O3 (if needed)`. Those are not clean
  synonyms for sodium thiosulfate.
- Major: `cellular_metabolic_roles.ELECTRON_DONOR` is backed only by a
  `COMPUTATIONAL_PREDICTION` evidence object from in-session LLM reasoning, and
  the curator note explicitly marks it provisional.

## Completeness

- The corrected ChEBI target, canonical CAS RN, formula, structure, 119/119
  occurrence count, duplicate merge, and final exact row agree.
- The remaining consequential gaps are stale unrelated synonyms, malformed final
  synonyms, and the unsupported electron-donor role.

## Recommended Edits

- Major: reject or delete the three nonaethylene-glycol synonyms inherited from
  the old `CHEBI:59168` mapping, and demote the malformed or conditional
  thiosulfate labels so they no longer publish as exact `CHEBI:132112`
  synonyms. Rebuild final SSSOM and rerun final SSSOM validation plus product
  label validation.
- Major: either remove `cellular_metabolic_roles.ELECTRON_DONOR` or replace its
  LLM placeholder with source-backed evidence from maintained role-text or
  literature inputs. Rerun strict validation and the role/output SSSOM checks
  after the role facet change.
