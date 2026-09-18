# `data/ingredients/mapped/Artepaulin.yaml`

## Verdict

Needs curation; severity blocker. The record is a CAS fallback for
`cas:13902-54-0`, but current PubChem evidence separates that CAS from the CID
that carries the `ARTEPAULIN` synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Artepaulin.yaml`.
- Identifier and grounding: `identifier: cas:13902-54-0` with
  `ontology_mapping.ontology_id: cas:13902-54-0`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem Registry Number lookup for `13902-54-0` resolves only CID `10977881`;
  that CID's synonym list contains `13902-54-0` but not `Artepaulin`.
- PubChem name lookup for `Artepaulin` resolves CIDs `325292` and `73440797`.
  CID `325292` carries synonym `ARTEPAULIN` and ChEBI cross-reference
  `CHEBI:174307`.
- OLS resolves `CHEBI:174307` as non-obsolete ChEBI `Cadabicilone` with the
  same first InChIKey block and formula as PubChem CID `325292`, not as a
  synonym or cross-reference of CAS `13902-54-0`.
- The active record therefore no longer proves that its preferred name and CAS
  identifier denote the same stereospecific compound.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Artepaulin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the CAS sqlite adapter with `sqlite3.OperationalError: no such
  table: rdfs_label_statement`. This matches the repository contract: CAS
  registry CURIEs are skipped by `just validate-terms` and must be reviewed as
  fallback registry identifiers.
- PubChem lookups for the CAS, the `Artepaulin` name, and the returned CIDs
  confirmed a name/CAS mismatch in the current fallback.
- OLS4 lookup for `CHEBI:174307` resolved a current non-obsolete ChEBI term for
  the PubChem CID that carries the Artepaulin name.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs corresponded and 104 non-blocking plausibility
  warnings were reported.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; docs
  data were fresh and every curated label was resolvable.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` row 480 exactly maps
  `MIM:Artepaulin` to `cas:13902-54-0`, so downstream consumers will treat the
  record as the CAS RN compound.
- `mappings/ingredient_mappings_row_review_manifest.tsv` row 324 only verified
  that a CAS registry object was expected and self-referential; it did not prove
  that CAS `13902-54-0` still denotes Artepaulin.
- A hidden, ignored-inclusive search across the full checkout, excluding stale
  `data/curated/backups`, generated docs, HTML coverage, and review output,
  found no maintained `compounds_to_cas.csv` source row for `Artepaulin`,
  `13902-54-0`, or PubChem CID `10977881`. The local provenance bottoms out in
  the YAML, SSSOM row, and row-review TSVs.

## Completeness

- The record is structurally complete for a CAS fallback and correctly has zero
  CultureMech occurrences.
- Chemical structure fields are absent; that was acceptable while the CAS was
  an unpromoted fallback, but the present name/CAS mismatch is consequential
  and must be resolved before any structure should be backfilled.
- No roles, components, environmental context, datasets, or discussion entries
  are needed until the exact identity is repaired.

## Recommended Edits

- In `data/ingredients/mapped/Artepaulin.yaml`, re-evaluate the CultureBotHT
  source name and CAS. If `Artepaulin` should follow PubChem/ChEBI, reground it
  to the exact supported ChEBI/CAS identity instead of `cas:13902-54-0`.
- If CAS `13902-54-0` is intentionally retained, rename the record to the
  compound denoted by that CAS and preserve `Artepaulin` only as rejected or
  discussion provenance.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv` from the maintained record and rerun
  strict validation plus SSSOM invariants.
