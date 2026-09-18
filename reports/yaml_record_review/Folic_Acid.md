# `data/ingredients/mapped/Folic_Acid.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym leaks. The exact folic acid
identity, ChEBI mapping, PubChem CAS lookup, CultureMech vitamin role, and
structure fields agree, but the record still exports one different folate and
one concentration-bearing CultureMech alias as `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Folic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:27470` with matching
  `ontology_mapping.ontology_id`, canonical label `folic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `59-30-3` resolved to CID 135398658 titled
  `Folic Acid` with formula `C19H19N7O6` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Folic_Acid.yaml data/ingredients/mapped/Folinic_Acid.yaml data/ingredients/mapped/Formaldehyde.yaml data/ingredients/mapped/Formamicin.yaml data/ingredients/mapped/Formamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Folic_Acid.yaml data/ingredients/mapped/Folinic_Acid.yaml data/ingredients/mapped/Formaldehyde.yaml data/ingredients/mapped/Formamicin.yaml data/ingredients/mapped/Formamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed with no diagnostics for the 5-file batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact mapping, structure fields, CAS RN, ingredient type,
  synonyms, CultureMech vitamin role, and bad ontology-mapping literature
  evidence as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Folic_Acid` to `CHEBI:27470` with `skos:exactMatch`, includes the valid
  `CAS:59-30-3` alias, and also publishes two unsafe `other` tokens.
- Major: `Folinic acid (citrovorum)` is not an exact folic acid synonym. It is
  the separate `Folinic_Acid` record mapped to `CHEBI:15640`, and its presence
  in this record came from the kg-microbe synonym sweep.
- Major: the concentration-bearing CultureMech alias added from
  `culturemech:output/ingredient_occurrences.tsv` is a recipe-specific surface,
  not a true synonym for bare folic acid, and it still appears in final SSSOM
  `other`.
- Major: the PMID `20415580` evidence under `ontology_mapping.evidence` quotes a
  pregnancy recommendation about iron and folic acid; it does not support the
  folic acid ontology mapping or any media-ingredient claim in this record.
- The `nutritional_roles.VITAMIN_SOURCE` claim is backed by CultureMech
  `DATABASE_ENTRY` evidence for the original `Role: Vitamin` import surface,
  and the raw `Role:` / `Properties:` aliases are filtered out of the final
  SSSOM payload.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` only records that
  the bad folinic acid candidate text was already present as a synonym; it does
  not make that label an exact synonym of folic acid.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports, found
  the active YAML, aggregate copy, final SSSOM row, row-review entries, residual
  triage row, and ignored historical aggregate backups.

## Completeness

- The exact folic acid identity, single-ingredient type, structure fields, CAS
  RN, occurrence counts, and CultureMech vitamin role are populated.
- No unresolved component, environment, or missing structure gap remains for
  the current exact ChEBI identity.

## Recommended Edits

- Major: remove or demote `Folinic acid (citrovorum)` in
  `data/ingredients/mapped/Folic_Acid.yaml`, sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
- Major: move the concentration-bearing CultureMech alias out of active
  resolving synonyms so final SSSOM no longer publishes it as `other`, then
  rerun the SSSOM synonym gates.
- Major: remove the unrelated PMID `20415580` ontology-mapping evidence entry
  unless a future curator inspects the article and attaches it to a narrower
  claim it actually supports.
