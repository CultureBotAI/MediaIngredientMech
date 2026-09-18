# `data/ingredients/mapped/TransTrans-Farnesol.yaml`

## Verdict

Pass. The stereospecific CHEBI regrounding, CAS RN, PubChem structure,
aggregate row, rejected broad synonym, and final SSSOM row for
trans,trans-farnesol are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/TransTrans-Farnesol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16619` with matching
  `ontology_mapping.ontology_id`, label `(2-trans,6-trans)-farnesol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `106-28-5`.
- PubChem CID: `445070`.
- Synonyms: one old inherited ChEBI label retained as `REJECTED_LABEL`.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trans-cinnamic_Acid` through `Trehalose`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `(2-trans,6-trans)-farnesol` returns
  `CHEBI:16619`, matching the September issue 456 stereochemistry repair.
- Fresh PubChem lookup for CID `445070` returns formula `C15H26O` and the same
  E,E InChI as the YAML.
- The final SSSOM row has
  `MIM:TransTrans-Farnesol skos:exactMatch CHEBI:16619` and exports only
  `CAS:106-28-5` in `other`; the old stereochemistry-free chemical name is
  marked `REJECTED_LABEL` in YAML and does not leak into final SSSOM.

## Completeness

- The stereospecific CHEBI identity, CAS RN, PubChem CID, structure fields,
  aggregate copy, and final SSSOM row agree.
- No media roles, components, environmental contexts, or bad final synonym
  tokens are asserted.

## Recommended Edits

- None.
