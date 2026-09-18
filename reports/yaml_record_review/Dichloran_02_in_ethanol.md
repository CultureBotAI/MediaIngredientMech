# `data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`

## Verdict

Needs curation. The current record exact-maps a CultureMech stock-solution
surface, `Dichloran (0.2% in ethanol)`, to active `CHEBI:27864` for neat
dichloran. That ChEBI term is valid for `Dichloran` alone, but not for a 0.2%
ethanol solution.

## Identity

- Reviewed record: `data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`.
- Current grounding: `identifier: CHEBI:27864` with
  `ontology_mapping.ontology_id: CHEBI:27864`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`,
  `mapping_status: MAPPED`, and one CultureMech occurrence.
- Local OAK resolves `CHEBI:27864` to active neat
  `2,6-dichloro-4-nitroaniline`, formula `C6H4Cl2N2O2`, InChI, SMILES, CAS
  xref `99-30-9`, exact synonym `2,6-dichloro-4-nitroaniline`, and related
  synonym `Dichloran`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27864`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:27864`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, and the stale
  residual triage row.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:27864` found only
  `data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dichloran_02_in_ethanol` to `CHEBI:27864` with `skos:exactMatch`,
  canonical object label `2,6-dichloro-4-nitroaniline`, CHEBI object source,
  and no `other` tokens.
- Major: the source label names a solution, not a neat single compound.
  `data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml` already records
  the local precedent for 0.2% stock solutions: mint a
  `kgmicrobe.ingredient:` identifier with `FALLBACK_REGISTRY` rather than
  exact-mapping the stock to the pure compound term.
- `mappings/culturemech_residual_triage.tsv` row 1175 still has
  `Dichloran (0.2% in ethanol)` as a `RESIDUAL` row normalized to
  `dichloran`, which is the lossy normalized form that caused the solution to
  be grounded to neat `CHEBI:27864`.

## Completeness

- The CultureMech occurrence count and structured residual-grounding
  provenance are populated.
- The record is missing the solution identity it needs to preserve the
  ethanol and 0.2% concentration boundary. The label does not encode whether
  the concentration is w/v, v/v, or another basis, so the future curation
  should either inspect the CultureMech source occurrence for the exact unit
  or keep that uncertainty explicit.

## Recommended Edits

- Major: in `data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`, replace
  the exact `CHEBI:27864` identity with a local
  `kgmicrobe.ingredient:dichloran_02_in_ethanol` solution identity, preserve
  neat dichloran as an explicit component or parent relation only if the source
  supports the partonomy, synchronize `data/curated/mapped_ingredients.yaml`,
  and regenerate final SSSOM so the published row no longer exact-maps the
  stock solution to the neat ChEBI compound.
- Minor: refresh or retire `mappings/culturemech_residual_triage.tsv` row 1175
  so the residual worklist no longer records the lossy
  `Dichloran (0.2% in ethanol)` to `dichloran` normalization as unresolved.
