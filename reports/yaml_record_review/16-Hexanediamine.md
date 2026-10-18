# `data/ingredients/mapped/16-Hexanediamine.yaml`

## Verdict

Needs curation, major. The stripped CAS fallback still denotes
`1,6-Hexanediamine`, but PubChem now carries an exact `CHEBI:39618`
cross-reference and the ChEBI page resolves to the same CAS-backed compound.

## Identity

- Reviewed record: `data/ingredients/mapped/16-Hexanediamine.yaml`.
- Current identifier and grounding: `identifier: cas:124-09-4`,
  `ontology_mapping.ontology_id: cas:124-09-4`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem check: CAS `124-09-4` resolves to CID `16402`,
  `Hexamethylenediamine`, formula `C6H16N2`, SMILES `C(CCCN)CCN`, and InChI
  `InChI=1S/C6H16N2/c7-5-3-1-2-4-6-8/h1-8H2`.
- Current promotion target: PubChem CID `16402` lists synonym `CHEBI:39618`, and
  the EMBL-EBI ChEBI page for `CHEBI:39618` lists `1,6-hexanediamine`,
  `1,6-diaminohexane`, `hexamethylenediamine`, CAS `124-09-4`, formula
  `C6H16N2`, and the same InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/14-naphthoquinone.yaml data/ingredients/mapped/15-Pentanediol.yaml data/ingredients/mapped/16-Hexanediamine.yaml data/ingredients/mapped/18-Crown-6.yaml data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- LinkML term validation was skipped because the active record intentionally
  points at `cas:124-09-4`, not an Engine A OBO term.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected registry row
  for `cas:124-09-4` with `validation_status: UNKNOWN_TERM`.

## Evidence

- The 2026-08-16 leading-zero repair was real: the maintained YAML and
  production SSSOM now use canonical `124-09-4` rather than padded
  `0124-09-4`.
- Major: the `FALLBACK_REGISTRY` mapping is stale because current PubChem and
  ChEBI expose `CHEBI:39618` as an exact CAS-backed target for the same
  compound.
- The fallback record has no formula, SMILES, or InChI even though both PubChem
  and ChEBI now provide structure-derived values for the same anhydrous
  compound.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found old queue rows for
  `cas:0124-09-4`; those rows are stale after #310, but the ChEBI promotion is
  a live issue.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Empty component and role slots are acceptable for this single chemical.
- The missing structure fields are no longer an unavoidable CAS-fallback gap
  once the record is promoted to an exact ChEBI mapping.

## Recommended Edits

1. In `data/ingredients/mapped/16-Hexanediamine.yaml`, promote the record from
   `cas:124-09-4`/`FALLBACK_REGISTRY` to exact `CHEBI:39618` with ChEBI label
   `1,6-hexanediamine`; preserve CAS `124-09-4` in `chemical_properties.cas_rn`.
2. Populate formula `C6H16N2`, SMILES, and InChI from the exact ChEBI/PubChem
   identity.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
4. Re-run strict/LinkML validation, Engine A OBO validation, and SSSOM export
   checks after promotion.
