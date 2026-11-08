import importlib.util
import json
from pathlib import Path

import pytest
from mediaingredientmech import campaign_publication as c

root = Path.cwd()
out = root / '.temp/campaign-publication-receipt-path-v1'
spec = importlib.util.spec_from_file_location('publisher_fixture', root/'tests/test_campaign_publication.py')
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)
workspace = out/'fixture'
workspace.mkdir()
case = fixture.case.__wrapped__(workspace, pytest.MonkeyPatch())
outside = case['root']/'outside-reports'
outside.mkdir()
spelling = case['root']/'reports'/'..'/'outside-reports'
before = (case['root']/c.SOURCE).read_bytes()
result = c.publish(case['root'], case['path'], spelling, apply=True)
actual = {'schema_version':1,'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1198','publisher_sha256':c.sha(Path(c.__file__).read_bytes()),'probe_sha256':c.sha(Path(__file__).read_bytes()),'argument_spelling':str(spelling),'physical_directory':str(outside),'lexically_under_reports':spelling.is_relative_to(case['root']/'reports'),'physically_under_reports':outside.is_relative_to(case['root']/'reports'),'returned_status':result['status'],'unexpected_receipt_paths':sorted(str(p.relative_to(case['root'])) for p in outside.iterdir()),'canonical_changed':(case['root']/c.SOURCE).read_bytes()!=before,'native_chain_replays':c.validate(case['root'],case['path'])['status']=='verified','production_publication':False,'fixture_boundaries':'Owner proof and native generation are isolated by the disclosed unit fixture; actual row/policy projection, native maker/receipt replay, path reservation and filesystem publication are exercised.'}
assert actual['returned_status']=='complete' and len(actual['unexpected_receipt_paths'])==3
(out/'result.json').write_bytes(c.encoded(actual))
print(json.dumps(actual,indent=2))
