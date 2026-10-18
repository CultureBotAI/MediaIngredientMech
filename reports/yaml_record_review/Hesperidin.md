# `data/ingredients/mapped/Hesperidin.yaml`

## Verdict

Pass. The exact `hesperidin` ChEBI identity, CAS RN, structure fields, ChEBI
synonym, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Hesperidin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28775` with
  `ontology_mapping.ontology_id: CHEBI:28775`, label `hesperidin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `520-26-3`, formula `C28H34O15`, InChI
  `InChI=1S/C28H34O15/c1-10-21(32)23(34)25(36)27(40-10)39-9-19-22(33)24(35)26(37)28(43-19)41-12-6-14(30)20-15(31)8-17(42-18(20)7-12)11-3-4-16(38-2)13(29)5-11/h3-7,10,17,19,21-30,32-37H,8-9H2,1-2H3/t10-,17-,19+,21-,22+,23+,24-,25+,26+,27+,28+/m0/s1`,
  and SMILES
  `COc1ccc([C@@H]2CC(=O)c3c(O)cc(O[C@@H]4O[C@H](CO[C@@H]5O[C@@H](C)[C@H](O)[C@@H](O)[C@H]5O)[C@@H](O)[C@H](O)[C@H]4O)cc3O2)cc1O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hesperidin.yaml data/ingredients/mapped/Hexachlorocyclo-hexane.yaml data/ingredients/mapped/Hexadecane.yaml data/ingredients/mapped/Hexadecanoate.yaml data/ingredients/mapped/Hexane.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:28775`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1424`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1424`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:28775` as active `hesperidin`, with `Hesperidin` and
  the stored IUPAC-like name as synonyms.
- PubChem resolves CAS RN `520-26-3` to `Hesperidin`, formula `C28H34O15`, and
  the same InChI.
- The final SSSOM exports the stored ChEBI synonym and `CAS:520-26-3`; both
  are valid exact tokens for this subject.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hesperidin` to
  `CHEBI:28775`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review `CONFIRMED` decision.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, synonym, final
  SSSOM row, and synchronized aggregate entry are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- None.
