# `data/ingredients/mapped/Sodium_Perchlorate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:132103` sodium perchlorate identity,
CAS-backed structure, ChEBI synonyms, and occurrence count pass, but
`ELECTRON_ACCEPTOR` is provisional and final SSSOM publishes the monohydrate
label as an anhydrous sodium perchlorate synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Perchlorate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132103` with
  `ontology_mapping.ontology_id: CHEBI:132103`, label `sodium perchlorate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 4 source occurrences across 4 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Perchlorate` through `Sodium_Phosphate_Buffer`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh EBI OLS4 lookup resolves active `CHEBI:132103` with label
  `sodium perchlorate`, the four curated ChEBI synonyms, and CAS
  `7601-89-0`.
- Fresh PubChem lookup for CAS `7601-89-0` resolves to sodium perchlorate with
  the same sodium perchlorate InChI and SMILES as the record.
- Major: final SSSOM publishes `Sodium perchlorate monohydrate` in `other` for
  the anhydrous sodium perchlorate subject. A hydrate is a distinct supplied
  form, not a synonym of the anhydrous salt.
- Major: `cellular_metabolic_roles.ELECTRON_ACCEPTOR` is backed only by an
  in-session `COMPUTATIONAL_PREDICTION` with no external evidence and a
  `review recommended` note.

## Completeness

- The ChEBI ID, canonical label, CAS RN, formula, core structure, four ChEBI
  synonyms, and 4/4 occurrence count agree.
- The consequential gaps are the unsafe hydrate synonym in final SSSOM and the
  unsupported role facet.

## Recommended Edits

- Major: fix the SSSOM enrichment source so the final
  `MIM:Sodium_Perchlorate` row no longer emits
  `Sodium perchlorate monohydrate` as an `other` synonym.
- Major: in `data/ingredients/mapped/Sodium_Perchlorate.yaml`, remove
  `cellular_metabolic_roles.ELECTRON_ACCEPTOR` unless a checked source supports
  perchlorate in the reviewed medium context.
