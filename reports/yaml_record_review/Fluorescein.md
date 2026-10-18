# `data/ingredients/mapped/Fluorescein.yaml`

## Verdict

Needs curation, with a major chemical-ontology grounding gap. The NCIT target is
an exact fluorescein class, but it cross-references `CHEBI:31624`, and a CHEBI
identity should be used for this MicrobeDecoder chemical so ChEBI structure
fields and the single-ingredient type can be populated.

## Identity

- Reviewed record: `data/ingredients/mapped/Fluorescein.yaml`.
- Identifier and grounding: `identifier: NCIT:C61766` with matching
  `ontology_mapping.ontology_id`, label `Fluorescein`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- EBI OLS for NCIT resolves `NCIT:C61766` as `Fluorescein`, marks it
  non-obsolete, and exposes `CHEBI_ID: CHEBI:31624`.
- PubChem lookup by NCIT's CAS RN `2321-07-5` resolved to CID 16850 titled
  `Fluorescein` with formula `C20H12O5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fleroxacin.yaml data/ingredients/mapped/Flucloxacillin.yaml data/ingredients/mapped/Fluoranthene.yaml data/ingredients/mapped/Fluorene.yaml data/ingredients/mapped/Fluorescein.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fluorescein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  NCIT identifier, MicrobeDecoder source occurrence, missing
  `ingredient_type`, and absent ChEBI/PubChem structure fields as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fluorescein` to `NCIT:C61766` with `skos:exactMatch` and an empty
  `other` column.
- Major: this is an exact chemical mapping to NCIT even though the NCIT term
  itself cross-references the corresponding ChEBI fluorescein identity; using
  NCIT leaves the chemical record without `ingredient_type` or structure fields
  that should be available from ChEBI/PubChem.
- `mappings/microbedecoder_auto_mapped_review.tsv` only checked that the NCIT
  identifier resolved to the same label; its own note says it did not check
  wrong-sense class-level matches.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MicrobeDecoder approval row, and ignored
  historical batch reports.

## Completeness

- The exact `Fluorescein` source label and MicrobeDecoder source occurrence are
  populated.
- The record is missing CHEBI-first chemical grounding, ingredient type,
  structure fields, and the CAS RN attached to the NCIT/CHEBI/PubChem identity.

## Recommended Edits

- Major: remap `data/ingredients/mapped/Fluorescein.yaml` from `NCIT:C61766` to
  the corresponding ChEBI fluorescein identity, populate
  `ingredient_type: SINGLE_INGREDIENT` and source-backed structure fields, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
