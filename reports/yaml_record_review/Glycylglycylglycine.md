# `data/ingredients/mapped/Glycylglycylglycine.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder synonym match to active
`CHEBI:63961` glycyl-glycyl-glycine, tripeptide structure fields, occurrence
provenance, and final SSSOM row pass, but the top-level note still says no
CHEBI or NCIT match was found and curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycylglycylglycine.yaml`.
- Identifier and grounding: `identifier: CHEBI:63961` with matching
  `ontology_mapping.ontology_id`, canonical label `glycyl-glycyl-glycine`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C6H11N3O4`, molecular weight `189.171`, InChI
  `InChI=1S/C6H11N3O4/c7-1-4(10)8-2-5(11)9-3-6(12)13/h1-3,7H2,(H,8,10)(H,9,11)(H,12,13)`,
  and SMILES `NCC(=O)NCC(=O)NCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycylglycine.yaml data/ingredients/mapped/Glycylglycylglycine.yaml data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml data/ingredients/mapped/Glyoxylate.yaml data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycylglycylglycine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:63961` as `glycyl-glycyl-glycine`, lists
  `glycylglycylglycine` as an exact synonym, and reports formula `C6H11N3O4`,
  the same InChI, the same SMILES, and CAS `556-33-2`.
- `mappings/microbedecoder_residual_grounded.tsv` records the residual
  MicrobeDecoder match from `Glycylglycylglycine` to `CHEBI:63961`; the record
  was promoted on 2026-08-04 and typed on 2026-08-13.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycylglycylglycine` to `CHEBI:63961` by `skos:exactMatch` and has an
  empty `other` payload.
- Minor: the top-level `notes` value is the original MicrobeDecoder import
  note and still says no CHEBI or NCIT match was found and curator review is
  needed, even though the record now has a reviewed CHEBI synonym match.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the residual
  grounding TSV, matching aggregate copies, generated products, the final SSSOM
  row, and ignored aggregate backups.

## Completeness

- The ChEBI identity, synonym-match rationale, formula, InChI, SMILES,
  molecular weight, MicrobeDecoder source occurrence, singleton type, and final
  SSSOM row are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- Minor: replace the stale top-level `notes` text in
  `data/ingredients/mapped/Glycylglycylglycine.yaml` with a current note saying
  the MicrobeDecoder residual label was reviewed and promoted to a ChEBI
  synonym match.
