# `data/ingredients/mapped/Mono-_And_Disaccharides.yaml`

## Verdict

Needs curation. The local registry row and #369 removal of false component
partonomy pass, but the record still classifies the coordinated carbohydrate
substrate-family label as a `NAMED_MEDIUM`, which contradicts the retained
curation rationale.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mono-_And_Disaccharides.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:mono_and_disaccharides` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:mono_and_disaccharides`,
  source `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: NAMED_MEDIUM`.
- Occurrences: one MicrobeDecoder `bergey:substrates` source occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Modified_Wolfes_Minerals` through `Mono-_And_Disaccharides`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- A fresh EBI OLS4 lookup for the exact source label found no same-label
  ontology class; the returned hits were unrelated text mentions rather than a
  class denoting this MicrobeDecoder carbohydrate category.
- #369 correctly removed the earlier false partonomy because monosaccharide and
  disaccharide are category members named by a coordinated class label, not
  physical constituents of a mixture.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mono-_And_Disaccharides` to the local registry identifier with empty
  `other`.

## Completeness

- The current local identity and final exact row avoid mapping the category to
  either named carbohydrate member class.
- `ingredient_type: NAMED_MEDIUM` now conflicts with the post-#369 model: the
  schema reserves that value for complete named medium formulations or recipes,
  while this record's own history and evidence describe a substrate-family
  label from `bergey:substrates`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Mono-_And_Disaccharides.yaml`, remove or
  replace `ingredient_type: NAMED_MEDIUM` so the record no longer claims this
  MicrobeDecoder carbohydrate category is a complete named medium.
