# `data/ingredients/mapped/Timentin.yaml`

## Verdict

Needs curation, major. The CAS registry row is synchronized, but the record
models a ticarcillin plus clavulanic-acid mixture as `SINGLE_INGREDIENT` and
has no component decomposition.

## Identity

- Reviewed record: `data/ingredients/mapped/Timentin.yaml`.
- Identifier and grounding: `identifier: cas:86482-18-0` with matching
  `ontology_mapping.ontology_id`, label `Timentin`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `86482-18-0`.
- PubChem CID: `6437075`.
- Synonyms: none.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Ticarcillin` through `TitaniumIII_Chloride`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- A fresh PubChem CAS lookup for `86482-18-0` resolves to CID `6437075` with
  formula `C23H25N3O11S2`, matching the YAML formula.
- That CID is a two-component record: PubChem returns disconnected ticarcillin
  and clavulanic-acid SMILES/InChI components and names it with mixture labels
  such as ticarcillin plus clavulanic acid and ticarcillin disodium plus
  clavulanate potassium.
- The final SSSOM row has `MIM:Timentin skos:exactMatch cas:86482-18-0`, uses
  `registry:cas`, and exports only `CAS:86482-18-0` in `other`.

## Issues

### Major: a combination antibiotic is modeled as one ingredient

`chemical_properties.inchi` and the PubChem response both contain two
disconnected formula layers, and PubChem names the CAS object as a
ticarcillin/clavulanic-acid mixture. The YAML nevertheless sets:

```yaml
ingredient_type: SINGLE_INGREDIENT
components: null
```

That loses the fact that a Timentin dose contributes two antimicrobial
constituents. The final CAS row is internally consistent, but downstream
component-aware consumers will see a single defined chemical rather than a
mixture.

## Completeness

- The CAS RN, PubChem structure, aggregate copy, and final SSSOM row agree.
- No final SSSOM synonym leakage is present.
- The missing mixture modeling is the remaining blocker.

## Recommended Edits

- Reclassify the record as a mixture or formulation and add reviewed
  components for ticarcillin and clavulanate, using the precise salt/hydration
  states supported by the source.
