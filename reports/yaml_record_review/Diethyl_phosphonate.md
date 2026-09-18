# `data/ingredients/mapped/Diethyl_phosphonate.yaml`

## Verdict

Pass with minor issues. The CultureMech residual is exact-grounded to active
`CHEBI:41962` diethyl phosphonate and the final SSSOM row has no unsafe
`other` tokens. One stale residual-triage row still treats the label as an
alias candidate even though the mapped record already exists.

## Identity

- Reviewed record: `data/ingredients/mapped/Diethyl_phosphonate.yaml`.
- Identifier and grounding: `identifier: CHEBI:41962` with
  `ontology_mapping.ontology_id: CHEBI:41962`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`,
  `mapping_status: MAPPED`, and one CultureMech occurrence.
- Local OAK resolves `CHEBI:41962` to active `diethyl phosphonate`, CAS xref
  `762-04-9`, formula `C4H11O3P`, InChI, SMILES, exact synonym
  `diethyl phosphonate`, and related synonyms including `Diethyl phosphite`
  and `Phosphonic acid diethyl ester`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml data/ingredients/mapped/Digested_Serum.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dicloxacillin_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/Diethyl_Ether.yaml data/ingredients/mapped/Diethyl_phosphonate.yaml data/ingredients/mapped/Difucosyllactose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-record CHEBI subset.
- `uv run --frozen linkml-term-validator validate-data ... Digested_Serum.yaml ... --labels`:
  failed after the four CHEBI records when the local `sqlite:obo:micro`
  adapter hit an incomplete cache with no `rdfs_label_statement` table.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:52019 CHEBI:35702 CHEBI:41962 CHEBI:89917`:
  returned the canonical ChEBI label, synonyms, CAS xref, formula, InChI,
  SMILES, charge, and mass for `CHEBI:41962`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, and
  CultureMech residual rows.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:41962` found only
  `data/ingredients/mapped/Diethyl_phosphonate.yaml`.
- `mappings/culturemech_residual_groundings.tsv` records the
  `Diethyl phosphonate` residual as a new `CHEBI:41962` record, matching the
  creation history.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diethyl_phosphonate` to `CHEBI:41962` with `skos:exactMatch`,
  canonical object label `diethyl phosphonate`, CHEBI object source, and no
  `other` tokens.

## Completeness

- The ChEBI identity, structured mapping evidence, occurrence statistics, and
  provenance-restoration history are populated.
- Chemical properties, supplied forms, mixture components, ingredient roles,
  and environmental contexts are correctly empty for this sparse residual
  record.

## Recommended Edits

- Minor: refresh or retire `mappings/culturemech_residual_triage.tsv` row 109
  after the residual-grounding state is reconciled; it still lists
  `Diethyl phosphonate` as an `ALIAS` triage row despite the active
  `CHEBI:41962` record.
