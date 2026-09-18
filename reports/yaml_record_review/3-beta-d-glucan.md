# `data/ingredients/mapped/3-beta-d-glucan.yaml`

## Verdict

Needs curation, minor. The `CHEBI:37671` `(1->3)-beta-D-glucan` identity,
polymer formula, monomer structure, SSSOM row, and aggregate row pass, but the
current notes still describe the pre-promotion unmapped state and the promotion
evidence explains the truncated label imprecisely.

## Identity

- Reviewed record: `data/ingredients/mapped/3-beta-d-glucan.yaml`.
- Identifier and grounding: `identifier: CHEBI:37671` with
  `ontology_mapping.ontology_id: CHEBI:37671`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:37671`
  resolves to `(1->3)-beta-D-glucan`, lists formula `(C6H10O5)n.H2O`, and
  publishes the same representative monomer SMILES and InChI recorded in the
  YAML.
- The `2026-09-10` curation event repaired the lowercase `d` stereodescriptor
  in the preferred term to `3-beta-D-glucan`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-aminobutyric_Acid.yaml data/ingredients/mapped/3-beta-d-glucan.yaml data/ingredients/mapped/3-dehydro-D-gluconate.yaml data/ingredients/mapped/3-fucosyllactose.yaml data/ingredients/mapped/3-hydroxybenzoate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-beta-d-glucan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-beta-d-glucan` to `CHEBI:37671` row.

## Evidence

- The active ChEBI page confirms the exact 1,3-linked beta-D-glucan term and
  chemistry copied into the record.
- Stale: top-level `notes` still say `no CAS-RN or CHEBI/NCIT match. Curator
  review needed.` even though the record has since been promoted to `MAPPED`.
- Imprecise: the `MIM curation (#213)` evidence says `3-beta-d-glucan` lost the
  leading `(1->` from `(1->3)-beta-D-glucan`; the raw label is better explained
  as a normalized shorthand for 1,3-beta-D-glucan. This does not make the
  destination CURIE wrong, but the rationale should not encode an impossible
  string transform.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, lowercase-stereodescriptor test, generated docs, and stale
  advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- ChEBI-backed formula, InChI, SMILES, and molecular weight are populated.
- The direct microbedecoder source occurrence is represented.

## Recommended Edits

1. In `data/ingredients/mapped/3-beta-d-glucan.yaml`, replace the stale
   top-level `notes` with a current note summarizing the `#213` promotion and
   the `#460` stereodescriptor repair.
2. Tighten the `MIM curation (#213)` evidence note so the exact-match rationale
   is not tied to losing the literal `(1->` prefix.
3. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
