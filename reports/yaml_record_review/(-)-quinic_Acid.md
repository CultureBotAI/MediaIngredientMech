# `data/ingredients/mapped/(-)-quinic_Acid.yaml`

## Verdict

Pass with a minor queue/reporting issue. The record maps the microbedecoder
`(-)-quinic acid` source label to the active ChEBI term for the same
stereospecific free acid, and the per-record, aggregate, SSSOM, and docs
surfaces are synchronized. The remaining findings are stale or optional rows in
`mappings/record_research_validation.tsv`, not blockers in the YAML.

## Identity

- Reviewed record: `data/ingredients/mapped/(-)-quinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17521` with
  `ontology_mapping.ontology_id: CHEBI:17521`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:17521`
  uses ChEBI ID `CHEBI:17521`, ChEBI name `(-)-quinic acid`, ASCII name
  `(-)-quinic acid`, definition `The (-)-enantiomer of quinic acid.`, formula
  `C7H12O6`, net charge `0`, average mass `192.167`, monoisotopic mass
  `192.06339`, the same SMILES string, and the same InChI string stored in
  `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:17521` to `(-)-quinic acid`; aliases include `(-)-Quinic acid`,
  `Quinic acid`, and the systematic
  `(1S,3R,4S,5R)-1,3,4,5-tetrahydroxycyclohexanecarboxylic acid`; metadata did
  not report an `is_obsolete` or `deprecated` flag.
- Source provenance: the microbedecoder import rows carry
  `kgmicrobe.trait:quinic_acid`, source label `(-)-quinic acid`, source column
  `BacDive_Metabolite_utilization`, and count `27`, matching
  `occurrence_statistics.source_occurrences[0]`.
- Boundary checked: `data/ingredients/mapped/Quinic_Acid.yaml` is the broader
  parent `CHEBI:26493` `quinic acid`; ChEBI states `CHEBI:17521` is a
  `CHEBI:26493`, so the two records are related but not duplicate identities.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/\(-\)-quinic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`: passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/\(-\)-quinic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`: passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/\(-\)-quinic_Acid.yaml`: passed; 1 file scanned, 0 ERROR rows.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`: exact equality for the `(-)-quinic Acid` entry; curation history length is `5` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:~28-~29-quinic_Acid skos:exactMatch CHEBI:17521`, with object label
  `(-)-quinic acid` and `validation_method` `OLS:chebi|CONFIRMED|2026-09-02`.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` carry the
  same `CHEBI:17521` identity; the label index marks the preferred label
  `unique`.

## Evidence

- The ontology mapping evidence is narrow enough for the claim it makes: the
  microbedecoder source label is `(-)-quinic acid`, and ChEBI currently resolves
  that ASCII name to the exact stereochemical free-acid record.
- The chemical properties are coherent with ChEBI `CHEBI:17521`: formula,
  average mass, SMILES, and InChI all matched the official ChEBI page inspected
  for that term.
- The record has `total_occurrences: 6` and `media_count: 6` from CultureMech
  occurrence refresh #337, while the non-media BacDive count is separately
  retained under `source_occurrences`.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:17521 -e "(-)-quinic Acid" -e "(-)-quinic acid" -e quinic_acid -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM/source rows,
  the broader sibling record noted above, and no contradictory curated record
  for `CHEBI:17521`.
- `mappings/record_research_validation.tsv` still has rows for this record that
  are stale or now directly resolved:
  - `P1 CURIE_REFUTED` and `P2 QUALITY_CONFLICT` both reduce to direct
    confirmation that `CHEBI:17521` is active and denotes neutral
    `(1S,3R,4S,5R)` quinic acid; the current ChEBI page and local OAK check
    satisfy that bound.
  - `P3 FIELD_MISSING` rows for `ingredient_type` and `chemical_properties` are
    stale because both fields are now present.
  - `P3 CAS_AVAILABLE` and synonym rows describe optional additions. Current
    ChEBI does list CAS `77-95-2` on the exact term, but the record is already
    identifiable without it.

## Completeness

- `synonyms: []` is acceptable for this source-backed record. The raw
  microbedecoder label differs from `preferred_term` only by the capitalization
  of `acid`, and ChEBI already carries the exact lowercase label.
- Empty component and role slots are acceptable: this is a single ChEBI
  molecule with no mixture partonomy, and the BacDive metabolite-utilization
  source column is not itself evidence for a narrower nutritional role.
- `find . -path ./.git -prune -o -iname '*quinic*' -print` included ignored
  files and found only `data/ingredients/mapped/(-)-quinic_Acid.yaml` and the
  broader `data/ingredients/mapped/Quinic_Acid.yaml` sibling; there is no local
  quinic-named research report alongside the live record.

## Recommended Edits

1. No edit is needed in `data/ingredients/mapped/(-)-quinic_Acid.yaml`.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the
   `(-)-quinic_Acid` rows resolved so stale field-missing rows and now-satisfied
   direct-ChEBI checks stop re-queuing this record.
3. On a future evidence-enrichment pass, consider adding CAS `77-95-2` from
   current ChEBI to `chemical_properties.cas_rn`; this is optional and not a
   mapping blocker.
