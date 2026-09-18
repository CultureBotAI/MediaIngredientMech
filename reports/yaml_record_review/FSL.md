# `data/ingredients/mapped/FSL.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback identifies a PubChem-backed defined
chemical, the current exact CHEBI/NCIT search still has no replacement term,
and the final registry SSSOM row is clean.

## Identity

- Reviewed record: `data/ingredients/mapped/FSL.yaml`.
- Identifier and grounding: `identifier: cas:322455-70-9` with matching
  `ontology_mapping.ontology_id`, canonical label `FSL`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `322455-70-9` resolved to CID 87858248 with formula
  `C84H140N14O18S` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/FSL.yaml data/ingredients/mapped/Fad.yaml data/ingredients/mapped/Farm_soil.yaml --out /tmp/mim_f_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `cas` registry prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, CAS RN, formula, InChI, SMILES, and PubChem CID as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:FSL` to
  `cas:322455-70-9` with `skos:exactMatch` and exports only
  `CAS:322455-70-9` as an `other` token.
- A fresh exact OLS4 search by CAS RN against CHEBI and NCIT returned no
  documents, so the existing CAS fallback is still the best available
  grounding among the reviewed targets.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` keeps this registry
  identifier because the CAS object ID matches the YAML identifier and
  `chemical_properties.cas_rn`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:FSL`,
  `cas:322455-70-9`, and `322455-70-9` found the active YAML, aggregate copy,
  final SSSOM row, row-review and UNKNOWN_TERM provenance, and ignored
  aggregate backups; it did not expose a contradictory active mapping.

## Completeness

- The CAS fallback identity, CAS RN, structure fields, PubChem CID, ingredient
  type, and final SSSOM payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
