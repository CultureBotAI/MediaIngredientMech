# `data/ingredients/mapped/Na2s2o3_X_5_H2o.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:32150` sodium thiosulfate
pentahydrate identity, CAS-backed structure, duplicate merges, occurrence
count, and final exact row pass, but final SSSOM still publishes
concentration-qualified or catalog-specific labels as synonyms, and the
`ELECTRON_DONOR` role is provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2s2o3_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:32150` with
  `ontology_mapping.ontology_id: CHEBI:32150`, label
  `sodium thiosulfate pentahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 716 CultureMech recipe occurrences across 716 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2s2o3_X_5_H2o` through `Na2seo3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:32150` as active
  `sodium thiosulfate pentahydrate`; the term carries the stored formula,
  InChI, SMILES, and CAS `10102-17-7`.
- A fresh PubChem CAS lookup for `10102-17-7` resolves to sodium thiosulfate
  pentahydrate with the same InChI as the record, so the CAS-backed chemical
  block agrees with the hydrate identity.
- The absorbed `Sodium_Thiosulfate_Pentahydrate` duplicate shares the same
  exact ChEBI term and hydrate-specific CAS, so the merge did not cross a
  hydrate or parent boundary.
- Major: final SSSOM `other` publishes concentration-qualified labels
  `Na2S2O3 x 5 H2O (10% solution)` and `Na2S2O3 x 5 H2O(24 % w/v)`, the
  catalog/procurement note
  `Sodium Thiosulfate Pentahydrate (agar media only,sterile)(Baker 3946)`,
  and typoed `Na2S2O3 x 5 H20`. These are not clean synonyms for the
  pentahydrate.
- Major: `cellular_metabolic_roles.ELECTRON_DONOR` is backed only by a
  `COMPUTATIONAL_PREDICTION` evidence object from in-session LLM reasoning, and
  the curator note explicitly marks it provisional.

## Completeness

- The active ChEBI term, canonical CAS RN, formula, structure, 716/716
  occurrence count, duplicate merges, and exact final SSSOM row agree.
- The final SSSOM row correctly filters the imported `Properties:` raw text, but
  still exports concentration and catalog strings as exact synonyms.
- The remaining consequential gaps are cleaning the final synonym surface and
  replacing or removing the unsupported electron-donor role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2s2o3_X_5_H2o.yaml`, demote the
  concentration-qualified, catalog-specific, and typoed labels so they no
  longer publish as exact `CHEBI:32150` synonyms. Rebuild final SSSOM and rerun
  final SSSOM validation plus product label validation.
- Major: either remove `cellular_metabolic_roles.ELECTRON_DONOR` or replace its
  LLM placeholder with source-backed evidence from maintained role-text or
  literature inputs. Rerun strict validation and the role/output SSSOM checks
  after the role facet change.
