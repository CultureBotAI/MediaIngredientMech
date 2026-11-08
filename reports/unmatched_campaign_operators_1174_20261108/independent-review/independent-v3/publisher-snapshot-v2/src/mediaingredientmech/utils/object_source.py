"""
The one table mapping a published prefix to its ``object_source``.

``object_source`` is how a consumer knows which ontology or registry to
resolve ``object_id`` against, so a row without one publishes an identifier
with no stated origin.

There were two of these tables (#385). ``reconcile_sssom`` listed eleven
prefixes; ``promote_resolved_unmapped`` listed eight, missing ``cas``,
``kgmicrobe.compound`` and ``kgmicrobe.ingredient`` -- **682 of the 2,999
published rows, 23%**. Both looked the value up with ``.get(prefix, "")``, so
promoting a record to a missing prefix did not raise: it wrote an empty column
and everything downstream kept working (#386). Rule C in
``validate_sssom_invariants`` catches the result after the fact; nothing
stopped it being written.

So there is one table, and :func:`object_source_for` raises rather than
returning a blank. A prefix this project does not publish is a decision
somebody has to make, not a cell to leave empty.
"""

from __future__ import annotations

#: Prefix (as it appears in an ``object_id``) to its ``object_source`` value.
#: Keys are matched case-insensitively, because CURIEs in the corpus are not
#: consistently cased -- ``mesh:`` is lowercase while OBO CURIEs are upper.
OBJECT_SOURCE: dict[str, str] = {
    "CHEBI": "obo:chebi.owl",
    "FOODON": "obo:foodon.owl",
    "ENVO": "obo:envo.owl",
    "UBERON": "obo:uberon.owl",
    "NCIT": "obo:ncit.owl",
    "MICRO": "obo:micro.owl",
    "BTO": "obo:bto.owl",
    "MESH": "registry:mesh",
    "CAS": "registry:cas",
    "kgmicrobe.compound": "kgm:compound",
    "kgmicrobe.ingredient": "kgm:ingredient",
}

_BY_UPPER = {prefix.upper(): source for prefix, source in OBJECT_SOURCE.items()}


class UnknownObjectSource(KeyError):
    """A published prefix has no declared ``object_source``."""


def prefix_of(curie_or_prefix: str) -> str:
    """
    Return the prefix of a CURIE, or the argument when it is already one.

    :param curie_or_prefix: ``"CHEBI:17234"`` or ``"CHEBI"``.
    :return: The prefix, unchanged in case.
    """
    text = (curie_or_prefix or "").strip()
    return text.split(":", 1)[0] if ":" in text else text


def object_source_for(curie_or_prefix: str) -> str:
    """
    Return the ``object_source`` for a CURIE or prefix.

    :param curie_or_prefix: ``"CHEBI:17234"`` or ``"CHEBI"``.
    :return: The declared ``object_source``.
    :raises UnknownObjectSource: When the prefix is not declared. Refusing is
        the point: the alternative is an empty column nobody notices (#386).
    """
    prefix = prefix_of(curie_or_prefix)
    try:
        return _BY_UPPER[prefix.upper()]
    except KeyError:
        raise UnknownObjectSource(
            f"no object_source declared for prefix {prefix!r}. Add it to "
            f"mediaingredientmech.utils.object_source.OBJECT_SOURCE, which is "
            f"the single table every writer reads; publishing a row with an "
            f"empty object_source is not an option (#385, #386)."
        ) from None
