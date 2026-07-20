# MIM CURIE standard

What an external repository should cite when it wants to refer to a MIM
ingredient, and what MIM guarantees about it. Written in response to issue #119,
where CommunityMech needed a stable join key and there wasn't a documented one.

Implementation: `src/mediaingredientmech/curie.py` (`CurieNormalizer`).
Run it: `just curie-check MIM:Tryptone` or `just curie-validate`.

---

## The short version

| You want to… | Cite | Stability |
|---|---|---|
| refer to a MIM **record** | `MIM:<name>` | **not rename-stable** — resolve through the alias map |
| assert **equivalence** to an ontology term | the `skos:exactMatch` object | as stable as the ontology |
| refer to something MIM only **close/narrow** matches | `MIM:<name>` only | — |

**Do not** persist `MIM:<name>` as a bare foreign key without also resolving it
through `mappings/mim_curie_aliases.tsv` on read.

## 1. `MIM:<name>` is identity, not a stable key

The SSSOM subject is derived from the ingredient YAML's filename stem
(`build_mim_ingredient_sssom._mim_curie`), with non-URL-safe characters escaped
`~HEX`. Filenames move: `git log --diff-filter=R -- data/ingredients/` shows
**205 renames**, of which **113** changed a CURIE and are published as aliases.

Two routine operations rename a record:

- **unmapped → mapped promotion**: `unmapped/NH42CO3.yaml` →
  `mapped/Nh42co3.yaml`, so `MIM:NH42CO3` → `MIM:Nh42co3`.
- **normalisation of the display name**, including case-only edits:
  `1-Naphtylacetic_Acid` → `1-naphtylacetic_Acid`.

Neither is a data error — they are curation working as intended — so the rename
rate will not go to zero.

**The contract:** MIM publishes `mappings/mim_curie_aliases.tsv`
(`old_curie → current_curie`, with the dates and chain length). Aliases are
transitively folded, so `A→B→C` publishes both `A→C` and `B→C`; a consumer never
needs more than one hop. An alias is withheld if its target no longer exists or
if the old name has since been reused, so a published alias never misdirects.

Regenerate with `just curie-aliases` after any rename.

## 2. Prefix registry

Recognised prefixes, in the exact case MIM emits:

`MIM`, `CHEBI`, `FOODON`, `UBERON`, `ENVO`, `NCIT`, `MICRO`, `BTO`, `GO`,
`NCBITaxon`, `mesh`, `cas`, `kgmicrobe.compound`, `kgmicrobe.ingredient`,
`mediadive.{ingredient,medium,solution}`, `CultureMech`, `CommunityMech`,
`TraitMech`.

Anything else is `UNKNOWN_PREFIX` and is **rejected, not ignored** — that is what
turns a typo (`CHBEI:`) into an error instead of a silent skip. Prefix case is
normalised on the way in, so `chebi:15377` resolves to `CHEBI:15377`.

## 3. Two identifier hazards the normalizer checks

**Foreign identifiers wearing an OBO prefix.** PubChem CIDs have appeared as
`CHEBI:` ids — `CHEBI:10716816` was asserted for "Nicotinate". The normalizer
rejects accessions above a per-ontology ceiling.

This check is **weak and deliberately loose**: real CHEBI accessions reach at
least **747,127** (`gepotidacin`), and several of the PubChem CIDs found in this
codebase (`503742`, `867561`, `501520`) are 6-digit values sitting *inside* the
real CHEBI range. A ceiling catches only the egregious cases. **It is not a
substitute for checking that the id resolves**, and must never be the sole reason
to reject an id an ontology can confirm.

**MicrO's malformed IRIs.** ~1,472 of MicrO's 3,450 classes are minted under
`…/obo/MicrO.owl/MICRO_nnnnnnn` rather than `…/obo/MICRO_nnnnnnn`. OLS4 reports
`is_defining_ontology: false` for those and the CURIE does not round-trip. This is
invisible offline, so `curie.py` carries an allowlist verified against OLS4;
anything outside it is refused. Regenerate with
`python scripts/verify_micro_ids.py`.

Note that **term-level PURLs 404 for all of MicrO**, well-formed or not (control
PURLs for CHEBI/FOODON/UBERON return 200). Do not use PURL status to triage this —
use `is_defining_ontology` and the IRI shape.

> Three MICRO ids currently in the published SSSOM are in the malformed class and
> need re-grounding: `MICRO:0002250` "V-8 juice", `MICRO:0002392` "rabbit serum",
> `MICRO:0002393` "Proteose Peptone No. 2".

## 4. Which ontology term does a MIM ingredient mean?

A selection rule, not a lookup. **180 of 1,876 subjects carry more than one
mapping** (up to 3), e.g.:

```
MIM:14-B-D-Galactobiose -> CHEBI:36226 | cas:2152-98-9 | kgmicrobe.compound:14-b-d-galactobiose
```

`CurieNormalizer.equivalent_term()` applies:

1. **Filter to `skos:exactMatch`.** Only that predicate asserts the two denote the
   same thing. `closeMatch` and `narrowMatch` are excluded — `narrowMatch` means
   the MIM subject is *more specific*, so citing the object as an equivalent
   silently generalises the ingredient. Of 2,200 published rows, 1,720 are
   `exactMatch` and **480 are not**.
2. **Rank the survivors by prefix**: ontology terms (CHEBI < FOODON < UBERON <
   ENVO < MICRO < BTO < NCIT < GO) before registry ids (`mesh`, `cas`) before
   local placeholders (`kgmicrobe.*`).

The rule never reaches past the `exactMatch` set to grab a better-ranked prefix
that is only a close match. When a subject has no exact match, the call returns
`NO_EXACT_MATCH` — a refusal, not a guess — so a caller cannot mistake a
`narrowMatch` for an equivalence.

## 5. For consumers

```python
from mediaingredientmech.curie import CurieNormalizer

n = CurieNormalizer()

v = n.resolve("MIM:1-Naphtylacetic_Acid")
# v.curie == "MIM:1-naphtylacetic_Acid"; v.note records the rename

e = n.equivalent_term("MIM:Tryptone")
# e.curie == "MICRO:0000182"

bad = n.normalize("CHBEI:15377")
# not bad  -> bad.problem == "UNKNOWN_PREFIX"
```

Every call returns a `Verdict`, falsy on failure with a `problem` code
(`UNKNOWN_PREFIX`, `MALFORMED`, `ACCESSION_OUT_OF_RANGE`, `MICRO_UNVERIFIED`,
`UNKNOWN_SUBJECT`, `NO_MAPPING`, `NO_EXACT_MATCH`) and a human-readable `note`.

**Recommended pattern for a repo like CommunityMech:** store the `exactMatch`
ontology term as the join key, and keep `MIM:<name>` alongside as provenance,
resolved through the alias map on read. That gives you a key MIM does not churn
and a pointer back to the curated record.

## 6. What this standard does not yet give you

There is **no immutable surrogate id**. `MIM:<name>` plus the alias map is
resolvable but not immutable, and the record's own `identifier:` field is a poor
substitute — 182 of 1,878 mapped records have `identifier != ontology_id`, and
identifiers are themselves corrected (one carried `CHEBI:867561`, a PubChem CID).

If a consumer needs a genuinely immutable key, that is a mint-and-backfill change
across 2,258 records and should be its own issue.
