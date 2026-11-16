# Historical owner assertions and current safeguards (#1447)

The original ten regression cases retain every assertion and parameter. They
now explicitly receive their dated data context instead of mixing that context
with later source-supported owner changes. All other cases retain their existing
inputs. New current-owner safeguards run against the actual current permanent-ID
corpus, independently of the historical fixture.

`context.json.gz` contains fifteen complete files from Git commit
`0dac278466699129a083343a921c2e0ca18a9ab4`. `source.json` declares the exact Git tree,
paths, modes, blob IDs, SHA256 values and lengths (18,517,173 logical bytes).
The helper pins both containers and checks every member independently. The
archive consists of the mapped collection, canonical SSSOM, membership table,
original unmapped trihydrate, all eight owner files visited by the historical
NCIT loop, and that loop/BSA case's three complete source-evidence objects.
No current record fills a historical gap. No archived executable is imported.

Reproduction: use `git show REVISION:PATH` for each declared path, verify its
Git blob/mode and SHA256/length, encode complete bytes as base64 alongside the
original metadata, then encode the schema version 1/revision/tree/files document
with sorted keys, compact JSON and one newline and gzip with mtime 0. Metadata
and complete bytes are preserved; historical ID or review hashes are never
restamped. The fixture is data for tests, not a current review input or approval.

Fixture arguments are explicit. Module-scoped current aggregate fixtures are
not overwritten: the selected test receives a separate historical value. Only
the Mg six-water parameter uses the historical aggregate in its four-case test;
the other three receive the unchanged cached current value. Only the selected
NCIT/BSA/trihydrate cases temporarily rebind their own module ROOT/EVIDENCE;
all fifteen historical files are materialized into a fresh pytest-owned root
and checked again at teardown. Globals restore on success or failure. The
current stable-ID lookup helper, production validators and current source tree
are never redirected.

## Scientific scope

These references explain the explicit current expectations. They do not certify
all fields on the owners or release source, role, quantity, component or export
holds. Primary bodies and independent source reviews were retained and read
before this test-only change; no acquisition runs during tests.

- JCM 680 names L-cysteine hydrochloride monohydrate **solution**; CHEBI:91248
  names its solute. #901 and MAPPING_SEMANTICS support an asymmetric form-of
  parent, not exact identity or subclass. The original QSY9 output assertion
  records a historical defect only; its current counterpart rejects that alias.
  The receiving 10 mL does not specify stock concentration, solvent or pH.
- Sigma 342432 names chromium(III) sulfate variable hydrate, CAS 15244-38-9;
  Wako W01W0109-0283 names ferric sulfate n-hydrate, CAS 15244-10-7. Anhydrous-basis
  masses and fixed structural widgets are not hydrate chemistry. The ferric
  monohydrate exclusion and #873 competing owner remain; #1245 separately
  governs exact source-routing/rejection-ledger coupling.
- The retained American Elements magnesium sulfate hexahydrate datasheet
  explicitly supports six waters and CAS 17830-18-1. Its questionable melting
  point is not imported. This is not an exclusive global CAS claim, anhydrous
  identity, monohydrate routing change or source 679 annotation approval.
- The retained CultureBotHT `Mixes.csv` Wolfe block says `Lipoic acid`, 5 mg/L;
  the separately sourced ATCC component says `Thioctic acid`, 5.0 mg/L. Each keeps
  generic CHEBI:16494, without R/S/racemate or lipoate inference. #1237 preserves
  the calcium-pantothenate D/DL and stock/final-volume/source limits. X100 does
  not authorize rescaling or stock merger.
- #1386's Acriflavine correction changes mapping-method provenance only. FDA
  GSRS 1T3A50395T is a mixture and distinguishes PRIMARY 65589-70-0 from its own
  SUPERSEDED 8048-52-0. This is not global CAS withdrawal. NCIT:C76253 and exact
  own-identifier semantics survive. Preserving old formula/SMILES/InChI bytes
  is deliberately not approval of those separately held mixture properties.
- DSMZ 661 explicitly states trisodium citrate with three waters. #882/#1021
  history and legacy 0852 survive on permanent MIM:0002928; retired 0820 cannot
  be reused. The local source-stated hydrate is not measured crystallography,
  a new CAS identity or an exact anhydrous/dihydrate match. Other source/owner
  conflicts remain unresolved.
- BSA's A7030/A9647/A7409 observations stay source-specific. `catalog_number`
  is optional; explicitly unknown manufacturer/catalog information stays
  absent. Additional separately evidenced forms do not authorize product
  equality. #1222 JCM 220 quantity and held-companion restrictions survive.

## Remaining gates

Historical 3/41 memberships and historical 17 BSA memberships are finite dated
assertions, not permanent scientific quotas. Current complete source ownership,
membership, canonical rows, companion, stable publication and #1325 current
route gates still require their actual reviewed products under #1431. No test is
skipped or weakened to make those products current. The existing currency tests
remain unchanged and can still fail while campaign products are unfinished.
This change does not resolve the separate 315 occurrence-statistics provenance
plan, assign counts or perform automatic zero backfill.

The #467 partonomy archive and its three-case selector are unchanged. This
helper has separate explicit fixtures and does not expand that selector or mix
its September corpus into the owner regressions. Focused integration checks
include the existing partonomy controls because both fixture sets are registered
in conftest. Scientific/source policies, existing pins, schema, workflows,
production code, record data and all prior failure evidence remain unchanged.
