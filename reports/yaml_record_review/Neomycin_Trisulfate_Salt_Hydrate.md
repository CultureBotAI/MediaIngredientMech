# `data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml`

## Verdict

Needs curation - major. The local hydrate registry identity, curated close
match to `CHEBI:31635`, CAS support for the neomycin-sulfate parent, and final
SSSOM companion rows agree, but `SELECTIVE_AGENT` remains only a provisional
name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:neomycin_trisulfate_salt_hydrate` with
  `ontology_mapping.ontology_id: CHEBI:31635`, label `neomycin sulfate`,
  source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Neomycin_F` through `Netilmycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this
  registry-primary record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:31635` as active
  `neomycin sulfate`, lists CAS `1405-10-3`, and does not publish an exact
  neomycin-trisulfate-hydrate structural definition.
- A fresh PubChem CAS lookup for `1405-10-3` resolves to a neomycin sulfate
  structure, supporting the parent sulfate match without establishing an exact
  hydrate identity.
- The final SSSOM keeps the intended two-row representation: a
  `skos:closeMatch` from `MIM:Neomycin_Trisulfate_Salt_Hydrate` to
  `CHEBI:31635`, plus an exact
  `kgmicrobe.compound:neomycin_trisulfate_salt_hydrate` registry row that
  preserves the local source identity. The hydrate-grounding report grades
  this as `OK_LOCAL_REGISTRY_ID`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence inferred from a name-pattern rule, and
  the evidence note explicitly marks the role provisional.

## Completeness

- The local identifier, close ChEBI parent, CAS RN, hydrate-grounding row, and
  final companion rows agree.
- The remaining consequential gap is source evidence for, or removal of, the
  provisional `SELECTIVE_AGENT` role.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Neomycin_Trisulfate_Salt_Hydrate.yaml`, either
  replace the provisional `SELECTIVE_AGENT` assertion with database or
  publication evidence at the role claim or remove it before rebuilding
  downstream products.
