# `data/ingredients/mapped/Meropenem.yaml`

## Verdict

Needs curation. The CAS-to-ChEBI regrounding correctly points at meropenem
trihydrate, but the YAML chemistry and final SSSOM `other` column still carry
anhydrous meropenem payloads, and `SELECTIVE_AGENT` is only a provisional
name-pattern inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Meropenem.yaml`.
- Identifier and grounding: `identifier: CHEBI:6770` with
  `ontology_mapping.ontology_id: CHEBI:6770`, label `meropenem trihydrate`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Current chemical fields are stale: the record stores formula
  `C17H25N3O5S` and an anhydrous InChI/SMILES even though it now denotes the
  trihydrate.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Menthol` through `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:6770` as active `meropenem trihydrate` with CAS
  `119478-56-7`, formula `C17H25N3O5S.3H2O`, and three water molecules in the
  InChI and SMILES.
- PubChem resolves CAS `119478-56-7` to CID 441129 with formula
  `C17H31N3O8S` and the same trihydrate InChI as ChEBI.
- EBI OLS4 resolves the separate anhydrous `CHEBI:43968` term as `meropenem`
  with formula `C17H25N3O5S`, CAS `96036-03-2`, and the anhydrous synonyms that
  were backfilled into this trihydrate record.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Meropenem` to
  `CHEBI:6770`, but its `other` column includes anhydrous labels such as
  `meropenem anhydrous` and the anhydrous IUPAC synonyms from `CHEBI:43968`.

## Completeness

- `chemical_properties.molecular_formula`, `chemical_properties.inchi`, and
  `chemical_properties.smiles` should describe `CHEBI:6770` / CAS
  `119478-56-7`, not the anhydrous parent.
- `SELECTIVE_AGENT` is only backed by a `COMPUTATIONAL_PREDICTION` inferred
  from a media-role name pattern. No source attached to the role verifies that
  this meropenem-trihydrate record was supplied as a selective agent.

## Recommended Edits

- Replace the anhydrous chemical properties in
  `data/ingredients/mapped/Meropenem.yaml` with `CHEBI:6770` trihydrate
  chemistry.
- Remove anhydrous `CHEBI:43968` labels from the curated synonym list or mark
  them as provenance-only rejected labels so they stop exporting in final
  SSSOM `other`.
- Curate recipe or literature evidence for `SELECTIVE_AGENT`, or remove the
  provisional physicochemical role.
