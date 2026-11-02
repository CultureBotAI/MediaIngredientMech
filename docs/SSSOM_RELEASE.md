# Reviewed MIM SSSOM

The standalone release assigns every current MIM mapping row a supported or
withheld disposition. Use the supported table for mapping. The withheld table
preserves complete source rows for further curation; it is not an approved
mapping set. Counts and source hashes change with reviewed curation batches.

```bash
just export-reviewed-sssom
just qc-reviewed-sssom
python -c 'import json; from pathlib import Path; m = json.loads(Path("output/mim-reviewed-sssom/manifest.json").read_text()); print(json.dumps({"source_sha256": m["source_sha256"], "counts": m["counts"]}, indent=2))'
```

The default output is `output/mim-reviewed-sssom/`:

| File | Purpose |
| --- | --- |
| `ingredient_mappings.sssom.tsv` | Supported mappings with SSSOM metadata |
| `withheld_mappings.sssom.tsv` | Separate, lossless mapping review backlog |
| `mapping-dispositions.tsv` | All source-row decisions, reasons, positions, owners and evidence references |
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

The generated manifest reports content-bound counts for this checkout; a
published September release remains a separate historical snapshot. The scoped
#669/#1003 correction receipt preserves all rows
and withdraws the carnitine registry row's prior approval after its owner
changes. The corrected aliases remain withheld pending complete mapping review.
The approval supersession mechanism and subsequent melezitose and sodium
perchlorate form reviews are now part of the native review chain. Their current
dispositions are determined by the exact row and owner evidence in
`reports/sssom_completion_20260921/mapping_review/form_reviews/`, not by an older
approval transferred to changed bytes.

The review corrects 46 activity phrases that had been published as ingredient
synonyms, retaining them as rejected provenance. It separates mapping evidence
from unrelated role/component findings and withdraws earlier approvals that
overstated source scope. All supported rows in this snapshot are `skos:exactMatch`;
other relations remain in the backlog pending an explicit review of their
meaning and aliases. A withheld decision can reflect missing evidence rather
than a false assertion.

The #875 receipt replaces the Na2HPO4·7H2O parent mapping and local registry
identity with one exact NCIT:C61946 mapping. That row remains withheld pending
mapping-specific review; its unresolved chemistry and BUFFER claims remain open.

The #1004 receipt replaces five carnitine salt rows with one exact NCIT:C216679
row, preserves the duplicate as a rejected tombstone, and removes the wrong
free-carnitine CAS and aliases. The corrected salt mapping remains withheld.
Retargeting NLDM's component reference changes its owner bytes, so its mapping
and all 68 component/role approvals also withdraw. Its original validation stamp
remains historical provenance; it does not approve the changed owner.

The #1005 receipt preserves a distinct local identity for sn-glycerol 3-phosphate
lithium salt and its broad CHEBI:15978 parent mapping. It removes the free-acid
CAS exact identity and the generic glycerol-phosphate alias, while preserving
the original #390 explanation, validation stamps and source tokens. The
supplier's free-acid CAS remains procurement metadata and a local registry
display token; it does not establish salt stoichiometry or structure. Both
surviving mappings stay withheld, and the provisional CARBON_SOURCE claim and
historical mixed/role findings remain open.

Review is agent-assisted and includes adversarial review; structural validation
alone is not scientific approval. Source confidence and earlier validation
annotations are preserved, including the open confidence-provenance question
[#662](https://github.com/CultureBotAI/MediaIngredientMech/issues/662). They are
not newly calibrated probabilities. This release does not approve ingredient
roles, components or downstream media regeneration.
