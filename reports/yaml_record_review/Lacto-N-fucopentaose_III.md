# `data/ingredients/mapped/Lacto-N-fucopentaose_III.yaml`

## Verdict

Needs curation. The CAS-primary identity, MeSH parent row, exact CAS row, exact
KG-Microbe registry row, and PubChem structure are internally consistent, but
CHEBI now has a plausible Lacto-N-fucopentaose III candidate that needs a
direct structural decision and the carbon-source role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Lacto-N-fucopentaose_III.yaml`.
- Identifier and grounding: `identifier: cas:25541-09-7` with
  `ontology_mapping.ontology_id: mesh:C434666`, label
  `lacto-N-fucopentaose III`, source `MESH`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `25541-09-7`, PubChem CID `53477857`, molecular
  formula `C32H55NO25`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacto-N-fucopentaose_II` through `Lactone`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this MeSH/CAS record because the
  successful batch check covered only the CHEBI-primary records.

## Evidence

- PubChem resolves CAS RN `25541-09-7` to CID `53477857` with formula
  `C32H55NO25` and the same InChI as the YAML record.
- OLS exact search resolves `mesh:C434666` as `lacto-N-fucopentaose III`, so the
  broad MeSH row matches the preferred term.
- The final SSSOM publishes the expected three-row NARROW_MATCH pattern: one
  `skos:narrowMatch` row to `mesh:C434666`, one identity-preserving exact row
  to `cas:25541-09-7`, and one exact KG-Microbe registry sibling row.
- Major: the CAS-fallback evidence still says no CHEBI entry exists for this
  compound, but current OLS lookup finds `CHEBI:61352` with the synonym
  `Lacto-N-fucopentaose III` and the same molecular formula. Its InChIKey
  differs from PubChem CID `53477857`, so a curator needs to either promote to
  CHEBI if that term is the same structure or keep the CAS/MeSH mapping with an
  explicit structural rejection of `CHEBI:61352`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule and
  explicitly says review is recommended.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  rows and Lacto-N-fucopentaose I/II sibling records, confirming this record
  denotes the III isomer specifically.

## Completeness

- The CAS RN, PubChem structure, MeSH parent, and required registry sibling rows
  are present.
- The record is incomplete until `CHEBI:61352` is checked and either adopted as
  the exact ontology grounding or documented as a near miss.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: inspect `CHEBI:61352` against PubChem CID `53477857`; then either
  promote `data/ingredients/mapped/Lacto-N-fucopentaose_III.yaml` to exact CHEBI
  grounding or add reviewed rejection/provenance explaining why the CHEBI term
  is structurally different from CAS RN `25541-09-7`.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected source
  evidence for exact Lacto-N-fucopentaose III use, or remove the provisional
  role.
- Sync the aggregate copy and regenerate final SSSOM after any YAML changes;
  rerun strict, product, component, and SSSOM validation.
