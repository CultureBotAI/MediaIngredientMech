# `data/ingredients/mapped/Gallium_Iiichloride.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback record represents gallium trichloride,
PubChem confirms the stored CAS-backed structure, and the final SSSOM row is an
expected exact CAS registry row.

## Identity

- Reviewed record: `data/ingredients/mapped/Gallium_Iiichloride.yaml`.
- Identifier and grounding: `identifier: cas:13450-90-3` with matching
  `ontology_mapping.ontology_id`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by stored CID 26010 resolved to `Gallium chloride` with
  formula `Cl3Ga`, InChI `InChI=1S/3ClH.Ga/h3*1H;/q;;;+3/p-3`, and SMILES
  `Cl[Ga](Cl)Cl`, agreeing with `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gallate_Formate.yaml data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gallium_Iiichloride.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this CAS-primary registry record
  because Engine A/OBO term validation does not cover CAS registry CURIEs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same CAS
  identifier, CultureBotHT source, CAS RN, PubChem CID, structure fields, one
  CultureBot occurrence, and ingredient type as the per-record YAML.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the CAS row as
  an expected registry identifier, and `mappings/mim_curie_aliases.tsv`
  preserves the pre-slugged `MIM:Gallium~28III~29chloride` subject as an alias
  of `MIM:Gallium_Iiichloride`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Gallium_Iiichloride` to `cas:13450-90-3` with `skos:exactMatch` and
  exports only `CAS:13450-90-3` in `other`.
- The record has no inferred nutritional, physicochemical, component, synonym,
  or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, MIM subject alias row, row-review decision, expected CAS unknown-term
  triage row, generated indexes, and ignored aggregate backups.

## Completeness

- The exact CAS registry identity, structure fields, one CultureBot occurrence,
  and final SSSOM row are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
