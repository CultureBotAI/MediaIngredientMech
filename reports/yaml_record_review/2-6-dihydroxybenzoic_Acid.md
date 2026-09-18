# `data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`

## Verdict

Needs curation, major. The preferred label and stripped CAS RN now identify
`2,6-dihydroxybenzoic acid`, but the record is still a CAS fallback even though
PubChem now exposes an exact `CHEBI:68465` target, and the invalid
`2-6-dihydroxybenzoic acid` surface still leaks into generated labels.

## Identity

- Reviewed record: `data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`.
- Current identifier and grounding: `identifier: cas:303-07-1`,
  `ontology_mapping.ontology_id: cas:303-07-1`,
  `ontology_mapping.ontology_label: 2-6-dihydroxybenzoic acid`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem check: CAS `303-07-1` resolves to CID `9338`,
  `2,6-Dihydroxybenzoic Acid`, formula `C7H6O4`, and InChI
  `InChI=1S/C7H6O4/c8-4-2-1-3-5(9)6(4)7(10)11/h1-3,8-9H,(H,10,11)`.
- Current promotion target: PubChem CID `9338` lists synonym `CHEBI:68465`, and
  the EMBL-EBI ChEBI page for `CHEBI:68465` resolves to
  `2,6-dihydroxybenzoic acid`, CAS `303-07-1`, formula `C7H6O4`, and the same
  InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/14-naphthoquinone.yaml data/ingredients/mapped/15-Pentanediol.yaml data/ingredients/mapped/16-Hexanediamine.yaml data/ingredients/mapped/18-Crown-6.yaml data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- LinkML term validation was skipped because the active record intentionally
  points at `cas:303-07-1`, not an Engine A OBO term.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected registry row
  for `cas:303-07-1`, but its object label is still the impossible
  `2-6-dihydroxybenzoic acid` text.

## Evidence

- The 2026-08-08 locant repair fixed `preferred_term` to
  `2,6-dihydroxybenzoic acid`, and the 2026-08-16 leading-zero repair fixed the
  maintained CAS RN to `303-07-1`.
- Major: the `FALLBACK_REGISTRY` mapping is stale because current PubChem and
  ChEBI expose `CHEBI:68465` as an exact CAS-backed target for the same
  compound.
- Major: the invalid `2-6-dihydroxybenzoic acid` source text remains in
  `ontology_mapping.ontology_label` and as a `synonyms` entry, which publishes
  the comma-truncation artifact into SSSOM/docs object labels and the label
  index.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found old queue rows for
  `cas:0303-07-1`; those rows are stale after #310, but the ChEBI promotion and
  invalid exported fallback label are live issues.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Empty component and role slots are acceptable for this single chemical.
- The missing formula and structure fields are no longer an unavoidable
  CAS-fallback gap once the record is promoted to an exact ChEBI mapping.

## Recommended Edits

1. In `data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`, promote the
   record from `cas:303-07-1`/`FALLBACK_REGISTRY` to exact `CHEBI:68465` with
   ChEBI label `2,6-dihydroxybenzoic acid`.
2. Remove `2-6-dihydroxybenzoic acid` from generated label-bearing fields; if
   the malformed source spelling must be retained, keep it only as traced raw
   source text that does not export as a synonym.
3. Populate formula `C7H6O4`, SMILES, and InChI from the exact ChEBI/PubChem
   identity.
4. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
5. Re-run strict/LinkML validation, Engine A OBO validation, the truncated
   locant audit, and SSSOM export checks after promotion.
