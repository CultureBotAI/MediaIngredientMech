# `data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml`

## Verdict

Needs curation. The CAS-primary identity, MeSH parent row, exact CAS row, exact
KG-Microbe registry row, and PubChem structure are internally consistent, but
CHEBI now has a plausible Lacto-N-fucopentaose I candidate that needs a direct
structural decision and the carbon-source role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml`.
- Identifier and grounding: `identifier: cas:7578-25-8` with
  `ontology_mapping.ontology_id: mesh:C045442`, label
  `lacto-N-fucopentaose I`, source `MESH`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7578-25-8`, PubChem CID `16219579`, molecular
  formula `C32H55NO25`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacidipine` through `Lacto-N-fucopentaose_I`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this MeSH/CAS record because the
  successful batch check covered only the CHEBI-primary records.

## Evidence

- PubChem resolves CAS RN `7578-25-8` to CID `16219579` with formula
  `C32H55NO25` and the same InChI as the YAML record.
- OLS resolves `mesh:C045442` exactly as `lacto-N-fucopentaose I`, so the broad
  MeSH parent row matches the preferred term.
- The final SSSOM publishes the expected three-row NARROW_MATCH pattern: one
  `skos:narrowMatch` row to `mesh:C045442`, one identity-preserving exact row
  to `cas:7578-25-8`, and one exact KG-Microbe registry sibling row.
- Major: the CAS-fallback evidence still says no CHEBI entry exists for this
  compound, but current OLS lookup finds `CHEBI:61357` with the synonym
  `Lacto-N-fucopentaose I` and the same molecular formula. Its InChIKey differs
  from PubChem CID `16219579`, so a curator needs to either promote to CHEBI if
  that term is the same structure or keep the CAS/MeSH mapping with an explicit
  structural rejection of `CHEBI:61357`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule and
  explicitly says review is recommended.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  rows and Lacto-N-fucopentaose II/III sibling records, confirming this record
  denotes the I isomer specifically rather than a family bucket.

## Completeness

- The CAS RN, PubChem structure, MeSH parent, and required registry sibling rows
  are present.
- The record is incomplete until `CHEBI:61357` is checked and either adopted as
  the exact ontology grounding or documented as a near miss.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: inspect `CHEBI:61357` against PubChem CID `16219579`; then either
  promote `data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml` to exact CHEBI
  grounding or add reviewed rejection/provenance explaining why the CHEBI term
  is structurally different from CAS RN `7578-25-8`.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected source
  evidence for exact Lacto-N-fucopentaose I use, or remove the provisional role.
- Sync the aggregate copy and regenerate final SSSOM after any YAML changes;
  rerun strict, product, component, and SSSOM validation.
