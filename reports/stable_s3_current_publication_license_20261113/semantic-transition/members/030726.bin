"""Data-derived metadata for emitted SSSOM mapping sets."""

from __future__ import annotations

import re
from collections.abc import Iterable, Mapping
from datetime import date
from typing import Any


def subset_date_metadata(
    metadata: Mapping[str, Any], rows: Iterable[Mapping[str, str]]
) -> dict[str, Any]:
    """Describe the emitted rows without inheriting an excluded row's date.

    Empty or wholly dateless sets omit both optional date fields; they have no
    row date to substantiate a version. Missing row dates stay untouched for
    Rule F to diagnose. Nonblank dates must be ASCII calendar dates, so malformed
    values cannot silently determine the set version. This adds no approval and
    does not modify row payloads, source provenance or other metadata (#1090).
    """
    dates = []
    for position, row in enumerate(rows, 1):
        raw = row.get("mapping_date", "")
        if not isinstance(raw, str):
            raise ValueError(f"Invalid mapping_date in emitted row {position}: {raw!r}")
        value = raw.strip()
        if not value:
            continue
        if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
            raise ValueError(f"Invalid mapping_date in emitted row {position}: {raw!r}")
        try:
            dates.append(date.fromisoformat(value))
        except ValueError as exc:
            raise ValueError(f"Invalid mapping_date in emitted row {position}: {raw!r}") from exc
    result = dict(metadata)
    if dates:
        newest = max(dates).isoformat()
        result.update(mapping_date=newest, mapping_set_version=newest)
    else:
        result.pop("mapping_date", None)
        result.pop("mapping_set_version", None)
    return result
