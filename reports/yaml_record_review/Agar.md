# `data/ingredients/mapped/Agar.yaml`

## Verdict

Needs curation. The `CHEBI:2509` grounding, CAS xref, occurrence count, and
solidifying-agent interpretation pass, but the record still keeps CultureMech
recipe annotations as raw synonyms and still attaches an auto-proposed PubMed
snippet to the mapping evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Agar.yaml`.
- Identifier and grounding: `identifier: CHEBI:2509` with
  `ontology_mapping.ontology_id: CHEBI:2509`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2509` to `agar` with
  CAS `9002-18-0`.
- ChEBI defines agar as the red-algal polysaccharide mixture containing agarose
  and agaropectin; the exact match is to agar itself, not to one of the complex
  agar media that were extracted into separate records.
- `kg_microbe_node_id: CHEBI:2509` matches the ontology identifier, and
  `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Adipate.yaml data/ingredients/mapped/Adipic_Acid.yaml data/ingredients/mapped/Aesculetin.yaml data/ingredients/mapped/Agar.yaml data/ingredients/mapped/Agarose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Agar.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned the expected `agar` label for `CHEBI:2509`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17128 CHEBI:30832 CHEBI:2509 CHEBI:2511 CHEBI:490095`:
  returned CAS `9002-18-0` for `CHEBI:2509`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 4079 rows for
  `CHEBI:2509`, matching `occurrence_statistics.media_count`, and their counts
  sum to `total_occurrences: 4456`.
- `mappings/ingredient_mappings.sssom.tsv` row 353 maps `MIM:Agar` to
  `CHEBI:2509`, preserves CAS `9002-18-0`, filters several parenthetical raw
  fragments out of `other`, but still exports optionality/catalogue surfaces
  such as `Agar (if needed)` and `Agar (Molecular Genetics)`.
- The raw synonyms `( Noble)`, `(alternative)`, `(for solid medium)`,
  `(for solid medium, alternative)`, `(if appropriate)`,
  `Role: Solidifying component`, `Properties: Undefined component, Complex component`,
  and `( modified)` are CultureMech recipe annotations or fragments, not names
  of the `CHEBI:2509` substance.
- The `LITERATURE` evidence entry for PMID `38905279` is still labelled
  `PubMed search ('Agar')` with explanation `Auto-proposed; curator should
  rephrase or remove.` The snippet shows agar as an ingredient in one medium,
  not an independent identity source for the MIM-to-ChEBI mapping.
- The hidden/ignored-inclusive searches over active `data` surfaces, `mappings`,
  `reports`, `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`
  found the active YAML, aggregate copy, SSSOM row, synonym-enrichment review
  row, CultureMech alias-backfill rows, occurrence-membership rows, generated
  indexes, and no active complex-medium aliases folded into this record.

## Completeness

- CAS, kg-microbe node, occurrence statistics, curation history,
  `ingredient_type`, and the provisional `SOLIDIFYING_AGENT` role are
  populated.
- The solidifying role is plausible but still rests on a computational
  name-pattern evidence object that says review is recommended.
- No formula, InChI, or SMILES gap is actionable for agar because ChEBI models
  it as a complex polysaccharide mixture rather than a fixed small molecule.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- In `data/ingredients/mapped/Agar.yaml`, delete or move the CultureMech
  parenthetical/property raw synonyms that are recipe annotations rather than
  agar names.
- Decide whether the CultureMech alias-backfill surfaces such as
  `Agar (if needed)` should remain in per-record synonyms, live only in an alias
  overlay, or be filtered from SSSOM `other`; rerun the SSSOM builder afterward.
- Either replace PMID `38905279` with a claim-level evidence object for the
  solidifying role or remove the auto-proposed literature entry from
  `ontology_mapping.evidence`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Agar.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
