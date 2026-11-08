"""Companion two-field attribution clarification; no payload or chemical change."""
from copy import deepcopy
from datetime import datetime,timezone
import json
from pathlib import Path
import build_successor_v2 as b
R=b.R;S=R/'selected-v2';OUT=R/'review-input-v2'
CID98='CM_NAME:b2842dee958925abda8f2e56af9eb9a5fd009b8306848c04ae6782597864506c'
TOGO_SHA='5cf01f0691361181fa733c2163aaed917feabce24da5c2fec876e5616ed83950'
NIES_SHA='02b520ffc3870143c8a3fa695dc717c536930131a527aa7770c53207b6039101'
COMMENT_SHA='99f4077aba620279276df0a1b6f1a013469bb094ae7556ea533a14f83fbf8be2'
OLD_REASON='Original NIES source marks manganese sulfate pentahydrate with footnote1). Its substitution note distinguishes250mgheptahydrate from217mgpentahydrate. Existing CHEBI131524 is the five-water substance; the marker is not part of a resolving chemical name.'
NEW_REASON='The successfully inspected TOGO M2509 capture reports the NIES table/footnote marking manganese sulfate pentahydrate with footnote1). Its reported NIES substitution note distinguishes250mgheptahydrate from217mgpentahydrate. Existing CHEBI131524 is the five-water substance; the marker is not part of a resolving chemical name. The direct NIES capture remains an unsuccessful formulation lookup.'
# Raw held input hashes are supplied by the immutable local intake receipt below.
PIN_FILE=R/'context/case98-companion-input-pins.json'
PIN_FILE_SHA='7b1b888aec076585bc52fa344fcdb22962aa71f223d84c226c9192fd51a2c3da'
def validate_pin_receipt(raw):
 b.require_pin(raw,PIN_FILE_SHA)
 return json.loads(raw)
def clarify(old):
 if old['case_id']!=CID98 or len(old['occurrence_ids'])!=1 or old['reasoning']!=OLD_REASON or old['applicability'].count(OLD_REASON)!=1 or old['proposal_ids']!=[]:raise ValueError('Wrong exact case98 preimage')
 new=deepcopy(old);new['reasoning']=NEW_REASON;new['applicability']=old['applicability'].replace(OLD_REASON,NEW_REASON);new['independent_review']={'status':'pending','evidence_ids':[]};return new
def validate_delta(before,after):
 if after!=clarify(before):raise ValueError('Unrequested case98 chemical/source/outcome/hold change')
def main():
 out=b.require_output(OUT);pins=b.FrozenFile.capture(PIN_FILE);pin_values=validate_pin_receipt(pins.content);held=[b.FrozenFile.capture(S/(n+'.json')) for n in ['decisions','proposals','evidence']]
 for n,f in zip(['decisions','proposals','evidence'],held,strict=True):b.require_pin(f.content,pin_values[n])
 held.append(pins);ds,ps,es=[json.loads(f.content) for f in held[:3]];old=deepcopy(ds)
 if len(ds['decisions'])!=188 or len(ps['proposals'])!=117 or len(es['evidence'])!=1827:raise ValueError('Wrong complete predecessor')
 cf=b.FrozenFile.capture(R/'context/issue1241-comment6719707702.json');b.require_pin(cf.content,COMMENT_SHA);comment=json.loads(cf.content);held.append(cf)
 if comment['id']!=6719707702 or CID98 not in comment['body']:raise ValueError('Wrong filed prerequisite')
 for p,h in [(b.A/'b/captures/retry-togo-M2509.json',TOGO_SHA),(b.A/'b/captures/source-c533a17a8ded25f29384.bin',NIES_SHA)]:
  f=b.FrozenFile.capture(p);b.require_pin(f.content,h);held.append(f)
 for p in ps['proposals']:
  f=b.FrozenFile.capture(b.A/p['after_capture']['path']);b.require_pin(f.content,p['after_capture']['sha256']);held.append(f)
 ds['decisions'][98]=clarify(ds['decisions'][98]);ds['decisions'][58]=b.pending_case(ds['decisions'][58]);validate_delta(old['decisions'][98],ds['decisions'][98])
 for i,(a,z) in enumerate(zip(old['decisions'],ds['decisions'],strict=True)):
  if i not in [58,98] and a!=z:raise ValueError('Unassigned case changed')
  if i==58 and z!=b.pending_case(a):raise ValueError('Case58 science changed')
 raw_old=b.raw_array_objects(held[0].content,'decisions');raw_new=b.raw_array_objects(b.encode(ds),'decisions');assert all(a==z for i,(a,z) in enumerate(zip(raw_old,raw_new,strict=True)) if i not in [58,98])
 receipt={'created_at':datetime.now(timezone.utc).isoformat(),'author':'worker02 /root','parent_head':b.HEAD,'finding_id':'W01-W02-SCI-001','filed_comment':comment['html_url'],'case_id':CID98,'case_index':98,'case_input_sha256':ds['decisions'][98]['case_input_sha256'],'before_case_canonical_sha256':b.digest(old['decisions'][98]),'after_case_canonical_sha256':b.digest(ds['decisions'][98]),'actual_fields_changed':['reasoning','applicability','independent_review'],'scientific_outcome_changes':False,'source_layer_only':True,'occurrence_count':1,'old_reasoning':OLD_REASON,'new_reasoning':NEW_REASON,'all_other_case98_fields_unchanged':True,'case58_only_pending_review_metadata':True,'unchanged_other_complete_case_objects':186,'all117proposal_objects_and_payload_bytes_unchanged':True,'proposal_ledger_sha256':b.sha(S/'proposals.json'),'cases':188,'occurrences':322,'proposals':117,'payload_changes_relative_f0':'Only the original seven category/history corrections; no additional payload change.','source_bindings':[{'path':str((b.A/'b/captures/retry-togo-M2509.json').relative_to(b.W)),'sha256':TOGO_SHA,'scope':'Successful TOGO provider capture reporting NIES table/footnote; original primary retrieval timestamp retained.'},{'path':str((b.A/'b/captures/source-c533a17a8ded25f29384.bin').relative_to(b.W)),'sha256':NIES_SHA,'scope':'Unsuccessful direct NIES formulation lookup retained; no fresh retrieval implied.'}],'queued_prompt':{'path':str((R/'context/queued-case98-prompt.txt').relative_to(b.W)),'sha256':b.sha(R/'context/queued-case98-prompt.txt'),'covered_by_this_active_successor':True,'separate_publication_required':False},'limits':'Report attribution only, no new source case, chemistry reassessment, ingredient/alias/history/quantity/owner/export change. Existing evidence1827objects remain unchanged prefix.'}
 rp=out/'case98-preservation-receipt.json';rr=b.encode(receipt)
 es['evidence'].extend([{'evidence_id':'w02-case98-filed-comment6719707702','kind':'source_snapshot','capture':{'root':'artifact','path':str(cf.path.relative_to(b.A)),'sha256':COMMENT_SHA},'url':None,'locator':'Exact filed minor advisory source-attribution scope; actual read receipt in context','supports_or_contradicts':'Administrative scope, not a new formulation source or chemical reassessment.'},{'evidence_id':'w02-case98-attribution-preservation-v1','kind':'local_validation','capture':{'root':'artifact','path':str(rp.relative_to(b.A)),'sha256':__import__('hashlib').sha256(rr).hexdigest()},'url':None,'locator':'Exact case98 two prose fields and review metadata; same117payloads and complete188case scope','supports_or_contradicts':'Chemical outcome, one occurrence, raw evidence/limitations and all holds unchanged; old queued prompt covered in this same successor.'}])
 assert b.raw_array_objects(b.encode(es),'evidence')[:1827]==b.raw_array_objects(held[2].content,'evidence')
 def verify():
  for f in held:f.verify()
 out.mkdir();b.publish_new_files([(out/'decisions.json',b.encode(ds)),(out/'proposals.json',held[1].content),(out/'evidence.json',b.encode(es)),(rp,rr)],verify);verify()
 print(json.dumps({'cases':188,'proposals':117,'case98_occurrences':1,'case58_occurrences':24,'additional_payload_changes':0,'evidence':1829}))
if __name__=='__main__':main()
