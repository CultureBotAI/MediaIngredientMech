# `data/ingredients/mapped/Spectinomycin.yaml`

## Verdict

Pass. The MicrobeDecoder import, CHEBI identity, structure fields, occurrence
counts, and final SSSOM row all agree for base spectinomycin.

## Identity

- Reviewed record: `data/ingredients/mapped/Spectinomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:9215` with
  `ontology_mapping.ontology_id: CHEBI:9215`, label `spectinomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C14H24N2O7` with ChEBI/PubChem structure
  values.
- Occurrences: 1 source occurrence across 1 CultureMech medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soyton` through `Spermidine_Trihydrochloride`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9215` with canonical label
  `spectinomycin`, matching the stored ontology target.
- The record's molecular formula, InChI, and SMILES describe base
  spectinomycin, not the dihydrochloride pentahydrate salt tracked separately
  in `Spectinomycin_Dihydrochloride_Pentahydrate`.
- The final SSSOM row exact-matches `CHEBI:9215`, has no `other` synonyms, and
  does not leak salt or hydrate labels from the sibling record.

## Completeness

- A gitignore-independent `rg --no-ignore --hidden` scan across maintained
  `data`, `src`, `tests`, `mappings`, `scripts`, and
  `reports/hydrate_grounding.tsv`, excluding generated backups and prior YAML
  review reports, found only the expected base and
  dihydrochloride-pentahydrate records.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
