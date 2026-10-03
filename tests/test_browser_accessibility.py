from html.parser import HTMLParser
from pathlib import Path


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.items = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.items.append((tag, dict(attrs)))

    def find(self, tag=None, **attrs):
        return [
            a
            for t, a in self.items
            if (tag is None or t == tag)
            and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in attrs.items())
        ]


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = "https://culturebotai.github.io/mechs/"


def test_browser_search_and_result_updates_have_accessible_semantics():
    dom = Elements((ROOT / "docs/browser.html").read_text())
    assert dom.find("label", for_="search")
    assert dom.find(role="status", aria_live="polite", aria_atomic="true")
    assert dom.find("button", id="reset-filters", type="button")
    assert dom.find("a", href=DIRECTORY)
    assert Elements((ROOT / "docs/index.html").read_text()).find("a", href=DIRECTORY)


def test_browser_javascript_parses(tmp_path):
    import re
    import shutil
    import subprocess

    import pytest

    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required for the browser JavaScript syntax check")
    html = (ROOT / "docs/browser.html").read_text()
    scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", html, re.DOTALL)
    assert scripts
    for number, script in enumerate(scripts):
        source = tmp_path / f"inline-{number}.js"
        source.write_text(script)
        checked = subprocess.run([node, "--check", str(source)], capture_output=True, text=True)
        assert checked.returncode == 0, checked.stderr
