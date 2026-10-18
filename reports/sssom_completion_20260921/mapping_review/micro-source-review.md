# Three MICRO identities restored from KG-Microbe source (#759)

Reviewed 2026-09-23 against the packaged KGX snapshot and original-IRI extract
in `src/mediaingredientmech/ontology_sources/micro/`. This is agent-assisted
mapping curation, not human sign-off or approval of ingredient roles.

| MIM record | Exact MICRO target | Source parent | Recipe memberships |
| --- | --- | --- | ---: |
| Proteose_Peptone_No_2 | MICRO:0002393, Proteose Peptone No. 2 | MICRO:0000180, proteose peptone | 7 |
| Rabbit_Serum | MICRO:0002392, rabbit serum | MICRO:0001236 | 21 |
| V-8_Juice | MICRO:0002250, V-8 juice | MICRO:0000167 | 3 |

For each record, the preferred name denotes the exact named source material;
differences in case do not alter its scope. Both node snapshots retain the exact
class label, and the current KGX has the named parent relationship. These are
material classes, with no assertion of a particular lot's composition. The
source supplies no description or CAS xref for these three terms.

The original `MicrO.owl/MICRO_...` IRIs explain the failed canonical-IRI lookup
that led to #137. This review retains those IRIs explicitly and restores the
same MICRO CURIE convention used by KG-Microbe. It does not claim successful
canonical-PURL round-tripping or OLS defining-ontology status.

Proteose's single exported synonym includes a catalog qualifier. The original
[DSMZ medium 403 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium403.pdf),
page 1, Solution A, inspected 2026-09-23, names
“Proteose peptone No 2 (DIFCO 0121-01-3)”. This is the same complete token already
held as a CATALOG_VARIANT by MIM; the number is a catalog reference, not a CAS RN.
The [MediaDive rendition](https://mediadive.dsmz.de/medium/403) associates the same
catalog qualifier with Proteose peptone no. 2. This supports that specific
source alias, not substitution of generic peptone or another numbered variant.
Rabbit serum and V-8 juice have no additional exported synonym tokens.

The three broad parent rows become exact MICRO rows, and their three local
identity rows are removed. The receipt preserves complete before/after claims;
the separate follow-up decisions bind the complete new rows, owner hashes and
source files. The 31 recipe memberships move by identifier with counts intact.
Proteose's provisional PROTEIN_SOURCE role stays unapproved.

CAS policy: retain a verified CAS RN in the MIM record and SSSOM `other` as
`CAS:<rn>` on symmetric mappings; a consuming KGX node can carry `cas:<rn>` in
`xref` alongside its MICRO identity. No verified CAS is available for these
three records, so their CAS fields remain empty. A broad parent mapping does
not license copying a material's CAS onto that parent. KG-Microbe #1131 handles
independently verified NCIT CAS annotations without changing node identities.
