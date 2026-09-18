# `data/ingredients/mapped/Acetosyringone.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:2404` acetosyringone identity, exact
synonym, CAS, chemistry, SSSOM row, and aggregate copy pass; one historic
auto-backfill `changes` string contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetosyringone.yaml`.
- Identifier and grounding: `identifier: CHEBI:2404` with
  `ontology_mapping.ontology_id: CHEBI:2404`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:2404` to `acetosyringone` with
  formula `C10H12O4`, CAS `2478-38-8`, and InChIKey
  `OJOBTAOGJIWAGB-UHFFFAOYSA-N`.
- Local OAK metadata carries the same formula, structure strings, CAS xref, and
  exact synonym as the record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetoin.yaml data/ingredients/mapped/Acetomycin.yaml data/ingredients/mapped/Acetone.yaml data/ingredients/mapped/Acetosyringone.yaml data/ingredients/mapped/Acetovanillone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetosyringone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15688 CHEBI:209246 CHEBI:15347 CHEBI:2404 CHEBI:2781`:
  returned the expected ChEBI labels and synonyms for all five target ChEBI
  identifiers.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15688 CHEBI:209246 CHEBI:15347 CHEBI:2404 CHEBI:2781`:
  returned formula and structure metadata for all five target ChEBI identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT import, CAS `2478-38-8`, official ChEBI record, and local
  OAK metadata support the exact acetosyringone identity.
- The stored
  `1-(4-hydroxy-3,5-dimethoxyphenyl)ethan-1-one` synonym is the ChEBI exact
  synonym.
- The SSSOM row maps `MIM:Acetosyringone` to `CHEBI:2404` with
  `skos:exactMatch` and exports the exact synonym plus `CAS:2478-38-8`.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI, but the live `chemical_properties` values are complete and agree with
  ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, OAK/OLS confirmation row, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No role, component, source occurrence, environmental context, or discussion
  entry needs review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/Acetosyringone.yaml` so it no longer shows a
  truncated InChI. No identity, chemistry, synonym, or SSSOM edit is required.
