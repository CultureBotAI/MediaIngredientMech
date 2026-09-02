"""Pin how scatter points are stroked in the published visualisations.

The plots draw ~2,400 ingredients at r=5-15 in a UMAP, so overlap is not incidental --
it is the density signal the plot exists to show. `fill-opacity: 0.7` is what conveys
it, and an opaque stroke silently cancels that: a background-coloured ring does not
merely look solid, it ERASES the point beneath it, so nothing ever blends.

These tests pin the rest state. They do not forbid a stroke on hover, which is where
an outline helps and where overlap no longer matters.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parent.parent
PAGES = ("docs/ingredient_umap.html", "docs/ingredient_graph.html")


@pytest.fixture(params=PAGES)
def page(request):
    path = _REPO / request.param
    assert path.is_file(), f"missing visualisation page {request.param}"
    return path.read_text(encoding="utf-8")


def test_points_keep_fill_transparency(page):
    """Without this the plot cannot show density at all."""
    assert "fill-opacity" in page
    assert re.search(r"\.attr\('fill-opacity',\s*0\.7\)", page), (
        "the rest-state fill opacity is what makes overlapping points readable"
    )


def test_no_background_coloured_halo_is_painted_at_rest(page):
    """A halo the colour of the plot background erases whatever it overlaps.

    It was introduced with dark mode for point separation, which is a real concern --
    but at this density it destroyed more information than it added, so it now applies
    on hover only.
    """
    assert "getComputedStyle(container).backgroundColor" not in page, (
        "a background-coloured stroke cancels fill-opacity by erasing neighbours"
    )


def test_the_rest_stroke_is_none_for_filled_points(page):
    """Filled points carry no outline at rest, so neighbours blend."""
    assert re.search(
        r"function restStroke\(d\)\s*{[^}]*:\s*'none';", page
    ), "filled points must have no rest stroke"
    assert re.search(
        r"function restStrokeWidth\(d\)\s*{[^}]*:\s*0;", page
    ), "filled points must have zero rest stroke width"


def test_the_unmapped_ring_survives_because_it_carries_meaning(page):
    """That ring encodes mapping status; it is not decoration and must not be dropped."""
    assert re.search(r"function restStroke\(d\).*STATUS_COLORS\.UNMAPPED", page), (
        "the hollow UNMAPPED ring distinguishes unmapped records and must remain"
    )


def test_hover_still_emphasises_a_point(page):
    """Removing the rest halo must not remove the hover affordance."""
    assert re.search(r"\.attr\('stroke',\s*HILITE\)", page)
    assert re.search(r"\.attr\('stroke-width',\s*2\)", page)


def test_every_rest_stroke_assignment_goes_through_the_helpers(page):
    """Four sites set the rest stroke (draw, mouseout, re-render, search).

    They drifted apart before -- the halo lived in three of them -- so they are pinned
    to the shared helpers rather than to repeated inline ternaries.
    """
    # The helper's own body is the one legitimate occurrence of the ternary.
    call_sites = [
        line for line in page.splitlines()
        if "isHollow(d, currentColorBy) ? STATUS_COLORS.UNMAPPED :" in line
        and "function restStroke" not in line
    ]
    assert not call_sites, (
        f"{len(call_sites)} inline rest-stroke ternaries bypass restStroke(): {call_sites}"
    )
