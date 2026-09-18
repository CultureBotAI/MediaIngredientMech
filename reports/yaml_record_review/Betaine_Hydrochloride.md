# `data/ingredients/mapped/Betaine_Hydrochloride.yaml`

## Verdict

Needs curation, major. The CAS and occurrence evidence denote betaine
hydrochloride, but the record is still modeled as a CAS primary with a
`CHEBI:17750` glycine betaine parent even though OLS now exposes exact
`CHEBI:749379` `betaine hydrochloride`; its SMILES, InChI, PubChem CID, and
only synonym are still inherited from glycine betaine rather than the chloride
salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Betaine_Hydrochloride.yaml`.
- Current primary identity: `identifier: cas:590-46-5` and
  `chemical_properties.cas_rn: 590-46-5`.
- Current ontology anchor: `ontology_mapping.ontology_id: CHEBI:17750`,
  `ontology_label: glycine betaine`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- OLS search now returns exact `CHEBI:749379` for `betaine hydrochloride`.
  The term has formula `Cl.C5H12NO2`, InChI
  `InChI=1S/C5H11NO2.ClH/c1-6(2,3)4-5(7)8;/h4H2,1-3H3;1H`, and SMILES
  `C[N+](C)(C)CC(=O)O.[Cl-]`.
- PubChem resolves CAS `590-46-5` to CID 11545 with formula `C5H12ClNO2` and
  the same chloride-containing InChI/SMILES as `CHEBI:749379`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-d-glucose.yaml data/ingredients/mapped/Beta-gentiobiose.yaml data/ingredients/mapped/Beta-lactose.yaml data/ingredients/mapped/Beta-nad.yaml data/ingredients/mapped/Betaine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative `CHEBI:17750` narrow-match SSSOM
  row at `mappings/ingredient_mappings.sssom.tsv` row 583, the CAS registry row
  at row 584, the kg-microbe registry row at row 585, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The CAS and kg-microbe rows were legitimate registry rows for the historical
  `narrowMatch` pattern, but they are stale once the record is promoted to an
  exact CHEBI primary.
- `mappings/culturemech_recipe_membership.tsv` contains three rows for
  `cas:590-46-5`, matching the record's refreshed 3/3 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- Major gap: the ontology mapping should be exact to `CHEBI:749379` rather than
  a narrow match to `CHEBI:17750`.
- Major gap: `chemical_properties.pubchem_cid: 247`, SMILES
  `C[N+](C)(C)CC(=O)[O-]`, and the stored InChI describe parent glycine
  betaine. The formula was corrected to the hydrochloride salt, but the rest of
  the structure block was not.
- Major gap: `(trimethylammonio)acetate` is an exact synonym of glycine
  betaine, not of the hydrochloride salt.

## Recommended Edits

- Major: update `data/ingredients/mapped/Betaine_Hydrochloride.yaml` to use
  `CHEBI:749379` `betaine hydrochloride` as its primary exact mapping and keep
  CAS `590-46-5` as a chemical property rather than as the primary identifier.
- Major: replace the parent-derived SMILES, InChI, and PubChem CID with the
  chloride-containing values from `CHEBI:749379` or PubChem CID 11545.
- Major: remove or demote the parent glycine betaine synonym
  `(trimethylammonio)acetate`.
- After synchronization, rebuild the SSSOM so the obsolete `CHEBI:17750`
  narrow-match and registry rows are replaced by the exact CHEBI row, then run
  focused strict/term validation and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
