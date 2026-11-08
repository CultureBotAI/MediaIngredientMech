# Independent sodium nicotinate exact-term check

Reviewer `/root/inorganics` independently checked the organic author's new sodium nicotinate proposal, CAS54-86-4. The reviewed payload SHA256 is `06447906860830a09cd5b77b4f3366e1533edcfb1041cc8f9f3332ce7c3e8f1d`. No author files or maintained data were edited.

The available read-only local ChEBI255 and NCIt26.02d databases returned no exact CAS54-86-4 statement and no sodium nicotinate / nicotinic acid sodium salt / sodium pyridine-carboxylate name candidate. The broad substring search returned three ChEBI false positives: CAS107254-86-4 contains the requested digits, one large oligonucleotide InChI contains the same digit substring, and a cephalosporin sodium synonym contains a nicotinamido fragment. None denotes sodium nicotinate. Full returned term statements are retained in `lookup.json` so this exclusion can be checked.

Database metadata and full-file hashes:

| Store | Reported ontology release | SHA256 |
|---|---|---|
| chebi.db | ChEBI255 | `26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f` |
| ncit.db | NCIt26.02d; versionIRI release2026-03-19 | `9aac307a33fcf57fb946944a0eaca6029a7d929e29f7522537909da6c71a31d3` |

These are the currently available local stores, not asserted campaign-pinned or current online releases. SQL, parameters, full rows, sizes and nanosecond mtimes are captured. The bounded negative result does not establish absence in every ontology or later release.

An ignored-inclusive scan read all2956 maintained ingredient YAML files under `data/ingredients`, matching the CAS and sodium/nicotinate/pyridine-carboxylate variants across complete text. It returned no owner candidate. This does not inspect other workers' proposed owners.

This check finds no local exact-term or maintained-owner blocker to the author's CAS fallback proposal. It supports preserving the sodium salt as distinct from CHEBI:15940 nicotinic acid and retaining an asymmetric parent relation. It does not approve the entire proposal, its source quantities, roles, SSSOM rows or publication. The author's current-online-release refresh caveat remains accurate; it is no longer a substitute for the local lookup, which has now been completed independently.
