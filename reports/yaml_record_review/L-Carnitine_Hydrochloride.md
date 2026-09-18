# `data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml`

## Verdict

Pass. The CAS-to-ChEBI lookup identity, exact ChEBI salt grounding, CAS value,
structure fields, IUPAC synonym, empty occurrence count, and final SSSOM row are
consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:233463` with
  `ontology_mapping.ontology_id: CHEBI:233463`, label `levocarnitine chloride`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `6645-46-1`, molecular formula `C7H15NO3.HCl`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Carnitine.yaml data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml data/ingredients/mapped/L-Cysteic_Acid_Monohydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2330`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2330`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `CHEBI:233463` as active ChEBI term
  `levocarnitine chloride`, with CAS xref `6645-46-1`, formula
  `C7H15NO3.HCl`, InChI, SMILES, and the same exact IUPAC synonym stored on the
  YAML record.
- PubChem resolves CAS RN `6645-46-1` with equivalent formula `C7H16ClNO3` and
  the same InChI as the YAML record, supporting the stored CAS and structure
  fields.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:L-Carnitine_Hydrochloride` to `CHEBI:233463` with the ChEBI IUPAC
  synonym and `CAS:6645-46-1` in `other`.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and row-review dispositions; it found no
  hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The exact ChEBI identity, CAS value, structure fields, aggregate copy, empty
  occurrence count, and final SSSOM row are present and consistent.
- No nutritional, physicochemical, cellular, or community role claim is present
  that would require additional claim-level evidence.

## Recommended Edits

- None.
