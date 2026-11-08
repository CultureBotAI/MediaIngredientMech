import pathlib, json, hashlib, copy, datetime, difflib, subprocess
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient
from scientific_assessments import CASE

O = pathlib.Path(__file__).parent
B = pathlib.Path('reports/all_unmatched_20261107/worker-05')
PUB = 'final-correction-v1/media/'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
AUTHOR = 'Codex GPT-6 /root/media_research'
def load(p): return json.loads(pathlib.Path(p).read_text())
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def objsha(x): return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
def put(n,x):
    p=O/n; p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists(): raise RuntimeError('Refusing overwrite: '+str(p))
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
    return {'root':'artifact','path':PUB+n,'sha256':sha(p)}

inputs=load(O/'input-manifest.json'); source=load(O/'predecessor-payloads.json'); D=load(O/'predecessor-decisions.json')
captures=load(O/'capture-index.json'); E=[copy.deepcopy(x['evidence']) for x in captures]
typing=load(O/'typing-audit-full-selected-rows.json'); typed={x['proposal_id']:x for x in typing}
assert len(D)==60 and len(source)==45 and len(typed)==39 and set(CASE)=={d['case_index'] for d in D}
assert subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()==inputs['assignment']['base_head']
for i in inputs['inputs']: assert sha(i['path'])==i['sha256'],i['path']

emjh=('Source 990 / DSMZ 1113 identifies Difco EMJH base, separate from 100 ml enrichment. '
      'The manufacturer approximate basal formula per litre lists disodium phosphate 1.0 g, '
      'monopotassium phosphate 0.3 g, sodium chloride 1.0 g, ammonium chloride 0.25 g and thiamine 5.0 mg. '
      'The listed total is 2.555 g/L; 2.3 g in 900 ml gives approximately 2.55556 g/L and is consistent with rounded directions, '
      'not a conflicting basis. These are approximate manufacturer basal-reconstitution equivalents, not concentrations in dry powder '
      'or in the final enriched medium. The table footnote permits adjustment and/or supplementation to meet performance criteria. '
      'All five names remain UNMAPPED at component level; no hydrate, thiamine salt, exact lot formula or enrichment composition is inferred. '
      'COMPLETE refers only to the five constituents in the cited basal table.')
marine=('The existing registry denotes the named commercial Difco Marine Broth 2216 preparation. '
        'The manufacturer manual, printed pages 351-352, independently lists broth and agar formulas: '
        'broth has magnesium chloride 5.9 g and magnesium sulfate 3.24 g per litre at standard reconstitution; '
        'agar has magnesium chloride 8.8 g and sodium sulfate 3.24 g. Thus the products do not differ only by agar. '
        'The corrected sixteen-part commercial broth formula is retained; unspecified salt forms remain UNMAPPED. '
        'The old MIM curation (#260) assertion and ATCC agar-minus-agar transcription are historical provenance, not the active identity basis. '
        'This source-bound correction does not merge generic marine-medium owners or resolve worker03 same-owner alias reconciliation.')
P=[]; ancestry=[]; validation=[]; typing_receipts=[]
for item in source:
    p=copy.deepcopy(item['proposal']); r=copy.deepcopy(item['record']); old=copy.deepcopy(r); pid=p['proposal_id']
    assert sha(item['payload_binding']['path'])==p['after_capture']['sha256']
    if p.get('before_sha256'): assert sha(p['owner_path'])==p['before_sha256']
    deltas=[]; exact_old_mapping=None
    if pid in typed:
        row=typed[pid]; assert row['field']=='ontology_mapping.evidence[0]'
        entry=r['ontology_mapping']['evidence'][0]
        assert entry==row['full_value'] and not row['baseline_full_value_match_indices']
        if item['before']:
            assert entry not in item['before']['record'].get('ontology_mapping',{}).get('evidence',[])
        entry['evidence_type']='LLM_SUGGESTION'
        deltas.append('Retype the documented campaign-agent mapping judgment from human-only MANUAL_CURATION to LLM_SUGGESTION under issue1226; scientific assertion and source unchanged except any separately listed finding.')
        typing_receipts.append({'proposal_id':pid,'audit_row_id':row['audit_row_id'],'field':row['field'],'old_value':row['full_value'],'new_type':'LLM_SUGGESTION','reason':row['rationale'],'authorship':row['author_evidence'],'baseline_full_value_match_indices':[]})
    if pid=='M1193-P-MARINE2216':
        exact_old_mapping=copy.deepcopy(r['ontology_mapping']['evidence'][0])
        r['ontology_mapping']['evidence']=[{'evidence_type':'LLM_SUGGESTION','source':'https://cdn.media.interlabdist.com.br/uploads/2021/01/Marine-2216-Agar-e-Broth.pdf','notes':marine}]
        r['notes'] += '\nFinal correction W05-MEDIA-F01: '+marine
        deltas.append('W05-MEDIA-F01: replace the false active agar-equivalence premise with the directly supported commercial broth basis. Preserve every component, alias, owner identifier and historical event.')
        p['description']=marine
    if pid=='M1193-P-LEPTOSPIRA_MEDIUM_BASE_EMJH':
        r['notes']=r['notes'].split(' Correction1193:')[0]+' Final correction W05-MEDIA-F02: '+emjh
        r['ontology_mapping']['evidence'][0]['notes']=emjh
        vals=[('1.0','G_PER_L_AT_STANDARD_BASAL_RECONSTITUTION'),('0.3','G_PER_L_AT_STANDARD_BASAL_RECONSTITUTION'),('1.0','G_PER_L_AT_STANDARD_BASAL_RECONSTITUTION'),('0.25','G_PER_L_AT_STANDARD_BASAL_RECONSTITUTION'),('5.0','MG_PER_L_AT_STANDARD_BASAL_RECONSTITUTION')]
        for part,(v,u) in zip(r['components'],vals): part.update(concentration_value=v,concentration_unit=u)
        r['component_assertion']['completeness']='COMPLETE'
        r['component_assertion']['evidence'][0]['notes']=emjh
        deltas.append('W05-MEDIA-F02: transcribe all five approximate manufacturer basal-per-litre amounts, resolve the rounding-compatible preparation basis, retain the performance footnote and component-form uncertainty; completeness is relative to the cited five-part table.')
        p['description']=emjh
    if deltas:
        changes=' '.join(deltas)+' Isolated report-only successor; maintained data and all original source, owner, role, cross-shard and export holds remain unchanged.'
        if exact_old_mapping is not None: changes+=' Withdrawn active assertion retained verbatim for historical attribution: '+json.dumps(exact_old_mapping,ensure_ascii=False,sort_keys=True)
        r.setdefault('curation_history',[]).append({'timestamp':NOW,'curator':AUTHOR,'action':'CORRECTED','changes':changes,'previous_status':r['mapping_status'],'new_status':r['mapping_status'],'llm_assisted':True,'llm_model':'gpt-6'})
    target=O/'proposed'/pathlib.Path(p.get('destination_owner_path',p['owner_path'])).name
    target.parent.mkdir(exist_ok=True)
    assert not target.exists()
    errs=validate_ingredient(r)
    assert not errs, (pid, errs)
    if r!=old: write_validated_ingredient(r,target,yaml_kwargs={'sort_keys':False,'allow_unicode':True,'width':100})
    else: target.write_bytes(pathlib.Path(item['payload_binding']['path']).read_bytes())
    assert yaml.safe_load(target.read_text())==r
    assert r.get('curation_history',[])[:len(old.get('curation_history',[]))]==old.get('curation_history',[])
    if pid!='M1193-P-LEPTOSPIRA_MEDIUM_BASE_EMJH': assert r.get('components')==old.get('components') and r.get('component_assertion')==old.get('component_assertion')
    for k in ['identifier','synonyms','supplied_form','occurrence_statistics','mapping_status','preferred_term']: assert r.get(k)==old.get(k), (pid,k)
    oldcap=copy.deepcopy(p['after_capture']); p['after_capture']={'root':'artifact','path':PUB+'proposed/'+target.name,'sha256':sha(target)}
    p['predecessor_proposal']={'source_head':inputs['assignment']['base_head'],'proposal_id':pid,'proposal_object_sha256':objsha(item['proposal']),'after_capture':oldcap}
    p['final_correction']={'author':AUTHOR,'at':NOW,'scope':'Full assigned case, owner payload and applicable primary-source reassessment; isolated successor only.','changes':deltas or ['No payload change after complete primary reassessment.']}
    p['evidence_ids']=[x for x in p['evidence_ids'] if x!='M1193-FOLLOWON-153']
    if pid in ['M1193-P-R2A-DAIGO','M1193-P-CM0643']:
        p['integration_dependencies']=([{'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1237','counterpart':'w03::b-proposal-daigo-r2a','obligation':'Same named Daigo 395-01681 dry product. Coordinator must form one source-union candidate and readable destination, preserving all eight components, historical/current wording, hydrate, 3.15 g list versus 3.2 g instruction and exact occurrence scope. Do not apply both proposals or extend to generic DSMZ1537/full KG1402.'}] if pid.endswith('R2A-DAIGO') else [{'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1237','counterpart':'w03::b-proposal-cm0643','obligation':'Retain this CM0643 powder proposal. Worker03 source context is prepared broth; same catalogue does not identify dry and prepared forms. Coordinator owns the separate prepared-broth correction and provenance reconciliation.'}])
    diff=''.join(difflib.unified_diff(pathlib.Path(item['payload_binding']['path']).read_text().splitlines(True),target.read_text().splitlines(True),fromfile=oldcap['path'],tofile=p['after_capture']['path']))
    dp=O/'diffs'/(target.stem+'.diff');dp.parent.mkdir(exist_ok=True);dp.write_text(diff)
    ancestry.append({'proposal_id':pid,'owner_path':p['owner_path'],'destination_owner_path':p.get('destination_owner_path'),'original_before_sha256':p.get('before_sha256'),'original_before_binding':item['before'] and {k:v for k,v in item['before'].items() if k!='record'},'predecessor_proposal':copy.deepcopy(item['proposal']),'predecessor_after':oldcap,'successor_after':p['after_capture'],'predecessor_record':old,'withdrawn_active_mapping_evidence':exact_old_mapping,'changes':deltas,'diff':{'path':PUB+'diffs/'+dp.name,'sha256':sha(dp)}})
    validation.append({'proposal_id':pid,'after_sha256':sha(target),'closed_schema_errors':[],'before_guard':'matched' if p.get('before_sha256') else 'new owner proposal; no maintained write','historical_events_preserved':True,'identity_alias_form_occurrence_fields_unchanged':True,'changed_payload':r!=old})
    P.append(p)

evidence_deltas=[]
for e in E:
    if e['evidence_id']=='M1193-WEB-web-more-2-131':
        evidence_deltas.append({'predecessor':copy.deepcopy(e),'change':'W05-MEDIA-F02 withdraw unsupported basis conflict.'});e['supports_or_contradicts']=emjh
    if e['evidence_id']=='M1193-FOLLOWON-153':
        evidence_deltas.append({'predecessor':copy.deepcopy(e),'change':'W05-MEDIA-F03 reclassify mismatched retrieval; same bytes, URL, access time and hash.'})
        e['kind']='unsuccessful_search';e['locator']='Title and document control pages: Environmental Noise Compliance Monitoring, Allergan Pharmaceuticals Ireland, Westport, IPPC licence P0126-02; report DC1093-01, 21 June 2012, David Cawley.'
        e['supports_or_contradicts']='Mismatched retrieval of an unrelated 124-page environmental noise report. This is not USDA1998 chapter14 and provides no positive microbial-medium or recipe evidence. The exact original body, URL, access timestamp and SHA256 are retained.'
        e['positive_scientific_use']=False

for d in D:
    old=copy.deepcopy(d)
    d['independent_review']={'status':'pending','evidence_ids':[]}
    d['evidence_ids']=[x for x in d['evidence_ids'] if x!='M1193-FOLLOWON-153']
    if d['case_index'] in [17,136]:d['reasoning']=marine
    if d['case_index']==131:d['reasoning']=emjh
    if d['case_index']==181:d['reasoning']=CASE[181]
    d['final_correction_reassessment']={'status':'complete','author':AUTHOR,'at':NOW,'predecessor_decision_object_sha256':objsha(old),'assessment':CASE[d['case_index']],'raw_source_case_and_occurrence_ids_preserved':True,'original_before_hashes_preserved':True,'prior_review_attribution':'Historical predecessor review only; this successor awaits a separately authored skeptical review.','new_network_queries':[],'retrieval_policy':'Reused exact free primary captures with original timestamps and hashes; no fabricated fresh retrieval. Discovery wrappers are not standalone primary support.'}
    assert d['source']==old['source'] and d['occurrence_ids']==old['occurrence_ids'] and d['case_input_sha256']==old['case_input_sha256'] and d['preserved_source_holds']==old['preserved_source_holds']

put('payload-ancestry.json',{'author':AUTHOR,'created_at':NOW,'predecessor_head':inputs['assignment']['base_head'],'proposals':ancestry,'evidence_changes':evidence_deltas})
put('mapping-evidence-typing.json',{'author':AUTHOR,'created_at':NOW,'issue':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226','rows':typing_receipts,'additional_marine_f01_replacement':'Inherited human assertion is preserved verbatim in old history, new withdrawal history and payload ancestry; its new agent-authored correction is LLM_SUGGESTION.','preserved_component_enum':'ComponentEvidenceTypeEnum.MANUAL_CURATION is a separate enum and is unchanged.','not_a_scientific_approval':True})

ledger={'author':AUTHOR,'created_at':NOW,'scope':{'cases':60,'proposals':45,'original_evidence_capture_hashes_checked':len(captures),'ignored_files_included_in_owner_inventory':True},'methods':['Read all complete selected after YAML payloads, original before-owner bytes and their source context/occurrence inventories.','Read all sixty full frozen scientific case contexts and the applicable primary documents, distinguishing whole supplied products, source recipes, receiving additions and explicit branches.','Inspected complete documents or precise product/formula sections of large manufacturer catalogues; search wrappers and failed retrievals are discovery or unsuccessful evidence only.','Checked all exact capture hashes and original access times; no new network retrieval was required.','Compared the full selected W02 authorship-provenance rows with exact before/after evidence objects; no human attribution inferred from a supplier URL.'],'source_capture_index':{'path':PUB+'capture-index.json','sha256':sha(O/'capture-index.json')},'cases':[{'case_id':d['case_id'],'case_index':d['case_index'],'case_input_sha256':d['case_input_sha256'],'source':d['source'],'occurrence_ids':d['occurrence_ids'],'evidence_refs':d['evidence_ids'],'proposal_ids':d['proposal_ids'],'assessment':CASE[d['case_index']],'missing_requirement':d.get('missing_requirement'),'preserved_holds':d['preserved_source_holds']} for d in D], 'proposals':[{'proposal_id':p['proposal_id'],'case_ids':p['case_ids'],'after_capture':p['after_capture'],'assessment_case_indices':[d['case_index'] for d in D if d['case_id'] in p['case_ids']],'components':len(source[i]['record'].get('components',[])),'complete_payload_read':True,'original_before_hash':p.get('before_sha256'),'source_refs':p['evidence_ids'],'changes':p['final_correction']['changes']} for i,p in enumerate(P)],'limitations':['This is the primary author reassessment, not independent skeptical review.','No schema/native curation gate or export release is claimed by this read ledger. Isolated schema validation is recorded separately.','The historical media validator checked individual proposals, not full-corpus identifier substitution. The coordinator final path-based overlay gate is authoritative.','Issue1237 source-union and supplied-form dependencies remain open to coordinator integration; no winner or merge was installed.']}
ledgercap=put('primary-read-ledger.json',ledger)
E.append({'evidence_id':'M-FINAL-PRIMARY-READ-LEDGER','kind':'source_snapshot','capture':ledgercap,'url':None,'locator':'Complete sixty-case / forty-five-payload primary reassessment ledger, with exact source evidence references and limitations.','supports_or_contradicts':'Authored scientific reassessment and explicit correction rationale, not a new external primary source or independent approval.','case_ids':[d['case_id'] for d in D],'accessed_at':NOW})
for d in D:d['evidence_ids'].append('M-FINAL-PRIMARY-READ-LEDGER')
for p in P:p['evidence_ids'].append('M-FINAL-PRIMARY-READ-LEDGER')
put('decisions.json',{'schema_version':1,'decisions':D})
put('proposals.json',{'schema_version':1,'proposals':P})
put('evidence.json',{'schema_version':1,'evidence':E})
put('validation.json',{'author':AUTHOR,'created_at':NOW,'scope':'Closed native schema validation of each isolated full YAML, exact original before guards, payload readback and preservation checks. This is not independent scientific review or a full-corpus substitution/export gate.','results':validation,'counts':{'cases':len(D),'proposals':len(P),'evidence':len(E),'changed_payloads':sum(x['changed_payload'] for x in validation),'unchanged_payloads':sum(not x['changed_payload'] for x in validation),'mapping_typing_corrections':len(typing_receipts),'additional_marine_active_evidence_replacement':1},'errors':[]})
print('Wrote',len(D),'decisions,',len(P),'full guarded payloads,',len(E),'evidence entries; closed schema errors: 0.')
