# `data/ingredients/mapped/Arabitol.yaml`

## Verdict

Needs curation. The CAS-backed `L-arabinitol` identity, formula, structure,
synonyms, CultureMech memberships, merged MicrobeDecoder raw synonym, SSSOM row,
and aggregate copy pass, but the `CARBON_SOURCE` role is still only a
provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Arabitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:18403` with
  `ontology_mapping.ontology_id: CHEBI:18403`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:18403` to non-obsolete ChEBI `L-arabinitol`, formula
  `C5H12O5`, CAS `7643-75-6`, KEGG Compound `C00532`, the stored InChI and
  SMILES, and exact/related synonyms covering `L-Arabinitol`, `L-Arabinol`,
  `L-Arabitol`, and `L-Lyxitol`.
- The local mapping contract explicitly documents why this bare `Arabitol`
  label is correctly grounded to stereospecific `CHEBI:18403`: the record has
  independent CAS and L-form synonym evidence, so the short preferred term does
  not override the record-level L-arabinitol identity.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI molecular
  entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arabinogalactan.yaml data/ingredients/mapped/Arabinose.yaml data/ingredients/mapped/Arabinotriose.yaml data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml data/ingredients/mapped/Arabitol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned formula, SMILES, InChI, InChIKey, CAS, KEGG, and MetaCyc metadata for
  `CHEBI:18403`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned the canonical `L-arabinitol` label and exact/related ChEBI synonyms
  for `CHEBI:18403`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has four
  `CHEBI:18403` memberships, matching `occurrence_statistics: 4/4`.
- `mappings/ingredient_mappings.sssom.tsv` row 465 maps `MIM:Arabitol` to
  `CHEBI:18403` with `skos:exactMatch`, CAS `7643-75-6`, and the retained
  L-form synonyms.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  ChEBI synonym-enrichment row as already represented.
- The merged `(+)-L-lyxitol` raw synonym is traceable through
  `mappings/microbedecoder_residual_research_proposed.tsv`,
  `scripts/apply_microbedecoder_residual_merges.py`, and the
  `microbedecoder-residual-dispositions` history event.
- The only `nutritional_roles` evidence cites `Inferred from CHEBI ancestry`
  and explicitly marks the carbon-source role as provisional, so the current
  role is not supported by claim-level source evidence.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, row-review
  rows, CultureMech recipe-membership rows, and MicrobeDecoder residual merge
  rows.

## Completeness

- CAS, formula, SMILES, InChI, ChEBI identity, L-form synonyms, CultureMech
  occurrence counts, merged raw MicrobeDecoder synonym, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported carbon-source role is the only consequential gap.

## Recommended Edits

- In `data/ingredients/mapped/Arabitol.yaml`, remove
  `nutritional_roles.CARBON_SOURCE` unless direct source evidence for
  L-arabinitol as a carbon source is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
