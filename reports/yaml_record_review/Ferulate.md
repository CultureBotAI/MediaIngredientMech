# `data/ingredients/mapped/Ferulate.yaml`

## Verdict

Needs curation, with a major identity issue. The record intentionally retained
a local close match to neutral `trans-ferulic acid` in August, but subsequent
record-research validation found that `CHEBI:29749` exists for the anion
`trans-ferulate` and is the more specific target for the Ferulate surface.

## Identity

- Reviewed record: `data/ingredients/mapped/Ferulate.yaml`.
- Current grounding: `identifier: CHEBI:17620`,
  `ontology_mapping.ontology_id: CHEBI:17620`, canonical label
  `trans-ferulic acid`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- `uv run runoak -i sqlite:obo:chebi info CHEBI:17620` resolved the current
  target as `trans-ferulic acid`.
- `uv run runoak -i sqlite:obo:chebi info CHEBI:29749` resolved the candidate
  anion target as `trans-ferulate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ferrous_Ion.yaml data/ingredients/mapped/Ferrous_ammonium_sulfate.yaml data/ingredients/mapped/Ferroverdin.yaml data/ingredients/mapped/Ferulate.yaml data/ingredients/mapped/Ferulic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ferulate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed against the current neutral-acid ChEBI target.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  close-match neutral-acid target and MicrobeDecoder source occurrence as the
  per-record YAML.
- Major: `mappings/record_research_validation.tsv` has two high-priority lanes
  disputing the current `CHEBI:17620` mapping and recommending correction to
  `CHEBI:29749` `trans-ferulate`; it also specifically refutes the current
  evidence claim that ChEBI has no ferulate anion term.
- The final `mappings/ingredient_mappings.sssom.tsv` row currently maps
  `MIM:Ferulate` to `CHEBI:17620` as `skos:exactMatch`, so the published row
  collapses the anion label into neutral `trans-ferulic acid` despite the YAML
  recording only `CLOSE_MATCH`.
- Minor: the top-level `notes` still say "no CAS-RN or CHEBI/NCIT match.
  Curator review needed." That sentence is stale after the August 2026
  promotion, and will remain stale after the future anion remap.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports` for `Ferulate` found the
  active YAML, aggregate copy, final SSSOM row, the record-research validation
  disputes, related Methyl Ferulate and Sodium ferulate row-review artifacts,
  old batch validation output, and ignored aggregate backups.

## Completeness

- The MicrobeDecoder source occurrence and ingredient type are populated.
- The identity, ontology mapping, and SSSOM row need correction to the
  existing anion term before chemical structure can be safely filled.

## Recommended Edits

- Major: remap `data/ingredients/mapped/Ferulate.yaml` from `CHEBI:17620`
  `trans-ferulic acid` to `CHEBI:29749` `trans-ferulate`, update the evidence
  that currently says no ChEBI anion term exists, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
