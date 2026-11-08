"""Preserve author-v1; narrow only new evidence applicability and issue pointers."""
from pathlib import Path
import copy,datetime,hashlib,json
R=Path.cwd();O=R/'.temp/columbia-controls-successor-v1';A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v7'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def cap(p):return {'root':'artifact','path':str(p.relative_to(A)),'sha256':sha(p)}
at=datetime.datetime.now(datetime.timezone.utc).isoformat()
save(S/'author-draft-binding-finding.json',{'at':at,'finding_id':'W10-SV7-AUTHOR-DRAFT-EVIDENCE-SCOPE-001','status':'reported_before_draft_metadata_correction','scope':'New unsealed author-core evidence associations only; no historical/source/payload defect or GitHub finding claimed.',
 'description':'Initial author-core attached both issue packets and Columbia-specific metadata to all four affected cases. Narrow new evidence case_ids and references to the actual Columbia or buffer applicability; preserve all original1218evidence entries and original memberships. New dependent0118 also inherited irrelevant new buffer refs through those drafts.',
 'proposed_fix':'Add author-core-v2, preserve all author-v1 files and four payload bytes; remove only inapplicable new sv7 references and the Columbia issue pointer from two buffer proposal markers.',
 'payload_change_required':False,'external_issue_mutation':False})
D=load(S/'author-core/decisions.json');P=load(S/'author-core/proposals.json');E=load(S/'author-core/evidence.json')
col={D['decisions'][i]['case_id'] for i in [118,178]};buf={D['decisions'][i]['case_id'] for i in [80,135]}
col_e={'sv7-filed-columbia','sv7-independent-columbia-decision','sv7-explicit-source-routing','sv7-external-oxoid-origins'}
buf_e={'sv7-filed-stock-completeness'};shared={'sv7-input-byteproof'}
for row in E['evidence']:
 if row['evidence_id'] in col_e:row['case_ids']=sorted(col)
 elif row['evidence_id'] in buf_e:row['case_ids']=sorted(buf)
for obj in [*D['decisions'],*P['proposals']]:
 if 'source_successor_v7' not in obj:continue
 ids=set(obj.get('case_ids',[obj.get('case_id')]))
 isbuffer=bool(ids & buf);allowed=(buf_e if isbuffer else col_e)|shared
 obj['evidence_ids']=[x for x in obj['evidence_ids'] if not x.startswith('sv7-') or x in allowed]
 if isbuffer:obj['source_successor_v7']['issues']=['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237#issuecomment-6720201281']
for name,doc in [('decisions.json',D),('proposals.json',P),('evidence.json',E)]:save(S/'author-core-v2'/name,doc)
old=load(A/'successor-v6/final-core/evidence.json')['evidence'];assert E['evidence'][:len(old)]==old
for p in P['proposals']:assert sha(A/p['after_capture']['path'])==p['after_capture']['sha256']
save(S/'author-freeze-v2.json',{'at':at,'supersedes_author_metadata':cap(S/'author-freeze.json'),'original_draft_finding':cap(S/'author-draft-binding-finding.json'),
 'core':{n:cap(S/'author-core-v2'/n) for n in ['decisions.json','proposals.json','evidence.json']},'unchanged_four_payloads':load(S/'author-freeze.json')['four_authored_payloads'],
 'source_routing':cap(S/'source-routing.json'),'review_pending':True,'science_or_payload_change':False,'all_original_evidence_objects_and_memberships_unchanged':True,
 'correction':'Only draft new evidence applicability/refs and exact buffer issue pointers narrowed; no fresh scientific or release claim.'})
with (S/'scripts/narrow_author_bindings.py').open('xb') as f:f.write(Path(__file__).read_bytes())
print(json.dumps({'status':'AUTHOR_V2_FROZEN','core':str(S/'author-core-v2'),'counts':[len(D['decisions']),len(P['proposals']),len(E['evidence'])],'payload_changes_since_author_v1':0},indent=2))
