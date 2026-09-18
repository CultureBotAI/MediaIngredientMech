# `data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml`

## Verdict

Needs curation; major. The record was correctly relabelled to the free base
`CHEBI:18397` 2-phenylethylamine, but final SSSOM `other` still exports the
old hydrochloride-salt label as if it were a free-base synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:18397` with
  `ontology_mapping.ontology_id: CHEBI:18397`, label `2-phenylethylamine`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:18397` resolves `CHEBI:18397`
  `2-phenylethylamine`; a CHEBI search for the old hydrochloride label does
  not resolve a phenethylamine-hydrochloride term.
- A local CAS checksum calculation confirmed that `64-04-0` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenethylamine_Hydrochloride` exactly to `CHEBI:18397`.

## Evidence

- The #235 relabelling made the primary identity honest: CultureBotHT supplied
  CAS `64-04-0`, which denotes the free base and resolves to `CHEBI:18397`.
- The CHEBI primary identifier, mapping target, structured formula, InChI,
  SMILES, curated `2-phenylethanamine` synonym, `Beta-phenylethylamine`
  synonym, and `CAS:64-04-0` all describe 2-phenylethylamine.
- Major: `Phenethylamine Hydrochloride` denotes a hydrochloride salt rather
  than the free base, but final SSSOM still exports it in `other`.

## Completeness

- The free-base identity is complete enough.
- The final synonym surface remains incomplete while the old salt label is
  exported as a free-base synonym.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml`, retype
  or suppress the `Phenethylamine Hydrochloride` raw synonym so it remains
  provenance for the #235 relabelling only and no longer appears in
  `mappings/ingredient_mappings.sssom.tsv`; rebuild the final SSSOM and rerun
  `scripts/validate_sssom_invariants.py`.
