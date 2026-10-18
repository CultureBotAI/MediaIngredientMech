# `data/ingredients/mapped/Menadione_Sodium_Bisulfate.yaml`

## Verdict

Needs curation. The CAS-grounded ChEBI identity, formula, exact IUPAC synonym,
and final `other` values pass, but the published preferred term says
`bisulfate` for a CAS-backed `bisulfite`/sulfonate compound and the
`VITAMIN_SOURCE` role is only a provisional name-pattern inference.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Menadione_Sodium_Bisulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63928` with
  `ontology_mapping.ontology_id: CHEBI:63928`, label `menadione sodium
  sulfonate`, source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 130-37-0`, formula `C11H9O5S.Na`, and InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Melibiose` through `Menaquinone`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:63928` as active `menadione sodium sulfonate` with
  CAS `130-37-0`, formula `C11H9O5S.Na`, the same InChI and SMILES carried in
  the YAML, and the curated exact IUPAC synonym.
- PubChem resolves CAS `130-37-0` to CID 23665888 with formula `C11H9NaO5S` and
  the same InChI carried in the YAML.
- A fresh exact all-ontology OLS4 search for `Menadione sodium bisulfate`
  returned zero results. PubChem's `130-37-0` synonym list contains bisulfite
  and sulfonate labels, but not the `bisulfate` form used in the local
  preferred term.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Menadione_Sodium_Bisulfate` to `CHEBI:63928`; the IUPAC `other` token
  is a same-compound ChEBI synonym and `CAS:130-37-0` matches
  `chemical_properties.cas_rn`.

## Completeness

- `preferred_term` and the final SSSOM `subject_label` are not exact labels for
  `CHEBI:63928` because they say `bisulfate` rather than bisulfite or
  sulfonate.
- `VITAMIN_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from
  a media-role name pattern. No source attached to the role verifies that this
  menadione sulfonate record was supplied as a vitamin source.

## Recommended Edits

- Rename the maintained record to a true `CHEBI:63928` synonym, such as
  `Menadione sodium bisulfite`, and keep `Menadione sodium bisulfate` only as a
  non-resolving source label if the original CultureBotHT row used that text.
- Curate recipe or literature evidence for `VITAMIN_SOURCE`, or remove the
  provisional nutritional role.
