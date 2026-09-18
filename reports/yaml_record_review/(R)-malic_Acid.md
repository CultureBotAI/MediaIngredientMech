# `data/ingredients/mapped/(R)-malic_Acid.yaml`

## Verdict

Pass with minor issues. The record maps the microbedecoder `(R)-malic acid`
source label to the active, structure-bearing ChEBI term for the same neutral
malic-acid stereoisomer, and the per-record, aggregate, SSSOM, and docs
surfaces are synchronized. Remaining concerns are stale triage/report rows, an
optional missing CAS and synonym, and a coarse curation-history timestamp that
sorts before the review flag it resolved.

## Identity

- Reviewed record: `data/ingredients/mapped/(R)-malic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30796` with
  `ontology_mapping.ontology_id: CHEBI:30796`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:30796`
  uses ChEBI ID `CHEBI:30796`, ChEBI name `(R)-malic acid`, formula `C4H6O5`,
  net charge `0`, average mass `134.087`, the same SMILES string, and the same
  InChI string stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:30796` to `(R)-malic acid`; aliases include `(+)-D-malic acid`,
  `(2R)-2-hydroxybutanedioic acid`, `(R)-2-hydroxybutanedioic acid`,
  `2-HYDROXY-SUCCINIC ACID`, `D-Malic acid`, and `D-malic acid`; metadata did
  not report an `is_obsolete` or `deprecated` flag.
- Source provenance: the microbedecoder import rows carry
  `kgmicrobe.trait:r_malic_acid`, source label `(R)-malic acid`, source column
  `BacDive_Metabolite_utilization`, and count `18`, matching
  `occurrence_statistics.source_occurrences[0]`.
- Boundaries checked: `data/ingredients/mapped/L-Malic_Acid.yaml` is the
  `CHEBI:30797` `(S)` enantiomer, `data/ingredients/mapped/Dl-malic_Acid.yaml`
  is the broader `CHEBI:6650` `malic acid` record, and
  `data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml` is a
  CAS-primary salt/hydrate with a parent NCIT mapping. Those are distinct
  neighboring forms, not active duplicates of `CHEBI:30796`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(R\)-malic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(R\)-malic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(R\)-malic_Acid.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `(R)-malic Acid` entry; curation history length is `4`
  in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28R~29-malic_Acid skos:exactMatch CHEBI:30796`, with object label
  `(R)-malic acid` and `validation_method` `OLS:chebi|CONFIRMED|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:30796` identity; the label index marks `(R)-malic Acid` `unique`.

## Evidence

- The ontology mapping evidence is narrow enough for the claim it makes: the
  microbedecoder source label is exactly `(R)-malic acid`, and ChEBI currently
  resolves that name to `CHEBI:30796`.
- The chemical properties describe the same ChEBI term: formula, mass, SMILES,
  and InChI all matched the official ChEBI page inspected for `CHEBI:30796`.
- The zero media counts are not evidence of absence from microbedecoder. The
  non-media count is retained under `source_occurrences`, so the BacDive-derived
  prevalence remains traceable without inflating `total_occurrences`.
- Minor: the `REVIEWED_AND_PROMOTED` event has a coarse
  `2026-08-04T00:00:00+00:00` timestamp that sorts before the
  `2026-08-04T03:08:34.142678+00:00` `FLAGGED_FOR_REVIEW` event it resolved.
  The list order still preserves the actual append order.
- `mappings/record_research_validation.tsv` still has stale or now-satisfied
  rows for this record: direct ChEBI verification has now confirmed
  `CHEBI:30796`, `ingredient_type` and core `chemical_properties` are no longer
  missing, and the remaining proposed CAS and `D-malic acid` exact synonym are
  useful enrichment but not mapping blockers.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:30796 -e "(R)-malic Acid" -e "(R)-malic acid" -e r_malic_acid -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM/source rows
  and no contradictory active curated record for `CHEBI:30796`.

## Completeness

- `synonyms: []` is acceptable for record identity because the only upstream
  source label is the preferred term modulo case. Adding `D-malic acid` from
  ChEBI would be reasonable future enrichment but is not needed for SSSOM
  correctness.
- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy, and the BacDive metabolite-utilization
  source column is not itself claim-level evidence for a narrower nutritional
  role.
- `find . -path ./.git -prune -o -iname '*malic*' -print` included ignored
  files and found only stereoisomeric, broader, and salt/hydrate siblings among
  active YAML records.

## Recommended Edits

1. No identity, mapping, occurrence, or chemical-property edit is needed in
   `data/ingredients/mapped/(R)-malic_Acid.yaml`.
2. On a future provenance cleanup pass, fix or annotate the coarse
   `REVIEWED_AND_PROMOTED` timestamp so curation history sorts in semantic
   order as well as append order.
3. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `(R)-malic_Acid` rows resolved so stale field-missing rows and now-satisfied
   direct-ChEBI checks stop re-queuing this record.
4. On a future evidence-enrichment pass, consider adding CAS `636-61-3` and
   exact synonym `D-malic acid` from current ChEBI. They are optional and not
   mapping blockers.
