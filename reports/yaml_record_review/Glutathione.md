# `data/ingredients/mapped/Glutathione.yaml`

## Verdict

Pass. The CultureMech exact match to active `CHEBI:16856` glutathione is
structurally consistent, the reduced-form synonyms are curated on this record
while oxidized glutathione remains separate, and the final SSSOM row exports
only same-record synonyms and CAS payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Glutathione.yaml`.
- Identifier and grounding: `identifier: CHEBI:16856` with matching
  `ontology_mapping.ontology_id`, canonical label `glutathione`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `70-18-8`, formula `C10H17N3O6S`, InChI,
  stereochemical SMILES, and `kg_microbe_node_id: CHEBI:16856`.

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

- The matching active `Glutathione` aggregate entry carries the same ChEBI
  exact match, synonym set, CultureMech occurrence count, CAS RN, formula,
  InChI, SMILES, source-backed nitrogen role, and singleton type as the
  per-record YAML. The aggregate also contains a separate rejected
  `L-Glutathione` tombstone with the same identifier, so duplicate-identifier
  comparisons must include the preferred term.
- OLS4 resolves `CHEBI:16856` as `glutathione`, matching the YAML
  `ontology_mapping`.
- PubChem resolves CAS `70-18-8` to formula `C10H17N3O6S` and the same reduced
  glutathione InChI as the record.
- The #260 curation event explicitly keeps `L-glutathione reduced` on this
  record because `CHEBI:16856` is reduced glutathione; the oxidized form is the
  separate `CHEBI:17858` record.
- The CultureMech `NITROGEN_SOURCE` role keeps `DATABASE_ENTRY` evidence with
  the original imported role text.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glutathione` to `CHEBI:16856` by `skos:exactMatch`; the final `other`
  tokens are curated same-subject synonyms or `CAS:70-18-8`.
- Raw `Cross-references: ...` and `Role: ...; Properties: ...` synonyms are
  retained in YAML for provenance and correctly filtered from final SSSOM
  `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, OAK/OLS row-review confirmations, the rejected L-glutathione tombstone,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The exact ChEBI identity, formula, CAS RN, InChI, SMILES,
  CultureMech-derived occurrence count, source-backed nitrogen role,
  reduced-form synonym coverage, ingredient type, and final SSSOM row are
  populated.

## Recommended Edits

- None.
