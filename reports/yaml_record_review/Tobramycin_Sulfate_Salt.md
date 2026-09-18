# `data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml`

## Verdict

Needs curation, major. The CAS registry identity is synchronized, but the ChEBI
parent is the generic `sulfate salt` class even though a specific tobramycin
sulfate term is available, and `SELECTIVE_AGENT` is still provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Tobramycin_Sulfate_Salt.yaml`.
- Identifier and grounding: `identifier: cas:79645-27-5`, parent
  `ontology_mapping.ontology_id: CHEBI:35175`, label `sulfate salt`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `79645-27-5`.
- Synonyms: none.
- Roles: one `physicochemical_roles.SELECTIVE_AGENT` facet at confidence
  `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Titanium_chloride` through `Tomatidine_Hydrochloride`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh PubChem lookup for CAS `79645-27-5` resolves to a CID whose formula and
  InChI contain neutral tobramycin plus one sulfuric-acid component.
- Fresh exact OLS4 search for `tobramycin sulfate` returns `CHEBI:756148`
  `tobramycin sulfate`; the current `CHEBI:35175` target is only the generic
  sulfate-salt class.
- The final SSSOM has three rows: a `skos:narrowMatch` to `CHEBI:35175`, an
  exact CAS registry row, and an exact `kgmicrobe.compound` companion row.

## Issues

### Major: the ChEBI parent erases the tobramycin identity

The stem-substring repair landed on:

```yaml
ontology_mapping:
  ontology_id: CHEBI:35175
  ontology_label: sulfate salt
  mapping_quality: NARROW_MATCH
```

Every sulfate antibiotic salt is narrower than generic `sulfate salt`, so this
parent does not carry the biologically important tobramycin identity into the
ontology row. A specific `CHEBI:756148` `tobramycin sulfate` term is now
visible in OLS and should be evaluated for exact remapping.

### Major: `SELECTIVE_AGENT` is provisional name-pattern evidence

The only role assertion is still the `infer_roles_from_name_lists`
`COMPUTATIONAL_PREDICTION` entry with the curator note `Provisional role from a
curated name-pattern rule; review recommended.` That needs curated evidence or
removal just like the other antibiotic-salt records.

## Completeness

- The CAS and local registry rows are internally synchronized.
- No final SSSOM free-text synonyms leak.
- The specific ontology parent and the provisional role facet still need
  curation.

## Recommended Edits

- Evaluate exact remapping to `CHEBI:756148` `tobramycin sulfate`; if accepted,
  retire the generic `CHEBI:35175` parent and the local registry companion row.
- Replace or remove the provisional `SELECTIVE_AGENT` role evidence.
