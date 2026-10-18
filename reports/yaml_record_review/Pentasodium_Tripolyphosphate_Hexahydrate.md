# `data/ingredients/mapped/Pentasodium_Tripolyphosphate_Hexahydrate.yaml`

## Verdict

Pass. The record keeps pentasodium tripolyphosphate hexahydrate on its CAS
registry identifier, represents FOODON sodium tripolyphosphate as a broader
parent, and emits the expected exact CAS and kg-microbe registry rows.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Pentasodium_Tripolyphosphate_Hexahydrate.yaml`.
- Identifier and grounding: `identifier: cas:15091-98-2` with
  `ontology_mapping.ontology_id: FOODON:03530244`, label
  `sodium tripolyphosphate`, source `FOODON`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `FOODON:03530244` resolves
  `sodium tripolyphosphate`.
- Fresh PubChem/OLS4 searches confirmed that `15091-98-2` resolves in PubChem
  but not as a CHEBI term, so the current CAS registry identity remains needed.
- The final SSSOM rows were inspected directly and publish the parent
  `skos:narrowMatch` to `FOODON:03530244` plus exact `cas:15091-98-2` and
  `kgmicrobe.ingredient:pentasodium_tripolyphosphate_hexahydrate` rows.

## Evidence

- The FOODON parent row is intentionally broader than the hydrate subject.
- `reports/hydrate_grounding.tsv` classifies this CAS-primary hydrate as
  `OK_OWN_CAS_ID`, and row review keeps both the CAS row and the local
  kg-microbe companion row as expected registry identifiers.
- The structured formula, SMILES, and InChI all preserve the five sodium
  counterions and six waters.
- Final SSSOM `other` exports only `CAS:15091-98-2` on the exact registry rows.

## Completeness

- The parent FOODON mapping and the exact registry rows are complete enough
  until a source-backed CHEBI primary exists for pentasodium tripolyphosphate
  hexahydrate.

## Recommended Edits

- None.
