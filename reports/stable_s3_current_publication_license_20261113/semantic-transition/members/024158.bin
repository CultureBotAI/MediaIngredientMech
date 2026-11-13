"""2026-11-12: current fourteen-delta primary review, two explicit local steps.

inspect binds actual terminal native payloads and preserved current science notes.
save authors one current batch, then native-validates/saves it. No collection check
until both actual reviewers have saved. No source writes or successor phases.
Author/executor: Codex /root/seven_cas_current_primary, including self-review of
the three method proposals it authored. This is not the independent skeptic.
"""
import argparse, copy, datetime, hashlib, json, os, shlex, subprocess, sys
from pathlib import Path
import yaml

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
C = ROOT.parent.parent
PY = C / 'integration/stable-campaign-adoption-worktree/.venv/bin/python3'
I = ROOT / '.temp/cumulative-source-successor-inspected-s3-v2'
HEAD = '3b6a0b54edddac053cf7f7cf2d9c8f63fb11c015'
HANDOFF_SHA = 'af1d4c650c53de3b6b0430d93000b5cebf992c2d2c2588cc960753f03147bdf2'
REQUEST_SHA = '336140127434edbd22467b4a9e58ae5e18d7be3c082c0fd20fca929e7e14dfaa'
NOTES = C / 'preflight/source-s3-primary-review-v1/READING-NOTES.json'
NOTES_SHA = 'c87f81b316f362f4e40638e980425889a01ac6bc21b9789588e5d4b5682893ab'
REPO = 'CultureBotAI/MediaIngredientMech'
AUTHOR = 'Codex primary /root/seven_cas_current_primary'
DESC = 'Exact reviewed source correction; permanent identity and residual holds retained'

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def digest(obj): return sha(json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode())
def pin(p): return {'path': str(p), 'sha256': sha(p.read_bytes())}
def relative(p): return str(p.relative_to(ROOT))
def read(p, expected):
    if p.is_symlink() or not p.is_file(): raise RuntimeError('Not a regular input: '+str(p))
    raw = p.read_bytes()
    assert sha(raw) == expected, str(p)
    return raw
def read_ref(ref): return read(ROOT/ref['path'], ref['sha256'])
def write(name, raw):
    p = OUT/name
    with p.open('xb') as h: h.write(raw)
    assert p.read_bytes() == raw
    return pin(p)
def save(name, obj): return write(name, (json.dumps(obj, indent=2, ensure_ascii=False)+'\n').encode())
def native_text(value):
    from mediaingredientmech.curate import curation_successor
    return curation_successor.native().encoded(value).decode().strip()
def run(name, args):
    command = [str(PY), '-B', 'scripts/record_review.py', *args]
    started = now()
    result = subprocess.run(command, cwd=ROOT, env={**os.environ, 'PYTHONPATH':str(ROOT/'src'), 'PYTHONDONTWRITEBYTECODE':'1'}, capture_output=True, timeout=300)
    stdout = write(name+'.stdout', result.stdout); stderr = write(name+'.stderr', result.stderr)
    receipt = {'started_at':started, 'finished_at':now(), 'argv':command, 'command':shlex.join(command), 'cwd':str(ROOT), 'exit_code':result.returncode, 'stdout':stdout, 'stderr':stderr}
    save(name+'.json', receipt)
    if result.returncode: raise RuntimeError(name+' failed: '+result.stderr.decode(errors='replace'))
    return json.loads(result.stdout), receipt

def current():
    assert sys.executable == str(PY) and Path.cwd() == ROOT and os.environ.get('PYTHONPATH') == str(ROOT/'src')
    assert subprocess.check_output(['git','--no-optional-locks','rev-parse','HEAD'],cwd=ROOT,text=True).strip() == HEAD
    handoff = json.loads(read(I/'HANDOFF.json', HANDOFF_SHA))
    assert handoff['status'] == 'NATIVE_INSPECTION_COMPLETE_NO_SCIENTIFIC_APPROVAL' and handoff['native_payloads'] == 14 and handoff['head'] == HEAD
    native_result = json.loads(read(Path(handoff['native_result']['path']), handoff['native_result']['sha256']))
    assert native_result['exit_code'] == 0
    request = json.loads(read(I/'INSPECTED-REQUEST.json', REQUEST_SHA))
    payloads = json.loads(read_ref(handoff['inspected']['payloads']))
    stubs = json.loads(read_ref(handoff['inspected']['targets']))
    assert request['context'] == handoff['inspected']['context'] and request['payloads'] == handoff['inspected']['payloads']
    assert len(request['operations']) == len(payloads) == len(stubs) == 14
    return handoff, native_result, request, payloads, stubs

def inspect_phase():
    started = now()
    handoff, native_result, request, payloads, stubs = current()
    notes_raw = read(NOTES, NOTES_SHA); notes = json.loads(notes_raw)
    write('original-reading-notes.json', notes_raw)
    copied = [{'source':pin(NOTES), 'destination':pin(OUT/'original-reading-notes.json')}]
    for source, expected, name in [
        (Path(handoff['native_result']['path']), handoff['native_result']['sha256'], 'native-inspection-result.json'),
        (C/'preflight/three-method-source-proposals-v3/sealed/NATIVE-EVENT-CONTROLS.json','07545f0e28468069e49c598ff6245c1101a06a0993228b33fef35c424235b398','native-event-controls.json'),
        (C/'preflight/three-method-source-proposals-v3/sealed/PROPOSAL-MANIFEST.json','cca5216e26105b1bd92810befec8ebb5ed14d4176e45751ada89d665fd5279de','three-method-v3-manifest.json'),
    ]:
        write(name, read(source, expected)); copied.append({'source':pin(source), 'destination':pin(OUT/name)})
    save('copy-provenance.json', {'at':now(), 'actual_copier':AUTHOR, 'copies':copied, 'no_fresh_acquisition':True, 'original_authors_timestamps_and_paths_retained':True, 'approval':False})
    required = {'MAPPING_SEMANTICS.md','AGENTS.md','docs/CURATION_SUCCESSOR.md','docs/record-reviews.md','docs/record-review-profile.md','.claude/skills/review-ingredients/SKILL.md','schema/record_review.yaml','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/schema/history.yaml','src/mediaingredientmech/curate/curation_successor.py','src/mediaingredientmech/curate/curation_event.py','scripts/record_review.py',relative(I/'HANDOFF.json'),relative(I/'INSPECTED-REQUEST.json'),relative(Path(__file__))}
    required.update(relative(OUT/name) for name in ['original-reading-notes.json','native-inspection-result.json','native-event-controls.json','three-method-v3-manifest.json','copy-provenance.json'])
    for key in ['context','payloads','source_context','operational_policy']:
        read_ref(request[key]); required.add(request[key]['path'])
    operations = {op['mim_id']:op for op in request['operations']}
    notes_by_id = {j['mim_id']:j for j in notes['notes']}
    targets=[]; qualified=[]
    for payload, stub in zip(payloads,stubs,strict=True):
        mid=payload['mim_id']; op=operations[mid]; j=copy.deepcopy(notes_by_id[mid])
        before=yaml.safe_load(read_ref(op['before'])); after=yaml.safe_load(read_ref(op['proposal']))
        assert payload['before']==before and payload['after']==after and payload['delta']==op['delta']
        assert before['mim_id']==after['mim_id']==mid and after['curation_history'][:-1]==before['curation_history']
        assert payload['residual_holds']==op['residual_holds']==op['inherited_holds']
        assert op['before']==j['before']
        if mid in {'MIM:0000264','MIM:0000361','MIM:0000068'}:
            prior_path=Path(notes['request']['path']).parents[2]/j['after']['path']
            prior=yaml.safe_load(read(prior_path,j['after']['sha256']))
            expected=copy.deepcopy(prior); event=expected['curation_history'][-1]
            event['changes'] += '\n\n'+event.pop('notes')
            assert after==expected
            j['v3_qualification']='Only the final event narrative representation changed: original notes survive verbatim in changes, with original timestamp, author, model and science retained.'
        else:
            assert op['proposal']['sha256']==j['after']['sha256'] and digest(op['delta'])==j['delta_sha256']
            j['v3_qualification']='Original eleven-operation scientific delta and afterimage remain exact.'
        j['before']=op['before']; j['after']=op['proposal']; j['delta_sha256']=digest(op['delta'])
        j['captured_corrective_evidence']=[next(e for e in op['evidence'] if e['sha256']==ref['sha256'] and Path(e['path']).name==Path(ref['path']).name) for ref in j['captured_corrective_evidence']]
        for ref in [op['before'],op['proposal'],*op['evidence']]:read_ref(ref);required.add(ref['path'])
        assert stub['semantic_digest']=={'algorithm':'sha256-canonical-json-v1','sha256':digest(payload),'description':DESC}
        target=copy.deepcopy(stub);target.update(path=request['payloads']['path'],label=before['preferred_term']+' — exact source correction',owner_paths=[{'repository':REPO,'path':request['payloads']['path'],'role':'proposed source correction'}]);targets.append(target);qualified.append(j)
    save('qualified-reading-notes.json', {'at':now(),'author':AUTHOR,'state':'EXACT_CURRENT_INPUT_QUALIFICATION_BEFORE_NATIVE_REVIEW_INSPECT','notes':qualified,'scientific_approval':False})
    required.add(relative(OUT/'qualified-reading-notes.json'))
    save('targets.json', {'targets':targets})
    inspected, receipt=run('record-review-inspect',['inspect','--targets',str(OUT/'targets.json'),*[arg for name in sorted(required) for arg in ['--input',name]]])
    assert inspected['source']['git_revision']==HEAD
    save('INSPECT-HANDOFF.json', {'started_at':started,'finished_at':now(),'native_inspection_handoff':pin(I/'HANDOFF.json'),'request':pin(I/'INSPECTED-REQUEST.json'),'inspection_stdout':pin(OUT/'record-review-inspect.stdout'),'inspection_receipt':receipt,'targets':pin(OUT/'targets.json'),'qualified_notes':pin(OUT/'qualified-reading-notes.json'),'state':'RECORD_REVIEW_INSPECT_COMPLETED_FINAL_ASSESSMENT_PENDING'})
    print(json.dumps({'inspection':pin(OUT/'INSPECT-HANDOFF.json'),'targets':14,'exit_code':0}))

def save_phase():
    handoff,native_result,request,payloads,stubs=current()
    h=json.loads((OUT/'INSPECT-HANDOFF.json').read_bytes())
    inspected=json.loads(read(Path(h['inspection_stdout']['path']),h['inspection_stdout']['sha256']))
    notes=json.loads(read(Path(h['qualified_notes']['path']),h['qualified_notes']['sha256']))
    targets=json.loads(read(Path(h['targets']['path']),h['targets']['sha256']))['targets']
    source={x['path']:x['sha256'] for x in inspected['source']['inputs']}
    for name,expected in source.items():read(ROOT/name,expected)
    operations={op['mim_id']:op for op in request['operations']};judgments={j['mim_id']:j for j in notes['notes']}
    accessed=now();evidence=[];assessments=[]
    def ev(eid,kind,path,support,summary,locator='/'):
        assert path in source
        evidence.append({'evidence_id':eid,'kind':kind,'reference':path,'locator':locator,'accessed_at':accessed,'support':support,'summary':summary,'snapshot_sha256':source[path]})
    ev('native-inspection','validation',relative(OUT/'native-inspection-result.json'),'context_only','Actual root-owned corrected source inspection exited zero. Structural success does not grant science approval.')
    ev('mapping-policy','authority','MAPPING_SEMANTICS.md','supports','Persistent identity and exact owner-specific deltas survive; method grade and identity predicate are independent; unsupported aliases cannot resolve and broad form links are not subclass assertions.','Permanent identity; sections 0–3')
    ev('source-context','record_content',request['source_context']['path'],'context_only','Complete 1879-case/1022-original-origin accounting and original canary source context are retained; no source/role/quantity/release hold is cleared.')
    ev('event-controls','validation',relative(OUT/'native-event-controls.json'),'context_only','Actual native event helper reconstructed all fourteen final events; original three v2 notes failures were reproduced. Original author/timestamps and all narrative content are retained.')
    locators={'facts.json':{'MIM:0000967':'/CHEBI:16494/statements','MIM:0001893':'/CHEBI:15940/statements','MIM:0000361':'/CHEBI:2769/statements','MIM:0000068':'/CHEBI:15930/statements'},'ADDITIONAL-SCOPE-DATABASE.json':{'MIM:0000967':'/facts/CHEBI:30313','MIM:0001893':'/facts/CHEBI:32544'}}
    for number,payload in enumerate(payloads,1):
        mid=payload['mim_id'];op=operations[mid];j=judgments[mid];ids=['mapping-policy','source-context','event-controls']
        for suffix,ref,summary in [('before',op['before'],'Complete current owner, original evidence and history; scope and restrictions retained.'),('after',op['proposal'],'Exact attributed correction; permanent identity, earlier history, every unrelated field and all residual holds retained.')]:
            eid=f'owner-{number}-{suffix}';ev(eid,'record_content',ref['path'],'supports',summary);ids.append(eid)
        for n,ref in enumerate(j['captured_corrective_evidence'],1):
            assert ref in op['evidence'];name=Path(ref['path']).name
            kind='primary_source' if name in ['SUPPLIER-WEB-CAPTURE.json','web-primary.txt','web-additional-primary.txt'] else 'database'
            if name in ['1229.json','issue-317.stdout','issue-799.stdout']:kind='prior_review'
            if name=='historical-PC-import.yaml':kind='record_content'
            if name=='primary-retrieval-v1.json':kind='validation'
            eid=f'owner-{number}-source-{n}'
            ev(eid,kind,ref['path'],'context_only' if kind in ['prior_review','validation'] else 'supports',j['current_scientific_reasoning'],locators.get(name,{}).get(mid,'Captured target-specific source content; see complete proposed delta and notes'))
            ids.append(eid)
        dims=[('curation_action','apply_exact_source_delta','Only the exact source correction is supported.'),('delta_sha256',digest(op['delta']),'Canonical JSON digest of the complete exact delta.'),('permanent_mim_id',mid,'Unchanged permanent record identity.'),('residual_holds_json',native_text(op['residual_holds']),'Exact inherited holds remain, with no release clearance.'),('rejected_identifiers_json',native_text(op['rejected_identifiers']),'Only listed disproved owner-specific resolving identities are removed.'),('corrective_delta_findings','none','No unresolved finding about this exact corrective delta.'),('residual_findings_json',native_text([]),'No new or superseding native finding is asserted; original issue/hold obligations remain verbatim and open at their original scope.'),('review_scope','exact_source_delta_only','Not whole-record, role, quantity, source-binding, subclass or publication approval.')]
        assessments.append({'assessment_id':'source-delta-'+mid.split(':')[1],'area':'grounding','topic':j['topic'],'outcome':'supported','summary':j['current_scientific_reasoning'],'target_ids':[mid],'evidence_ids':ids,'dimensions':[{'name':n,'value':v,'definition':d,'evidence_ids':ids} for n,v,d in dims],'details':j['limits_and_residual_holds']+' '+j['v3_qualification']+' Current final inspected payloads and raw corrective evidence were reviewed; later application, regeneration and publication review remain separate.'})
    tids=[t['target_id'] for t in targets]
    content={'schema_version':'1.0.0','review_id':datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-fourteen-source-deltas-current-primary','kind':'batch','repository':REPO,'title':'Current primary scientific review of fourteen exact source corrections','started_at':h['started_at'],'finished_at':now(),'reviewer':{'identity':AUTHOR,'kind':'agent','model':'Codex (exact model identifier not supplied)','independence':'self_review','independence_basis':'This primary reviewer authored the three #1386 method proposals and their attribution/API repairs. It independently read current source bytes and captured scientific evidence but does not claim independence from its own proposals; the separate skeptical reviewer is mandatory.'},'skill':'review-ingredients','completion':'completed','verdict':'pass_with_limitations','native_verdict':'SUPPORTED_EXACT_SOURCE_DELTAS_ONLY_ALL_RESIDUAL_HOLDS_RETAINED','scientific_review':True,'summary':'Support fourteen individually assessed exact current corrections. Permanent identities, historical source scope, all scientific holds and source/publication gates remain intact. The three event representation fixes preserve original notes verbatim and actual author/timestamps; no identity decisions derive from API compatibility.','source':inspected['source'],'scope':{'description':'Fourteen exact native source-correction payloads, complete before/after delta and all residual holds.','selection':'The fourteen current targets emitted by the successful corrected S3 native inspection, bound by actual semantic digests.','coverage':'full','population_size':14,'reviewed_target_ids':tids,'exclusions':[{'target':'All other campaign owners and the full 1879-case/1022-origin scientific scope','reason':'This bounded correction review preserves their existing evidence and holds; it does not replace their required science.'},{'target':'Final SSSOM/source identity/KGX/publication decisions','reason':'Require separate review on actual post-application generated bytes.'},{'target':'Existing multi-owner #1229/#1193 and NTA/Na2hpo4 method uncertainty','reason':'No broader finding closure, inferred method correction or source/role clearance.'}]},'targets':targets,'checks':[{'check_id':'successful-native-inspection','name':'Actual corrected S3 source-successor inspection','status':'passed','required':True,'summary':'Shared root-owned native invocation exited zero and returned fourteen actual full payloads; exact result/handoff read and pinned.','target_ids':tids,'exit_code':0,'expected_exit_code':0,'evidence_ids':['native-inspection']},{'check_id':'current-inputs-and-history','name':'Exact current payload/evidence/delta/history/hold binding','status':'passed','required':True,'summary':'Own bounded preflight checked all required pins, current full before/after payloads, stable IDs, history prefix, unchanged original eleven deltas and exact three-event v3 representation changes.','target_ids':tids,'exit_code':0,'expected_exit_code':0,'evidence_ids':['native-inspection','event-controls','mapping-policy']},{'check_id':'native-record-review-inspect','name':'Own native record review inspection before final assessment','status':'passed','required':True,'summary':'Own helper captured current HEAD and complete input union before this final assessment and save.','command':h['inspection_receipt']['command'],'target_ids':tids,'exit_code':h['inspection_receipt']['exit_code'],'expected_exit_code':0,'evidence_ids':['native-inspection']}],'evidence':evidence,'assessments':assessments,'findings':[],'actions':[],'limitations':['Exact-delta support only; no whole-record, role, quantity, source binding, subclass or final export approval.','Original 1879 cases/1022 origins, W01 thirteen/W09 eight historical review obligations, suppressions and all residual scientific holds remain unchanged.','Primary reviewer authored the three #1386 proposals; this is self-review and cannot substitute for the independent skeptical report or prepared-set technical review.','Current captured primary/database bytes were read without paid research or a new literature sweep; old proposals/reviews are not treated as primary science or inherited current approval.','Existing multi-owner findings remain open at their full scope. Empty findings means no new corrective finding, not retirement of inherited obligations.','Acriflavine fixed structure/ratio claims remain held; two corrected invalid-CAS owners retain inherited WITHHOLD; no source supplier/lot or role acceptance is transferred.'],'links':sorted({url for op in operations.values() for url in op['issues']})}
    save('review-content.json',content)
    _,valid=run('record-review-validate',['validate',str(OUT/'review-content.json')])
    saved,saved_receipt=run('record-review-save',['save','--content',str(OUT/'review-content.json')])
    rp=Path(saved['review']);mp=Path(saved['markdown']);report=yaml.safe_load(rp.read_bytes())
    assert report['reviewer']['identity']==AUTHOR and len(report['assessments'])==14
    refs={}
    for assessment in report['assessments']:
        mid=assessment['target_ids'][0];op=operations[mid];dims={x['name']:x['value'] for x in assessment['dimensions']}
        assert dims['delta_sha256']==digest(op['delta']) and dims['residual_holds_json']==native_text(op['residual_holds']) and dims['residual_findings_json']==native_text([])
        refs[mid]={'path':relative(rp),'sha256':sha(rp.read_bytes()),'markdown_sha256':sha(mp.read_bytes()),'target_id':mid,'assessment_id':assessment['assessment_id']}
    for op in request['operations']:read_ref(op['before']);read_ref(op['proposal'])
    result={'at':now(),'status':'CURRENT_PRIMARY_FOURTEEN_SOURCE_DELTAS_NATIVE_SAVED','review':pin(rp),'markdown':pin(mp),'references':refs,'reviewed_targets':14,'verdict':'pass_with_limitations','record_review_inspect':h['inspection_receipt'],'record_review_validate':valid,'record_review_save':saved_receipt,'native_inspection_handoff':pin(I/'HANDOFF.json'),'source_head':HEAD,'maintained_source_writes':False,'native_successor_phases':False,'collection_check':'PENDING_SINGLE_SHARED_CHECK_AFTER_BOTH_REPORTS_SAVE','scientific_scope':'Exact corrective deltas only; all original holds retained.'}
    result_pin=save('HANDOFF.json',result)
    print(json.dumps({'handoff':result_pin,'review':result['review'],'markdown':result['markdown'],'targets':14}))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('phase',choices=['inspect','save']);args=parser.parse_args()
    inspect_phase() if args.phase=='inspect' else save_phase()
