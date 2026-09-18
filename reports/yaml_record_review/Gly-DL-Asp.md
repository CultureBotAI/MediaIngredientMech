# `data/ingredients/mapped/Gly-DL-Asp.yaml`

## Verdict

Pass with a minor stale-evidence issue. The CAS fallback record was correctly
regraded to exact ChEBI identity through `CHEBI:193741` Glycyl-Aspartate, its
PubChem CID matches the recorded formula and InChIKey, and both final SSSOM rows
obey the identity-row and `other` synonym rules, but the oldest CultureBotHT
evidence note still describes the obsolete state where no ChEBI term had been
accepted.

## Identity

- Reviewed record: `data/ingredients/mapped/Gly-DL-Asp.yaml`.
- Identifier and grounding: `identifier: cas:79731-35-4`, mapping to
  `CHEBI:193741` with canonical label `Glycyl-Aspartate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `79731-35-4`, PubChem CID `273261`, formula
  `C6H10N2O5`, and InChIKey `SCCPDJAQCXWPTF-UHFFFAOYSA-N`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS primary identifier, ChEBI synonym match, exact synonym, chemical
  properties, singleton type, and stale CultureBotHT evidence note as the
  per-record YAML.
- OLS4 resolves `CHEBI:193741` as `Glycyl-Aspartate`, matching the YAML
  `ontology_mapping`.
- PubChem CID `273261` resolves to formula `C6H10N2O5`, CAS RN `79731-35-4`,
  and InChIKey `SCCPDJAQCXWPTF-UHFFFAOYSA-N`, matching the #326
  same-formula regrade.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map `MIM:Gly-DL-Asp`
  to `CHEBI:193741` and to the record's own `cas:79731-35-4` identifier with
  `skos:exactMatch`.
- The final ChEBI SSSOM row keeps
  `2-[(2-aminoacetyl)amino]butanedioic acid` and `CAS:79731-35-4` in `other`.
  The first token is curated in the YAML and the CAS token matches
  `chemical_properties.cas_rn`.
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
  InChI, SMILES, exact synonym, and final ChEBI and CAS SSSOM rows are
  populated.

## Recommended Edits

- Minor: rephrase `ontology_mapping.evidence[0].notes` in
  `data/ingredients/mapped/Gly-DL-Asp.yaml` so it preserves the CultureBotHT CAS
  fallback provenance without saying the current mapping still lacks a ChEBI
  grounding.
