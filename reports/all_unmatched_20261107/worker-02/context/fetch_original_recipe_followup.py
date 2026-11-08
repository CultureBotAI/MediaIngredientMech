"""Capture explicit original-source follow-up URLs without editing source data."""
import importlib.util
from pathlib import Path
import json
from concurrent.futures import ThreadPoolExecutor

path = Path(__file__).with_name("fetch_metatraits_primary.py")
spec = importlib.util.spec_from_file_location("fetch_primary", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.ROOT = Path(__file__).parent / "original-recipes"
URLS = {
    "elkins2008-supplement-escholarship.pdf": "https://escholarship.org/content/qt28w1d3zs/qt28w1d3zs.pdf",
    "elkins2008-europepmc.xml": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2430366/fullTextXML",
    "elkins2008-oa-api.xml": "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=PMC2430366",
}

if __name__ == "__main__":
    module.ROOT.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=3) as pool:
        observations = list(pool.map(module.fetch, URLS.items()))
    (module.ROOT / "retrieval-log.json").write_text(json.dumps(observations, indent=2) + "\n")
    print(json.dumps(observations, indent=2))
