# Ingredient bundle review — 2026-09-24

This opt-in cohort implements MIM #769 and #770 after the scope profile in #768.
It applies explicit scope rulings to the 20 previously supported KG-Microbe case
identities. It exports 18 source-qualified identifier claims (15 eligible xrefs,
two retained historical/original Acriflavine claims and one rejected raw Lysozyme
claim), three BSA supplier products, and ten source occurrences.

`scope-rulings.json` records the case-specific application of the profile. These
decisions use the archived ingredient and ontology reviews; they are not inferred
from namespace preference or CAS syntax. No existing identity decision changes.
Composition remains unknown for generic BSA, unresolved Lysozyme/Sorbitan and the
rifamycin family; unknown composition does not supply missing entity scope.

`claims.json` contains the complete reviewed payloads. `review.json` binds their
bytes, selected original owner records, scientific evidence and the existing
mapping review. `review-evidence.json` contains matching complete-claim decisions
and owner hashes in the existing reviewed-SSSOM evidence format. The source row,
predicate, original fields, owning record and base disposition must still agree
before any mapping receives scope extensions. A receipt or refreshed checksum
alone supplies no approval.

The occurrence cohort preserves all seven BSA recipes, the original CultureBotHT
A7030 occurrence and two Sorbitan recipe occurrences. The explicit one-of group
in CultureMech:015191 preserves A9647 or A7409. No A7409 CAS or concentration is
invented. The original recipe payload, including its reported 350 g/L component,
remains evidence about that occurrence, not a universal product attribute.

The two Acriflavine historical/original claims retain different source meanings:
FDA says SUPERSEDED; the archived CultureBotHT row reports that number without a
currentness ruling. Both are kept outside active xrefs. Lysozyme's invalid raw RN
is retained without a normalized replacement. These representations do not reopen
the unresolved preparation evidence tracked by #753 and #761.

Review round 1 passed 134 focused checks including existing review/profile tests.
Round 2 reproduced seven additional failures in stable claim-ID binding, activation
through withheld products, and whitespace-hidden historical statuses (#774). The
fixes passed 142 focused checks and require matching IDs, supported product endpoints for active facts, and
normalized status recognition while preserving original source text. Inactive
history remains valid. Synthetic review mutations in tests are deliberately
confined to fixtures and are not scientific approvals for production data.

See [the bundle contract](../../docs/INGREDIENT_BUNDLE.md) for reproduction,
capabilities, immutable release pins, owner-bound validation and representation
rules. CI exports this cohort as a consumer-acceptance candidate; this does not
change KG-Microbe production source pins or satisfy its independent release gate.
