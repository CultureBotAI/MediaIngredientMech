# Reviewed MICRO admission evidence

The normalizer has two distinct evidence routes. Canonical OLS terms belong in
`curie.MICRO_VERIFIED` only after exact canonical-IRI, defining-ontology and
nonobsolete checks. Legacy `MicrO.owl/MICRO_` terms use `micro_source.load_source`,
which checks the packaged table hashes, row counts, original IRI, label, status
and complete immediate-parent list. A context node alone admits nothing.

Issue #1477 adds the following identifier evidence for current ingredient
records. This is not a new ingredient mapping, source binding, composition,
quantity, role or release approval. In particular, the Soy Peptone source hold
and all other source/formulation limits remain unchanged.

| Identifier | Exact source label | Admission route | Native source parent |
| --- | --- | --- | --- |
| MICRO:0000181 | soy peptone | canonical OLS | — |
| MICRO:0001736 | DSMZ Medium 29 | canonical OLS | — |
| MICRO:0001795 | Phytone peptone | canonical OLS | — |
| MICRO:0002115 | defibrinated blood | legacy IRI | MICRO:0001233 |
| MICRO:0002390 | Oxoid Blood Agar Base No. 2 | legacy IRI | MICRO:0000067 |
| MICRO:0002399 | water-lysed sheep blood | legacy IRI | MICRO:0002401 |

`ols-1477-*.json` are complete, byte-preserved responses from the original
November 2026 captures, not fresh queries. Their original capture paths, URLs,
hashes and route distinctions are in `admission-1477.json`. The three legacy
responses have `is_defining_ontology=false`; none is added to the canonical set.
Ontology descriptions and restrictions are retained as evidence, not adopted
as ingredient facts. For example, the Phytone ontology description is not
authority to replace the separately reviewed supplied-material description.

The added legacy rows were generated offline from the pinned MicrO OWL and its
20 local import modules using KG-Microbe's existing MIREOT extractor and ROBOT.
`native-micro-1477.json` is the exact resulting OBO Graph JSON. It retains the
original class and parent IRIs; the parent edges are actual `is_a` axioms, not
inferences from labels. `admission-1477.json` records the source commit, raw OWL,
import and generator hashes, actual extraction times and native output hashes.
This finite extraction does not publish or rebuild KG-Microbe.

The original September 2026 package is preserved as an unchanged byte prefix
of each table and recorded in `manifest.json`'s `base_snapshot` and the admission
provenance. Four missing native nodes and four native edges were appended, giving
94 nodes and 93 edges. Six class/parent rows were appended to `legacy_nodes.tsv`,
giving 12 rows. For these new original-IRI rows, metadata comes from the native
TSV and the ID spelling from the native graph. Empty extra edge columns are
padding to the existing table schema, not invented provenance. Every overlapping
native row matched the existing row before packaging.

The original three admissions and their evidence remain unchanged:

| Identifier | Source label | Source parent |
| --- | --- | --- |
| MICRO:0002393 | Proteose Peptone No. 2 | MICRO:0000180 |
| MICRO:0002392 | rabbit serum | MICRO:0001236 |
| MICRO:0002250 | V-8 juice | MICRO:0000167 |

Their original six archived rows preserve the complete cells from the archived
full ontology node table. Its full-file hash and row count remain in the base
manifest. The archived edge table lacked edges for those three classes; their
parent evidence remains the original current KGX table. No source description
or CAS identifier is inferred from a parent or similar material.

Only the six explicit `reviewed_terms` enter the legacy route. Newly packaged
parents such as `MICRO:0002401` remain unadmitted context. These JSON/TSV files
use the existing package-data rules so offline verification works in a wheel.
Integration into a native campaign requires a reviewed code/proof successor:
changing `curie.py` and these packaged inputs is not proof-neutral, and does not
clear any historical or current scientific/publication hold.
