# `data/ingredients/mapped/Spermidine_Trihydrochloride.yaml`

## Verdict

Pass. The CultureBotHT record, CHEBI identity, CAS, exact synonym, structure
fields, and final SSSOM row all agree for spermidine trihydrochloride.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Spermidine_Trihydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:233088` with
  `ontology_mapping.ontology_id: CHEBI:233088`, label
  `spermidine trihydrochloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 334-50-9`, formula `C7H19N3.3HCl`, and
  trihydrochloride InChI and SMILES.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soyton` through `Spermidine_Trihydrochloride`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:233088` with label
  `spermidine trihydrochloride` and the same exact synonym retained in YAML.
- PubChem resolves CAS `334-50-9` to CID `9539`, with IUPAC name
  `N'-(3-aminopropyl)butane-1,4-diamine;trihydrochloride` and an InChI that
  decomposes to `C7H19N3.3ClH`, agreeing with the stored
  trihydrochloride identity.
- The final SSSOM row exact-matches `CHEBI:233088` and publishes only the
  ChEBI exact synonym plus `CAS:334-50-9` in `other`.

## Completeness

- A gitignore-independent `rg --no-ignore --hidden` scan across maintained
  `data`, `src`, `tests`, `mappings`, `scripts`, and
  `reports/hydrate_grounding.tsv`, excluding generated backups and prior YAML
  review reports, found only the expected distinction between this
  trihydrochloride salt and the separate base `spermidine` record.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
