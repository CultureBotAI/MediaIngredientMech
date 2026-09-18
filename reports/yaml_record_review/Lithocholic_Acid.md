# `data/ingredients/mapped/Lithocholic_Acid.yaml`

## Verdict

Needs curation. The CultureBotHT exact CHEBI:16325 identity, CAS RN, PubChem
structure, and real ChEBI synonym pass, but Tricine and berbaman labels from
`sssom_other_backfill` are attached to lithocholic acid and exported in the
final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Lithocholic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16325` with
  `ontology_mapping.ontology_id: CHEBI:16325`, label `lithocholic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `434-13-9`, molecular formula `C24H40O3`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lincomycin_Hydrochloride` through `Lithocholic_Acid`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for all five
  CHEBI-grounded records in the batch.

## Evidence

- EBI OLS4 resolves `CHEBI:16325` as active `lithocholic acid`, lists the real
  synonym `3alpha-hydroxy-5beta-cholan-24-oic acid`, lists CAS `434-13-9`, and
  records the same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `434-13-9` to CID `9903` with formula `C24H40O3` and
  the same InChI as the YAML record.
- PubChem resolves `N-(tri(hydroxymethyl)methyl)glycine` to CID `79784` with
  formula `C6H13NO5`, not lithocholic acid.
- PubChem resolves `berbaman` to CID `9548852` with formula `C32H30N2O2`, not
  lithocholic acid.
- Major: the YAML `synonyms` list and final SSSOM `other` field publish
  `N-(tri(hydroxymethyl)methyl)glycine`,
  `N-[2-hydroxy-1,1-bis(hydroxymethyl)ethyl]glycine`,
  `N-tris(hydroxymethyl)methylglycine`, and `berbaman` as exact same-substance
  labels for lithocholic acid. The first three are Tricine names and the fourth
  resolves to a distinct alkaloid scaffold.
- The final SSSOM also carries the valid ChEBI synonym
  `3alpha-hydroxy-5beta-cholan-24-oic acid` and `CAS:434-13-9`.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and valid final SSSOM payload are present and consistent.
- The published synonym surface is incomplete as a safe final product until
  Tricine and berbaman labels are removed from this record.

## Recommended Edits

- Major: remove the Tricine and berbaman `sssom_other_backfill` synonyms from
  `data/ingredients/mapped/Lithocholic_Acid.yaml`; keep only true
  lithocholic-acid synonyms on `CHEBI:16325`.
- Sync the aggregate copy and regenerate final SSSOM after the YAML changes;
  rerun strict, term, round-trip, component, and SSSOM validation.
