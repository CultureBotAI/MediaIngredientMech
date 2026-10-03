"""Discussion previews use the maintained local ingredient renderer layout."""

import json
import re
from pathlib import Path
from urllib.parse import urlsplit

from mediaingredientmech import render_ingredient_pages as render

ROOT = Path(__file__).resolve().parents[1]


def test_every_discussion_preview_link_matches_a_rendered_record_section(tmp_path):
    source = (ROOT / "app/discussions/data.js").read_text()
    records = json.loads(
        re.search(
            r"window.searchData = (.*?);\nwindow.searchMetrics", source, re.S
        ).group(1)
    )
    assert records
    output = tmp_path / "pages/ingredient"
    env = render.make_env()
    for record in records:
        sources = [
            ROOT / "data/ingredients" / kind / record["source_file"]
            for kind in ("mapped", "unmapped")
        ]
        sources = [path for path in sources if path.is_file()]
        assert (
            len(sources) == 1
        ), "Discussion source must resolve without guessing its identifier"
        status, _, slug = render.render_one(env, sources[0], output, force=True)
        assert status == "rendered"
        url = urlsplit(record["page_url"])
        target = (tmp_path / "app/discussions" / url.path).resolve()
        assert target == output / (slug + ".html")
        assert url.fragment == "discussions"
        assert 'id="discussions"' in target.read_text()
