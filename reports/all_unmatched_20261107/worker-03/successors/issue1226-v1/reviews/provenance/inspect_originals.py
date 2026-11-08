"""Independent read-only provenance reconstruction, not identity adjudication."""
from pathlib import Path
import json,hashlib,subprocess,datetime,collections,yaml
R=Path.cwd();C=R.parents[2];A=R/'.temp/w03-provenance-successor-v1/review';Q=C/'preflight/w03-current-provenance-allowlist-v1';P=R/'reports/all_unmatched_20261107/worker-03';S=P/'successors/issue1224-v1/publication-v1';HEAD='f6bfbf3c185f705484aa106405f813209146c766';BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def read(p):return json.loads(p.read_bytes())
def out(n,x):
 with (A/n).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def git(*args):return subprocess.check_output(['git',*args])
def blob(path):return git('show',HEAD+':'+str(path.relative_to(R)))
assert git('rev-parse','HEAD').decode().strip()==HEAD
allow=read(Q/'repair-allowlist.json');manifest=read(Q/'MANIFEST.json');errors=[]
for x in manifest['files']:
 if sha((Q/x['path']).read_bytes())!=x['sha256']:errors.append(x['path'])
assert len(manifest['files'])==122 and not errors
core={n:read(S/(n+'.json'))[n] for n in ['decisions','proposals','evidence']}
for n in core:assert blob(S/(n+'.json'))==(S/(n+'.json')).read_bytes()==(Q/('current-'+n+'.json')).read_bytes()
assert [len(core[n]) for n in ['decisions','proposals','evidence']]==[188,74,863]
proposals={p['proposal_id']:p for p in core['proposals']};decisions={d['case_id']:d for d in core['decisions']};allowrows={x['proposal_id']:x for x in allow['rows']};assert len(allowrows)==49
reconstructed=[];allowproof=[];exclusions=[];all_inputs={}
for p in core['proposals']:
 path=P/p['after_capture']['path'];b=path.read_bytes();assert b==blob(path) and sha(b)==p['after_capture']['sha256'];cur=yaml.safe_load(b);all_inputs[str(path)]=sha(b)
 before=None;bb=None
 if p['kind']=='edit_existing_owner':
  bb=git('show',BASE+':'+p['owner_path']);assert sha(bb)==p['before_sha256'];assert (R/p['owner_path']).read_bytes()==bb;before=yaml.safe_load(bb)
 else:assert p['before_sha256'] is None and not (R/p['owner_path']).exists()
 ev=cur.get('ontology_mapping',{}).get('evidence',[]);bev=(before or {}).get('ontology_mapping',{}).get('evidence',[]);remaining=collections.Counter(canon(x) for x in bev);added=[];inherited=[]
 for i,x in enumerate(ev):
  key=canon(x)
  if remaining[key]>0:remaining[key]-=1;inherited.append(i)
  else:added.append(i)
 manuals=[i for i,x in enumerate(ev) if x.get('evidence_type')=='MANUAL_CURATION'];newmanual=[i for i in manuals if i in added]
 reconstructed.append({'proposal_id':p['proposal_id'],'kind':p['kind'],'payload_sha256':sha(b),'before_sha256':sha(bb) if bb else None,'mapping_evidence_count':len(ev),'added_mapping_indices':added,'inherited_mapping_indices':inherited,'manual_indices':manuals,'new_manual_indices':newmanual})
 if p['proposal_id'] in allowrows:
  a=allowrows[p['proposal_id']];assert newmanual==[0];assert a['current_published_head']==HEAD;assert a['proposal_kind']==p['kind'];assert a['owner_path']==p['owner_path'];assert a['case_ids']==p['case_ids'];assert a['published_payload_path']==str(path.relative_to(R));assert sha((Q/a['payload']['path']).read_bytes())==sha(b)==a['payload']['sha256'];assert a['field']=='ontology_mapping.evidence[0].evidence_type';assert a['change']=={'from':'MANUAL_CURATION','to':'LLM_SUGGESTION'}
  parent={k:v for k,v in cur['ontology_mapping'].items() if k!='evidence'};bparent={k:v for k,v in (before or {}).get('ontology_mapping',{}).items() if k!='evidence'}
  assert parent==a['parent_context'] and sha(canon(parent))==a['parent_context_sha256'];assert bparent==a['before_parent_context'];assert ev[0]==a['complete_mapping_evidence_object'] and sha(canon(ev[0]))==a['complete_object_canonical_sha256'];assert cur['identifier']==a['current_identifier'];assert cur['mapping_status']==a['current_mapping_status'];assert sha(canon(cur.get('curation_history',[])))==a['history_prefix_sha256']
  hist=cur.get('curation_history',[]);oldhist=(before or {}).get('curation_history',[]);assert hist[:len(oldhist)]==oldhist
  ae=a['author_evidence']['added_curation_history'];assert ae and all(x in hist[len(oldhist):] for x in ae);assert all(x.get('llm_assisted') is True for x in ae)
  if bb:
   assert a['authentic_before_path']==p['owner_path'] and a['authentic_before']['sha256']==sha(bb);assert (Q/a['authentic_before']['path']).read_bytes()==bb
  else:assert a['authentic_before'] is None and a['authentic_before_path'] is None
  for cid in p['case_ids']:assert a['case_input_sha256'][cid]==decisions[cid]['case_input_sha256']
  refs=[]
  for ref in a['author_evidence']['linked_review_reports']:
   rp=Path(ref['path']);assert sha(rp.read_bytes())==ref['sha256'];j=read(rp);refs.append({'path':str(rp),'sha256':ref['sha256'],'actual_reviewer':j.get('reviewer'),'declared_authorship_scope':ref.get('authorship_scope_metadata')});all_inputs[str(rp)]=ref['sha256']
  original=Q/a['original_full_provenance_row']['path'];assert sha(original.read_bytes())==a['original_full_provenance_row']['sha256'];full=read(original);assert full['full_value']==ev[0] and full['suggested_native_type']=='LLM_SUGGESTION';assert not full['baseline_full_value_match_indices']
  allowproof.append({'proposal_id':p['proposal_id'],'audit_row_id':a['audit_row_id'],'payload_sha256':sha(b),'before_sha256':sha(bb) if bb else None,'complete_object':ev[0],'object_sha256':sha(canon(ev[0])),'parent':parent,'parent_sha256':sha(canon(parent)),'history_prefix_sha256':sha(canon(hist)),'actual_added_agent_events':ae,'actual_linked_review_receipts':refs,'original_case_review_metadata':[{'case_id':cid,'independent_review':decisions[cid]['independent_review']} for cid in p['case_ids']],'assessment':'The complete assertion is a source-bound interpretation or identity/formulation selection added by documented agent authors, not a human-supplied MappingEvidence object. URL presence does not establish human authorship. LLM_SUGGESTION accurately types the new assertion without altering its meaning; scientific truth is not reassessed.'})
 else:assert not newmanual,p['proposal_id']
 for i in set(manuals)&set(inherited):exclusions.append({'proposal_id':p['proposal_id'],'index':i,'full_object':ev[i],'object_sha256':sha(canon(ev[i])),'payload_sha256':sha(b),'authentic_before_sha256':sha(bb)})
assert {(x['proposal_id'],x['index']) for x in exclusions}=={('b-proposal-marine-aliases',0),('c-copper-trihydrate-alias',4),('m-arabinan_source_alias',2)}
ox=proposals['w03-oxoid-cm0149-product-1224-v1'];oxrec=yaml.safe_load((P/ox['after_capture']['path']).read_bytes());assert ox['after_capture']['sha256']=='1ec7554da19d5a6ab2259ee79d178a95511a923e611f4fc176af498248ab76ae';assert [x['evidence_type'] for x in oxrec['ontology_mapping']['evidence']]==['LLM_SUGGESTION','LLM_SUGGESTION'];assert 'b-proposal-cm0149-form' not in proposals
out('original-provenance-reconstruction.json',{'reviewer':'/root/provenance_review','at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':HEAD,'manifest_members':122,'manifest_errors':errors,'current_counts':{n:len(core[n]) for n in core},'all74':reconstructed,'allowlisted49':allowproof,'inherited_exclusions':exclusions,'new_oxoid_excluded':ox['after_capture'],'retired_mixed_rcm_active':False,'scope':'Metadata provenance only; original science/roles/exports not reapproved.','input_hashes':all_inputs,'status':'PASS_CURRENT_BINDING_AND_PROVENANCE_SCOPE'})
print(json.dumps({'all74':len(reconstructed),'allowlisted49':len(allowproof),'inherited':len(exclusions),'new_manual':sum(len(x['new_manual_indices']) for x in reconstructed),'kinds':dict(collections.Counter(allowrows[x['proposal_id']]['proposal_kind'] for x in allowproof)),'head':HEAD,'status':'PASS'}))
