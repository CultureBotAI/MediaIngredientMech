Independent media review, chemistry reviewer

All63 original source cases, full frozen recipes, evidence and six original payloads were reviewed for v1. For v2, all revised decisions, new primary evidence and added payloads are inspected and rebound to final hashes. No maintained YAML or SSSOM was modified.

Actual tool failures during re-review: BeautifulSoup import failed (ModuleNotFoundError); HTML inspection continued using Python standard-library HTMLParser. An attempted read of captures/media/media-followup-owner-comparison.json failed because the filename was followup-owner-comparison.json; the actual file was then read. A combined full-file output exceeded the output limit; the necessary scientific sections were read separately. Shell startup repeatedly reported pyenv cannot rehash its nonwritable shims; the explicit frozen Python environment itself ran successfully.

Additional final-pass operations: independent rg -uu search across maintained per-record data saved media-chemistry-owner-search.txt (ignored files included). Existing owner comparison inspected all active identity/mapping/synonym fields. Primary catalogue PDF was inspected using pdftotext: physical pages6/9/17 correspond to printed pages4/7/15. No composition was inferred from package size.

Independent primary-discovery searches located Merck manual and Sigma RCA data sheet; GET attempts to the Merck mirror returned403 and Sigma timed out after45seconds. A web.open retry to the Merck mirror also returned403. Exact unsuccessful retrieval receipts are under media-chemistry-captures/. These attempts confer no scientific support. Author independently retrieved original DSMZ550, whose explicit Merck48g component resolves product-identity evidence placement.
