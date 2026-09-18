# `data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml`

## Verdict

Needs curation - major. The CHEBI and CAS identity for the pentahydrate
dihydrochloride salt is sound, but the `SELECTIVE_AGENT` role is still a
provisional name-pattern inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:9217` with
  `ontology_mapping.ontology_id: CHEBI:9217`, label
  `spectinomycin hydrochloride hydrate`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 22189-32-8`, formula
  `C14H24N2O7.5H2O.2HCl`, and salt/hydrate InChI and SMILES.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soyton` through `Spermidine_Trihydrochloride`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9217` with label
  `spectinomycin hydrochloride hydrate` and exact synonyms including the
  dihydrochloride pentahydrate IUPAC labels stored in YAML.
- PubChem resolves CAS `22189-32-8` to CID `30971`, with formula
  `C14H36Cl2N2O12` and an InChI that decomposes to
  `C14H24N2O7.2ClH.5H2O`, agreeing with the stored pentahydrate
  dihydrochloride identity.
- `reports/hydrate_grounding.tsv` records this row as `OK_HYDRATE_TERM`, so
  the hydrate-specific grounding is already recognized by the repository's
  hydrate audit.
- The final SSSOM row exact-matches `CHEBI:9217` and its `other` payload is
  limited to the curated CHEBI exact synonyms plus `CAS:22189-32-8`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note. That source does not verify a
  claim-level selective-agent role for this supplied form.

## Completeness

- The identity, hydrate state, CAS, CHEBI synonyms, chemical properties, and
  final SSSOM row agree.
- No unsupported active synonym, component, or final SSSOM payload was found;
  the remaining unsupported claim is the provisional selective-agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Spectinomycin_Dihydrochloride_Pentahydrate.yaml`, or
  replace the name-pattern evidence with a source that explicitly uses
  spectinomycin dihydrochloride pentahydrate as a selective agent in a culture
  context.
