# `data/ingredients/mapped/Uranyl_Acetate.yaml`

## Verdict

Needs curation, major. The CAS primary identity, MeSH parent mapping, registry
SSSOM siblings, aggregate row, and final SSSOM rows pass, but the PubChem
structure fields are pinned to an older CID that no longer carries the CAS RN.

## Identity

- Reviewed record: `data/ingredients/mapped/Uranyl_Acetate.yaml`.
- Identifier and grounding: `identifier: cas:541-09-3` with parent
  `ontology_mapping.ontology_id: mesh:C005460`, label `uranyl acetate`, source
  `MESH`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `541-09-3`.
- Synonyms: none.
- Occurrences: 2 CultureBotHT media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uranyl_Acetate` through `Uridine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch.
  The lower-case `mesh:C005460` parent and CAS registry identity are covered by
  exact OLS/PubChem checks and by the existing unknown-term triage rows that
  classify the final validation stamps as expected local registry or
  missing-prefix-validator coverage.

## Evidence

- Fresh exact OLS4 search for `uranyl acetate` in MeSH returns active
  `mesh:C005460`, supporting the parent `skos:narrowMatch` row.
- The final SSSOM rows correctly publish
  `MIM:Uranyl_Acetate skos:narrowMatch mesh:C005460` plus exact CAS and
  `kgmicrobe.compound:uranyl_acetate` registry siblings.

## Issues

### Major: PubChem fields are pinned to an outdated CAS representation

`chemical_properties.pubchem_cid` is `10915`, whose current PubChem synonyms no
longer include `541-09-3` and whose formula is `C4H8O6U`. A fresh PubChem CAS
lookup for `541-09-3` resolves instead to CID 21226249 with formula `C4H6O6U`
and a charged diacetate representation.

The CAS primary identifier and parent MeSH mapping still make sense, but the
record should refresh `chemical_properties` from the current CAS-specific
PubChem compound.

## Completeness

- The CAS identity, MeSH parent, aggregate copy, and three final SSSOM rows
  agree.
- The hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` found the expected missing-prefix and expected-registry triage rows
  for the MeSH parent, CAS registry row, and `kgmicrobe.compound` sibling.

## Recommended Edits

- Refresh `chemical_properties` from the current PubChem record for
  `CAS:541-09-3`, preserving the `NARROW_MATCH` MeSH parent and exact CAS /
  `kgmicrobe.compound` registry SSSOM rows.
