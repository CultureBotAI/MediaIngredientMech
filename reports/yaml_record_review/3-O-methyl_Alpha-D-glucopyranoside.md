# `data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml`

## Verdict

Needs curation, minor. The local `kgmicrobe.compound` fallback identity and the
single microbedecoder occurrence bucket pass, but the record still carries stale
pre-promotion notes and lacks the expected single-ingredient classification and
chemical properties.

## Identity

- Reviewed record:
  `data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:3-o-methyl_alpha-d-glucopyranoside` with a
  matching `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The `promote_resolved_unmapped` event documents the deliberate
  `UNMAPPED_0671` to local-fallback promotion under issue `#213`, and the
  SSSOM row preserves that exact local identity.
- `source_occurrences` preserves the direct microbedecoder
  `BacDive_Metabolite_utilization` count of 9.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Methylglutaric_Acid.yaml data/ingredients/mapped/3-O-Methyl-D-glucopyranose.yaml data/ingredients/mapped/3-O-methyl-glucose.yaml data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/3-O-methylgallate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable; the `kgmicrobe.compound` adapter attempted to download
  `kgmicrobe.compound.db.gz`, received HTML instead of gzip content, and failed
  before judging this record.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-O-methyl_Alpha-D-glucopyranoside` to
  `kgmicrobe.compound:3-o-methyl_alpha-d-glucopyranoside` registry row.

## Evidence

- The fallback evidence reports a bounded search across repo-available
  ontologies and live OLS4 before minting the local compound CURIE.
- Stale: top-level `notes` still say `no CAS-RN or CHEBI/NCIT match. Curator
  review needed.` even though the record has since been promoted to `MAPPED`.
  The same wording is appropriate historical context in the creation event, but
  misleading as the current record note.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, and `tests` found the active YAML,
  aggregate, SSSOM, generated docs, expected-registry advisory row, and no
  nonlocal ontology mapping for this exact fallback CURIE.

## Completeness

- Missing: `ingredient_type` is not populated despite the mapped
  single-compound fallback identity.
- Missing: no `chemical_properties` are populated. That is less severe for a
  local fallback than for a ChEBI-backed record, but future curation should add
  CAS, formula, InChI, or SMILES if a registry entry can be verified for this
  exact alpha-D-glucopyranoside form.
- The source occurrence count is complete for the observed microbedecoder row.

## Recommended Edits

1. In `data/ingredients/mapped/3-O-methyl_Alpha-D-glucopyranoside.yaml`, replace
   the stale top-level `notes` with a current local-fallback note that cites
   `#213` and the bounded search.
2. Add `ingredient_type: SINGLE_INGREDIENT` and any exact registry-backed
   chemical properties that can be verified for this form.
3. Run the per-record strict validator, compare the record against
   `data/curated/mapped_ingredients.yaml`, rebuild the SSSOM/docs with the
   maintained generators, and then rerun the whole-corpus SSSOM and flat-export
   checks.
