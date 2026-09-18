# `data/ingredients/mapped/Resazurin.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Resazurin` is exactly grounded to defining `CHEBI:8806` /
`Resazurin`. Fresh OLS4 lookup resolved the ChEBI CURIE, and PubChem lookup by
the stored CAS `550-82-3` resolved CID 11077 with the same formula and InChI as
the YAML.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Reducing_Agent.yaml data/ingredients/mapped/Resazurin.yaml
data/ingredients/mapped/Resistomycin.yaml data/ingredients/mapped/Resveratrol.yaml
data/ingredients/mapped/Rhamnogalacturonan_From_Soy_Bean_Pectic_Fibre.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for this CHEBI
record.

**Evidence**: The exact ChEBI identity, CAS, chemical structure, refreshed
3671-occurrence count, and CultureMech redox-indicator role pass. The raw
`Role: pH dependent redox indicator` synonyms are also filtered from the final
SSSOM.

The published `other` payload in final SSSOM row 2494 is over-broad. `Sodium
resazurin` and `resazurin sodium salt` name the sodium salt while this record is
grounded to neutral resazurin, and the seven CultureMech alias-backfill strings
such as `Resazurin (0.1%)` and `Resazurin (1 mg/L)` are concentration-qualified
recipe labels, not true alternate names for `CHEBI:8806`. The auto-proposed
PubMed evidence is also too broad for `ontology_mapping.evidence`: it mentions
resazurin as an assay reagent, not this media-ingredient grounding.

**Completeness**: The exact chemical identity is complete enough, and the role
has CultureMech database evidence. The unsafe data is confined to synonyms and
the irrelevant PubMed mapping-evidence row.

**Recommended Edits**: Remove the concentration-qualified CultureMech labels
from active exported synonyms, split or quarantine the sodium-salt labels so
they are not exported on the neutral ChEBI record, and drop or rewrite the
auto-proposed PubMed mapping evidence. Regenerate final SSSOM and confirm row
2494 no longer exports salt or concentration strings in `other`.
