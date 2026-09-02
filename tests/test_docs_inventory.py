"""Guards against stale, hand-maintained inventory counts in documentation."""

from pathlib import Path

ROOT = Path(__file__).parent.parent


def test_landing_page_derives_counts_from_generated_browser_catalog() -> None:
    html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

    assert 'fetch("data/ingredients.json")' in html
    assert 'record.mapping_status === "MAPPED"' in html
    for element_id in ("ingredient-count", "mapped-count", "coverage-count"):
        assert f'id="{element_id}">…<' in html


def test_landing_statistics_link_to_matching_browser_views() -> None:
    landing = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    browser = (ROOT / "docs" / "browser.html").read_text(encoding="utf-8")

    assert '<a class="stat" href="browser.html">' in landing
    assert landing.count('<a class="stat" href="browser.html#status=MAPPED">') == 2
    assert '<div class="stat">' not in landing
    assert "new URLSearchParams(window.location.hash.replace(/^#/, ''))" in browser
    assert "statusControl.value = supported ? status : '';" in browser


def test_readme_links_generated_inventory_instead_of_embedding_review_counts() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "data/curated/ALL_INGREDIENTS.md" in readme
    assert "995 mapped" not in readme
    assert "136 unmapped" not in readme
