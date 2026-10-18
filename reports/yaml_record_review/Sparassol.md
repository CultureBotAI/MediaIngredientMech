# `data/ingredients/mapped/Sparassol.yaml`

## Verdict

Needs curation - major. The CAS identity itself resolves to Sparassol, but the
record still asserts that no CHEBI entry exists even though current PubChem and
OLS lookups identify active `CHEBI:92544` for the same compound.

## Identity

- Reviewed record: `data/ingredients/mapped/Sparassol.yaml`.
- Identifier and grounding: `identifier: cas:520-43-4` with
  `ontology_mapping.ontology_id: cas:520-43-4`, label `Sparassol`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 520-43-4`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soyton` through `Spermidine_Trihydrochloride`: exited 0 and wrote zero ERROR
  rows.
- Engine A term validation was skipped for this CAS target; the non-OBO CURIE
  is covered by the product validator rather than OAK.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- PubChem resolves both `Sparassol` and `520-43-4` to CID `596344`; that CID
  has formula `C10H12O4`, the IUPAC name `methyl
  2-hydroxy-4-methoxy-6-methylbenzoate`, and synonym `CHEBI:92544`.
- Fresh OLS4 lookup resolves active `CHEBI:92544` with label
  `2-hydroxy-4-methoxy-6-methylbenzoic acid methyl ester`, matching the same
  ester identity.
- Major: the maintained YAML says no CHEBI entry exists and therefore keeps a
  CAS fallback as its primary mapping. That fallback is now stale unless a
  follow-up ChEBI inspection finds a form conflict not visible in the current
  PubChem and OLS evidence.
- A gitignore-independent `rg --no-ignore --hidden` scan across maintained
  `data`, `src`, `tests`, `mappings`, and `scripts`, excluding generated
  backups and prior YAML review reports, found no existing `CHEBI:92544` usage.

## Completeness

- The final SSSOM row is internally consistent with the current CAS fallback
  and only publishes `CAS:520-43-4` as `other`.
- No unsupported active synonym, role, or component was found, but the mapping
  should be promoted from the CAS fallback if CHEBI source verification
  confirms the PubChem/OLS identity.

## Recommended Edits

- Major: verify `CHEBI:92544` directly against the ChEBI term and, if it is the
  exact Sparassol identity, update `data/ingredients/mapped/Sparassol.yaml` and
  the aggregate mapped row from `cas:520-43-4` to `CHEBI:92544`, retaining
  `520-43-4` as `chemical_properties.cas_rn`.
- Regenerate the SSSOM row after that YAML repair so
  `mappings/ingredient_mappings.sssom.tsv` points at the CHEBI target instead
  of a stale CAS fallback.
