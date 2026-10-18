# `data/ingredients/mapped/AQDS.yaml`

## Verdict

Needs curation, major. The CAS fallback identity and PubChem chemistry for the
AQDS disodium salt pass, but the related dianion label
`anthraquinone-2,6-disulfonate` is stored and exported as an exact synonym of
the disodium salt.

## Identity

- Reviewed record: `data/ingredients/mapped/AQDS.yaml`.
- Identifier and grounding: `identifier: cas:853-68-9` with
  `ontology_mapping.ontology_id: cas:853-68-9`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem maps CAS `853-68-9` to CID `70070`, the disodium
  anthraquinone-2,6-disulfonate salt with formula `C14H6Na2O8S2` and the live
  record's InChI.
- ChEBI `CHEBI:85112` resolves to `anthraquinone-2,6-disulfonate`, formula
  `C14H6O8S2`, charge `-2`, and a different InChIKey, confirming the local
  curation note that it is a related dianion rather than the exact sodium salt.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/8-hydroxy-nitroquinoline.yaml data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml data/ingredients/mapped/A-Cyclodextrin.yaml data/ingredients/mapped/A-Ketoglutaric_Acid_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/AQDS.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/AQDS.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed because the validator tried to resolve registry CURIE
  `cas:853-68-9` through the OAK sqlite label table and raised
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/AQDS.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord`:
  failed with the same CAS-registry OAK lookup error.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected dianion label and synonyms for `CHEBI:85112`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:67121 CHEBI:32139 CHEBI:40585 CHEBI:30915 CHEBI:85112`:
  returned the expected dianion formula, charge, structure strings, and mass
  for `CHEBI:85112`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- CAS `853-68-9`, PubChem CID `70070`, and the stored formula, InChI, and
  PubChem CID support the AQDS disodium-salt identity.
- The SSSOM row maps `MIM:AQDS` to `cas:853-68-9` with `skos:exactMatch`, which
  is the expected registry fallback shape for a salt that lacks an exact
  ontology term.
- `Na2-9,10-anthraquinone-2,6-disulfonate` is consistent with the PubChem
  disodium salt identity, but `anthraquinone-2,6-disulfonate` is the ChEBI
  dianion label. The merge event explicitly says `CHEBI:85112` is related and
  not the exact salt, so that shorter label should not be exported as an exact
  SSSOM `other` value for CAS `853-68-9`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row,
  unknown-term triage row, prior unmapped audit for the merged Na2 surface, and
  ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, occurrence counts, and
  `ingredient_type` are populated.
- The exact synonym list is not complete enough because one entry names the
  related dianion rather than the disodium salt.

## Recommended Edits

- In `data/ingredients/mapped/AQDS.yaml`, remove
  `anthraquinone-2,6-disulfonate` from `synonyms`, or move it to
  source-occurrence-only provenance that will not be exported as an exact
  `other` value for CAS `853-68-9`.
- Regenerate `data/curated/mapped_ingredients.yaml` and
  `mappings/ingredient_mappings.sssom.tsv`, then rerun strict validation and
  SSSOM invariants.
