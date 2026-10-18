# `data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`

## Verdict

Needs curation; major issue. The current parent `CHEBI:17126` mapping and
companion CAS row obey the narrow-match export contract, but OLS now contains
active `NCIT:C216679` with the exact label `DL-Carnitine Hydrochloride`; its
CAS conflicts with this record, so the exact candidate needs a targeted
curation decision.

## Identity

- Reviewed record: `data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:461-06-3`,
  `ontology_mapping.ontology_id: CHEBI:17126`,
  `ontology_label: carnitine`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:17126` returns active parent carnitine with CAS
  `461-06-3`, formula `C7H15NO3`, and the same InChI/SMILES as the local
  `chemical_properties`.
- PubChem resolves CAS `461-06-3` to CID `288` with formula `C7H15NO3` and the
  same carnitine InChI/SMILES as the local record.
- PubChem resolves the label `DL-carnitine hydrochloride` to CID `5970`, a
  chloride salt with formula `C7H16ClNO3`, so the source label's hydrochloride
  wording is chemically narrower than the stored parent carnitine structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carboxymethyl_Cellulose`, then stopped on `Carcinomycin` because
  the local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the three active
  `MIM:Carnitine_Dl_Hydrochloride` SSSOM rows: a `skos:narrowMatch` to parent
  `CHEBI:17126`, an exact registry row for `cas:461-06-3`, and an exact local
  kgmicrobe registry row. The same search also found the expected row-review
  notes for registry CURIEs that neither OAK nor OLS resolves.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `cas:461-06-3`, matching `occurrence_statistics` `0/0`.
- Direct exact OLS search for `DL-carnitine hydrochloride` found active
  `NCIT:C216679`, exactly labelled `DL-Carnitine Hydrochloride`. That term
  carries CAS `461-05-2`, which conflicts with this record's CAS `461-06-3`
  and with the sibling `Carnitine_Hydrochloride` record's curation note that
  rejected `461-05-2` because ChEBI assigns that CAS to carnitinamide chloride.

## Completeness

- The broader ChEBI parent, exact CAS registry row, exact local registry row,
  0/0 occurrence count, SSSOM rows, aggregate copy, and docs rows are
  populated.
- The record has no role or component assertions requiring extra evidence.

## Recommended Edits

- Major: decide whether `NCIT:C216679` is a valid exact mapping despite its
  conflicting `461-05-2` CAS annotation. If it is valid, promote
  `data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml` from the CAS
  registry identifier and parent `CHEBI:17126` mapping to the NCIT exact term
  while preserving any needed CAS/local companion rows; if not, add a
  discussion explaining why the exact-label NCIT candidate is rejected. Then
  rerun strict validation, term validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
