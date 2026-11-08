"""Read-only independent whole-selection mechanical comparison; no chemistry approval.
Output must be new under this technical directory. No root author's helper imported.
"""
from pathlib import Path
import argparse,copy,hashlib,json
from datetime import datetime,timezone
import yaml
HERE=Path(__file__).resolve().parent
R=HERE.parent
A=R.parent
W=R.parents[3]
PID='b2-proposal-sodium_resazurin_01_percent_wv_jcm363_1023'
ACID='b2-proposal-sulfuric_acid_10n_named_sources'
AFFECTED={88,93,114,118}
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canon(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def main():
 ap=argparse.ArgumentParser();ap.add_argument('selection');ap.add_argument('output');args=ap.parse_args()
 new=R/args.selection;out=HERE/args.output
 if '/' in args.selection or '/' in args.output or out.exists():raise ValueError('Use fresh single-member names')
 inputs=[]
 def read(p,fmt='json'):
  b=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'sha256':sha(b)})
  return (json.loads(b) if fmt=='json' else yaml.safe_load(b)),b
 old=A/'final-corrections-v1/review-bound-v1'
 before={};after={};raw_before={};raw_after={}
 for name in ['decisions','proposals','evidence']:
  before[name],raw_before[name]=read(old/(name+'.json'));after[name],raw_after[name]=read(new/(name+'.json'))
 frozen,fr=read(A/'context/frozen-shard-02.json')
 ds=before['decisions']['decisions'];ns=after['decisions']['decisions'];cases=frozen['cases']
 assert len(ds)==len(ns)==len(cases)==188
 assert len({x['case_id'] for x in ds})==188
 assert {k:v for k,v in before['decisions'].items() if k!='decisions'}=={k:v for k,v in after['decisions'].items() if k!='decisions'}
 case_rows=[]
 for i,(b,n,c) in enumerate(zip(ds,ns,cases,strict=True)):
  assert b['case_id']==n['case_id']==c['case_id']
  assert b['case_input_sha256']==n['case_input_sha256']==canon(c)
  assert n['occurrence_ids']==[v['occurrence_id'] for v in c.get('occurrences',[])]
  assert n['source']=={k:c[k] for k in ['source','source_case_id','source_label','raw_source_label']}
  delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k))
  expected=['applicability','independent_review','reasoning'] if i in {114,118} else ['independent_review'] if i in {88,93} else []
  assert delta==expected,(i,delta)
  if i in AFFECTED:assert n['independent_review']=={'status':'pending','evidence_ids':[]}
  if i in {114,118}:
   assert n['applicability']==b['applicability'].replace(b['reasoning'],n['reasoning'])
   prefix='The six occurrences in case 114' if i==114 else 'The one occurrence in case 118'
   assert n['reasoning'].startswith(prefix)
   assert 'unchanged shared proposal covers seven occurrences.' in n['reasoning']
   tail='Normality is source-stated and does not require a guessed solvent or conversion to molarity. A source-supported isolated stock proposal now replaces the previous unperformed-curation deferral.'
   assert b['reasoning'].endswith(tail) and n['reasoning'].endswith(tail)
  case_rows.append({'index':i,'case_id':n['case_id'],'old_canonical_sha256':canon(b),'new_canonical_sha256':canon(n),'frozen_case_canonical_sha256':canon(c),'occurrences':len(n['occurrence_ids']),'changed_fields':delta})
 ps=before['proposals']['proposals'];qs=after['proposals']['proposals']
 assert len(ps)==len(qs)==117 and len({p['proposal_id'] for p in ps})==117
 assert {k:v for k,v in before['proposals'].items() if k!='proposals'}=={k:v for k,v in after['proposals'].items() if k!='proposals'}
 proposal_rows=[];changed=0
 for b,n in zip(ps,qs,strict=True):
  assert b['proposal_id']==n['proposal_id'];pid=b['proposal_id']
  bv,bb=read(A/b['after_capture']['path'],'yaml');nv,nb=read(A/n['after_capture']['path'],'yaml')
  assert sha(bb)==b['after_capture']['sha256'];assert sha(nb)==n['after_capture']['sha256']
  if pid!=PID:assert b==n and bb==nb
  else:
   changed+=1;p=copy.deepcopy(b);p['after_capture']=n['after_capture'];assert p==n
   assert sha(bb)=='8c43d59c4d4adcd07300804b29b219c2197328630bb6077adcc4fd95f8b3062d'
   assert bv['solution_type']=='MINERAL_STOCK' and nv['solution_type']=='OTHER'
   stripped=copy.deepcopy(nv);stripped['solution_type']=bv['solution_type'];stripped['curation_history']=bv['curation_history'];assert stripped==bv
   assert nv['curation_history'][:-1]==bv['curation_history'] and len(nv['curation_history'])==len(bv['curation_history'])+1
   event=nv['curation_history'][-1];assert event['llm_assisted'] is True and event['action']=='CORRECTED' and event['curator']=='worker02 /root'
   assert 'W02-FC-D-SODIUM-RESAZURIN-TYPE' in event['changes']
   timestamp=datetime.fromisoformat(event['timestamp']);assert timestamp.utcoffset() is not None and timestamp<=datetime.now(timezone.utc)
  if pid==ACID:
   assert sha(nb)=='95aca3c8092ca7430df24c8cbdaa65151b36d5cb15346abb86f7d7cb7d934ee1'
   assert set(n['case_ids'])=={ns[114]['case_id'],ns[118]['case_id']}
  proposal_rows.append({'proposal_id':pid,'old_canonical_sha256':canon(b),'new_canonical_sha256':canon(n),'old_capture':b['after_capture'],'new_capture':n['after_capture'],'bytes_identical':bb==nb})
 assert changed==1
 be=before['evidence']['evidence'];ae=after['evidence']['evidence']
 assert ae[:len(be)]==be and len(ae)==len(be)+2
 assert len({e['evidence_id'] for e in ae})==len(ae)
 assert {k:v for k,v in before['evidence'].items() if k!='evidence'}=={k:v for k,v in after['evidence'].items() if k!='evidence'}
 for e in ae[len(be):]:
  cap=e['capture'];v,b=read(A/cap['path']);assert sha(b)==cap['sha256']
 receipt={'status':'PASS','reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'selection':str(new.relative_to(W)),'scope':'Mechanical preservation only; no chemistry or owner/release approval','input_bindings':inputs,'counts':{'cases':188,'occurrences':sum(len(d['occurrence_ids']) for d in ns),'proposals':117,'unchanged_payloads':116,'changed_payloads':1,'unchanged_full_cases':184,'narrative_changes':2,'pending_review_cases':4,'new_administrative_evidence':2},'case_rows':case_rows,'proposal_rows':proposal_rows,'new_evidence':ae[len(be):]}
 with out.open('x') as f:json.dump(receipt,f,indent=2,ensure_ascii=False);f.write('\n')
 print(json.dumps({'output':str(out.relative_to(W)),'sha256':sha(out.read_bytes()),'counts':receipt['counts']}))
if __name__=='__main__':main()
