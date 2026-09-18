# `data/ingredients/mapped/Kh2po4.yaml`

## Verdict

Needs curation. The exact potassium dihydrogen phosphate identity, CAS value,
structure fields, occurrence count, and buffer role are consistent, but final
SSSOM still exports non-synonym `KH PO` and concentration-qualified CultureMech
surface forms.

## Identity

- Reviewed record: `data/ingredients/mapped/Kh2po4.yaml`.
- Identifier and grounding: `identifier: CHEBI:63036` with
  `ontology_mapping.ontology_id: CHEBI:63036`, label
  `potassium dihydrogen phosphate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7778-77-0`, molecular formula `H2O4P.K`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kcl.yaml data/ingredients/mapped/Keratin.yaml data/ingredients/mapped/Ketomycin.yaml data/ingredients/mapped/Kf.yaml data/ingredients/mapped/Kh2po4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:63036` as active ChEBI term
  `potassium dihydrogen phosphate` and lists `MKP`, `Monopotassium phosphate`,
  and the other long-form phosphate names stored on the YAML record as
  same-substance aliases.
- PubChem resolves CAS RN `7778-77-0` with the same InChI and an equivalent
  `OP(=O)(O)[O-].[K+]` salt SMILES, supporting the stored CAS and structure
  fields.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Kh2po4` to
  `CHEBI:63036`.
- Major: final SSSOM `other` includes `KH PO`, which is not a ChEBI synonym for
  `CHEBI:63036` and loses the phosphate digits.
- Major: final SSSOM `other` includes `KH2PO4 (0.4 g/l)` and
  `KH2PO4 (7% w/v)`, which are concentration-qualified recipe labels rather
  than exact synonyms for the chemical identity.
- The raw CultureMech role/property pseudo-synonyms are filtered out of the
  final SSSOM and do not themselves create a published synonym defect.
- `physicochemical_roles.BUFFER` is supported by the original CultureMech
  `Buffer` role text and the current 5649 occurrence count.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, residual alias rows, and the
  synonym-enrichment review row; it found no hits in
  `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, formula, structure fields, aggregate
  copy, occurrence count, and buffer role are present and consistent.
- The record is incomplete until non-identity formula fragments and
  concentration labels stop publishing as SSSOM `other` tokens.

## Recommended Edits

- Major: remove or demote `KH PO`, `KH2PO4 (0.4 g/l)`, and
  `KH2PO4 (7% w/v)` in `data/ingredients/mapped/Kh2po4.yaml`, then regenerate
  the aggregate and final SSSOM so these tokens disappear from
  `mappings/ingredient_mappings.sssom.tsv`; rerun strict, term, round-trip,
  component, and SSSOM validation.
