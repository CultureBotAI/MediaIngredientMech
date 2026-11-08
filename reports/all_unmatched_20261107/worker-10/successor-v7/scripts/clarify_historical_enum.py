"""Append-only response to exact independent buffer-case metadata finding."""
from pathlib import Path
import copy,datetime,hashlib,json
R=Path.cwd();O=R/'.temp/columbia-controls-successor-v1';A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
f=O/'science/historical-completeness-finding-v1.json';assert sha(f)=='51932d3685ea0d2e871fd21089773d532b0c6d40b467ff8ea7bd8a31e2e4647d'
target=S/'inputs/historical-completeness-finding-v1.json'
with target.open('xb') as o:o.write(f.read_bytes())
D=load(S/'author-core-v2/decisions.json');old=copy.deepcopy(D);rows=[]
P=load(S/'author-core-v2/proposals.json')['proposals']
for i in [80,135]:
 d=D['decisions'][i];p=next(p for p in P if p['proposal_id'] in d['proposal_ids'])
 oldblock=copy.deepcopy(d['completion_reassessment'])
 d['source_successor_v7']['old_completion_reassessment_is_historical']=True
 d['source_successor_v7']['historical_completion_reassessment_preserved']='The original completion_reassessment object remains verbatim, including its former PARTIAL completeness wording. That wording is historical; the active source-qualified preparation assertion is now UNKNOWN. The prohibition on inventing a complete stock formula and every original chemistry/source/quantity/role/export hold remains in force.'
 d['source_successor_v7']['active_component_assertion']={'method':'LABEL_ENUMERATION','completeness':'UNKNOWN','selected_capture':p['after_capture']}
 d['source_successor_v7']['historical_enum_finding']={'finding_id':'W10-SV7-SKEPTIC-HISTORICAL-COMPLETENESS-001','captured_finding':cap(target),'correction_state':'implemented_in_author_v3_awaiting_exact_independent_recheck'}
 assert d['completion_reassessment']==oldblock
 rows.append({'case_index':i,'case_id':d['case_id'],'before_case_sha256':canon(old['decisions'][i]),'after_case_sha256':canon(d),'preserved_completion_reassessment_sha256':canon(oldblock),'selected_payload':p['after_capture']})
save(S/'author-core-v3/decisions.json',D)
for n in ['proposals.json','evidence.json']:
 with (S/'author-core-v3'/n).open('xb') as f:f.write((S/'author-core-v2'/n).read_bytes())
save(S/'historical-enum-correction.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'finding':cap(target),'old_author_decisions':cap(S/'author-core-v2/decisions.json'),'new_author_decisions':cap(S/'author-core-v3/decisions.json'),'rows':rows,'other186caseobjects_exact':all(old['decisions'][i]==d for i,d in enumerate(D['decisions']) if i not in [80,135]),'all_payloads_proposals_evidence_and_original_history_unchanged':True,'no_new_science_or_issue_closure':True})
save(S/'author-freeze-v3.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'supersedes_author_metadata':cap(S/'author-freeze-v2.json'),'independent_finding_and_correction':cap(S/'historical-enum-correction.json'),'core':{n:cap(S/'author-core-v3'/n) for n in ['decisions.json','proposals.json','evidence.json']},'unchanged_four_payloads':load(S/'author-freeze.json')['four_authored_payloads'],'source_routing':cap(S/'source-routing.json'),'review_pending':True,'scope':'Two explicit historical/current enum clarifications only; no historical-object or payload rewrites.'})
with (S/'scripts/clarify_historical_enum.py').open('xb') as f:f.write(Path(__file__).read_bytes())
print(json.dumps({'status':'AUTHOR_V3_FROZEN','finding_before_fix':sha(target),'author_freeze_v3_sha256':sha(S/'author-freeze-v3.json'),'payload_changes':0,'case_clarifications':[80,135]},indent=2))
