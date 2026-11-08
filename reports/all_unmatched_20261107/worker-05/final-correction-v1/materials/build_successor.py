"""Build private, isolated materials proposals with native guards; never apply them."""
from pathlib import Path
import json, yaml, hashlib, copy, datetime, difflib, re, sys
sys.path.insert(0,str(Path.cwd()/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.synonym_policy import is_resolving_synonym
from case_conclusions import CONCLUSIONS
W=Path.cwd();L=Path(__file__).resolve().parent;O=W/'reports/all_unmatched_20261107/worker-05'
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
P8=C/'workers/w08/worktree/.temp/w05-published-head-independent-review-v1'
A=json.loads((P8/'assignments/materials.json').read_text())
OLD=json.loads((O/'correction-1193-v1/materials/proposals.json').read_text())['proposals']
E=json.loads((O/'correction-1193-v1/materials/evidence.json').read_text())['evidence']
at=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def objsha(x):return sha(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
def save(name,value):
 p=L/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n');return p
def ref(p):return {'root':'artifact','path':'final-correction-v1/materials/'+str(p.relative_to(L)),'sha256':sha(p.read_bytes())}
def preserve(src,name):
 p=L/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(src.read_bytes());return p
for d in ['before','predecessor','proposed','diffs','context','captures','validation']: (L/d).mkdir(exist_ok=True)
assign=preserve(P8/'assignments/materials.json','context/w08-materials-assignment.json')
peer=preserve(P8/'materials/findings.json','context/w08-findings.json')
peerreview=preserve(P8/'materials/review.json','context/w08-review.json')
auditpath=C/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1/provenance/native-type-suggestions-v1.json'
audit=json.loads(auditpath.read_text());auditcopy=preserve(auditpath,'context/w02-native-type-suggestions-v1.json')
preserve(C/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1/HANDOFF.md','context/w02-HANDOFF.md')
for n in [1193,1176,1212,1236,1226]:
 for typ in ['issue','comments']:preserve(W/f'.temp/w05-final-correction-v1/issues/{typ}-{n}.json',f'context/{typ}-{n}.json')
issue_index=preserve(W/'.temp/w05-final-correction-v1/issues/capture-index.json','context/issue-capture-index.json')
issue_times={x['name']:x for x in json.loads(issue_index.read_text())}
pr=C/'preflight/existing-owner-scope-decisions-v1/fresh-primary'
ols=preserve(pr/'micro1795.body','captures/micro1795.body')
retr=preserve(pr/'retrievals.json','captures/coordinator-retrievals.json')
olsm=next(x for x in json.loads(retr.read_text()) if x['name']=='micro1795');assert olsm['sha256']==sha(ols.read_bytes())
coordroot=C/'integration/final-same-target-reconciliation-v2'
coordpath=coordroot/'publication-v4/candidate-summary-v4.json';coord=json.loads(coordpath.read_text());assert coord['candidate_count']==37
coordcopy=preserve(coordpath,'context/coordinator-candidate-summary-v4.json')
overlaps=[]
owners={p['owner_path'] for p in OLD}
for g in coord['groups']:
 if g['owner_path'] in owners:
  q=preserve(coordroot/g['candidate']['path'],'context/coordinator-candidates/'+g['candidate_id']+'-'+Path(g['owner_path']).name)
  assert sha(q.read_bytes())==g['candidate']['sha256']
  overlaps.append({'candidate_id':g['candidate_id'],'owner_path':g['owner_path'],'candidate':ref(q),'origins':g['origins'],'case_ids_not_imported':g['case_ids'],'status':'pending independent whole-candidate review and source-aware integration','bounded_conclusion_reused':g['candidate_id'] in ['TARGET-005','TARGET-017','TARGET-024'],'no_whole_owner_approval_transferred':True})
newE=[]
def evidence(eid,p,kind,locator,claim,url=None,access=None,cases=None):
 q={'evidence_id':eid,'capture':ref(p),'kind':kind,'locator':locator,'supports_or_contradicts':claim,'url':url,'case_ids':cases or A['case_ids'],'accessed_at':access or at}
 newE.append(q);return eid
evidence('FINAL-MATERIALS-W08-FINDINGS',peer,'source_snapshot','All seven MAT findings, exact selected payloads and bounded requested fixes','External independent review is a finding source, not primary ingredient evidence or successor approval.')
evidence('FINAL-MATERIALS-W02-PROVENANCE',auditcopy,'source_snapshot','Exact 27 W05 materials rows, field/value/payload guards and claim-specific types','Documents authorship provenance; independent of scientific truth and source credibility.')
evidence('FINAL-MATERIALS-MICRO1795',ols,'ontology','Nonobsolete term, definition, definition source and specific trademark','Specific Phytone identity; erroneous Hordeum vulgare parenthetical is excluded, not a barley assertion.',olsm['url'],olsm['accessed_at'],[d['case_id'] for d in A['decisions'] if d['case_index']==139])
evidence('FINAL-MATERIALS-COORDINATOR',coordcopy,'source_snapshot','37 pending candidates; overlapping material owners retained separately','Bounded Phytone and Catalase conclusions may inform W05 successors; full unions, other-worker cases, counts and approvals are not imported.')
for n in [1193,1176,1212,1236,1226]:
 for typ in ['issue','comments']:
  receipt=issue_times[f'{typ}-{n}'];capture=L/f'context/{typ}-{n}.json';assert sha(capture.read_bytes())==receipt['sha256']
  evidence(f'FINAL-MATERIALS-{typ.upper()}-{n}',capture,'source_snapshot','Complete captured '+('issue body' if typ=='issue' else 'comment array')+'; original receipt in context/issue-capture-index.json','Filed-before-fix trace and held scope; no new GitHub mutation.',f'https://github.com/CultureBotAI/MediaIngredientMech/issues/{n}',receipt['accessed_at'])
oldj=next(e for e in E if e['evidence_id']=='MATERIALS-C1193-JCM117');save('context/superseded-jcm117-evidence-entry.json',oldj)
oldj['kind']='unsuccessful_search';oldj['locator']='Complete no-result response: Nothing found.';oldj['supports_or_contradicts']='No direct recipe content was returned. TOGO M109 carries the substantive recipe and JCM_M117 lineage; this response does not corroborate ingredient facts.'
auditrows=[x for x in audit['rows'] if x['worker']==5 and x['proposal_id'] in A['proposal_ids']];assert len(auditrows)==27
by_audit={x['proposal_id']:x for x in auditrows}
changes={};prov=[];ancestry=[];newP=[];newrecords={};old_to_new={}
def addnote(r,s):r['notes']=((r.get('notes') or '').rstrip()+'\n\n'+s).strip()
def reject(r,tokens):
 found=[]
 for s in r.get('synonyms',[]):
  if s['synonym_text'] in tokens:
   found.append(copy.deepcopy(s));s['synonym_type']='REJECTED_LABEL'
 assert len(found)==len(tokens),(r['preferred_term'],tokens,found)
 return found
for i,p0 in enumerate(A['proposals'],1):
 p=copy.deepcopy(p0);pid=p0['proposal_id'];oldpath=O/p0['after_capture']['path'];raw=oldpath.read_bytes();assert sha(raw)==p0['after_capture']['sha256']
 prior=preserve(oldpath,'predecessor/'+oldpath.name);r=yaml.safe_load(raw);before=None;bp=None
 if p0['before_sha256']:
  bp=preserve(W/p0['owner_path'],'before/'+oldpath.name);assert sha(bp.read_bytes())==p0['before_sha256'];before=yaml.safe_load(bp.read_text())
 delta=[];fieldchanges=[]
 if pid in by_audit:
  ar=by_audit[pid];assert ar['payload_sha256']==sha(raw);ix=int(ar['field'].split('[')[1].split(']')[0]);ev=r['ontology_mapping']['evidence'][ix];assert ev['evidence_type']=='MANUAL_CURATION'
  orig=copy.deepcopy(ev);ev['evidence_type']=ar['suggested_native_type']
  prov.append({'audit_row_id':ar['audit_row_id'],'proposal_id':pid,'field':ar['field'],'guarded_payload_sha256':sha(raw),'original_evidence':orig,'original_evidence_canonical_sha256':objsha(orig),'audit_full_value_sha256':ar['full_value_sha256'],'disposition':'reclassified same claim' if 'phytone-boundary' not in pid else 'superseded by source-specific ontology and applicability evidence below; original retained in predecessor','new_native_type':ar['suggested_native_type'],'reason':'Narrow named-term database lookup and quoted definition.' if 'Neopeptone' in pid else 'The object contains this agent author’s ingredient identity, source applicability or registry-boundary judgment; primary source authorship does not make the MIM judgment human supplied.'})
  delta.append('Correct the exact campaign MappingEvidence method under issue 1226 to '+ar['suggested_native_type']+'; preserve its source and claim. Inherited human/process evidence and ComponentEvidence types are unchanged.')
 if pid=='MATERIALS-C1193-bacto-aliases':
  fieldchanges=reject(r,['Fish peptone (Fluka)']);delta.append('Reject the Fish peptone (Fluka) identity alias on Bacto Peptone because the inspected Bacto 211677 specification names bovine and porcine protein, whereas the rejected token explicitly names fish. Preserve the exact text, original source and all history; no Fluka catalog or replacement identity is inferred.')
 if pid=='MATERIALS-C1193-fish-sperm-dna':
  tokens=['(Deoxyribonucleotide)m','(Deoxyribonucleotide)n','(Deoxyribonucleotide)n+m','DNA','DNAn','DNAn+1','Desoxyribonukleinsaeure','deoxyribonucleic acids','desoxyribose nucleic acid','thymus nucleic acid']
  fieldchanges=reject(r,tokens);delta.append('Retire ten generic-DNA or conflicting-thymus exact identity aliases from the source-specific fish-sperm material. Their texts, kg_microbe sources and all history remain. The independent basis is the fish-sperm source boundary versus generic CHEBI:16991, not an absent-formula heuristic. The herring-sperm tombstone is unchanged; species, counterion and molecular length remain unspecified.')
 if pid=='MATERIALS-C1193-peptone-identity':
  fieldchanges=reject(r,['Peptone (0.01 %']);delta.append('Reject only the incomplete concentration token Peptone (0.01 % as an identity name of generic Peptone. Preserve its original microbedecoder provenance and plural Peptones. Do not invent a missing parenthesis, percent basis or preparation. Eighteen retained historical inbound MICRO:0000178 component references and current proposed components remain a source-level integration dependency; no automatic retargeting is authorized.')
 if pid=='MATERIALS-C1193-soy-peptone-boundary':
  tokens=['Phytone peptone','Phytone peptone (BD-BBL)','Soytone (BD-Difco) or Phytone peptone (BD-BBL)','Soytone','Bacto Soytone']
  fieldchanges=reject(r,tokens);delta.append('Retire five branded or alternative identity aliases on the generic soy-digest owner. The three Phytone-bearing dispositions reuse the bounded coordinator conclusion in issue 1212 comment 6718503130. Separate review of the original kg_microbe Soytone token, Bacto Soytone merge history and manufacturer guide pages 13, 33 and 92 confirms distinct named products and processing; generic soy digest is not their exact product identity. Preserve raw texts, original sources, merge history, occurrence totals, all quarantine holds and the Bacto Soytone tombstone. This does not merge or select the competing W08/W10 owner deltas.')
 if pid in ['MATERIALS-C1193-catalase-source-form','MATERIALS-C1193-soy-peptone-boundary']:
  ts=[s['synonym_text'] for s in r.get('synonyms',[]) if s['synonym_text'].startswith('Properties:')]
  assert all(not is_resolving_synonym(s) for s in r['synonyms'] if s['synonym_text'] in ts)
  fieldchanges+=reject(r,ts);delta.append('Optionally classify the retained Properties metadata tokens as REJECTED_LABEL. Native synonym policy already excludes these texts; this is provenance classification only, with no resolver change, filter change or release blocker.')
 if pid=='MATERIALS-C1193-catalase-source-form':
  old='JCM117 directly supplies the catalog spelling and60mg filter-sterilized addition'
  r['notes']=r['notes'].replace(old,'TOGO M109, carrying original_media_id JCM_M117, supplies literal Catalase (Sigma C--10), 60 mg and filtration; the direct JCM 117 capture returns Nothing found')
  for sf in r.get('supplied_form',[]):
   if sf.get('catalog_number')=='C-10':sf['notes']='TOGO M109 records original_media_id JCM_M117 and literal Catalase (Sigma C--10), 60 mg with separate filtration. The direct JCM 117 response says Nothing found. Historical species and formulation are unverified; contemporary C100 is not assigned. The separately supported C9322 proposal remains in the pending coordinator union and is not imported into W05 case membership.'
  delta.append('Correct active attribution to the inspected TOGO M109 recipe and preserve the unsuccessful JCM 117 capture honestly. Reuse only this bounded conclusion from coordinator TARGET-005; preserve the W05 history prefix and source ownership. The historical event remains unedited as superseded history. Keep literal C--10, the distinct C9322 dependency, the C100 uncertainty and the human NCIT:C61062 exclusion under issue 312.')
 if pid=='MATERIALS-C1193-phytone-boundary':
  r['identifier']='MICRO:0001795'
  r['ontology_mapping']={'ontology_id':'MICRO:0001795','ontology_label':'Phytone peptone','ontology_source':'MICRO','mapping_quality':'EXACT_MATCH','evidence':[
   {'evidence_type':'LLM_SUGGESTION','source':olsm['url'],'notes':'Agent interpretation applying the specific nonobsolete Phytone peptone term to the authentic existing Phytone owner and MediaDive 125/362 source scope. The term names the BBL/Difco trademark and cites the manufacturer papaic soybean-meal digest definition. The erroneous Hordeum vulgare parenthetical is excluded; it is not accepted as a barley identity.'},
   {'evidence_type':'LLM_SUGGESTION','source':'https://assets.thermofisher.com/TFS-Assets/BPD/brochures/peptones-supplements-feeds-technical-reference-guide.pdf','notes':'Manufacturer product descriptions and listings distinguish Phytone from Phytone UF, Difco Soytone and Bacto Soytone. This supports the bounded product interpretation, not an invariant component formula or product interchangeability.'},
   {'evidence_type':'LLM_SUGGESTION','source':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1212#issuecomment-6718503130','notes':'Reuse of the separately attributed bounded coordinator Phytone identity conclusion and three coupled Soy alias withdrawals. The combined TARGET-017 payload remains pending independent review; no other-worker histories, cases, counts or approval are imported.'}]}
  delta.append('Use specific MICRO:0001795 Phytone peptone for the authentic Phytone owner, superseding the unnecessary local fallback and the older broad FOODON identity. This reuses the bounded coordinator conclusion while preserving W05 source ownership and all historical events. Couple the correction to the three Phytone-bearing Soy_Peptone alias withdrawals. Exclude the term annotation’s erroneous Hordeum vulgare parenthetical. No count redistribution, whole-union approval, W10 case import or component formula is asserted.')
 if pid=='MATERIALS-C1193-Sucrose_20_Percent_Stock':
  assert r['components'][0]['component_name']=='Sucrose';r['components'][0]['reference_scope']='MIM_CATALOG';r['components'][0]['component_id']='CHEBI:17992'
  delta.append('Optionally link the explicitly named sucrose constituent to existing Sucrose CHEBI:17992 using MIM_CATALOG. Retain PARTIAL completeness, the explicit 20% w/v basis and unspecified solvent. Section 6 permits named UNMAPPED components; the predecessor was not a schema or identity failure and this improvement is not a release prerequisite.')
 if delta:
  if pid in ['MATERIALS-C1193-phytone-boundary','MATERIALS-C1193-soy-peptone-boundary','MATERIALS-C1193-peptone-identity']:
   r['notes']='Previous published proposal scope, preserved as historical provenance and superseded where corrected below:\n'+r.get('notes','')
  addnote(r,'Final W05 report-only correction: '+' '.join(delta)+' All original source, organism, role, owner and export holds remain. Independent review of these exact successor bytes is pending.')
  record_curation_event(r,curator='Codex /root/materials_research; W05 final report-only correction',action='CORRECTED',changes=' '.join(delta)+' Isolated proposal only; no maintained data or source membership change.',previous_status=r['mapping_status'],new_status=r['mapping_status'],llm_assisted=True,llm_model='gpt-6',timestamp=at)
 out=L/'proposed'/oldpath.name;write_validated_ingredient(r,out);assert not validate_ingredient(r)
 assert r.get('curation_history',[])[:len(yaml.safe_load(raw).get('curation_history',[]))]==yaml.safe_load(raw).get('curation_history',[])
 newid=f'W05-FINAL-MAT-{i:03d}';old_to_new[pid]=newid;changes[pid]=delta;newrecords[p0['owner_path']]=r
 p['proposal_id']=newid;p['replaces_proposal_ids']=list(dict.fromkeys([pid]+p.get('replaces_proposal_ids',[])));p['predecessor_capture']=copy.deepcopy(p0['after_capture']);p['predecessor_copy']=ref(prior);p['after_capture']=ref(out);p['before_capture']=ref(bp) if bp else None
 p['description']=p0['description']+(' Final correction: '+' '.join(delta) if delta else ' The exact scientific payload is retained after full source and owner re-review; historical support is not transferred to unreviewed claims.')
 p['evidence_ids']=list(dict.fromkeys(p['evidence_ids']+['FINAL-MATERIALS-W08-FINDINGS','FINAL-MATERIALS-W02-PROVENANCE']+(['FINAL-MATERIALS-MICRO1795','FINAL-MATERIALS-COORDINATOR'] if 'phytone' in pid else [])))
 p['primary_author']='/root/materials_research';p['independent_review']={'status':'pending','evidence_ids':[]};p['successor_scope']='W05 assigned source cases only; no whole-owner, component-coupling or export approval.'
 if fieldchanges:p['changed_labels']=list(dict.fromkeys(p.get('changed_labels',[])+[s['synonym_text'] for s in fieldchanges]))
 if pid=='MATERIALS-C1193-phytone-boundary':
  p['identity_consequence']='Authentic Phytone owner uses specific MICRO:0001795, replacing generic FOODON and unnecessary registry fallback.';p['predicate_consequence']='Own-identifier exactMatch under mapping semantics; coordinator must regenerate canonical rows only after source-aware integration and independent review.'
 newP.append(p)
 diff=''.join(difflib.unified_diff(raw.decode().splitlines(True),out.read_text().splitlines(True),fromfile='published/'+oldpath.name,tofile='successor/'+oldpath.name));(L/'diffs'/f'{i:03d}-from-published.diff').write_text(diff)
 if bp:(L/'diffs'/f'{i:03d}-from-original.diff').write_text(''.join(difflib.unified_diff(bp.read_text().splitlines(True),out.read_text().splitlines(True),fromfile='original/'+oldpath.name,tofile='successor/'+oldpath.name)))
 ancestry.append({'proposal_id':newid,'replaces_proposal_id':pid,'owner_path':p['owner_path'],'destination_owner_path':p.get('destination_owner_path',p['owner_path']),'original_before_sha256':p['before_sha256'],'predecessor':p0['after_capture'],'successor':p['after_capture'],'history_prefix_preserved':True,'source_case_ids_unchanged':p['case_ids']==p0['case_ids'],'occurrence_statistics_unchanged':r.get('occurrence_statistics')==yaml.safe_load(raw).get('occurrence_statistics'),'changes':delta,'retyped_original_synonyms':fieldchanges})
save('proposals.json',{'schema_version':'1.0.0','proposals':newP})
save('payload-ancestry.json',{'author':'/root/materials_research','base_head':A['head'],'at':at,'entries':ancestry,'coordinator_union_policy':'All 37 candidates remain pending independent review; bounded source conclusions are separate from combined payload authorship.'})
save('mapping-evidence-dispositions.json',{'at':at,'author':'/root/materials_research','audit_source':ref(auditcopy),'dispositions':prov,'historical_human_or_process_types_unchanged':True,'component_evidence_enum_unchanged':True,'independent_review_pending':True})
dep=json.loads((O/'correction-1193-v1/validation/component-identity-dependencies.json').read_text());peptone=next(x for x in dep['old_identifier_dependencies'] if x['old_identifier']=='MICRO:0000178')
catalog={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in sorted((W/'data/ingredients').rglob('*.yaml'))}
base_inbound=[]
for path,r in catalog.items():
 for i,z in enumerate(r.get('components') or []):
  if z.get('component_id')=='MICRO:0000178':base_inbound.append({'owner_path':path,'owner_sha256':sha((W/path).read_bytes()),'component_path':f'components/{i}','component':z})
published=json.loads((O/'correction-1193-v1/proposals.json').read_text())['proposals'] if (O/'correction-1193-v1/proposals.json').exists() else []
overlay=copy.deepcopy(catalog)
for p in published:
 overlay.pop(p['owner_path'],None);overlay[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load((O/p['after_capture']['path']).read_text())
for p in newP:overlay.pop(p['owner_path'],None);overlay[p.get('destination_owner_path',p['owner_path'])]=yaml.safe_load((L/'proposed'/Path(p['after_capture']['path']).name).read_text())
current_inbound=[]
for path,r in overlay.items():
 for i,z in enumerate(r.get('components') or []):
  if z.get('component_id')=='MICRO:0000178':current_inbound.append({'owner_path':path,'component_path':f'components/{i}','component':z})
dependencies=save('integration-dependencies.json',{'at':at,'author':'/root/materials_research','status':'held for source-aware coordinator integration','coordinator_summary':ref(coordcopy),'coordinator_candidate_count':37,'overlapping_candidates':overlaps,'historical_peptone_dependency':peptone,'fresh_baseline_inbound':base_inbound,'published_overlay_plus_materials_successors_inbound':current_inbound,'limitations':['No component retargeting was performed. Bacto remaining on MICRO:0000178 makes references structurally valid without proving source identity.','The 18 historical retained references are enumerated, with the separately changed Marine Broth reference distinguished. Current other-lane successor claims require root-wide reconciliation.','Coordinator combined candidates and other-worker support remain separate from W05 case membership.']})
evidence('FINAL-MATERIALS-DEPENDENCIES',dependencies,'source_snapshot','Exact historical and recomputed component dependencies plus pending coordinator overlaps','Explicit unresolved source-level integration obligations; not approval or automatic retargeting.')
ds=[];assess=[]
for d0 in A['decisions']:
 d=copy.deepcopy(d0);n=d['case_index'];assert n in CONCLUSIONS;c=next(x for x in A['cases'] if x['case_id']==d['case_id'])
 d['reasoning']=CONCLUSIONS[n];d['applicability']=f'Full final materials reassessment, case {n}: '+CONCLUSIONS[n]
 d['proposal_ids']=[old_to_new[p] for p in d0['proposal_ids']]
 d['primary_author']='/root/materials_research';d['primary_reviewer']='/root/materials_research';d['independent_review']={'status':'pending','evidence_ids':[]}
 d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+['FINAL-MATERIALS-W08-FINDINGS','FINAL-MATERIALS-W02-PROVENANCE']+(['FINAL-MATERIALS-MICRO1795','FINAL-MATERIALS-COORDINATOR'] if n==139 else [])+(['FINAL-MATERIALS-DEPENDENCIES'] if n in [62,71,116,139,173,176] else [])))
 d['final_reassessment']={'status':'primary complete; independent review pending','author':'/root/materials_research','at':at,'predecessor_decision_sha256':objsha(d0),'changed_proposal_ids':[old_to_new[p] for p in d0['proposal_ids'] if changes[p]],'source_case_and_occurrence_membership_unchanged':True,'full_selected_payloads_reviewed':d['proposal_ids'],'scientific_conclusion':CONCLUSIONS[n],'historical_review_not_transferred':True}
 if not d['proposal_ids']:d['no_change_reason']=CONCLUSIONS[n]
 if n==116:d['missing_requirement']='Historical catalog specification or other independent primary evidence for C--10 species, formulation and relation to C100. The positive recipe evidence is TOGO M109; direct JCM 117 retrieval was unsuccessful.'
 if n==139:d['missing_requirement']='Exact W05 successor and competing coordinator union require independent review and source-aware integration; shared occurrence counts and other-worker claims are not approved.'
 ds.append(d)
 assess.append({'case_id':d['case_id'],'case_index':n,'source_label':c['raw_source_label'],'case_input_sha256':d['case_input_sha256'],'occurrence_ids':d['occurrence_ids'],'conclusion':CONCLUSIONS[n],'proposal_ids':d['proposal_ids'],'evidence_ids':d['evidence_ids'],'missing_requirement':d['missing_requirement'],'hold_objects_preserved_from_published_decision':{k:objsha(d0[k]) for k in ['preserved_downstream_holds','preserved_source_holds'] if k in d0},'actual_scope':'Full assigned case, original owner and selected payload review; primary sources assessed at substantive recipe, product and term sections. Complete unrelated manual chapters and inherited role experiments were not newly reviewed.'})
assert set(CONCLUSIONS)=={d['case_index'] for d in ds};assert len(ds)==61
save('decisions.json',{'schema_version':'1.0.0','decisions':ds})
save('primary-conclusions.json',{'at':at,'author':'/root/materials_research','scope':'All 61 assigned materials cases and all 39 complete selected payloads; no sampling. Authored primary reassessment, not independent skeptical review.','case_assessments':assess,'limits':['Unchanged inherited roles and historical human/process evidence are preserved without new scientific or release approval.','Source-unit and stock-hierarchy defects remain assigned to their existing upstream issues.','No exact formulation is inferred solely from source numbers, shared ontology IDs, absent details or nominal doses.']})
E+=newE;save('evidence.json',{'schema_version':'1.0.0','evidence':E})
findings=json.loads(peer.read_text())['findings'];fd=[]
for f in findings:
 n=f['finding_id'];ids=[old_to_new[x['proposal_id']] for x in f['selected_payloads']];text={'W05-MAT-001':'Five branded/alternative Soy aliases retired with exact source/history preservation; authentic Phytone uses the independently sourced specific term. Difco Soytone remains distinct. Full competing coordinator unions and shared counts remain pending.', 'W05-MAT-002':'Ten generic/conflicting-tissue identity aliases are nonresolving. Fish-sperm source scope, raw strings, history and the herring tombstone are preserved; the old structureless-term heuristic is not renewed.','W05-MAT-003':'Malformed concentration token retired; plural and original assay claims preserved. Exact 18 retained historical component dependencies and current coupling are explicitly held, with no automatic retargeting.','W05-MAT-004':'The single fish-Fluka token is nonresolving based on fish versus the evidenced bovine/porcine product boundary; no catalog or other generic-alias inference.','W05-MAT-005':'Optional metadata classification completed. Native policy already excludes all three Properties texts, so no resolver/filter fix or blocker is claimed.','W05-MAT-006':'Optional exact sucrose component reference added. Named UNMAPPED parts were already legal; PARTIAL composition, unknown solvent and owner/export holds remain.','W05-MAT-007':'Active notes and supplied-form attribution corrected to TOGO M109; JCM117 evidence reclassified as unsuccessful. Historical event remains intact. C--10 literal, C100 uncertainty, human NCIT exclusion and separate C9322 coordinator dependency preserved.'}[n]
 fd.append({'finding_id':n,'prior_finding':f,'status':'author remediation proposed; independent exact-byte review pending','disposition':text,'successor_proposal_ids':ids,'successor_captures':[p['after_capture'] for p in newP if p['proposal_id'] in ids],'blocking_classification':'optional improvement; not a resolver or scientific release blocker' if n in ['W05-MAT-005','W05-MAT-006'] else 'material correction with retained integration and release obligations','no_issue_closed':True})
save('finding-dispositions.json',{'at':at,'author':'/root/materials_research','dispositions':fd,'source_finding_count':7,'independent_review_pending':True})
viol=validate_component_partonomy(overlay.values())
save('validation/native-validation.json',{'at':at,'guarded_writer':'mediaingredientmech.validation.write_validated.write_validated_ingredient','writer_sha256':sha((W/'src/mediaingredientmech/validation/write_validated.py').read_bytes()),'event_helper_sha256':sha((W/'src/mediaingredientmech/curate/curation_event.py').read_bytes()),'schema_sha256':sha((W/'src/mediaingredientmech/schema/mediaingredientmech.yaml').read_bytes()),'closed_schema_payloads':39,'closed_schema_errors':0,'overlay_baseline_owners':len(catalog),'published_proposals_substituted':len(published),'materials_successors_substituted':39,'overlay_owners':len(overlay),'component_partonomy_violations':[str(v) for v in viol],'component_partonomy_status':'PASS' if not viol else 'FAIL','scientific_limit':'Structural checks cannot resolve the held peptone source identity coupling or grant whole-owner/source/export approval.'})
save('validation/ancestry-and-coverage.json',{'at':at,'cases':len(ds),'complete_payloads':len(newP),'original_proposals_replaced':len(old_to_new),'mapping_evidence_dispositions':len(prov),'all_before_and_predecessor_hashes_verified':True,'all_history_prefixes_preserved':True,'all_occurrence_statistics_preserved':all(x['occurrence_statistics_unchanged'] for x in ancestry),'all_case_ids_preserved':set(d['case_id'] for d in ds)==set(A['case_ids']),'all_case_occurrence_memberships_preserved':all(d['occurrence_ids']==o['occurrence_ids'] for d,o in zip(ds,A['decisions'])),'all_source_holds_preserved':all(all(d.get(k)==o.get(k) for k in ['preserved_source_holds','preserved_downstream_holds']) for d,o in zip(ds,A['decisions'])),'optional_metadata_policy_before':{'Catalase_2_Properties_tokens':'already nonresolving','Soy_1_Properties_token':'already nonresolving'},'errors':[]})
print(json.dumps({'cases':len(ds),'proposals':len(newP),'evidence':len(E),'changed_payloads':sum(bool(x) for x in changes.values()),'native_partonomy_errors':len(viol),'original_inbound_peptone':len(base_inbound),'overlay_inbound_peptone':len(current_inbound)}))
