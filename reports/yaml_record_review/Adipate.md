# `data/ingredients/mapped/Adipate.yaml`

## Verdict

Needs curation. The close grounding to ChEBI `adipate(2-)` is internally
consistent, but the record still carries stale unresolved-import prose and is
missing the ChEBI-backed dianion structure block.

## Identity

- Reviewed record: `data/ingredients/mapped/Adipate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17128` with
  `ontology_mapping.ontology_id: CHEBI:17128`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:17128` to
  `adipate(2-)` with formula `C6H8O4`, charge `-2`, SMILES
  `O=C([O-])CCCCC(=O)[O-]`, InChIKey `WNLRTRBMVRJNCN-UHFFFAOYSA-L`, and
  PubChem resolves CAS `764-65-8` to the same dianion structure.
- Local OAK does not list bare `Adipate` as a synonym of `CHEBI:17128`, which
  supports `CLOSE_MATCH` rather than `SYNONYM_MATCH`.
- `ingredient_type: SINGLE_INGREDIENT` is present and agrees with the modeled
  ChEBI dianion.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adipate.yaml data/ingredients/mapped/Adipic_Acid.yaml data/ingredients/mapped/Aesculetin.yaml data/ingredients/mapped/Agar.yaml data/ingredients/mapped/Agarose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adipate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned the expected labels and aliases for all ChEBI terms checked in this
  batch, including canonical `adipate(2-)`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:17128`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:adipate` in `BacDive_Metabolite_utilization` with count
  `466`, matching `source_occurrences`.
- `mappings/ingredient_mappings.sssom.tsv` row 350 maps `MIM:Adipate` to
  `CHEBI:17128` with the expected `PROMOTED` trailer.
- The top-level `notes` still say the MicrobeDecoder import had no CAS or
  CHEBI/NCIT match and needed curator review even though the same file now maps
  to `CHEBI:17128`.
- Advisory rows under `mappings/record_research_validation.tsv` are stale:
  they include an Edison status conflict that the same TSV later marks resolved
  by the Claude lane, and a now-actionable `FIELD_MISSING` row for ChEBI
  chemistry.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence,
  advisory research-validation rows, generated indexes, and ignored aggregate
  backups.

## Completeness

- The record is missing `chemical_properties` even though ChEBI and PubChem have
  formula and structure metadata for the `CHEBI:17128` dianion.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Adipate.yaml`, refresh the stale top-level
  `notes` to record the deliberate `CHEBI:17128` close mapping.
- Add `chemical_properties` from `CHEBI:17128`/PubChem CID `200164`, keeping the
  dianion formula and structure distinct from neutral adipic acid.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adipate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
