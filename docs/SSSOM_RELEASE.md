# Reviewed MIM SSSOM

The standalone release has a decision for every one of the 3,018 MIM mapping
rows: **1,763 supported** and **1,255 withheld**. Use the supported table for
mapping. The withheld table preserves complete source rows for further curation;
it is not an approved mapping set.

```bash
just export-reviewed-sssom
just qc-reviewed-sssom
```

The default output is `output/mim-reviewed-sssom/`:

| File | Purpose |
| --- | --- |
| `ingredient_mappings.sssom.tsv` | Supported mappings with SSSOM metadata |
| `withheld_mappings.sssom.tsv` | Separate, lossless mapping review backlog |
| `mapping-dispositions.tsv` | All 3,018 decisions, reasons, source positions, owners and evidence references |
| `manifest.json` | Counts, distinct mapping-set identifiers and SHA-256 checksums |

These are MIM-only mappings. No KG-Microbe export or KGX installation is needed.
Skip the leading `#` metadata lines when using a generic TSV reader. Use a
SSSOM-aware reader to retain the prefix map and other metadata.

The [review evidence](../reports/sssom_completion_20260921/README.md) binds each
decision to the exact row, source YAML and archived scientific review. The
assembler checks the completed review against its frozen source boundary; it
does not assign scientific approval to new or changed records. The exporter
checks all evidence hashes and independently reproduces both partitions. CI
also runs SSSOM JSON Schema, prefix-map and CURIE validation.

The review corrects 46 activity phrases that had been published as ingredient
synonyms, retaining them as rejected provenance. It separates mapping evidence
from unrelated role/component findings and withdraws earlier approvals that
overstated source scope. All supported rows in this snapshot are `skos:exactMatch`;
other relations remain in the backlog pending an explicit review of their
meaning and aliases. A withheld decision can reflect missing evidence rather
than a false assertion.

Review is agent-assisted and includes adversarial review; structural validation
alone is not scientific approval. Source confidence and earlier validation
annotations are preserved, including the open confidence-provenance question
[#662](https://github.com/CultureBotAI/MediaIngredientMech/issues/662). They are
not newly calibrated probabilities. This release does not approve ingredient
roles, components or downstream media regeneration.
