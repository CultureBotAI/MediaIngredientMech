# `data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`

## Verdict

Pass with minor issues. The CAS-primary gold(III) chloride hydrate record keeps
its local identity separate from anhydrous `CHEBI:30076` gold trichloride and
publishes the correct close parent plus exact registry rows, but the mapping
evidence still contains pre-`#342` narrow-match wording and the hydrate
stoichiometry still depends on unverified supplier/source context.

## Identity

- Reviewed record: `data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:27988-77-8` for the local hydrate
  identity with `ontology_mapping.ontology_id: CHEBI:30076`, canonical label
  `gold trichloride`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: PubChem CID `86810463`, CAS-RN `27988-77-8`, formula
  `AuCl4H3O`, InChI `InChI=1S/Au.4ClH.H2O/h;4*1H;1H2/q+3;;;;;/p-3`, and SMILES
  `O.Cl.Cl[Au](Cl)Cl`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycylglycine.yaml data/ingredients/mapped/Glycylglycylglycine.yaml data/ingredients/mapped/Glycyrrhizic_Acid_Ammonium_Salt.yaml data/ingredients/mapped/Glyoxylate.yaml data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `CHEBI:30076` as active `gold trichloride`, with formula
  `AuCl3`, the same anhydrous InChI represented by the ChEBI parent, and
  exact synonyms `gold trichloride`, `gold(3+) chloride`, and
  `gold(III) chloride`.
- PubChem CID `86810463` carries the same formula, InChI, and SMILES as the
  record and has supplier-style aliases for gold(III) chloride hydrate and
  hydrogen tetrachloroaurate hydrate.
- `mappings/hydrate_review.tsv` marks the CAS/local identity as the correct own
  identity and says the parent hydrate label has unspecified stoichiometry that
  needs original recipe or supplier context.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Gold_Iii_Chloride_Hydrate` to `CHEBI:30076` by `skos:closeMatch` and to
  `cas:27988-77-8` by `skos:exactMatch`; the only `other` token is the
  structured CAS synonym for the exact local identity.
- Minor: the `anchor_cas_hydrate_records` evidence still says the hydrate was
  anchored to `CHEBI:30076` by `narrowMatch`, although the record was
  intentionally regraded to `CLOSE_MATCH` in `#342`.
- Minor: PubChem's current CAS name lookup for `27988-77-8` returned no CID,
  and an exact, ignored-inclusive search for `27988-77-8` across the whole
  repository found only this record, generated products, hydrate review TSVs,
  SSSOM/row-review TSVs, and ignored aggregate backups. The retained CAS/local
  identity is plausible, but the original CultureBotHT source row was not
  available in this checkout to prove the supplied CAS and label together.
- Common Chemistry lookup for `27988-77-8` was unavailable because
  `commonchemistry.cas.org` did not resolve from this environment.

## Completeness

- The local CAS identity, ChEBI close parent, PubChem structure fields, exact
  CAS registry SSSOM row, final SSSOM parent row, ingredient type, and hydrate
  audit coverage are populated.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- Minor: update `ontology_mapping.evidence` in
  `data/ingredients/mapped/Gold_Iii_Chloride_Hydrate.yaml` so the
  `anchor_cas_hydrate_records` entry no longer describes the current
  `CLOSE_MATCH` as a `narrowMatch`.
- Minor: add the original CultureBotHT row or supplier/source detail that
  verifies `cas:27988-77-8` as gold(III) chloride hydrate, then rerun the
  hydrate review to clear the `NEEDS_SOURCE` uncertainty for this record.
