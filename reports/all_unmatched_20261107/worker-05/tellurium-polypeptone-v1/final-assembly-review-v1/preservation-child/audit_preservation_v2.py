import collections,datetime,hashlib,json,pathlib,subprocess,yaml
W=pathlib.Path.cwd();S=W/'.temp/w05-tellurium-polypeptone-v1';O=S/'final-assembly-review-v1/preservation-child';B=W/'reports/all_unmatched_20261107/worker-05';P=B/'tellurium-polypeptone-v1';N=B/'postseal-source-corrections-v1';BASE='76bca688b4f55e8bdf791079df8d4156cded6c4c';OLD='43f7cf6e8681fa617b5d6d3529d94d537ca01f0d'
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
j=lambda p:json.loads(pathlib.Path(p).read_text())
objsha=lambda d:hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
errors=[]
def check(ok,what):
 if not ok:errors.append(what)
 return ok
def bind(p):return {'path':str(pathlib.Path(p).relative_to(W)) if pathlib.Path(p).is_relative_to(W) else str(p),'sha256':sha(p)}
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
packets=[]
for rel,manifest in [('tellurium','FINAL-MANIFEST-v1.json'),('polypeptone','MANIFEST.json'),('review','FINAL-MANIFEST-v1.json')]:
 private=S/rel;public=P/rel;m=j(private/manifest);checks=[]
 for entry in m.get('files',m.get('members',[])):
  a=private/entry['path'];b=public/entry['path'];checks.append({'path':entry['path'],'private_sha256':sha(a),'public_sha256':sha(b),'manifest_sha256':entry['sha256'],'match':check(sha(a)==sha(b)==entry['sha256'],f'copy:{rel}/{entry["path"]}')})
 check(sha(private/manifest)==sha(public/manifest),f'manifestcopy:{rel}')
 packets.append({'lane':rel,'private_manifest':bind(private/manifest),'public_manifest':bind(public/manifest),'members_checked':len(checks),'author_or_reviewer':m.get('author',m.get('reviewer')),'original_timestamp':m.get('created_at',m.get('sealed_at',m.get('completed_at'))),'members':checks})
oldman=[]
for mp in [N/'MANIFEST.json',B/'final-correction-v1/MANIFEST.json',W/'.temp/final-preparation-comparison-v1/MANIFEST.json']:
 m=j(mp);checks=[]
 for x in m.get('files',m.get('members',[])):
  p=mp.parent/x['path'];check(sha(p)==x['sha256'],'oldmanifest:'+str(p));checks.append({'path':x['path'],'sha256':sha(p)})
 for x in m.get('native_review',[]):check(sha(W/x['path'])==x['sha256'],'oldnative:'+x['path'])
 oldman.append({'manifest':bind(mp),'members':len(checks),'native_pairs_members':m.get('native_review',[]),'all_member_hashes_match':True})
mp=B/'correction-1193-v1/MANIFEST.sha256';lines=mp.read_text().splitlines();correct=[]
for line in lines:
 if not line.strip():continue
 h,name=line.split(maxsplit=1);name=name.lstrip('*');p=mp.parent/name
 if not p.exists():p=W/name
 check(p.exists() and sha(p)==h,'oldsha256manifest:'+name);correct.append(name)
oldman.append({'manifest':bind(mp),'members':len(correct),'all_member_hashes_match':not any(x.startswith('oldsha256manifest:') for x in errors)})
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();branch=subprocess.check_output(['git','branch','--show-current'],text=True).strip();check(head==BASE,'head advanced from base during audit')
gitchecks=[]
for base in [BASE,OLD]:
 check(subprocess.run(['git','merge-base','--is-ancestor',base,'HEAD'],capture_output=True).returncode==0,'sourcehead-not-ancestor:'+base)
 raw=subprocess.check_output(['git','ls-tree','-r','-z',base,'--','reports/all_unmatched_20261107/worker-05','reviews/structured','data','mappings','src','conf','scripts','MAPPING_SEMANTICS.md','justfile','.claude/skills','docs/record-reviews.md','docs/record-review-profile.md'])
 count=0;bad=[];byroot=collections.Counter()
 for row in raw.split(b'\0'):
  if not row:continue
  left,name=row.split(b'\t',1);mode,typ,blob=left.split();p=W/name.decode();count+=1;byroot[name.decode().split('/')[0]]+=1
  if not p.is_file():bad.append(name.decode());continue
  data=p.read_bytes();actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
  if actual!=blob.decode():bad.append(name.decode())
 check(not bad,'git-preserved-blobs:'+base+':'+','.join(bad));gitchecks.append({'source_head':base,'tracked_blobs_checked':count,'roots':dict(byroot),'changed_or_missing':bad})
changed=subprocess.check_output(['git','diff','--name-only',BASE],text=True).splitlines();check(not changed,'tracked-diff-from-base:'+str(changed))
frozen=j(B/'contracts/frozen-baseline.json');ownership={};shards=[]
for worker,entry in frozen['queue']['shards'].items():
 p=pathlib.Path(entry['path']);check(sha(p)==entry['sha256'],'shard-hash:'+worker);data=j(p)
 for c in data['cases']:
  check(c['case_id'] not in ownership,'duplicate-campaign-case:'+c['case_id']);ownership[c['case_id']]=worker
 shards.append({'worker':worker,'path':str(p),'sha256':sha(p),'cases':len(data['cases'])})
f5=j(B/'contracts/shard-05.json');check(sha(B/'contracts/shard-05.json')==frozen['queue']['shards']['5']['sha256'],'private shard05 differs')
Ds=j(P/'core/decisions.json')['decisions'];oldDs=j(N/'core/decisions.json')['decisions'];dm={x['case_id']:x for x in Ds};om={x['case_id']:x for x in oldDs};casechecks=[]
check(set(dm)==set(om)=={x['case_id'] for x in f5['cases']},'W05-case-sets')
def holdnodes(x,p=''):
 out={}
 if isinstance(x,dict):
  for k,v in x.items():
   if 'hold' in k.lower():out[p+'/'+k]=v
   out.update(holdnodes(v,p+'/'+k))
 elif isinstance(x,list):
  for i,v in enumerate(x):out.update(holdnodes(v,p+'/'+str(i)))
 return out
for c in f5['cases']:
 a=om[c['case_id']];b=dm[c['case_id']];h=holdnodes(a);nh=holdnodes(b);checks={k:a.get(k)==b.get(k) for k in ['case_id','case_input_sha256','source','occurrence_ids','preserved_source_holds','preserved_downstream_holds']};checks['all_nested_old_hold_nodes_preserved']=all(k in nh and v==nh[k] for k,v in h.items());checks['frozen_occurrence_ids_exact']=b['occurrence_ids']==[x['occurrence_id'] for x in c.get('occurrences',[])];checks['campaign_worker05']=ownership[c['case_id']]=='5';checks['raw_frozen_source_fields']=all(b['source'].get(k)==c.get(k) for k in ['source','source_case_id','source_label','raw_source_label']);check(all(checks.values()),'caseboundary:'+c['case_id']);casechecks.append({'case_id':c['case_id'],'case_index':b.get('case_index'),'unchanged_complete_decision':a==b,'old_object_sha256':objsha(a),'new_object_sha256':objsha(b),'hold_node_count':len(h),'checks':checks})
props=j(P/'core/proposals.json')['proposals'];prev=j(N/'core/proposals.json')['proposals'];pm={x['proposal_id']:x for x in props};pr={x['proposal_id']:x for x in prev};check(set(pm)==set(pr),'current-proposal-set');payloads=[]
for pid,p in pm.items():
 cap=p['after_capture'];oc=pr[pid]['after_capture'];a=B/oc['path'];b=B/cap['path'];check(sha(a)==oc['sha256'] and sha(b)==cap['sha256'],'payloadhash:'+pid);payloads.append({'proposal_id':pid,'old_capture':oc,'new_capture':cap,'payload_byte_identical':a.read_bytes()==b.read_bytes(),'proposal_object_identical':p==pr[pid]})
Es=j(P/'core/evidence.json')['evidence'];oldEs=j(N/'core/evidence.json')['evidence'];em={x['evidence_id']:x for x in Es};check(len(em)==len(Es),'duplicate-evidence-id');retained=[]
for e in oldEs:
 check(em.get(e['evidence_id'])==e,'old-evidence:'+e['evidence_id']);retained.append({'evidence_id':e['evidence_id'],'canonical_object_sha256':objsha(e),'exact_retained':em.get(e['evidence_id'])==e})
orig=j(B/'correction-1193-v1/proposals.json')['proposals'];origmap={x['proposal_id']:x for x in orig};lineage=j(P/'core/proposal-lineage.json')['rows'];origrows=[x for x in lineage if x.get('predecessor_proposal_id')];check(collections.Counter(x['predecessor_proposal_id'] for x in origrows)==collections.Counter(origmap.keys()),'original-lineage-1to1');linchecks=[]
for lin in origrows:
 oldp=origmap[lin['predecessor_proposal_id']];newp=pm[lin['proposal_id']];a=B/oldp['after_capture']['path'];b=B/newp['after_capture']['path'];av=yaml.safe_load(a.read_text());bv=yaml.safe_load(b.read_text());ah=av.get('curation_history',[]);neg=[x for x in av.get('synonyms',[]) if x.get('synonym_type')=='REJECTED_LABEL'];fields=[k for k in set(av)|set(bv) if 'occurrence' in k or k.endswith('roles') or k=='causal_graphs'];checks={'predecessor_object_hash':lin['predecessor_proposal_sha256']==objsha(oldp),'original_capture_exact':lin['predecessor_after_capture']==oldp['after_capture'],'successor_capture_exact':lin['successor_after_capture']==newp['after_capture'],'history_prefix_preserved':bv.get('curation_history',[])[:len(ah)]==ah,'negatives_preserved':all(x in bv.get('synonyms',[]) for x in neg),'scope_fields_preserved':all(av.get(k)==bv.get(k) for k in fields)};check(all(checks.values()),'lineage:'+lin['proposal_id']);linchecks.append({'original_proposal_id':oldp['proposal_id'],'selected_proposal_id':newp['proposal_id'],'checks':checks})
preserve=j(S/'control/preservation-start.json');contracts=[]
for r in preserve['contracts']:check(sha(W/r['path'])==r['sha256'],'contract:'+r['path']);contracts.append(r)
inv=j(W/'.temp/w05-final-correction-v1/control/maintained-baseline-preservation-start.json');actual={str(p.relative_to(W)) for p in (W/'data/ingredients').rglob('*.yaml')};check(actual=={x['path'] for x in inv['records']},'maintained-record-set')
for r in inv['records']:check(sha(W/r['path'])==r['sha256'],'maintained-record:'+r['path'])
for r in j(S/'control/protected-private-handoffs.json'):check(sha(W/r['path'])==r['sha256'],'private-handoff:'+r['path'])
out={'reviewer':'/root/final_skeptical/preservation_audit','started_at':started,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Mechanical preservation and authorship/source attribution only; no chemistry or final native/owner approval.','head':head,'branch':branch,'status':'PASS' if not errors else 'FAIL','errors':errors,'new_public_private_packets':packets,'historical_manifests':oldman,'historical_git_blob_checks':gitchecks,'tracked_changes_from_base':changed,'campaign_shards':shards,'campaign_case_count':len(ownership),'W05_decision_count':len(Ds),'occurrence_memberships':sum(len(x['occurrence_ids']) for x in Ds),'case_checks':casechecks,'unchanged_decisions':sum(x['unchanged_complete_decision'] for x in casechecks),'payload_count':len(payloads),'unchanged_payloads':sum(x['payload_byte_identical'] for x in payloads),'payload_bindings':payloads,'old_evidence_retained':len(retained),'current_evidence_count':len(Es),'evidence_bindings':retained,'original_lineage_count':len(linchecks),'lineage_checks':linchecks,'maintained_records_checked':len(actual),'contracts':contracts,'stable_inputs':[bind(P/'core'/n) for n in ['decisions.json','proposals.json','evidence.json','proposal-lineage.json','assembly-receipt.json']],'mutable_assembly_metadata_excluded':'README, final root controls/validation receipts and new native review pair are parent-owned and may be copied after this read; final root preservation inventory will receive a separately bound readback.','includes_ignored_files':True}
path=O/'preservation-readback-v2.json';assert not path.exists();path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps({k:out[k] for k in ['status','errors','campaign_case_count','W05_decision_count','occurrence_memberships','unchanged_decisions','payload_count','unchanged_payloads','old_evidence_retained','current_evidence_count','original_lineage_count','maintained_records_checked']},indent=2))
