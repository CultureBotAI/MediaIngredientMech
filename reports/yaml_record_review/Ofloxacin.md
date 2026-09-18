# `data/ingredients/mapped/Ofloxacin.yaml`

## Verdict

Needs curation, major. The CAS-backed `CHEBI:7731` ofloxacin identity and final
SSSOM synonyms pass, but `SELECTIVE_AGENT` is only a provisional name-pattern
inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Ofloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7731` with
  `ontology_mapping.ontology_id: CHEBI:7731`, label `ofloxacin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonym: the curated `rac-9-fluoro-3-methyl-10-(4-methylpiperazin-1-yl)-7-oxo-2,3-dihydro-7H-[1,4]oxazino[2,3,4-ij]quinoline-6-carboxylic acid`
  exact synonym.
- Structure: CAS `82419-36-1` and formula `C18H20FN3O4`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7731` as active `ofloxacin`, carries
  CAS xref `82419-36-1`, lists the curated racemic IUPAC name as an exact
  synonym, and reports formula `C18H20FN3O4`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms the final
  `CHEBI:7731` mapping.
- The final SSSOM row maps `MIM:Ofloxacin` exactly to `CHEBI:7731`; its
  `other` tokens are the curated ChEBI synonym and structured
  `CAS:82419-36-1`.
- `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with a
  provisional curator note.

## Completeness

- The active ChEBI term, CAS xref, exact synonym, formula, final SSSOM
  synonyms, and SSSOM row-review result agree.
- The only consequential gap is source evidence for the selective-agent role.

## Recommended Edits

- In `data/ingredients/mapped/Ofloxacin.yaml`, remove
  `physicochemical_roles.SELECTIVE_AGENT` or replace the provisional
  `COMPUTATIONAL_PREDICTION` evidence with source evidence that demonstrates
  this role for ofloxacin.
- Sync the aggregate record, regenerate the final SSSOM, and rerun strict
  validation plus `scripts/validate_sssom_invariants.py`.
