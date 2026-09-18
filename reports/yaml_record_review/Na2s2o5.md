# `data/ingredients/mapped/Na2s2o5.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:114786` sodium disulfite identity,
CAS-backed structure, occurrence count, ChEBI synonyms, and final exact row
pass, but the `REDUCING_AGENT` role is still an unsupported in-session LLM
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2s2o5.yaml`.
- Identifier and grounding: `identifier: CHEBI:114786` with
  `ontology_mapping.ontology_id: CHEBI:114786`, label `sodium disulfite`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech recipe occurrences across 6 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2s2o3_X_5_H2o` through `Na2seo3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:114786` as active
  `sodium disulfite`; `Na2S2O5`, sodium metabisulfite, E223, and the stored
  synonyms are ChEBI synonyms on the same term.
- A fresh PubChem CAS lookup for `7681-57-4` resolves to sodium disulfite with
  the same formula and InChI as the record, so the chemical block matches the
  ChEBI identity.
- The final SSSOM row maps `MIM:Na2s2o5` exactly to `CHEBI:114786`, uses the
  canonical object label, and keeps only ChEBI same-substance aliases plus
  `CAS:7681-57-4` in `other`.
- Major: `physicochemical_roles.REDUCING_AGENT` is backed only by a
  `COMPUTATIONAL_PREDICTION` evidence object from in-session LLM reasoning, and
  the curator note explicitly marks it provisional.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 6/6 occurrence count, and
  final exact SSSOM row agree.
- The remaining consequential gap is source-backed evidence for the
  `REDUCING_AGENT` role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na2s2o5.yaml`, either remove
  `physicochemical_roles.REDUCING_AGENT` or replace its LLM placeholder with
  source-backed evidence from maintained role-text or literature inputs. Rerun
  strict validation and the role/output SSSOM checks after the role facet
  change.
