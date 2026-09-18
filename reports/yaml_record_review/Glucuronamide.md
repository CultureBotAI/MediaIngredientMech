# `data/ingredients/mapped/Glucuronamide.yaml`

## Verdict

Pass with a minor stale-evidence issue. The CAS fallback record was correctly
regraded to exact ChEBI identity through `CHEBI:32323`
beta-D-glucuronamide, its PubChem CID matches the recorded formula, CAS-RN, and
InChIKey, and both final SSSOM rows obey the identity-row and `other` synonym
rules, but the oldest CultureBotHT evidence note still describes the obsolete
state where no ChEBI term had been accepted.

## Identity

- Reviewed record: `data/ingredients/mapped/Glucuronamide.yaml`.
- Identifier and grounding: `identifier: cas:3789-97-7`, mapping to
  `CHEBI:32323` with canonical label `beta-D-glucuronamide`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `3789-97-7`, PubChem CID `636367`, formula
  `C6H11NO6`, and InChIKey `VOIFKEWOFUNPBN-QIUUJYRFSA-N`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml data/ingredients/mapped/Glucose_Xylose.yaml data/ingredients/mapped/Glucose_Yeast_Extract.yaml data/ingredients/mapped/Glucuronamide.yaml data/ingredients/mapped/Glucuronate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glucuronamide.yaml data/ingredients/mapped/Glucuronate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two ChEBI-primary records in this batch. Engine A was skipped
  for the three `kgmicrobe.ingredient` local fallback records because that
  private prefix is outside the OBO-only term validator.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS primary identifier, ChEBI synonym match, exact synonyms, chemical
  properties, singleton type, and stale CultureBotHT evidence note as the
  per-record YAML.
- OLS4 resolves `CHEBI:32323` as `beta-D-glucuronamide`, matching the YAML
  `ontology_mapping`.
- PubChem CID `636367` resolves to formula `C6H11NO6`, CAS synonym
  `3789-97-7`, beta-D-glucopyranuronamide as a synonym, and InChIKey
  `VOIFKEWOFUNPBN-QIUUJYRFSA-N`, matching the #326 same-formula regrade.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Glucuronamide` to `CHEBI:32323` and to the record's own
  `cas:3789-97-7` identifier with `skos:exactMatch`.
- The final ChEBI SSSOM row keeps `D-Glucuronamide`,
  `beta-D-glucopyranuronamide`, and `CAS:3789-97-7` in `other`. The first two
  are curated exact synonyms in the YAML, and the CAS token is allowed because
  it matches `chemical_properties.cas_rn`.
- The final CAS SSSOM row keeps only `CAS:3789-97-7` in `other`, preserving the
  same own-identifier registry row reviewed in the unknown-term triage.
- Minor: `ontology_mapping.evidence[0].notes` still says no ChEBI entry exists
  and recommends future promotion. That was true of the import state, but it is
  stale on the current record after the PubChem-xref discovery and #326
  identity regrade.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  rows, row-review decisions for the CAS registry row and already represented
  synonym enrichment, generated indexes, old batch validation reports, and
  ignored aggregate backups.

## Completeness

- The CAS primary identity, exact ChEBI match, CAS RN, PubChem CID, formula,
  InChI, SMILES, exact synonyms, and final ChEBI and CAS SSSOM rows are
  populated.
- Empty occurrence and role slots are acceptable because this record is present
  through CultureBotHT CAS import rather than as a MicrobeDecoder substrate
  occurrence.

## Recommended Edits

- Minor: rephrase `ontology_mapping.evidence[0].notes` in
  `data/ingredients/mapped/Glucuronamide.yaml` so it preserves the CultureBotHT
  CAS fallback provenance without saying the current mapping still lacks a
  ChEBI grounding.
