# `data/ingredients/mapped/Galactomannan_From_Guar.yaml`

## Verdict

Needs curation, with major structure and unsupported-role issues. The CAS/local
identity rows and the broad parent mapping to ChEBI `galactomannan` are
coherent, but the stored PubChem structure is a small `D-Galacto-d-mannan`
oligosaccharide rather than the guar galactomannan ingredient, and
`CARBON_SOURCE` is still only a provisional name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Galactomannan_From_Guar.yaml`.
- Identifier and grounding: `identifier: cas:11078-30-1` with
  `ontology_mapping.ontology_id: CHEBI:27680`, canonical label
  `galactomannan`, source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:27680` as the active broad `galactomannan` class, "a
  heteroglycan consisting of a mannan backbone with galactose side groups".
- PubChem lookup by CAS RN `11078-30-1` resolved the stored CID 439336 as
  `D-Galacto-d-mannan` with formula `C18H32O16`, matching the recorded
  structure fields but not the source-specific guar polymer named by the MIM
  subject.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Galactomannan_From_Guar.yaml data/ingredients/mapped/Galactonate.yaml data/ingredients/mapped/Galactose.yaml data/ingredients/mapped/Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml data/ingredients/mapped/Galacturonate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this CAS-primary registry record
  because Engine A/OBO term validation does not cover CAS registry CURIEs.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same CAS
  identifier, broad ChEBI parent, CAS RN, PubChem CID, provisional carbon role,
  and ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` output has the expected
  Rule B1 shape for the non-exact ontology mapping: `skos:narrowMatch` to
  `CHEBI:27680`, an exact CAS registry row, and an exact
  `kgmicrobe.compound:galactomannan_from_guar` registry row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the CAS row and
  local kg-microbe row as expected registry identifiers, and the final SSSOM
  rows publish only `CAS:11078-30-1` in `other`.
- Major: `chemical_properties` stores formula, SMILES, InChI, and CID 439336
  for a defined `D-Galacto-d-mannan` oligosaccharide; those fields should not
  make the guar-derived galactomannan ingredient look like a single defined
  `C18H32O16` molecule.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with a
  provisional curator note; no inspected source in the record supports guar
  galactomannan as a medium carbon source.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  rows, synonym-enrichment decision, row-review decisions, and expected
  unknown-term triage rows.

## Completeness

- The broad galactomannan parent row, exact CAS registry row, local exact
  registry row, and CultureBotHT provenance are populated.
- Structure and ingredient-type fields are overspecified for this polymeric
  source material.

## Recommended Edits

- Major: in `data/ingredients/mapped/Galactomannan_From_Guar.yaml`, remove the
  CID 439336 small-molecule structure fields or replace them with a
  polymer-appropriate representation, and consider an ingredient type that does
  not assert a single defined chemical structure.
- Major: replace the provisional `CARBON_SOURCE` role with source-backed
  evidence or remove it.
- Regenerate `data/curated/mapped_ingredients.yaml` and final SSSOM, then rerun
  strict validation and SSSOM invariants.
