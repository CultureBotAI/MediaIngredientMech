# `data/ingredients/mapped/Hepes.yaml`

## Verdict

Needs curation. The re-grounded exact HEPES identity, CAS RN, and
CultureMech-backed `BUFFER` role pass, but final SSSOM exports concentration,
CAS-decorated, and catalog-decorated labels as exact `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Hepes.yaml`.
- Identifier and grounding: `identifier: CHEBI:42334` with
  `ontology_mapping.ontology_id: CHEBI:42334`, label
  `2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:42334`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7365-45-9`.
- Role: `physicochemical_roles.BUFFER`, with `DATABASE_ENTRY` evidence from
  CultureMech `Role: Buffer` source text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hepes.yaml data/ingredients/mapped/Heptadecane.yaml data/ingredients/mapped/Heptadecanoic_Acid.yaml data/ingredients/mapped/Heptanoic_Acid.yaml data/ingredients/mapped/Heptanol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:42334`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1421`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1421`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:42334` as active
  `2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid`, with `Hepes` and
  `4-(2-Hydroxyethyl)-1-piperazineethane sulfonic acid` as synonyms.
- PubChem resolves CAS RN `7365-45-9` to
  `4-(2-Hydroxyethyl)-1-piperazineethanesulfonic acid`, formula `C8H18N2O4S`,
  SMILES `C1CN(CCN1CCO)CCS(=O)(=O)O`, and the corresponding InChI.
- The `BUFFER` role is supported by the attached CultureMech database entry:
  the excerpt explicitly records `Role: Buffer`.
- The raw `Role:`/`Properties:` synonyms stay out of final SSSOM, which is the
  right behavior for role/provenance payload.
- Major: the final SSSOM `other` column still exports `HEPES (10mM)`,
  `HEPES buffer(CAS: 7365-45-9)`, and `HEPES buffer(Sigma H-3375)`. These are
  concentration-specific, CAS-decorated, or supplier/catalog-decorated recipe
  surfaces rather than exact synonyms of the HEPES molecule.
- The final SSSOM otherwise publishes one `skos:exactMatch` row from
  `MIM:Hepes` to `CHEBI:42334`.

## Completeness

- The active ChEBI identifier, corrected KG-Microbe node ID, CAS RN,
  exact-match row, exact long-form ChEBI alias, occurrence count, and
  database-supported buffer role are present and consistent.
- The record is incomplete until non-identity HEPES buffer recipe aliases stop
  reaching the published SSSOM `other` column.

## Recommended Edits

- Major: suppress or retype `HEPES (10mM)`,
  `HEPES buffer(CAS: 7365-45-9)`, and `HEPES buffer(Sigma H-3375)` so they are
  retained only as provenance and no longer exported as final exact synonyms.
