import json,pathlib,hashlib,subprocess,datetime,collections
O=pathlib.Path('.temp/w05-postseal-source-corrections-v1/final-assembly-review-v1/preservation-child');S=pathlib.Path('.temp/w05-postseal-source-corrections-v1');B=pathlib.Path('reports/all_unmatched_20261107/worker-05');P=B/'postseal-source-corrections-v1';OLD=B/'final-correction-v1';C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107');H='5156d92bec6bd885ca8bae3c5e18bfdce0069176';H43='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d';sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest();bsha=lambda b:hashlib.sha256(b).hexdigest();objsha=lambda x:bsha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode());bind=lambda p:{'path':str(p),'sha256':sha(p)};now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();errors=[];started=now()
def run(*args):return subprocess.run(args,check=True,capture_output=True).stdout
def save(name,obj):
 p=O/name;assert not p.exists();p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n');return bind(p)
def err(label,details):
 if details:errors.append({'check':label,'details':details})
head=run('git','rev-parse','HEAD').decode().strip();branch=run('git','branch','--show-current').decode().strip();ancestry=subprocess.run(['git','merge-base','--is-ancestor',H43,head],capture_output=True).returncode
# All tracked historical report and native-review blobs compared independently with actual current bytes.
def tree(rev):
 out=[]
 for item in run('git','ls-tree','-rz',rev,'--',str(B),'reviews/structured').split(b'\0'):
  if not item:continue
  desc,path=item.split(b'\t',1);mode,typ,oid=desc.decode().split();p=pathlib.Path(path.decode());bad=None
  if typ!='blob':continue
  if not p.is_file():bad='missing';size=None;sh=None;actual=None
  else:
   raw=p.read_bytes();size=len(raw);sh=bsha(raw);actual=hashlib.sha1(b'blob '+str(size).encode()+b'\0'+raw).hexdigest()
   if actual!=oid:bad='content_differs_from_git_blob'
  out.append({'path':str(p),'historical_git_blob':oid,'actual_git_blob':actual,'sha256':sh,'bytes':size,'error':bad})
 err('historical_tree_'+rev,[x for x in out if x['error']]);return out
oldtree=tree(H);originaltree=tree(H43);treebinding=save('historical-tree-readback-v1.json',{'method':'Git object SHA1 is recomputed as SHA1(blob + length + NUL + bytes); current SHA256 also retained. Exact-byte preservation, no semantic approval.','base5156':oldtree,'original43':originaltree})
# All members and complete private/public trees must be copies, including original metadata.
copychecks=[];timestamp_fields=[]
def walk_time(x,loc=''):
 if isinstance(x,dict):
  for k,v in x.items():
   l=loc+'/'+k
   if k in ['accessed_at','retrieved_at','retrieval_date','retrieval_timestamp','fetched_at','capture_time','requested_at','captured_at','downloaded_at'] and isinstance(v,(str,int,float)):yield l,v
   yield from walk_time(v,l)
 elif isinstance(x,list):
  for i,v in enumerate(x):yield from walk_time(v,loc+'/'+str(i))
for rel in ['materials/FINAL-MANIFEST.json','media/MANIFEST.json','chemicals/FINAL-MANIFEST-v1.json','review/FINAL-MANIFEST-v1.json','chemical-ledger-remediation-v1/FINAL-MANIFEST-v1.json']:
 m=S/rel;pub=P/rel;d=json.loads(m.read_text());ms=d.get('files',d.get('members'));lane=m.parent.relative_to(S);a={str(p.relative_to(m.parent)):p for p in m.parent.rglob('*') if p.is_file()};b={str(p.relative_to(pub.parent)):p for p in pub.parent.rglob('*') if p.is_file()};deltas=[];members=[]
 for x in ms:
  pp=m.parent/x['path'];qp=pub.parent/x['path'];ok=pp.is_file() and qp.is_file() and sha(pp)==x['sha256']==sha(qp);members.append({'path':x['path'],'sha256':x['sha256'],'exact_private_public_match':ok});
  if not ok:deltas.append({'member':x['path'],'error':'declared_digest_or_copy_mismatch'})
 for path in sorted(set(a)|set(b)):
  if path not in a or path not in b:deltas.append({'path':path,'error':'tree_membership_mismatch'});continue
  if sha(a[path])!=sha(b[path]):deltas.append({'path':path,'error':'copy_bytes_differ'})
  if a[path].suffix=='.json':
   try:j=json.loads(a[path].read_text())
   except Exception:continue
   for loc,v in walk_time(j):timestamp_fields.append({'private_path':str(a[path]),'public_path':str(b[path]),'json_pointer':loc,'original_value':v,'private_public_file_sha256':sha(a[path])})
 err('exact_copy_'+str(lane),deltas);copychecks.append({'lane':str(lane),'private_manifest':bind(m),'public_manifest':bind(pub),'manifest_members':len(ms),'complete_private_file_count':len(a),'complete_public_file_count':len(b),'manifest_identical':sha(m)==sha(pub),'members':members,'errors':deltas,'author_or_reviewer':d.get('author',d.get('reviewer'))})
copybinding=save('copied-packet-readback-v1.json',{'packets':copychecks,'capture_timestamp_bindings':timestamp_fields,'timestamp_qualification':'Fields are reported exactly as stored; equality proves preservation of historical acquisition metadata, not correctness of the original acquisition claim.'})
# The exact supplied issue captures are also preserved, no new fetching.
issuefiles=[]
for p in sorted((S/'issues').rglob('*')):
 if p.is_file():
  q=P/'issues'/p.relative_to(S/'issues');ok=q.is_file() and sha(p)==sha(q);issuefiles.append({'private':bind(p),'public':str(q),'identical':ok});err('issue_capture_copy',[] if ok else [str(q)])
# Case ownership denominator independently reconstructed from ten frozen shards.
shardrows=[];seen={};duplicates=[]
for p in sorted((C/'queue/preliminary-v5/shards').glob('shard-*.json')):
 d=json.loads(p.read_text());ids=[x['case_id'] for x in d['cases']];shardrows.append({'path':str(p),'sha256':sha(p),'worker_slot':d['worker_slot'],'case_count':len(ids),'case_ids':ids})
 for cid in ids:
  if cid in seen:duplicates.append(cid)
  seen[cid]=d['worker_slot']
err('source_case_unique_ownership',duplicates)
contract=B/'contracts/shard-05.json';frozen=C/'queue/preliminary-v5/shards/shard-05.json';assert sha(contract)==sha(frozen)=='457c957af21271b120190093dd311bf4044b82a3ad26b54e2fc5b52083dec1c4';sc=json.loads(contract.read_text())['cases'];source={x['case_id']:x for x in sc}
oldD=json.loads((OLD/'core/decisions.json').read_text())['decisions'];newD=json.loads((P/'core/decisions.json').read_text())['decisions'];od={x['case_id']:x for x in oldD};nd={x['case_id']:x for x in newD};err('case_set',[] if set(source)==set(od)==set(nd) else [{'frozen':len(source),'old':len(od),'new':len(nd)}]);casechecks=[];changed=[]
for cid,c in source.items():
 a=od[cid];b=nd[cid];checks={'case_input_sha256_unchanged':a['case_input_sha256']==b['case_input_sha256'],'source_object_unchanged':a['source']==b['source'],'raw_names_match_frozen':all(b['source'].get(k)==c[k] for k in ['source','source_case_id','source_label','raw_source_label']),'occurrences_unchanged':a['occurrence_ids']==b['occurrence_ids'],'frozen_occurrences_match':set(b['occurrence_ids'])=={x['occurrence_id'] for x in c.get('occurrences',[])},'preserved_source_holds_identical':a.get('preserved_source_holds')==b.get('preserved_source_holds')};bad=[k for k,v in checks.items() if not v];err('case_preservation_'+cid,bad)
 if a!=b:changed.append(cid)
 casechecks.append({'case_id':cid,'source_case_sha256':objsha(c),'old_decision_sha256':objsha(a),'new_decision_sha256':objsha(b),'raw_source_label':c['raw_source_label'],'source_case_id':c['source_case_id'],'source_owner_worker':seen[cid],'occurrence_ids':b['occurrence_ids'],'checks':checks,'preserved_source_holds':b.get('preserved_source_holds')})
casebinding=save('source-ownership-readback-v1.json',{'shards':shardrows,'total_unique_source_cases':len(seen),'duplicate_case_ids':duplicates,'w05_contract':bind(contract),'frozen_w05':bind(frozen),'decisions':casechecks,'changed_decision_ids':changed,'raw_occurrence_memberships':sum(len(x['occurrence_ids']) for x in newD)})
# Original18 findings are retained as identical objects/dispositions; new register extensions not conflated.
F0=json.loads((OLD/'finding-register.json').read_text());F1=json.loads((P/'finding-register.json').read_text());of=F0['original_findings'];nf=F1['original_findings'];assert len(of)==18;err('original_findings',[] if of==nf else ['original findings objects differ']);findings=[{'finding_id':x['finding_id'],'whole_original_registered_object_sha256':objsha(x),'native_status':x.get('native_status'),'final_disposition':x.get('final_disposition'),'identical':x==next(y for y in nf if y['finding_id']==x['finding_id'])} for x in of]
# Authenticate the138 original proposal objects from original43 git and link to current142 rows.
L0=json.loads((OLD/'core/proposal-lineage.json').read_text());L1=json.loads((P/'core/proposal-lineage.json').read_text());oldP=json.loads((OLD/'core/proposals.json').read_text())['proposals'];newP=json.loads((P/'core/proposals.json').read_text())['proposals'];op={x['proposal_id']:x for x in oldP};np={x['proposal_id']:x for x in newP};err('proposal_id_set',[] if set(op)==set(np) else ['old142 vs new set differs']);original= json.loads(run('git','show',H43+':'+str(B/'correction-1193-v1/proposals.json')).decode())
original=original['proposals'] if isinstance(original,dict) else original;org={x['proposal_id']:x for x in original};lineage=[]
for row in L1['rows']:
 pid=row['proposal_id'];pre=row.get('predecessor_proposal_id');p=np[pid];oldrow=next(x for x in L0['rows'] if x['proposal_id']==pid);corecapture=p['after_capture'];capturepath=B/corecapture['path'];ok=sha(capturepath)==corecapture['sha256'];err('proposal_capture_'+pid,[] if ok else ['actual payload differs']);checks={'original_predecessor_id_unchanged':pre==oldrow.get('predecessor_proposal_id'),'original_predecessor_hash_unchanged':row.get('predecessor_proposal_sha256')==oldrow.get('predecessor_proposal_sha256'),'original_before_unchanged':row.get('original_before_sha256')==oldrow.get('original_before_sha256'),'cases_unchanged':row.get('case_ids')==oldrow.get('case_ids')==p['case_ids'],'owner_path_unchanged':row['owner_path']==oldrow['owner_path']==p['owner_path'],'selected_capture_matches_core':row['successor_after_capture']==corecapture}
 if pre:
  checks['original_proposal_exists_at_43']=pre in org
  # Historical object digests are recomputed in the campaign canonical serialization below.
  og=org.get(pre);checks['original_after_capture_authentic']=og and og['after_capture']==row['predecessor_after_capture']
 err('lineage_'+pid,[k for k,v in checks.items() if not v]);lineage.append({'proposal_id':pid,'original_proposal_id':pre,'checks':checks,'selected_payload':bind(capturepath),'selected_capture':corecapture,'old_payload_sha256':op[pid]['after_capture']['sha256'],'current_payload_unchanged':op[pid]['after_capture']['sha256']==corecapture['sha256']})
claimed_originals=[r['original_proposal_id'] for r in lineage if r['original_proposal_id']];err('original138_lineage_coverage',[] if set(claimed_originals)==set(org) and len(claimed_originals)==len(org) else ['missing or duplicate original138lineage']);lineagebinding=save('proposal-and-finding-lineage-readback-v1.json',{'original43_proposal_count':len(org),'old_selected_proposal_count':len(op),'current_selected_proposal_count':len(np),'unique_original_ids_accounted':len(set(claimed_originals)),'lineage':lineage,'findings':findings,'old_finding_register':bind(OLD/'finding-register.json'),'current_finding_register':bind(P/'finding-register.json')})
# Original evidence objects retain exact timestamp, author and source fields; added rows are not replacements.
E0=json.loads((OLD/'core/evidence.json').read_text())['evidence'];E1=json.loads((P/'core/evidence.json').read_text())['evidence'];e1={x['evidence_id']:x for x in E1};evbad=[x['evidence_id'] for x in E0 if e1.get(x['evidence_id'])!=x];err('historical_evidence_objects',evbad)
# Original correction manifest and sealed22comparison continue unchanged.
p=B/'correction-1193-v1/MANIFEST.sha256';manlines=[]
for line in p.read_text().splitlines():
 if not line.strip():continue
 h,f=line.split('  ',1);q=p.parent/f;manlines.append({'path':str(q),'expected_sha256':h,'actual_sha256':sha(q)});err('original1857manifest',[] if sha(q)==h else [f])
q=pathlib.Path('.temp/final-preparation-comparison-v1/MANIFEST.json');mm=json.loads(q.read_text());cmp=[]
for x in mm['files']:
 f=q.parent/x['path'];actual=sha(f);cmp.append({'path':x['path'],'sha256':actual,'identical':actual==x['sha256']});err('sealed22comparison',[] if actual==x['sha256'] else [x['path']])
oldmanifestbinding=save('old-manifest-readback-v1.json',{'correction1193_manifest':bind(p),'original_git43_manifest_sha256':bsha(run('git','show',H43+':'+str(p))),'members':manlines,'comparison_manifest':bind(q),'comparison_members':cmp,'comparison_counts_as_sealed':mm['counts']})
# Maintained surfaces and controls remain untouched; public assembly additions excluded by authorized scope.
tracked_diff=run('git','diff','--name-only',H,'--').decode().splitlines();between=run('git','diff','--name-only',H43,H,'--').decode().splitlines();maintained_between=[x for x in between if not(x.startswith(str(B)+'/') or x.startswith('reviews/structured/'))];err('tracked_changes_since5156',tracked_diff);err('nonreport_changes_43_to5156',maintained_between)
# Actual author attribution in source ledger binds exact copied ledgers.
sl=json.loads((P/'source-ledger.json').read_text());authorchecks=[]
for row in sl['primary_scopes']:
 lane=row['lane'];expected={'materials':'/root/materials_research','media':'/root/media_research','chemicals':'/root/chemicals_research'}[lane];ds=json.loads((P/lane/'decisions.json').read_text());ps=json.loads((P/lane/'proposals.json').read_text());drows=ds['decisions'] if isinstance(ds,dict) else ds;prows=ps['proposals'] if isinstance(ps,dict) else ps;matches=[]
 for ref in row['selected_bindings']:matches.append({'path':ref['path'],'sha256':ref['sha256'],'matches':sha(P/ref['path'])==ref['sha256']})
 ok=row['primary_author']==expected and row['decisions']==len(drows) and row['payloads']==len(prows) and all(x['matches'] for x in matches);err('primary_source_attribution_'+lane,[] if ok else [row]);authorchecks.append({'lane':lane,'author':expected,'decision_count':len(drows),'proposal_count':len(prows),'exact_source_bindings':matches,'pass':ok})
receipt={'reviewer':'/root/final_skeptical/preservation_audit','scope':'Disjoint mechanical preservation and attribution only; no fresh chemistry or whole-owner/export approval. Root mutable control/README/native15target semantic review excluded.','started_at':started,'completed_at':now(),'base_head':head,'branch':branch,'original43_ancestor':ancestry==0,'checks':{'historical5156_blobs':len(oldtree),'historical43_blobs':len(originaltree),'copied_packet_counts':[{'lane':x['lane'],'members':x['manifest_members'],'all_files':x['complete_public_file_count']} for x in copychecks],'capture_timestamp_fields_preserved_by_exact_bytes':len(timestamp_fields),'issue_capture_copies':len(issuefiles),'all_campaign_source_cases':len(seen),'w05_cases':len(source),'w05_occurrence_memberships':sum(len(x['occurrence_ids']) for x in newD),'original_findings':len(of),'original_finding_objects_and_dispositions_unchanged':of==nf,'original_proposal_lineage':len(set(claimed_originals)),'selected_proposals':len(np),'changed_selected_payload_hashes':sum(not x['current_payload_unchanged'] for x in lineage),'unchanged_selected_payload_hashes':sum(x['current_payload_unchanged'] for x in lineage),'changed_decision_objects':len(changed),'old_evidence_objects_exactly_retained':len(E0)-len(evbad),'new_evidence_entries':len(E1),'correction_manifest_members':len(manlines),'sealed_comparison_members':len(cmp),'tracked_changes_since5156':tracked_diff,'nonreport_changes_between_original43_and5156':maintained_between},'primary_source_authorship':authorchecks,'issue_captures':issuefiles,'evidence_artifacts':[treebinding,copybinding,casebinding,lineagebinding,oldmanifestbinding],'inputs':[bind(P/'core'/f) for f in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json']]+[bind(P/'source-ledger.json'),bind(P/'finding-register.json')],'findings':errors,'status':'PASS' if not errors else 'FINDINGS_REQUIRE_REVIEW','not_approval':['No new scientific review; original scientific authors and reviewers remain credited by exact copied packets.','No final publication/owner/export acceptance.','The current README and newly appended control metadata are outside this child scope; parent owns semantic/native review.']};save('main-receipt.json',receipt);print(json.dumps({'status':receipt['status'],'checks':receipt['checks'],'errors':errors,'receipt_sha256':sha(O/'main-receipt.json'),'completed_at':receipt['completed_at']},indent=2))
