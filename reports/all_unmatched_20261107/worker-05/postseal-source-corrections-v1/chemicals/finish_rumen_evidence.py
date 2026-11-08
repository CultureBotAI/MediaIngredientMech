from pathlib import Path
import json,hashlib,datetime,sys,yaml,collections
sys.path.insert(0,str(Path('src').resolve()))
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
O=Path(__file__).parent; S=O.parent; R=Path('reports/all_unmatched_20261107/worker-05'); B=R/'final-correction-v1/core'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(n,x):
 p=O/n;assert not p.exists();p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n');return p
def cap(p):return {'root':'artifact','path':'postseal-source-corrections-v1/'+str(p.relative_to(S)),'sha256':sha(p)}
P=json.loads((O/'proposals.json').read_text())['proposals'];D=json.loads((O/'decisions.json').read_text())['decisions'];caseids=[D[0]['case_id']]
attempts=[json.loads(p.read_text()) for p in sorted((O/'captures').glob('*.receipt.json'))]
attempt_manifest=dump('primary-access-results-v1.json',{'attempts':attempts,'direct_requests':'Three distinct publisher full-text URLs, each requested once with HTTP and once through the web tool. HTTP returned 403; web tool reported inaccessible. Earlier sandbox-only HTTP attempts failed DNS before reaching publisher.','source_scope':'The publisher abstract supplies organism-isolation context but cannot establish processing of medium rumen-fluid inputs. No full publication was obtained.','no_support_inferred_from_failures':True})
items=[
 ('POSTSEAL-CHEM-RAW-PARENTS','source_snapshot',O/'microbedecoder-three-parent-source-records-v1.json',None,'Complete MicrobeDecoder raw rows 5903, 5905 and 20394; exact original database SHA and raw substrate fields.','All three literal labels name rumen fluid without a processing qualifier. This is evidence about the imported source fields, not proof of untreated material or complete primary-publication protocols.'),
 ('POSTSEAL-CHEM-1204-COMMENT','source_snapshot',S/'issues/issue1204-comments.json','https://github.com/CultureBotAI/MediaIngredientMech/issues/1204#issuecomment-6718503591','Comment 6718503591, current full response array.','Current filed source-scope decision explicitly supersedes redirecting these same three generic rumen-fluid parts to the clarified owner and prescribes literal UNMAPPED parts without identifiers.'),
 ('POSTSEAL-CHEM-1237','source_snapshot',S/'issues/issue1237.json','https://github.com/CultureBotAI/MediaIngredientMech/issues/1237','BIO-COMP-002 family disposition and owner-scope discussion.','Current family tracker supersedes the old comparison redirect and preserves source-specific processing uncertainty; other family decisions do not authorize arbitrary owner selection.'),
 ('POSTSEAL-CHEM-FINDING001','local_validation',O/'new-rumen-applicability-finding-v1.json',None,'Exact pre-fix three-payload reproduction and initial issue comparison.','Reported to the coordinator before correction; immutable precursor to the three bounded successor proposals.'),
 ('POSTSEAL-CHEM-PRIMARY-ACCESS','unsuccessful_search',attempt_manifest,None,'Three cited publisher full-text requests plus web retrieval attempts; retained HTTP bodies and receipts.','Retrieval failures only. They do not resolve processing, species or recipe equivalence. The literal source labels and explicit current source-scope decision support withdrawal of the unsupported clarification claim.')]
now=datetime.datetime.now(datetime.timezone.utc).isoformat(); E=[]
for eid,kind,p,url,locator,support in items:
 e={'evidence_id':eid,'kind':kind,'capture':cap(p),'url':url,'locator':locator,'supports_or_contradicts':support,'case_ids':caseids,'accessed_at':now,'author':'/root/chemicals_research','timestamp_scope':'This is the current local read/assessment time. Original remote issue retrieval times are preserved in issues/rumen-receipt.json and issues/receipt.json; individual publisher attempts retain their own request timestamps.'}
 if kind=='unsuccessful_search':e['search_scope']='Exact raw-row cited DOI full-text URLs, three distinct publisher pages, web tool and direct HTTP. No paid session or bypass attempted.'
 E.append(e)
dump('evidence.json',{'fragment':True,'additive_only':True,'base':{'path':str(B/'evidence.json'),'sha256':sha(B/'evidence.json')},'evidence':E})
# Substitute proposals into their exact path slots, including promotions, without writing catalog files.
records={str(p):yaml.safe_load(p.read_text()) for p in Path('data/ingredients').rglob('*.yaml')}
baseP=json.loads((B/'proposals.json').read_text())['proposals']; replacement={p['proposal_id']:p for p in P}
for original in baseP:
 p=replacement.get(original['proposal_id'],original)
 cp=p['after_capture']; actual=O/Path(cp['path']).relative_to('postseal-source-corrections-v1/chemicals') if p['proposal_id'] in replacement else R/cp['path']
 assert sha(actual)==cp['sha256']
 destination=p.get('destination_owner_path',p['owner_path'])
 if destination!=p['owner_path']:records.pop(p['owner_path'],None)
 records[destination]=yaml.safe_load(actual.read_text())
violations=validate_component_partonomy(list(records.values()))
receipt={'status':'PASS' if not violations else 'FAIL','catalog_records':len(records),'sealed_proposals_substituted':len(baseP),'postseal_replacements':len(P),'violations':[str(v) for v in violations],'guarded_writer':'All three full IngredientRecord payloads passed the native closed-schema writer and parsed roundtrip.','source_case_and_origin_counts_changed':False,'base_sha256':{n:sha(B/n) for n in ['decisions.json','proposals.json','evidence.json']},'fragment_sha256':{n:sha(O/n) for n in ['decisions.json','proposals.json','evidence.json']},'schema_sha256':sha('src/mediaingredientmech/schema/mediaingredientmech.yaml'),'component_validator_sha256':sha('src/mediaingredientmech/validation/component_partonomy.py'),'scope':'Local structural overlay only; not an approval of unchanged scientific claims, conditional installation, or export. Parent will validate all concurrent postseal deltas together.'}
dump('rumen-validation-v1.json',receipt);print(json.dumps(receipt,indent=2))
