import pathlib,json,hashlib,datetime,subprocess,copy
O=pathlib.Path(__file__).parent
C=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
PUB='final-correction-v1/media/'
def load(p):return json.loads(pathlib.Path(p).read_text())
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def put(n,v):
 p=O/n
 if p.exists():raise RuntimeError('Refusing overwrite: '+str(p))
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n');return {'path':PUB+n,'sha256':sha(p)}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
P=load(O/'proposals.json')['proposals'];D=load(O/'decisions.json')['decisions'];E=load(O/'evidence.json')['evidence'];pp={p['proposal_id']:p for p in P}
original=load(O/'predecessor-payloads.json');op={x['proposal']['proposal_id']:x for x in original};ee={e['evidence_id']:e for e in E}
issues=O.parent/'issues';index={x['name']:x for x in load(issues/'capture-index.json')}
receipt=[]
for name in ['issue-1193','comments-1193','issue-1208','comments-1208','issue-1226','comments-1226']:
 path=issues/(name+'.json');assert sha(path)==index[name]['sha256']
 dest=O/'captures'/path.name;dest.parent.mkdir(exist_ok=True);assert not dest.exists();dest.write_bytes(path.read_bytes())
 receipt.append({**index[name],'capture':{'root':'artifact','path':PUB+'captures/'+path.name,'sha256':sha(dest)},'reuse_only':True})
for name in ['latest-issues-30-v1.json','latest-issues-30-v1-receipt.json']:
 path=issues/name;dest=O/'captures'/name;assert not dest.exists();dest.write_bytes(path.read_bytes());receipt.append({'name':name,'source_path':str(path.resolve()),'capture':{'root':'artifact','path':PUB+'captures/'+name,'sha256':sha(dest)},'reuse_only':True})
put('issue-capture-reuse.json',{'assembled_at':now,'records':receipt,'policy':'Original response bytes and acquisition metadata are reused exactly; assembly time is not a new source access time.'})

reviewroot=C/'workers/w08/worktree/.temp/w05-published-head-independent-review-v1'
paths=[C/'preflight/w05-final-issue-plan-v1/AUTHOR-TASK.md',C/'preflight/w05-final-issue-plan-v1/TRIAGE.json',reviewroot/'media/HANDOFF.md',reviewroot/'media/review.json',reviewroot/'media/findings.json',reviewroot/'media/source-read-ledger.json',reviewroot/'media/capture-coverage-addendum-HANDOFF-v1.md']
prior=[]
for p in paths:
 assert p.exists(),p
 prior.append({'path':str(p),'sha256':sha(p),'role':'task authority' if 'preflight/w05-final' in str(p) else 'historical independent worker08 review; not successor approval'})
put('authority-and-review-bindings.json',{'author':'/root/media_research','read_at':now,'inputs':prior,'typing_audit':load(O/'typing-audit-suggestions.json')['source'],'typing_ledger':load(O/'typing-audit-suggestions.json')['provenance_ledger'],'current_successor_skeptic':'Pending separately authored exact-byte review.'})

def pbind(pid):
 p=pp[pid];return {'proposal_id':pid,'owner_path':p['owner_path'],'before_sha256':p.get('before_sha256'),'predecessor_after':op[pid]['proposal']['after_capture'],'successor_after':p['after_capture']}
findings=[
 {'finding_id':'W05-MEDIA-F01','status':'corrected_in_isolated_successor_pending_independent_review','filed_before_correction':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1208#issuecomment-6718700948','case_indices':[17,136],'payloads':[pbind('M1193-P-MARINE2216')],'evidence_refs':['M1193-DIRECT-15'],'source_locator':'Manufacturer manual printed pages351-352, separately headed agar and broth formula tables.','correction':'Replace the active assertion that agar and broth differ only by gelling agent. Preserve the complete former human assertion verbatim in withdrawal history and payload ancestry, every preexisting history event and the already corrected sixteen commercial-broth components. New correction is agent-authored LLM_SUGGESTION.','limitations':['Commercial broth is not the ATCC agar-minus-agar scratch recipe.','Worker03 same-owner alias proposal still requires coordinator reconciliation against original before bytes.','No whole-owner, role or release approval is transferred.']},
 {'finding_id':'W05-MEDIA-F02','status':'corrected_in_isolated_successor_pending_independent_review','filed_before_correction':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6718699859','case_indices':[131],'payloads':[pbind('M1193-P-LEPTOSPIRA_MEDIUM_BASE_EMJH')],'evidence_refs':['M1193-DIRECT-7','M1193-WEB-web-more-2-131'],'source_locator':'Manufacturer printed page301, approximate basal formula per litre and adjustment/supplementation footnote; page302,2.3 g in900 ml followed by separate100 ml enrichment.','calculation':{'listed_g_per_l':1+0.3+1+0.25+0.005,'direction_g_divided_by_l':2.3/0.9,'conclusion':'Agreement at the precision of the rounded directions; no contradictory basis.'},'correction':'Add all five manufacturer approximate basal amounts with explicit G_PER_L_AT_STANDARD_BASAL_RECONSTITUTION or MG_PER_L_AT_STANDARD_BASAL_RECONSTITUTION units. Mark completeness only relative to that five-part cited table. Replace active false-deferral text; the predecessor assertion and historical event remain preserved.','limitations':['No powder concentration or final enriched-medium concentration.','No phosphate hydrate, thiamine salt, molecular grounding or exact lot composition inferred.','The manufacturer may adjust or supplement to meet performance criteria.','Enrichment, reconstitution water and receiving medium remain outside the dry base.']},
 {'finding_id':'W05-MEDIA-F03','status':'corrected_in_isolated_successor_pending_independent_review','filed_before_correction':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6718699859','case_indices':[181],'payloads':[pbind('M1193-P-FOLLOWON-MODIFIED_COOKED_MEAT_MEDIUM'),pbind('M1193-P-FOLLOWON-FASTIDIOUS_ANAEROBE_BROTH_WITH_MEAT_GRANULES')],'evidence_refs':['M1193-FOLLOWON-153','M1193-FOLLOWON-150','M1193-FOLLOWON-151','M1193-FOLLOWON-152','M1193-FOLLOWON-154','M1193-FOLLOWON-155'],'mismatched_capture':ee['M1193-FOLLOWON-153'],'correction':'Reclassify the exact unrelated EPA environmental-noise PDF as unsuccessful_search/mismatched retrieval and remove its ID from all active positive decision/proposal evidence links. Preserve original bytes, timestamp, URL, hash and prior faulty metadata in ancestry. Both dependent cooked-meat payloads remain byte-identical because the independently justified withdrawal of unsupported FoodOn grounding survives.','limitations':['No USDA1998 or chapter14 content was obtained from this URL.','FoodOn skeletal cooked-meat definition and commercial mixture comparisons do not establish a historical ingredient product.','Literal dependent cooked-meat parts remain named UNMAPPED; no automatic Oxoid or EXTERNAL_TERM substitution.']}
]
put('finding-dispositions.json',{'author':'Codex GPT-6 /root/media_research','at':now,'findings':findings,'typing_issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226','typing_receipt':{'path':PUB+'mapping-evidence-typing.json','sha256':sha(O/'mapping-evidence-typing.json')},'additional_unfiled_scientific_fixes':[],'historical_fields':'The retained correction_reassessment fields in decisions and the complete predecessor capture-index entries are historical input records. final_correction_reassessment and canonical evidence.json govern this successor; they do not reactivate the superseded EMJH deferral or EPA attribution.','independent_review':'pending'})

# Reproduce complete case and full recipe bindings without altering any raw snapshot.
queue=C/'queue/preliminary-v5';shard=load(queue/'shards/shard-05.json');cases={c['case_id']:c for c in shard['cases']};bindings=[];recipe_paths={}
for d in D:
 c=cases[d['case_id']];assert [x['occurrence_id'] for x in c.get('occurrences',[])]==d['occurrence_ids']
 occurrences=[]
 for occ in c.get('occurrences',[]):
  path=queue/occ['full_recipe_snapshot'];h=sha(path);assert h==occ['source_file_sha256']
  recipe_paths[str(path)]={'path':str(path),'sha256':h,'bytes':path.stat().st_size}
  occurrences.append({'occurrence_id':occ['occurrence_id'],'component_path':occ['component_path'],'full_recipe_snapshot':occ['full_recipe_snapshot'],'sha256':h,'raw_component':occ['raw_component'],'recipe_source_identifiers':occ['recipe_source_identifiers']})
 bindings.append({'case_id':d['case_id'],'case_index':d['case_index'],'case_input_sha256':d['case_input_sha256'],'raw_case':c,'occurrences':occurrences})
put('complete-source-bindings.json',{'at':now,'shard':{'path':str(queue/'shards/shard-05.json'),'sha256':sha(queue/'shards/shard-05.json')},'cases':bindings,'full_recipe_files':list(recipe_paths.values()),'counts':{'cases':len(bindings),'context_occurrences':sum(len(x['occurrences']) for x in bindings),'unique_recipe_files':len(recipe_paths)},'scope':'Complete original raw cases, full frozen recipe byte guards and all occurrence/component/source-identifier bindings are retained. Scientific readings and limits are in the primary read ledger; hash coverage alone is not scientific approval.'})

# Existing positive references and immutable predecessor bytes, not new semantic approval.
oldids={x['proposal']['proposal_id'] for x in original};assert oldids==set(pp)
for p in P:
 path=O/p['after_capture']['path'].removeprefix(PUB);assert sha(path)==p['after_capture']['sha256']
 assert 'M1193-FOLLOWON-153' not in p['evidence_ids']
for d in D:assert 'M1193-FOLLOWON-153' not in d['evidence_ids']
for x in load(O/'input-manifest.json')['inputs']:assert sha(x['path'])==x['sha256'],x['path']
for e in E[:-1]:
 old=next(x['evidence'] for x in load(O/'capture-index.json') if x['evidence']['evidence_id']==e['evidence_id']);assert e['capture']==old['capture'] and e.get('accessed_at')==old.get('accessed_at')
put('final-accounting.json',{'at':now,'predecessor_head':'43f7cf6e8681fa617b5d6d3529d94d537ca01f0d','cases':len(D),'original_proposals_retained':len(P),'changed_payloads':40,'byte_identical_payloads':5,'new_proposals':0,'removed_proposals':0,'original_evidence_entries':482,'successor_evidence_entries':len(E),'changed_original_evidence_metadata':2,'original_capture_bytes_urls_timestamps_preserved':True,'original_before_and_input_hashes_rechecked':True,'full_recipe_files':len(recipe_paths),'context_occurrences':sum(len(x['occurrences']) for x in bindings),'independent_review':'pending','new_network_retrievals':0,'maintained_or_git_or_github_mutations':False,'validation_scope_correction':'Earlier media checks called validate_component_partonomy([record]) per proposal, not a full-catalogue substitution. No claim of full closure follows from that receipt. The final coordinator path-based overlay, with replaced owners removed, is authoritative.'})
hand='''Media final scientific correction successor

Primary author: Codex GPT-6 /root/media_research. Complete scope: all 60 assigned cases and all 45 original full payloads, preserving raw source labels, occurrences, original before hashes and prior captures. No maintained records, Git state, GitHub, generated surfaces or sealed comparison packets were changed.

W05-MEDIA-F01 replaces Marine Broth's false active agar-equivalence premise while preserving its exact historical human assertion and the already corrected commercial formula. W05-MEDIA-F02 adds the five approximate manufacturer basal-per-litre EMJH amounts with explicit basis and performance footnote; 2.555 versus 2.3/0.9 is compatible rounding. W05-MEDIA-F03 preserves the unrelated EPA noise PDF as a mismatched retrieval and removes all positive links; the two independently supported dependent-component withdrawals are unchanged.

The 39 W02-audited newly agent-authored MappingEvidence entries now use LLM_SUGGESTION. Marine's new correction uses that type as well, with the prior human object retained historically. Two inherited active human mapping assertions and the distinct component-evidence enum remain unchanged. There are 40 changed payloads and 5 byte-identical payloads, with 45 predecessor-to-successor diffs and full ancestry. All 45 isolated YAMLs passed the native closed schema and guarded serialization/readback checks. This is primary author validation, not independent scientific approval.

Files: decisions.json, evidence.json, proposals.json; proposed/ contains every complete final YAML. primary-read-ledger.json supplies case-specific conclusions and limits. complete-source-bindings.json contains all raw cases and frozen recipe/occurrence hashes. payload-ancestry.json, mapping-evidence-typing.json, finding-dispositions.json and diffs/ document every change. validation.json and final-accounting.json state the actual validation scope. Original source bytes and timestamps are reused; no new network access is claimed.

Pending coordinator obligations: obtain authorship-separated exact-byte skeptical review; run the authoritative path-based full overlay with old owners removed; retain source, role and export holds. Issue1237 requires one joint Daigo395-01681 candidate with worker03, preserving eight parts, 3.15 g listed sum versus3.2 g instruction and restricted occurrence routing. CM0643 powder remains separate from worker03's prepared broth. Marine's worker03 same-owner aliases require reconciliation, not blind application. The retained PPLO, source1941 L-15 and unselected generic-product relationships remain explicit scientific reconciliation holds.

Validation-scope correction: historical media validation checked each proposal in isolation. It did not establish combined identifier-substitution closure. No corpus, native curation-review or export gate pass is claimed here; the coordinator final full-substitution gate is authoritative. Historical predecessor correction_reassessment and capture-index metadata remain input history, superseded where stated by the final reassessment and canonical evidence index.

The primary lane is complete and stops here for a separately authored review.
'''
path=O/'HANDOFF.md';assert not path.exists();path.write_text(hand)
members=[]
for p in sorted(O.rglob('*')):
 if p.is_file():members.append({'path':str(p.relative_to(O)),'sha256':sha(p),'bytes':p.stat().st_size})
put('MANIFEST.json',{'sealed_at':now,'author':'Codex GPT-6 /root/media_research','scope':'Complete primary lane; independent review pending.','members':members,'core':{n:sha(O/n) for n in ['decisions.json','evidence.json','proposals.json','HANDOFF.md']}})
print(json.dumps({'manifest_sha256':sha(O/'MANIFEST.json'),'core':{n:sha(O/n) for n in ['decisions.json','evidence.json','proposals.json','HANDOFF.md']},'files':len(members)},indent=2))
