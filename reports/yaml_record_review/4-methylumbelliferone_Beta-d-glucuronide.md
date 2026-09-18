# `data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`

## Verdict

Pass, none. The `CHEBI:1904` beta-D-glucuronide identity, corrected
stereodescriptor, chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`.
- Identifier and grounding: `identifier: CHEBI:1904` with
  `ontology_mapping.ontology_id: CHEBI:1904`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:1904` is active, resolves to
  `4-methylumbelliferone beta-D-glucuronide`, has formula `C16H16O9`, CAS
  `6160-80-1`, SMILES
  `Cc1cc(=O)oc2cc(O[C@@H]3O[C@H](C(=O)O)[C@@H](O)[C@H](O)[C@H]3O)ccc12`,
  and the stored InChI.
- PubChem CAS lookup for `6160-80-1` resolves to CID `91553` with formula
  `C16H16O9` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-hydroxybutyrate.yaml data/ingredients/mapped/4-hydroxybutyric_Acid.yaml data/ingredients/mapped/4-hydroxychalcone.yaml data/ingredients/mapped/4-hydroxyphenyl_Acetic_Acid.yaml data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-methylumbelliferone_Beta-d-glucuronide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed in the immediately preceding batch; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The current ChEBI term, formula, InChI, SMILES, and PubChem CAS lookup all
  support the exact beta-D-glucuronide identity and match the #460 uppercase-D
  stereodescriptor correction.
- The active microbedecoder import row is exact-label evidence:
  `kgmicrobe.trait:4_methylumbelliferone_beta_d_glucuronide` supplied count 1
  in `BacDive_Metabolite_utilization`; the 2026-09-10 curation event repaired
  only the case of the D stereodescriptor.
- The `source_occurrences` block correctly keeps the single microbedecoder
  occurrence separate from verified CultureMech recipe counts
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps `MIM:4-methylumbelliferone_Beta-d-glucuronide` to
  `CHEBI:1904` with `skos:exactMatch`, `semapv:LexicalMatching`, and no
  `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder review row,
  stereodescriptor regression test, generated docs, stale advisory rows, and
  ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- CAS `6160-80-1` is available on ChEBI and PubChem but not required for the
  active exact-label grounding because the structural fields already match.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
