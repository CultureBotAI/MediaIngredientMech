# `data/ingredients/mapped/Hygromycin_B.yaml`

## Verdict

Needs curation. The CAS-derived exact ChEBI identity, structure fields,
systematic synonym, CAS alias, and final SSSOM row pass, but
`SELECTIVE_AGENT` is still only a provisional name-pattern assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Hygromycin_B.yaml`.
- Identifier and grounding: `identifier: CHEBI:16976` with
  `ontology_mapping.ontology_id: CHEBI:16976`, label `hygromycin B`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `31282-04-9`, formula `C20H37N3O13`, populated
  InChI, and populated SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hygromycin.yaml data/ingredients/mapped/Hygromycin_A.yaml data/ingredients/mapped/Hygromycin_B.yaml data/ingredients/mapped/Hymecromone_Methyl_Ether.yaml data/ingredients/mapped/Hypotaurine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hygromycin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1520`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1520`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16976` as the active ChEBI class `hygromycin B` and
  lists the stored systematic name as an exact synonym.
- PubChem resolves CAS RN `31282-04-9` to `Hygromycin B` with formula
  `C20H37N3O13`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Hygromycin_B`
  to `CHEBI:16976` and exports only the inspected ChEBI synonym plus
  `CAS:31282-04-9` in `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureBotHT, FEBA, Hans80, or literature evidence attached to the
  claim.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  aggregate copy, and final SSSOM row are present and consistent.
- The record is incomplete until the selective-agent role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `physicochemical_roles.SELECTIVE_AGENT` unless an inspected
  CultureBotHT, FEBA, Hans80, or literature source can support hygromycin B as
  a selective agent, then rerun strict, term, round-trip, id-label, component,
  and SSSOM validation.
