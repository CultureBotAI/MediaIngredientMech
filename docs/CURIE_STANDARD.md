# MIM CURIE standard

Use a record's permanent `mim_id`, such as `MIM:0000001`, when referring to a MIM
ingredient. It stays fixed when the label, mapping, filename or storage directory
changes. The existing `identifier` remains a mapping or unresolved-placeholder
value; it is not a unique record key.

Implementation: `src/mediaingredientmech/stable_ids.py` and
`src/mediaingredientmech/curie.py`. See [stable IDs and consumer migration](STABLE_MIM_IDS.md).

| Reference | Meaning and stability |
| --- | --- |
| `MIM:` followed by seven digits | Permanent registered ingredient record ID; never reused |
| Historical `MIM:<filename-stem>` | Preserved alias; resolve against the current corpus and historical alias map |
| Historical placeholder or external identifier | Preserved when present in `legacy_identifiers`; may refer to several records |
| An `skos:exactMatch` object | A separately supported mapping; scientific scope still governs substitution |

## Registry and public URL

The `MIM:` prefix expands to
`https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_`.
For example, `MIM:0000001` expands to
`https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_0000001`.
The Pages build creates a directory-index resolver at that route. It locates the
current record by `mim_id`, and preserves terminal IDs as historical pages.
Retired/merged IDs show replacement links, split IDs list every declared successor
without choosing one, and deprecated IDs have no guessed replacement. Existing
filename-based record pages remain available; filenames are not renamed by the
ID migration.

`data/ids/mim_id_registry.tsv` retains immutable mint rows;
`data/ids/mim_id_lifecycle.tsv` appends terminal retirement/merge/split/deprecation
events using the status-dependent target cell documented in
[stable IDs](STABLE_MIM_IDS.md). Unknown IDs, cycles, duplicate current IDs and
incomplete active-record coverage fail validation. An ID's lifecycle is separate
from the record's mapping status. Single-ID lookup refuses splits/deprecations;
inspect their typed lifecycle context instead of selecting an arbitrary child.

The current generation of a site is established by its Pages build/deployment
checks. Source changes alone do not prove a URL is live. w3id is deferred to a
separately approved change.

## Legacy references and ambiguity

Each current record retains former identifiers in `legacy_identifiers`. The
existing `mappings/mim_curie_aliases.tsv` remains useful for historical filename
renames. `CurieNormalizer.resolve()` follows these references to permanent IDs.
It does not derive current identity from filenames or a preferred ontology term.

An alias shared by several records produces `AMBIGUOUS_ALIAS`; consumers must
provide record-specific evidence instead of choosing the first result. Stable
registered IDs retain their own authority even if a legacy spelling collides.
Do not decode old `~HEX` filename aliases to invent public paths.

```python
from mediaingredientmech.curie import CurieNormalizer

normalizer = CurieNormalizer()
reference = normalizer.resolve("MIM:0000001")
if not reference:
    raise ValueError(reference.problem)
permanent_id = reference.curie

legacy = normalizer.resolve("MIM:Tryptone")
# A known unambiguous alias resolves to a numeric MIM ID; inspect the verdict.

mapping = normalizer.equivalent_term(permanent_id)
# An absent or insufficiently exact mapping remains NO_MAPPING/NO_EXACT_MATCH.
```

The normalizer uses a current local registry and corpus. For another verified
snapshot, pass its root as `repo_root`. It performs no network access.

## Mapping semantics remain separate

`equivalent_term()` filters to `skos:exactMatch` before ranking targets by the
maintained prefix preference. `skos:closeMatch`, `broadMatch` and `narrowMatch`
do not become equivalences because the subject now has a permanent ID. The
selected mapping is not a replacement for MIM record identity.

`normalize()` still checks syntax, recognized prefix spelling and known malformed
identifier hazards. Prefix case is canonicalized, unknown prefixes fail, and
accession ceilings are only a weak typo/foreign-identifier guard. Ontology
existence and scientific identity require separate evidence. For legacy MicrO
IRIs, the maintained reviewed
[source snapshot](../src/mediaingredientmech/ontology_sources/micro/README.md)
continues to determine valid original IRIs.

Verdicts are falsy on failure and retain a `problem` and `note`, including
`UNKNOWN_SUBJECT`, `AMBIGUOUS_ALIAS`, `ALIAS_CYCLE`, `UNKNOWN_PREFIX`,
`MALFORMED`, `ACCESSION_OUT_OF_RANGE`, `MICRO_UNVERIFIED`, `NO_MAPPING` and
`NO_EXACT_MATCH`. Never convert a failed lookup to a guessed ontology identity.
