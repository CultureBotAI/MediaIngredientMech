# `data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml`

## Verdict

Needs curation, blocker. The record label and registry fallback identify
different hydrochloride salts: PubChem resolves the stored CAS `3287-99-8` to
benzylamine hydrochloride, while `Benzylhydrazine Hydrochloride` resolves to a
two-nitrogen benzylhydrazine hydrochloride compound with CAS `1073-62-7`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml`.
- Current identifier and grounding: `identifier: cas:3287-99-8` with
  `ontology_mapping.ontology_id: cas:3287-99-8`,
  `ontology_label: Benzylhydrazine Hydrochloride`,
  `ontology_source: CAS`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- CAS `3287-99-8` resolves in PubChem to CID 2724127, whose synonyms are
  benzylamine hydrochloride names and whose formula is `C7H10ClN`.
- PubChem resolves the preferred label `Benzylhydrazine Hydrochloride` to CID
  14084 with formula `C7H11ClN2`; CID 14084 lists `1073-62-7` as the primary CAS
  synonym and does not list `3287-99-8`.
- OLS search in `chebi` for `Benzylhydrazine Hydrochloride` found no CHEBI
  candidate.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed on the intentional CAS fallback because the term validator tried to
  resolve `cas:3287-99-8` through the ontology SQL label table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in the same batch.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative CAS fallback SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 563 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` row 143 only verified
  that `cas:3287-99-8` is an expected registry identifier rather than an
  OAK/OLS ontology term; it did not check that CAS against the preferred label.
- The stored `chemical_properties` formula, InChI, SMILES, and `pubchem_cid:
  2724127` all belong to benzylamine hydrochloride, so the structure block
  agrees with the CAS but not with the record label.

## Completeness

- The SSSOM row, registry-fallback shape, and aggregate copy are synchronized.
- The exact identity is unresolved because the maintained record combines a
  Benzylhydrazine label with a Benzylamine CAS and PubChem structure.
- No component list, role, or ontology parent can repair the identity conflict.

## Recommended Edits

- Blocker: inspect the CultureBotHT source value for this row and choose the
  intended compound. If the ingredient is truly benzylhydrazine hydrochloride,
  update `data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml` to the
  correct CAS fallback identity around CAS `1073-62-7` and PubChem CID 14084.
  If the CAS was the intended identity, rename and relabel the record to
  benzylamine hydrochloride. Then run `just sync-curated`.
