# `data/ingredients/mapped/Mes.yaml`

## Verdict

Needs curation. The CHEBI label-exact row is active and the BUFFER role is
CultureMech-backed, but the record duplicates the structural MES acid record
and publishes CAS `4432-31-9` against a skeletal `CHEBI:39010` entry that lacks
that registry xref and structure.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mes.yaml`.
- Identifier and grounding: `identifier: CHEBI:39010` with
  `ontology_mapping.ontology_id: CHEBI:39010`, label `MES`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 111 CultureMech recipes.
- Current chemical properties only contain `cas_rn: 4432-31-9`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Menthol` through `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid`: exited 0 and
  wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:39010` as active `MES`, but that entry currently has
  no formula, CAS xref, structure, definition, or synonym annotations.
- EBI OLS4 resolves sibling `CHEBI:39005` as active
  `2-(N-morpholino)ethanesulfonic acid`, with CAS `4432-31-9`, formula
  `C6H13NO4S`, and the same InChI that PubChem returns for CAS `4432-31-9`.
- `rg --no-ignore --hidden` over `data`, `mappings`, `reports`, `scripts`,
  `src`, and `tests` found the active
  `data/ingredients/mapped/Mes_2-_N-morpholino_Ethane_Sulfonic_Acid.yaml`
  sibling with the same CAS and the structural `CHEBI:39005` grounding.
- The `BUFFER` facet is backed by the original CultureMech role text `Buffer`,
  so it is not only a name-derived inference.
- The final SSSOM publishes `CAS:4432-31-9` in `MIM:Mes` `other`, but that CAS
  belongs to `CHEBI:39005` and the duplicate `MIM:Mes_2-_N-morpholino_Ethane_Sulfonic_Acid`
  record.

## Completeness

- The raw CultureMech role/property synonyms remain in YAML as provenance but
  are filtered from final SSSOM.
- The record needs duplicate reconciliation with the structural MES acid row, or
  it needs its local CAS field and final CAS `other` removed if `CHEBI:39010`
  should intentionally remain distinct.

## Recommended Edits

- Merge or remap `Mes.yaml` into
  `Mes_2-_N-morpholino_Ethane_Sulfonic_Acid.yaml` if both denote CAS
  `4432-31-9`.
- If `CHEBI:39010` is intentionally a distinct MES class, remove
  `cas_rn: 4432-31-9` and stop exporting `CAS:4432-31-9` from the `MIM:Mes`
  final SSSOM row.
