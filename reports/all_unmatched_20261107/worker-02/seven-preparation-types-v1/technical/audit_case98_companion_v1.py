"""Independent read-only companion preservation audit; no source-science approval."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
T=Path(__file__).resolve().parent;R=T.parent;A=R.parent;W=R.parents[3]
def sha(b):return hashlib.sha256(b).hexdigest()
def canonical(x):return sha(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def objects(raw,key):
 s=raw.decode();p=s.index('[',s.index(json.dumps(key)+':'))+1;d=json.JSONDecoder();out=[]
 while True:
  while s[p].isspace() or s[p]==',':p+=1
  if s[p]==']':return out
  _,end=d.raw_decode(s,p);out.append(s[p:end].encode());p=end

def main():
 out=T/'case98-preservation-review-v1.json'
 if out.exists():raise FileExistsError(out)
 inputs=[]
 def read(p):
  raw=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'sha256':sha(raw)});return json.loads(raw),raw
 old={};new={};obr={};nbr={}
 for name in ['decisions','proposals','evidence']:
  old[name],obr[name]=read(R/'selected-v2'/(name+'.json'));new[name],nbr[name]=read(R/'review-input-v2'/(name+'.json'))
  assert {k:v for k,v in old[name].items() if k!=name}=={k:v for k,v in new[name].items() if k!=name}
 pins,_=read(R/'context/case98-companion-input-pins.json')
 for name in old:assert pins[name]==sha(obr[name])
 ds=old['decisions']['decisions'];ns=new['decisions']['decisions'];assert len(ds)==len(ns)==188
 frozen,_=read(A/'context/frozen-shard-02.json');cases=frozen['cases'];ob=objects(obr['decisions'],'decisions');nb=objects(nbr['decisions'],'decisions');rows=[]
 oldreason='Original NIES source marks manganese sulfate pentahydrate with footnote1). Its substitution note distinguishes250mgheptahydrate from217mgpentahydrate. Existing CHEBI131524 is the five-water substance; the marker is not part of a resolving chemical name.'
 newreason='The successfully inspected TOGO M2509 capture reports the NIES table/footnote marking manganese sulfate pentahydrate with footnote1). Its reported NIES substitution note distinguishes250mgheptahydrate from217mgpentahydrate. Existing CHEBI131524 is the five-water substance; the marker is not part of a resolving chemical name. The direct NIES capture remains an unsuccessful formulation lookup.'
 for i,(b,n,c) in enumerate(zip(ds,ns,cases,strict=True)):
  assert b['case_id']==n['case_id']==c['case_id'] and b['case_input_sha256']==n['case_input_sha256']==canonical(c)
  assert b['occurrence_ids']==n['occurrence_ids']==[x['occurrence_id'] for x in c.get('occurrences',[])]
  delta=sorted(k for k in set(b)|set(n) if b.get(k)!=n.get(k));expected=['applicability','independent_review','reasoning'] if i==98 else ['independent_review'] if i==58 else [];assert delta==expected
  if i in [58,98]:assert n['independent_review']=={'status':'pending','evidence_ids':[]}
  else:assert ob[i]==nb[i]
  if i==98:
   assert len(n['occurrence_ids'])==1 and n['proposal_ids']==[] and n['disposition']=='supplied_form_correction'
   assert b['reasoning']==oldreason and n['reasoning']==newreason
   assert n['applicability']==b['applicability'].replace(oldreason,newreason)
  rows.append({'index':i,'case_id':n['case_id'],'before_sha256':canonical(b),'after_sha256':canonical(n),'changed_fields':delta,'raw_object_bytes_equal':ob[i]==nb[i]})
 assert nbr['proposals']==obr['proposals'];ps=new['proposals']['proposals'];assert len(ps)==117
 payloads=[]
 for p in ps:
  cap=p['after_capture'];path=A/cap['path'];assert sha(path.read_bytes())==cap['sha256'];payloads.append({'proposal_id':p['proposal_id'],'after_capture':cap})
 oe=old['evidence']['evidence'];ne=new['evidence']['evidence'];assert len(oe)==1827 and len(ne)==1829 and ne[:len(oe)]==oe
 assert objects(nbr['evidence'],'evidence')[:len(oe)]==objects(obr['evidence'],'evidence')
 assert len({e['evidence_id'] for e in ne})==len(ne)
 for e in ne[len(oe):]:assert sha((A/e['capture']['path']).read_bytes())==e['capture']['sha256']
 for path,digest in [('b/captures/retry-togo-M2509.json','5cf01f0691361181fa733c2163aaed917feabce24da5c2fec876e5616ed83950'),('b/captures/source-c533a17a8ded25f29384.bin','02b520ffc3870143c8a3fa695dc717c536930131a527aa7770c53207b6039101')]:assert sha((A/path).read_bytes())==digest
 receipt={'reviewer':'/root/research_b','reviewed_at':datetime.now(timezone.utc).isoformat(),'scope':'Technical attribution/preservation only; independent source interpretation remains D scope','status':'PASS','inputs':inputs,'counts':{'cases':188,'occurrences':sum(len(x['occurrence_ids']) for x in ns),'proposals':117,'additional_payload_changes':0,'case98_occurrences':1,'case58_occurrences':24,'unchanged_complete_cases':186,'case98_attribution_fields':2,'review_metadata_resets':2,'old_evidence_prefix':1827,'new_administrative_evidence':2},'case_rows':rows,'payloads':payloads,'preserved_chemical_outcome_source_ids_occurrences_and_holds':True,'no_new_ingredient_alias_or_history':True,'source_capture_hashes_unchanged':True,'no_chemistry_or_release_approval':True}
 with out.open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
 print(json.dumps({'status':'PASS','receipt':str(out.relative_to(W)),'sha256':sha(out.read_bytes()),'counts':receipt['counts']}))
if __name__=='__main__':main()
