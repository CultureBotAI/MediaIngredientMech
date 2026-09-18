# `data/ingredients/mapped/Lithium_Chloride_Hydrate.yaml`

## Verdict

Needs curation. The CAS-primary lithium chloride hydrate identity, PubChem
hydrate structure, and close match to anhydrous CHEBI:48607 are internally
coherent, but the final SSSOM is missing the kgmicrobe compound anchor rows
tracked by `reports/hydrate_grounding.tsv`.

## Identity

- Reviewed record: `data/ingredients/mapped/Lithium_Chloride_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:85144-11-2` with
  `ontology_mapping.ontology_id: CHEBI:48607`, label `lithium chloride`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `85144-11-2`, molecular formula `ClH2LiO`,
  InChI, SMILES, and PubChem CID `23681138`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lincomycin_Hydrochloride` through `Lithocholic_Acid`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  CHEBI-grounded records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:48607` as active anhydrous `lithium chloride`, which
  is correctly retained only as a `CLOSE_MATCH` parent because the hydrate has
  a distinct CAS identity.
- PubChem resolves CAS RN `85144-11-2` to CID `23681138` with formula
  `ClH2LiO` and the same water-containing InChI as the YAML record.
- The final SSSOM publishes the expected `skos:closeMatch` row to anhydrous
  `CHEBI:48607` plus an exact row to `cas:85144-11-2`.
- Major: `reports/hydrate_grounding.tsv` classifies this record as
  `CAS_MISSING_ANCHOR_ROWS`. The final SSSOM still lacks exact
  `kgmicrobe.compound` registry sibling rows for the hydrate bucket, so
  downstream consumers only see the anhydrous close match plus the CAS row.

## Completeness

- The CAS identity, hydrate formula, PubChem CID, aggregate copy, close parent
  mapping, and exact CAS registry row are present and consistent.
- The missing kgmicrobe compound anchor rows need curation or export work before
  the final SSSOM fully preserves this hydrate as a distinct KG-Microbe node.

## Recommended Edits

- Major: add or generate the missing exact `kgmicrobe.compound` registry rows
  for `data/ingredients/mapped/Lithium_Chloride_Hydrate.yaml` so
  `reports/hydrate_grounding.tsv` no longer reports `CAS_MISSING_ANCHOR_ROWS`.
- Regenerate final SSSOM after the registry fix; rerun hydrate grounding,
  strict, term, round-trip, component, and SSSOM validation.
