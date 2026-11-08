"""Bounded source-successor accounting. No scientific or release authority."""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib,json
CASE='CM_NAME:2be5d4f231ea346e62be345a8e8b35adbc735ccdced2de73963ce5265c48fd66'
OLD='b-proposal-cm0149-form';NEW='w03-oxoid-cm0149-product-1224-v1'
DEST='data/ingredients/mapped/reinforced_clostridial_medium_oxoid_cm0149.yaml'
EXPECTED_PAYLOAD='1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae'
FIXED_CASE_FIELDS=('case_id','case_input_sha256','source','occurrence_ids','owner_records','frozen_index','preserved_original_kg_entry_downstream_holds','native_owner_review_rows','hold_scope_note')
def require(v,message):
 if not v:raise ValueError(message)
def indexed(rows,key):
 require(isinstance(rows,list),key+' rows must be list')
 result={}
 for row in rows:
  k=row[key];require(k not in result,'duplicate '+key);result[k]=row
 return result
def canon(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def check_objects(od,op,oe,nd,np,ne,retirement):
 ds=indexed(od['decisions'],'case_id');dt=indexed(nd['decisions'],'case_id')
 ps=indexed(op['proposals'],'proposal_id');pt=indexed(np['proposals'],'proposal_id')
 es=indexed(oe['evidence'],'evidence_id');et=indexed(ne['evidence'],'evidence_id')
 require(len(ds)==188 and len(ps)==74 and len(es)==852,'unexpected frozen original counts')
 require(set(ds)==set(dt),'case membership changed')
 require(all(ds[k]==dt[k] for k in ds if k!=CASE),'unrelated decision changed')
 require({k:v for k,v in od.items() if k!='decisions'}=={k:v for k,v in nd.items() if k!='decisions'},'decision ledger header changed')
 for key in FIXED_CASE_FIELDS:require(ds[CASE].get(key)==dt[CASE].get(key),'frozen case/context field changed: '+key)
 require(set(pt)==(set(ps)-{OLD})|{NEW},'active proposal replacement set wrong')
 require(all(ps[k]==pt[k] for k in ps if k!=OLD),'unrelated proposal changed')
 require(set(es)<=set(et),'original evidence removed')
 require(all(es[k]==et[k] for k in es),'original evidence changed')
 require(retirement.get('retired_proposal')==ps[OLD],'retired proposal object changed')
 require(retirement.get('retired_decision')==ds[CASE],'retired decision object changed')
 require(dt[CASE]['proposal_ids']==[NEW],'changed case must bind one new proposal')
 require(pt[NEW]['case_ids']==[CASE],'new proposal must bind exact owned case')
 require(pt[NEW]['kind']=='new_owner','new proposal kind incorrect')
 require(pt[NEW].get('before_sha256') is None,'new proposal fabricated beforeimage')
 require(pt[NEW]['owner_path']==DEST,'new owner path incorrect')
 require(pt[NEW]['after_capture']['sha256']==EXPECTED_PAYLOAD,'candidate differs from assigned coordinator v4 bytes')
 require(sum(NEW in r['proposal_ids'] for r in dt.values())==1,'new proposal has duplicate origin')
 require(all(OLD not in r['proposal_ids'] for r in dt.values()),'retired proposal remains active')
 changed_fields=[key for key in sorted(set(ds[CASE])|set(dt[CASE])) if ds[CASE].get(key)!=dt[CASE].get(key)]
 return {'status':'PASS','scientific_approval':False,'case_count':len(dt),'proposal_count':len(pt),'evidence_count':len(et),'unchanged_other_case_count':187,'unchanged_other_proposal_count':73,'unchanged_original_evidence_count':852,'changed_case_fields':changed_fields,'original_case_object_sha256':canon(ds[CASE]),'successor_case_object_sha256':canon(dt[CASE]),'original_proposal_object_sha256':canon(ps[OLD]),'successor_proposal_object_sha256':canon(pt[NEW]),'new_evidence_ids':sorted(set(et)-set(es))}
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--original-root',type=Path,required=True);parser.add_argument('--successor-root',type=Path,required=True);parser.add_argument('--retirement',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
 paths=[args.original_root/(n+'.json') for n in ['decisions','proposals','evidence']]+[args.successor_root/(n+'.json') for n in ['decisions','proposals','evidence']]+[args.retirement]
 h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();inputs={str(p):h(p) for p in paths};result=check_objects(*[json.loads(p.read_text()) for p in paths]);result['input_hashes']=inputs;result['helper_sha256']=h(Path(__file__))
 np=json.loads(paths[4].read_text());proposal=next(p for p in np['proposals'] if p['proposal_id']==NEW);cap=proposal['after_capture'];require(cap['root']=='artifact','candidate artifact root incorrect');relative=Path(cap['path']);require(not relative.is_absolute() and '..' not in relative.parts,'unsafe candidate path');payload=args.original_root/relative;require(payload.is_file() and not payload.is_symlink(),'candidate capture unavailable');require(h(payload)==EXPECTED_PAYLOAD,'candidate exact bytes mismatch');result['payload_sha256']=h(payload)
 require(all(h(Path(p))==v for p,v in inputs.items()),'input changed during check');require(not args.output.exists(),'refuse output overwrite');args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','case_count','proposal_count','evidence_count','scientific_approval']}))
if __name__=='__main__':main()
