# Archived OLS fixture

`ols-91258-list.json` preserves the exact 6,240-byte OLS list response from the existing Step 7(a/b) preflight source capture, SHA256 `e14e1a91519d14765d91d25ca145a56376d176814c62df304f78116dd4ad9278`. The archived response identifies its endpoint as `http://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91258`. No new request was made for these tests.

The one returned term is CHEBI:91258, disodium hydrogenphosphate dihydrate. Tests explicitly extract `_embedded.terms[0]`, assert that it is the sole term, and serialize that unchanged term object as the mocked exact-term response. Those serialized bytes are derived test input, not a claim that an exact-term HTTP response was separately captured. The strict client hashes the same mocked response bytes it parses.

The source lists formula `2H2O.HO4P.2Na` and both water-bearing structures. This fixture supports source-parsing and form-consistency tests; passing tests does not approve any real ingredient record.

`precorrection-owners.json` retains exact UTF-8 YAML byte streams and SHA256
identities for all 15 proposed #871/#268 owners from durable Git revision
`b162cb9c567db34296125230b997f5459f44d185`. Its matrix digest identifies the
reviewed preparatory field matrix. Tests verify each byte hash before parsing;
mutable post-correction source files are not fixture inputs. These historical
records test preservation/refusal only and confer no scientific approval.
