# `data/ingredients/mapped/4-dihydroxy-biphenyl.yaml`

## Verdict

Needs curation, major. The repaired `CHEBI:34367` target is the real
4,4'-dihydroxybiphenyl compound, but the active record still exports the
impossible raw text `4-dihydroxy-biphenyl` as a synonym and still carries
pre-repair "no CAS-RN or CHEBI/NCIT match" provenance.

## Identity

- Reviewed record: `data/ingredients/mapped/4-dihydroxy-biphenyl.yaml`.
- Identifier and grounding: `identifier: CHEBI:34367` with
  `ontology_mapping.ontology_id: CHEBI:34367`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:34367` is active, resolves to
  `biphenyl-4,4'-diol`, defines the para/para dihydroxybiphenyl isomer, lists
  `4,4'-Dihydroxybiphenyl` as a synonym, and has formula `C12H10O2`, CAS
  `92-88-6`, SMILES `Oc1ccc(-c2ccc(O)cc2)cc1`, and the stored InChI.
- PubChem CAS lookup for `92-88-6` resolves to CID `7112` with formula
  `C12H10O2` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-coumarate.yaml data/ingredients/mapped/4-dihydroxy-biphenyl.yaml data/ingredients/mapped/4-guanidinobutyric_Acid.yaml data/ingredients/mapped/4-hydroxy-L-proline.yaml data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-dihydroxy-biphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2,951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, K; Rule B4 was skipped because the
  sibling `kg-microbe` ontology transforms are absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed;
  `docs/data/` is fresh and every curated label is published.

## Evidence

- The active target is chemically plausible after #308: the source label
  `4-dihydroxy-biphenyl` was a comma-truncated microbedecoder artifact, and the
  repaired preferred term `4,4'-dihydroxybiphenyl` names the same neutral
  compound as ChEBI's `biphenyl-4,4'-diol`.
- Major: the malformed raw label remains as a `RAW_TEXT` synonym and still
  publishes in `mappings/ingredient_mappings.sssom.tsv` `other`. `RAW_TEXT`
  makes sense for preserving the source artifact in YAML, but exporting
  `4-dihydroxy-biphenyl` beside real names makes generated label surfaces treat
  an impossible, locant-incomplete string as a synonym of `CHEBI:34367`.
- Major: top-level `notes` still say the record had no CAS-RN or CHEBI/NCIT
  match and needed curator review even though it was promoted and repaired.
- Minor: the mapping evidence note correctly marks the original CLOSE_MATCH
  rationale as superseded, but the remaining rationale says alternative names
  are a close match rather than a synonym match. That is weaker than the current
  ChEBI synonym evidence for `4,4'-dihydroxybiphenyl`.
- The SSSOM row maps `MIM:4-dihydroxy-biphenyl` to `CHEBI:34367` and exposes
  `4-dihydroxy-biphenyl` in `other`, so the stale raw synonym is already part
  of the final SSSOM surface.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, truncation overlay, generated docs,
  stale advisory research rows, and ignored aggregate backups.

## Completeness

- The record lacks `chemical_properties` even though ChEBI now supplies CAS,
  formula, InChI, mass, and SMILES for the selected compound. That is an
  enrichment gap, not a blocker for the current identity.
- No roles, components, environment, or discussion entries need review.
- The raw microbedecoder string should remain traceable, but only in a
  provenance field that does not publish as a real synonym.

## Recommended Edits

1. Update `data/ingredients/mapped/4-dihydroxy-biphenyl.yaml` and
   `data/curated/mapped_ingredients.yaml` so the malformed source text is
   preserved as provenance without publishing through SSSOM `other`.
2. Replace the stale top-level import note with post-#308 provenance that
   explains the reconstructed `4,4'-dihydroxybiphenyl` decision.
3. Consider changing `mapping_quality` from `CLOSE_MATCH` to a synonym/manual
   grade that reflects the exact active ChEBI synonym.
4. Regenerate `mappings/ingredient_mappings.sssom.tsv` and `docs/data/*`, then
   rerun strict validation, `qc-sssom`, and flat-export coverage.
