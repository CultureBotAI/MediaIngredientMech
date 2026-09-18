# `data/ingredients/mapped/Marinostatin.yaml`

## Verdict

Pass. The MicrobeDecoder exact ChEBI identity, reviewed promotion, ChEBI
structure, empty synonym surface, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Marinostatin.yaml`.
- Identifier and grounding: `identifier: CHEBI:221095` with
  `ontology_mapping.ontology_id: CHEBI:221095`, label `Marinostatin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder metabolite-production occurrence and zero
  CultureMech recipe occurrences.
- Chemical identity: formula `C60H83N15O21S`, InChI and SMILES copied from
  ChEBI, molecular weight `1382.475`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Marine_agar_2216` through `Mc_general_salts`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:221095` as active `Marinostatin` with formula
  `C60H83N15O21S`, molecular weight `1382.475`, and the same InChI and SMILES
  carried in the YAML.
- The local `review-ingredients` promotion says the MicrobeDecoder
  `ols-label-exact` import was held at `PENDING_REVIEW`, then promoted after
  local OAK confirmed the term and canonical label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Marinostatin`
  to `CHEBI:221095` with empty `other`.

## Completeness

- The record does not assert unsupported roles, CAS numbers, or curated
  synonyms that would need narrower support.

## Recommended Edits

- None.
