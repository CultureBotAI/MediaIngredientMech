# `data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml`

## Verdict

Pass. The CultureMech record is now grounded to the generic or racemic ChEBI
lipoic acid class, the R-only and S-only source records have been rejected and
merged, the CAS RN and structure match PubChem, and the final SSSOM row keeps
the broad/generic lipoic and thioctic acid aliases on the generic subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16494` with
  `ontology_mapping.ontology_id: CHEBI:16494`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 1748 CultureMech source
  occurrences.
- Local OAK resolves `CHEBI:16494` to active `lipoic acid`, a
  non-stereospecific lipoic acid class with formula `C8H14O2S2`, the expected
  non-isomeric InChIKey, SMILES, and broad lipoic/thioctic acid synonyms.
- Local OAK separately resolves `CHEBI:30314` to `(R)-lipoic acid` and
  `CHEBI:43796` to `(S)-lipoic acid`; the previously over-specific tombstones
  keep their R-only and S-only labels as `REJECTED_LABEL` provenance.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:16494 CHEBI:22660 CHEBI:17126 CHEBI:18320 CHEBI:42106 CHEBI:30314 CHEBI:43796`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:16494`, `CHEBI:30314`,
  and `CHEBI:43796`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- PubChem resolves CAS `1077-28-7` to CID 864 with formula `C8H14O2S2` and the
  same non-isomeric InChIKey as `CHEBI:16494`.
- A focused hidden/ignored-inclusive search over `data/ingredients/mapped`,
  `mappings/other_cross_record_baseline.tsv`, and the final SSSOM for
  `CHEBI:16494`, `Thioctic acid`, and `1077-28-7` found the active lipoic acid
  record, expected vitamin-mix component usages, the rejected R- and S-target
  tombstones, a stale cross-record baseline row against the now-rejected
  thioctic acid record, and the final SSSOM row.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-alpha-lipoic_Acid` to `CHEBI:16494` with `skos:exactMatch`,
  canonical object label `lipoic acid`, CHEBI object source, a comment
  documenting the stereochemistry repair, same-substance lipoic/thioctic acid
  aliases, and `CAS:1077-28-7`.
- `nutritional_roles.VITAMIN_SOURCE` carries `DATABASE_ENTRY` evidence imported
  from CultureMech role text rather than a provisional name-list or ChEBI
  ancestry inference.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonymy, generic/racemic merged
  aliases, CultureMech vitamin-source evidence, and occurrence provenance are
  populated.
- The raw role strings are correctly excluded from final SSSOM synonym
  publication.
- Mixture components, supplied forms, physicochemical roles, biological roles,
  and environmental contexts are correctly empty.

## Recommended Edits

- None.
