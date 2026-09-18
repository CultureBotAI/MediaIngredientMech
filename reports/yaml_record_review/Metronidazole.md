# `data/ingredients/mapped/Metronidazole.yaml`

## Verdict

Needs curation. The exact `CHEBI:6909` metronidazole identity, CAS value,
ChEBI/PubChem structure, exact ChEBI synonym, row-review stamp, and final SSSOM
row pass, but `SELECTIVE_AGENT` is still a provisional name-list role with only
`COMPUTATIONAL_PREDICTION` evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Metronidazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:6909` with
  `ontology_mapping.ontology_id: CHEBI:6909`, label `metronidazole`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: CAS `443-48-1`, formula `C6H9N3O3`, SMILES, and InChI.
- Role: one `physicochemical_roles` entry, `SELECTIVE_AGENT`, inferred by
  `infer_roles_from_name_lists` as a curated name-pattern rule.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Metronidazole` through `MgO`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:6909` as active `metronidazole` with exact synonym
  `2-(2-methyl-5-nitro-1H-imidazol-1-yl)ethanol`.
- PubChem resolves CAS `443-48-1` to CID 4173 with formula `C6H9N3O3` and the
  same InChI carried in the YAML.
- The OAK/OLS row-review manifest confirmed the `CHEBI:6909` mapping.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Metronidazole` to `CHEBI:6909`; its `other` tokens are the exact ChEBI
  synonym and `CAS:443-48-1`.

## Completeness

- The chemical identity, CAS value, active ChEBI target, exact synonym, and
  final SSSOM synonym export agree.
- The `SELECTIVE_AGENT` role is not backed by recipe-specific or imported
  database evidence. The only role evidence says it was inferred from a curated
  media-role name pattern and is provisional.

## Recommended Edits

- Major: replace the provisional `SELECTIVE_AGENT` role with a supported
  physicochemical-role assertion if this ingredient is intentionally used as a
  selective agent in media, or remove the role facet from
  `data/ingredients/mapped/Metronidazole.yaml`.
