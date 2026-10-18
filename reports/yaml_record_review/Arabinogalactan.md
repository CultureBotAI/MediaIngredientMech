# `data/ingredients/mapped/Arabinogalactan.yaml`

## Verdict

Needs curation. The CAS-backed ChEBI identity, CAS xref, SSSOM row, and
aggregate copy pass, but the `CARBON_SOURCE` role is still only a provisional
ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Arabinogalactan.yaml`.
- Identifier and grounding: `identifier: CHEBI:27569` with
  `ontology_mapping.ontology_id: CHEBI:27569`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:27569` to non-obsolete ChEBI `arabinogalactan`,
  with CAS `9036-66-2`, KEGG Compound `C00569`, and related synonyms including
  `Arabinogalactan`.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI
  polysaccharide identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arabinogalactan.yaml data/ingredients/mapped/Arabinose.yaml data/ingredients/mapped/Arabinotriose.yaml data/ingredients/mapped/Arabinoxylan_Rye_Flour.yaml data/ingredients/mapped/Arabitol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinogalactan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned CAS and KEGG xrefs for `CHEBI:27569`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27569 CHEBI:22599 CHEBI:62799 CHEBI:18403`:
  returned the canonical `arabinogalactan` label and related ChEBI synonyms for
  `CHEBI:27569`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The record was created by an explicit CultureBotHT CAS-to-ChEBI lookup, and
  the current ChEBI target carries the stored CAS `9036-66-2`.
- `mappings/ingredient_mappings.sssom.tsv` row 460 maps
  `MIM:Arabinogalactan` to `CHEBI:27569` with `skos:exactMatch`, CAS
  `9036-66-2`, and a `SYNONYM_ENRICH` row-review trailer.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classified the old
  parenthesized `MIM:~28~29-Arabinogalactan` row as already represented; the
  current SSSOM emits the canonical `MIM:Arabinogalactan` subject.
- The only `nutritional_roles` evidence cites `Inferred from CHEBI ancestry`
  and explicitly marks the carbon-source role as provisional, so the current
  role is not supported by claim-level source evidence.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row, row-review
  rows, and MIM CURIE alias row.

## Completeness

- CAS, ChEBI identity, CAS lookup history, `ingredient_type`, SSSOM, and the
  aggregate copy are populated.
- Formula and structure are correctly absent because the ChEBI
  `arabinogalactan` entry is a polymer class and has no fixed molecular formula
  in the local OBO metadata.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS import rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported carbon-source role is the only consequential gap.

## Recommended Edits

- In `data/ingredients/mapped/Arabinogalactan.yaml`, remove
  `nutritional_roles.CARBON_SOURCE` unless direct source evidence for
  Arabinogalactan as a carbon source is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinogalactan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
