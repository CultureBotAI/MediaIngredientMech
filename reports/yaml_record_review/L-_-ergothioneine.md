# `data/ingredients/mapped/L-_-ergothioneine.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI lookup identity, active ChEBI term, formula,
PubChem structure, ChEBI synonym, empty occurrence count, and final SSSOM row
are consistent, but `AMINO_ACID_SOURCE` is only provisional ChEBI-ancestry
evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/L-_-ergothioneine.yaml`.
- Identifier and grounding: `identifier: CHEBI:4828` with
  `ontology_mapping.ontology_id: CHEBI:4828`, label `ergothioneine`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `497-30-3`, molecular formula `C9H15N3O2S`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Pipecolic_Acid.yaml data/ingredients/mapped/L-Pyroglutamic_Acid.yaml data/ingredients/mapped/L-Rhamnose_Monohydrate.yaml data/ingredients/mapped/L-Xylose.yaml data/ingredients/mapped/L-_-ergothioneine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:4828` as active `ergothioneine` and lists
  `(2S)-3-(2-mercapto-1H-imidazol-5-yl)-2-(trimethylazaniumyl)propanoate` as a
  synonym, supporting the CAS lookup identity and curated synonym.
- PubChem resolves CAS RN `497-30-3` to CID `5351619` with formula
  `C9H15N3O2S` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:4828` with
  only the ChEBI exact synonym and `CAS:497-30-3` in `other`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry, with no inspected
  CultureMech, FEBA, Hans80, or literature evidence attached to the role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, and OAK/OLS row-review confirmation.

## Completeness

- The active ChEBI identity, CAS RN, formula, ChEBI synonym, structure,
  aggregate copy, empty occurrence count, and final SSSOM row are present and
  consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-(+)-
  ergothioneine as an amino acid source.
- Rerun strict, term, round-trip, role, component, and SSSOM validation after
  the role change.
