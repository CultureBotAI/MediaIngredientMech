# `data/ingredients/mapped/Indigocarmine.yaml`

## Verdict

Pass. The CultureMech exact ChEBI mapping, CAS-backed structure fields, ChEBI
and kg-microbe synonyms, PH indicator role, raw-role filtering, and final
SSSOM row all describe indigo carmine.

## Identity

- Reviewed record: `data/ingredients/mapped/Indigocarmine.yaml`.
- Identifier and grounding: `identifier: CHEBI:31695` with
  `ontology_mapping.ontology_id: CHEBI:31695`, label `indigo carmine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:31695`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `860-22-0`, formula `C16H8N2O8S2.2Na`, InChI
  `InChI=1S/C16H10N2O8S2.2Na/c19-15-9-5-7(27(21,22)23)1-3-11(9)17-13(15)14-16(20)10-6-8(28(24,25)26)2-4-12(10)18-14;;/h1-6,17-18H,(H,21,22,23)(H,24,25,26);;/q;2*+1/p-2/b14-13+;;`,
  and SMILES
  `O=C1/C(=C2Nc3ccc(S(=O)(=O)[O-])cc3C2=O)Nc2ccc(S(=O)(=O)[O-])cc21.[Na+].[Na+]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Impenum_Monohydrate.yaml data/ingredients/mapped/Indigocarmine.yaml data/ingredients/mapped/Indochrome.yaml data/ingredients/mapped/Indole-3-acetate.yaml data/ingredients/mapped/Indole-3-butyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4-file CHEBI/OBO subset;
  `Indochrome` was outside adapter scope because it uses a local
  `kgmicrobe.compound` identifier.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1545`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1545`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:31695` as the active ChEBI class `indigo carmine`, with
  CAS xref `860-22-0`, formula `C16H8N2O8S2.2Na`, the same ChEBI InChI and
  SMILES stored on the record, and all inspected exported names as ChEBI
  synonyms.
- PubChem resolves CAS RN `860-22-0` to a disodium indigo-carmine compound
  with the expected condensed formula.
- `physicochemical_roles.PH_INDICATOR` is backed by imported CultureMech
  `DATABASE_ENTRY` evidence that quotes the original role text.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Indigocarmine`
  to `CHEBI:31695` and exports inspected synonyms plus `CAS:860-22-0` in
  `other`; it correctly omits the object-label duplicate `Indigo carmine` and
  filters the raw `Role: pH indicator; Properties: ...` text.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, inspected
  synonyms, PH indicator role evidence, aggregate copy, and final SSSOM row
  are present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
