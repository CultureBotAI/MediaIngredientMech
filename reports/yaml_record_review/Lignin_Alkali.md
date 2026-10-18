# `data/ingredients/mapped/Lignin_Alkali.yaml`

## Verdict

Needs curation. The local CAS fallback row for alkali lignin is scoped
honestly, and no exact CHEBI/NCIT/MeSH replacement surfaced, but the populated
`chemical_properties` block is from an unrelated PubChem CID synonym collision.

## Identity

- Reviewed record: `data/ingredients/mapped/Lignin_Alkali.yaml`.
- Identifier and grounding: `identifier: cas:8068-05-1` with
  `ontology_mapping.ontology_id: cas:8068-05-1`, label `Lignin alkali`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties currently assert CAS RN `8068-05-1` but also formula
  `C18H13N3Na2O8S2`, SMILES, InChI, and `pubchem_cid: 175586`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lignin_Alkali` through `Lincomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Limonin.yaml`, `Linalool.yaml`, and `Lincomycin.yaml`. `Lignin_Alkali.yaml`
  and `Limocrocin.yaml` were skipped from that CHEBI/OBO subset because their
  ontology IDs are local CAS and MeSH registry CURIEs.

## Evidence

- PubChem lookup by CAS RN `8068-05-1` found no CID.
- PubChem CID `175586` resolves to formula `C18H13N3Na2O8S2` and the same
  InChI as the YAML record, but its IUPAC name is
  `disodium;4-acetamido-5-hydroxy-6-phenyldiazenylnaphthalene-1,7-disulfonate`,
  not alkali lignin.
- EBI OLS4 search for exact `Lignin alkali` found no usable current chemical
  ontology target; the returned ligninophile NCBITaxon hit is irrelevant.
- The final SSSOM publishes one `skos:exactMatch` row to `cas:8068-05-1`; its
  `other` field contains only `CAS:8068-05-1`.
- Major: the `chemical_properties.molecular_formula`, `smiles`, `inchi`, and
  `pubchem_cid` values describe PubChem CID `175586`, a discrete azo compound,
  rather than the `cas:8068-05-1` alkali lignin subject.

## Completeness

- The fallback CAS identity, aggregate copy, and final SSSOM row are present and
  consistent.
- The structure block needs removal or replacement with source-backed alkali
  lignin properties.

## Recommended Edits

- Major: remove the CID `175586` formula, SMILES, InChI, and `pubchem_cid` from
  `data/ingredients/mapped/Lignin_Alkali.yaml` unless a curator can prove those
  values denote CAS `8068-05-1`.
- Retain the `cas:8068-05-1` fallback identity unless a more specific active
  ontology term is found.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, round-trip, component, and SSSOM validation.
