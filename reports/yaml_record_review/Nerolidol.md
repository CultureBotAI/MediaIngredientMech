# `data/ingredients/mapped/Nerolidol.yaml`

## Verdict

Needs curation - major. The exact generic `CHEBI:7524` nerolidol grounding,
generic structure, reviewed ChEBI synonym, and final row otherwise agree, but
stored CAS `7212-44-4` resolves in PubChem to a stereospecific `(6E)` compound.

## Identity

- Reviewed record: `data/ingredients/mapped/Nerolidol.yaml`.
- Identifier and grounding: `identifier: CHEBI:7524` with
  `ontology_mapping.ontology_id: CHEBI:7524`, label `nerolidol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Neomycin_F` through `Netilmycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7524` as active generic `nerolidol`
  with formula `C15H26O`, CAS `7212-44-4`, the retained IUPAC synonym, and the
  same generic InChI and SMILES as the record.
- Major: a fresh PubChem CAS lookup for `7212-44-4` resolves to a compound with
  IUPAC name `(6E)-3,7,11-trimethyldodeca-1,6,10-trien-3-ol` and an InChI that
  fixes the `6E` double bond, while `CHEBI:7524` is the generic parent whose
  definition covers more than one geometric isomer. The final SSSOM currently
  exports `CAS:7212-44-4` as `other` on the generic exact row.
- A fresh OLS4 search did not find a direct ChEBI record for CAS `7212-44-4`;
  OLS does resolve narrower `(3S,6E)-nerolidol` and `(3R,6E)-nerolidol`
  children, so the CAS needs curator review before being asserted on the
  generic term.

## Completeness

- The active ChEBI term, generic formula and structure, 0/0 occurrence count,
  and final exact row otherwise agree.
- The remaining consequential gap is deciding whether the CultureBotHT CAS
  should be rejected for the generic record, replaced by a less specific
  source note, or remapped to a stereospecific nerolidol child.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nerolidol.yaml`, review CAS
  `7212-44-4` against the source row and either reject/delete it from the
  generic `CHEBI:7524` record or remap the source to a specific supported
  nerolidol isomer before rebuilding final SSSOM.
