# `data/ingredients/mapped/Mg-citrate.yaml`

## Verdict

Needs curation. The #320 regrounding moved the identifier and ontology target to
`CHEBI:131391` trimagnesium dicitrate, the 3:2 salt identified by CAS
`3344-18-1`, but the local chemistry and final SSSOM `other` synonyms still
describe `CHEBI:131389` magnesium citrate, a 1:1 magnesium hydrogen citrate
salt.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mg-citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:131391` with
  `ontology_mapping.ontology_id: CHEBI:131391`, label
  `trimagnesium dicitrate`, source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: five CultureMech recipe occurrences.
- Current chemical identity in the YAML: CAS `3344-18-1`, formula
  `C6H6O7.Mg`, and one-citrate/one-magnesium SMILES and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Metronidazole` through `MgO`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:131391` as active `trimagnesium dicitrate` and
  defines it as a magnesium salt composed of magnesium and citrate ions in a
  3:2 ratio.
- PubChem resolves CAS `3344-18-1` to CID 6099959 with formula
  `C12H10Mg3O14`, SMILES containing two citrate anions and three magnesium
  cations, and a matching 2-citrate/3-magnesium InChI.
- The YAML's formula `C6H6O7.Mg`, SMILES, and InChI describe the old
  one-citrate/one-magnesium salt, not `CHEBI:131391`.
- EBI OLS4 exact searches resolve `E345`, `Magnesium citrate dibasic`,
  `Magnesium hydrogen citrate`, and
  `magnesium 3-carboxy-3-hydroxypentanedioate` to `CHEBI:131389`, whose
  description is a 1:1 magnesium/dibasic-citrate salt.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mg-citrate` to
  `CHEBI:131391`, but `other` still contains the four `CHEBI:131389` synonyms
  above alongside `CAS:3344-18-1`.

## Completeness

- The CAS-based target choice from #320 is coherent: `CHEBI:131391` is the
  3:2 salt and PubChem maps `3344-18-1` to the same stoichiometry.
- The stale chemistry fields and stale `kg_microbe` synonyms make the YAML and
  final SSSOM simultaneously assert the new 3:2 salt and the old 1:1 salt.

## Recommended Edits

- Major: backfill `chemical_properties.molecular_formula`, `smiles`, and
  `inchi` from the active `CHEBI:131391` or PubChem CID 6099959 structure.
- Major: remove or replace the four `CHEBI:131389` `kg_microbe` synonyms so the
  final SSSOM `other` field exports only names that are exact for
  trimagnesium dicitrate.
