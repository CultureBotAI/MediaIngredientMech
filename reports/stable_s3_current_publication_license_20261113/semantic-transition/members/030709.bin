"""Standard helper for appending CurationEvent entries to an ingredient record.

Every script that mutates an IngredientRecord YAML should call
``record_curation_event`` to leave an audit trail. Centralizing here means:

* timestamps are ISO-8601 with UTC tz, consistently;
* the ``curation_history`` slot is created on demand;
* re-runs of idempotent migration scripts can short-circuit when the most
  recent event already matches (``skip_if_recent`` flag);
* the schema's ``CurationEvent`` field names (timestamp / curator / action /
  changes / previous_status / new_status / llm_assisted / llm_model)
  are honored, so future schema diffs only need to touch one file.

Drop-in usage::

    from mediaingredientmech.curate.curation_event import record_curation_event

    record_curation_event(
        record,
        curator="enrich_from_ols.py",
        action="ENRICHED_OLS_LABELS",
        changes="Filled preferred_label from OLS",
    )

Ported from CultureMech's ``src/culturemech/curate/curation_event.py``.
Field signature differs from CultureMech's because the MIM
``CurationEvent`` class doesn't define ``source`` or ``notes`` — pass
narrative detail in ``changes`` instead.
"""

from __future__ import annotations

import datetime
from typing import Any

__all__ = ["record_curation_event", "now_iso"]


def now_iso() -> str:
    """Current UTC timestamp as an ISO-8601 string."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def record_curation_event(
    record: dict[str, Any],
    *,
    curator: str,
    action: str,
    changes: str | None = None,
    previous_status: str | None = None,
    new_status: str | None = None,
    llm_assisted: bool = False,
    llm_model: str | None = None,
    timestamp: str | None = None,
    skip_if_recent: bool = False,
) -> dict[str, Any]:
    """Append a CurationEvent to ``record['curation_history']``.

    Args:
        record: The ingredient record dict being mutated. Mutated in place.
        curator: Script / human identifier (e.g. ``"migrate_legacy_fields.py"``
            or ``"jane.smith"``). Required because the schema requires it.
        action: SCREAMING_SNAKE_CASE action label (e.g.
            ``"ENRICHED_CHEBI"``, ``"MERGED_DUPLICATES"``). Required; must
            match the schema's pattern ``^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$``.
        changes: Optional human-readable description of what changed
            (e.g. ``"Set mapping_status to MAPPED (was UNMAPPED)"``).
            Maps to ``CurationEvent.changes`` — also the right field to use
            for narrative notes since the schema has no separate ``notes``.
        previous_status: Optional ``MappingStatusEnum`` value held before
            this action.
        new_status: Optional ``MappingStatusEnum`` value held after this
            action.
        llm_assisted: True when an LLM produced this change. When True the
            field is emitted; when False the field is omitted so downstream
            consumers can distinguish "explicitly not LLM" from "older
            event written before this field existed".
        llm_model: LLM model identifier (e.g. ``"claude-sonnet-4-6"``);
            emitted only when ``llm_assisted`` is True.
        timestamp: Override the ISO-8601 timestamp (used for tests /
            deterministic snapshots). Defaults to current UTC.
        skip_if_recent: When True, do nothing if the most recent
            curation_history entry already matches the same
            ``(curator, action)`` pair. Useful when refactoring a script
            into the helper without producing duplicate trail entries
            during a re-run.

    Returns:
        The appended event dict (or the most recent matching one if
        ``skip_if_recent`` short-circuited).
    """
    history = record.setdefault("curation_history", [])
    if history is None:
        record["curation_history"] = history = []

    if skip_if_recent and history:
        last = history[-1]
        if (
            isinstance(last, dict)
            and last.get("curator") == curator
            and last.get("action") == action
        ):
            return last

    event: dict[str, Any] = {
        "timestamp": timestamp or now_iso(),
        "curator": curator,
        "action": action,
    }
    if changes is not None:
        event["changes"] = changes
    if previous_status is not None:
        event["previous_status"] = previous_status
    if new_status is not None:
        event["new_status"] = new_status
    if llm_assisted:
        event["llm_assisted"] = True
        if llm_model is not None:
            event["llm_model"] = llm_model

    history.append(event)
    return event
