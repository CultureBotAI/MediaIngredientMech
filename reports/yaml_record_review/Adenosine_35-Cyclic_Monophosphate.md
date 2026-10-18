# `data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml`

## Verdict

Pass with minor issues. The CAS-backed `CHEBI:17489` identity, exact synonyms,
ChEBI chemistry, SSSOM row, and aggregate copy pass; one historical
auto-backfill change string has truncated structure text.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17489` with
  `ontology_mapping.ontology_id: CHEBI:17489`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:17489` to
  `3',5'-cyclic AMP` with formula `C10H12N5O6P`, CAS `60-92-4`, SMILES,
  InChI, and InChIKey `IVOMOUWHDPKRLL-KQYNXXCUSA-N`.
- The stored synonyms are exact ChEBI synonyms for `CHEBI:17489`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adenine_Hydrochloride_Hydrate.yaml data/ingredients/mapped/Adenomycin.yaml data/ingredients/mapped/Adenosine.yaml data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml data/ingredients/mapped/Adenosine_5-monophosphate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned the expected labels and aliases for the ChEBI targets in this batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16335 CHEBI:17489 CHEBI:16027 CHEBI:16708`:
  returned formula and structure metadata for all four ChEBI terms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS lookup, official ChEBI record, and local OAK metadata
  support the exact `CHEBI:17489` identity.
- The official ChEBI page and local OAK metadata support the stored formula,
  SMILES, and InChI.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records that the
  proposed `Adenosine 3,5-Cyclic Monophosphate` enrichment was already
  represented by the preferred term or synonyms.
- `mappings/ingredient_mappings.sssom.tsv` row 348 maps
  `MIM:Adenosine_35-Cyclic_Monophosphate` to `CHEBI:17489` with the expected
  exact-synonym and CAS `other` strings.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, synonym-enrich review row, generated indexes, and ignored
  aggregate backups.

## Completeness

- CAS, formula, SMILES, InChI, exact synonyms, curation history, and
  `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally annotate the stale 2026-05-01 history `changes` prose in
  `data/ingredients/mapped/Adenosine_35-Cyclic_Monophosphate.yaml`; the active
  `chemical_properties` fields are already correct.
