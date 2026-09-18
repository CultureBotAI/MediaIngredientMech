# `data/ingredients/mapped/Urocanic_Acid.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI identity, structure fields, aggregate row,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Urocanic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:27248` with matching
  `ontology_mapping.ontology_id`, label `urocanic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical fields: formula `C6H6N2O2` and ChEBI/PubChem SMILES/InChI.
- Occurrences: four MicrobeDecoder metabolite-utilization occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uridine_5-monophosphate_Disodium_Salt` through `V-8_Juice`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset of
  this batch exited 0 for `Urocanic_Acid` and `Usnic_Acid`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 exact-label search returns active `CHEBI:27248` with label
  `urocanic acid`; the generic MicrobeDecoder source label therefore maps to
  the generic ChEBI acid, not the cis or trans stereoisomer children.
- The final SSSOM row correctly has
  `MIM:Urocanic_Acid skos:exactMatch CHEBI:27248`, with review provenance and
  no leaked sibling synonyms in `other`.

## Issues

None.

## Completeness

- The exact CHEBI mapping, structural annotation, MicrobeDecoder occurrence
  count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
