Two assay substrate labels in the frozen metatraits and metatraits_gtdb sources carry a chemically significant **bis** prefix that conflicts with the ChEBI structures cross-referenced by BacDive. The source wording and the linked identifier cannot both be accepted as exact identity without resolving the original assay reagent.

Primary/source evidence: [BacDive strain 23795](https://bacdive.dsmz.de/strain/23795), substrate rows for reference 25050, independently retrieved during the worker09 skeptical review. It links:

- `bis-4-nitrophenyl-phenyl phosphonate` to [CHEBI:91050](https://www.ebi.ac.uk/chebi/CHEBI:91050). The ChEBI structure/formula `C12H10NO5P` has one nitrophenyl group and a phosphorus-bound hydrogen, rather than the literal bis ester.
- `bis-4-nitrophenyl-phosphorylcholine` to [CHEBI:55394](https://www.ebi.ac.uk/chebi/CHEBI:55394). The ChEBI structure/formula `C11H18N2O6P`, charge +1, has one nitrophenyl group.

The reviewed MIM owners are `data/ingredients/mapped/Bis-4-nitrophenyl-phenyl_Phosphonate.yaml` and `data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml`. Worker09 retains their source registry identities and raw labels, makes no exact external mapping proposal, and preserves all publication holds. This finding does not determine whether the source label or cross-reference is wrong, and does not select a salt form.

Follow-up requires the original assay protocol/catalogue or reagent structure behind the source records, followed by a source-specific correction with provenance and a fresh complete-payload review before any exact mapping/export approval. Do not normalize away `bis` based on an untyped database cross-reference.

Four independently reviewed frozen cases (one pair per source provider):

- `KG_CASE:7f8fe6714739ec034ab245e5a11d8c9ce1e306d07dedc05a8a25aa8496f65f70` (metatraits).
- `KG_CASE:95ef91bffa349e236f9bd4fdd547f10511cfcaf099d6543017ef35f81ebe4745` (metatraits).
- `KG_CASE:b7505c4a7dd6b233c972555cd74160221aa8f94dd6e1a23805b6760568d2bf96` (metatraits_gtdb).
- `KG_CASE:bf2e24ef1bbddb861e3b91f5dedca3ad46729b3ba7c6fdd963fc7cebaefa6331` (metatraits_gtdb).

Deduplication checked the live all-state issue search and saved all-state MIM issue bodies; no prior issue about these two substrate identity conflicts was found. This is part of the explicitly authorized all-unmatched campaign; no maintained YAML or mapping was changed.
