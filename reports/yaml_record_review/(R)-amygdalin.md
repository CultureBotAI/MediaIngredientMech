# `data/ingredients/mapped/(R)-amygdalin.yaml`

## Verdict

Pass with minor issues. The record maps the microbedecoder `(R)-amygdalin`
source label to the active, structure-bearing ChEBI term for the same
cyanohydrin stereoisomer, and the per-record, aggregate, SSSOM, and docs
surfaces are synchronized. Remaining concerns are stale triage/report rows,
an optional missing CAS, and a coarse curation-history timestamp that sorts
before the review flag it resolved.

## Identity

- Reviewed record: `data/ingredients/mapped/(R)-amygdalin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17019` with
  `ontology_mapping.ontology_id: CHEBI:17019`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:17019`
  uses ChEBI ID `CHEBI:17019`, ChEBI name `(R)-amygdalin`, ASCII name
  `(R)-amygdalin`, definition
  `An amygdalin in which the stereocentre on the cyanohydrin function has R-configuration.`,
  formula `C20H27NO11`, net charge `0`, average mass `457.432`, the same SMILES
  string, and the same InChI string stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:17019` to `(R)-amygdalin`; aliases include `(R)-Amygdalin`,
  `(R)-Amygdaloside`, `(R)-Laenitrile`, `D-amygdalin`, and
  `D-(-)-mandelonitrile-beta-D-gentiobioside`; metadata did not report an
  `is_obsolete` or `deprecated` flag.
- Source provenance: the microbedecoder import rows carry
  `kgmicrobe.trait:r_amygdalin`, source label `(R)-amygdalin`, source column
  `BacDive_Metabolite_utilization`, and count `2`, matching
  `occurrence_statistics.source_occurrences[0]`.
- Boundary checked: `data/ingredients/mapped/Amygdalin.yaml` is the broader
  parent `CHEBI:27613` `amygdalin`; ChEBI states `(R)-amygdalin` is an
  `amygdalin`, so the two records are related but not duplicate identities.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(R\)-amygdalin.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(R\)-amygdalin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(R\)-amygdalin.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`: exact equality for the `(R)-amygdalin` entry; curation history length is `4` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28R~29-amygdalin skos:exactMatch CHEBI:17019`, with object label
  `(R)-amygdalin` and `validation_method` `OLS:chebi|CONFIRMED|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:17019` identity; the label index marks `(R)-amygdalin` `unique`.

## Evidence

- The ontology mapping evidence is narrow enough for the claim it makes: the
  microbedecoder source label is exactly `(R)-amygdalin`, and ChEBI currently
  resolves that ASCII name to `CHEBI:17019`.
- The chemical properties describe the same ChEBI term: formula, mass, SMILES,
  and InChI all matched the official ChEBI page inspected for `CHEBI:17019`.
- The zero media counts are not evidence of absence from microbedecoder. The
  non-media count is retained under `source_occurrences`, so the BacDive-derived
  prevalence remains traceable without inflating `total_occurrences`.
- Minor: the `REVIEWED_AND_PROMOTED` event has a coarse
  `2026-08-04T00:00:00+00:00` timestamp that sorts before the
  `2026-08-04T03:08:34.142678+00:00` `FLAGGED_FOR_REVIEW` event it resolved.
  The list order still preserves the actual append order.
- `mappings/record_research_validation.tsv` still has stale or now-satisfied
  rows for this record: direct ChEBI verification has now confirmed
  `CHEBI:17019`; `ingredient_type` and `chemical_properties` are no longer
  missing; ChEBI lists CAS `29883-15-6` on the exact term but the record is
  already identifiable without it; and adding generic `amygdalin` as a synonym
  would collide with the deliberate parent `Amygdalin.yaml` record.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:17019 -e "(R)-amygdalin" -e r_amygdalin -e Amygdalin -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM/source rows,
  the `Amygdalin.yaml` parent, and no contradictory curated record for
  `CHEBI:17019`.

## Completeness

- `synonyms: []` is acceptable here because the only upstream source label is
  the preferred term. The generic `amygdalin` name is already maintained as the
  `CHEBI:27613` parent record and should not be silently promoted to an exact
  synonym on this stereospecific child.
- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy, and the BacDive metabolite-utilization
  source column is not itself claim-level evidence for a narrower nutritional
  role.
- `find . -path ./.git -prune -o -iname '*amygdalin*' -print` included ignored
  files and found only `data/ingredients/mapped/(R)-amygdalin.yaml` and the
  broader `data/ingredients/mapped/Amygdalin.yaml` sibling among YAML records.

## Recommended Edits

1. No identity, mapping, occurrence, or chemical-property edit is needed in
   `data/ingredients/mapped/(R)-amygdalin.yaml`.
2. On a future provenance cleanup pass, fix or annotate the coarse
   `REVIEWED_AND_PROMOTED` timestamp so curation history sorts in semantic
   order as well as append order.
3. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `(R)-amygdalin` rows resolved so stale field-missing rows and now-satisfied
   direct-ChEBI checks stop re-queuing this record.
4. On a future evidence-enrichment pass, consider adding CAS `29883-15-6` from
   current ChEBI to `chemical_properties.cas_rn`; this is optional and not a
   mapping blocker.
