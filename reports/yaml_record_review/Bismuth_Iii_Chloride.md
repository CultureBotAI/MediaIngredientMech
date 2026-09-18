# `data/ingredients/mapped/Bismuth_Iii_Chloride.yaml`

## Verdict

Needs curation, major. The CAS `7787-60-2` identity, bismuth trichloride
structure fields, SSSOM row, occurrence count, and aggregate copy agree, but a
live OLS exact search now exposes `mesh:C534543` `bismuth trichloride`, so the
CAS fallback should be reviewed for promotion to an external ontology term.

## Identity

- Reviewed record: `data/ingredients/mapped/Bismuth_Iii_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:7787-60-2` with
  `ontology_mapping.ontology_id: cas:7787-60-2`,
  `ontology_label: bismuth(III) chloride`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `ingredient_type: SINGLE_INGREDIENT`,
  and `mapping_status: MAPPED`.
- PubChem resolves CAS `7787-60-2` to CID 24591, title
  `Bismuth trichloride`, formula `BiCl3`, and the same standard InChI and
  SMILES stored in `chemical_properties`.
- Live OLS exact search still found no exact `bismuth(III) chloride` document,
  but exact search for PubChem's `Bismuth trichloride` label found
  `mesh:C534543`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Bismuth_Iii_Chloride.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation is intentionally skipped for this record because CAS
  registry CURIEs have no OBO adapter; SSSOM unknown-term triage already
  classifies `cas:7787-60-2` as an expected registry identifier.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the CAS SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 608, the expected-registry row
  in `mappings/ingredient_mappings_unknown_term_triage.tsv`, the row-review
  manifest disposition, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- A second hidden/ignored-inclusive search over the same local paths found no
  existing `mesh:C534543`, `C534543`, or `bismuth trichloride` triage note.
- The local SSSOM row maps `MIM:Bismuth_Iii_Chloride` to `cas:7787-60-2` with
  `skos:exactMatch`, matching the current primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The CAS identifier, formula, InChI, SMILES, PubChem CID, occurrence count,
  expected-CAS-fallback SSSOM row, and aggregate copy are populated.
- Major gap: the fallback registry mapping predates the live MeSH exact term and
  should be re-reviewed; if `mesh:C534543` is accepted, the primary identifier,
  mapping evidence, and SSSOM row need synchronized promotion.

## Recommended Edits

- Major: evaluate `mesh:C534543` for exact identity to bismuth(III) chloride in
  `data/ingredients/mapped/Bismuth_Iii_Chloride.yaml`; if accepted, promote the
  CAS fallback to MeSH, retain CAS `7787-60-2` in `chemical_properties`, rebuild
  the SSSOM row, then run `just sync-curated`, focused strict/term validation,
  and `just qc-sssom`.
