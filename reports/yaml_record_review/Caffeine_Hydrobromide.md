# `data/ingredients/mapped/Caffeine_Hydrobromide.yaml`

## Verdict

Pass. The caffeine hydrobromide CAS fallback identity, PubChem-derived
structure fields, CAS registry SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Caffeine_Hydrobromide.yaml`.
- Identifier and grounding: `identifier: cas:5743-18-0`,
  `ontology_mapping.ontology_id: cas:5743-18-0`,
  `ontology_label: Caffeine Hydrobromide`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The Engine A OBO label validator correctly skips this non-OBO CAS target.
- PubChem resolves CAS `5743-18-0` to CID 57351081 with formula
  `C8H11BrN4O2`, the same InChI and SMILES stored locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cadmium_Nitrate.yaml data/ingredients/mapped/Caffeic_Acid.yaml data/ingredients/mapped/Caffeine.yaml data/ingredients/mapped/Caffeine_Hydrobromide.yaml data/ingredients/mapped/Cahpo4.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Caffeine_Hydrobromide.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  skipped Engine A because the record uses a non-OBO `cas:` mapping target;
  strict validation and the SSSOM invariant validator covered the registry
  shape.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`, `docs/data`,
  and `reports`, excluding bulky backups and generated review-report
  directories, found the active SSSOM row, the exact aggregate copy, and the
  expected-registry row in `mappings/ingredient_mappings_unknown_term_triage.tsv`.
- The SSSOM row maps `MIM:Caffeine_Hydrobromide` to `cas:5743-18-0` with
  `skos:exactMatch`, matching both the YAML `identifier` and
  `chemical_properties.cas_rn`.
- The record was created from CultureBotHT rather than CultureMech media
  occurrences, so 0/0 occurrence statistics are expected.

## Completeness

- The CAS primary identifier, PubChem CID, formula, InChI, SMILES,
  single-ingredient classification, SSSOM row, and aggregate copy are
  populated.
- `synonyms: []` is acceptable here because no inspected source in this pass
  supplied exact aliases beyond the preferred term.

## Recommended Edits

- None for this record.
