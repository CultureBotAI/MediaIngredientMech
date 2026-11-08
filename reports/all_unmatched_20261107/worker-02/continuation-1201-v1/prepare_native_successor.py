"""Prepare an immutable native source-review successor from reviewed outcomes.

Native inspect/validate/save remain authoritative; this script is not a review
generator that can substitute for primary research or skeptical assessments.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import yaml

S=Path(__file__).resolve().parent
R=S.parent
T=Path('.temp/all-unmatched-worker-02/continuation-1201-v1/native-v2')
PY='.temp/all-unmatched-worker-02/venv/bin/python'
PRIOR=Path('reviews/structured/20261108T054002Z-w02-all-unmatched-source-review/review.yaml')


class PlainDumper(yaml.SafeDumper):
    def ignore_aliases(self,data):return True


def load(path):return json.loads(path.read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def relative(path):return str(path.relative_to(Path.cwd())) if path.is_absolute() else str(path)
def utc(value):
    if value.endswith(' UTC'):value=value[:-4]+'+00:00'
    return datetime.fromisoformat(value.replace('Z','+00:00')).astimezone(timezone.utc).isoformat().replace('+00:00','Z')


def main():
    ds=load(S/'decisions.json')['decisions'];es=load(S/'evidence.json')['evidence'];ps=load(S/'proposals.json')['proposals']
    coverage=load(S/'integration/independent-review-coverage.json')
    prior=yaml.safe_load(PRIOR.read_text())
    assert len(ds)==188 and all(d['independent_review']['status']=='complete' for d in ds)
    now=datetime.now(timezone.utc);finish=utc(now.isoformat())
    targets=[]
    for d in ds:
        target={'target_id':d['case_id'],'path':relative(R/'context/frozen-shard-02.json'),'selector':f'cases[case_id={d["case_id"]}]','label':d['source']['source_label'],'kind':'snapshot_row','record_class':'Frozen source ingredient case'}
        if d['owner_records']:
            target['owner_paths']=[{'repository':'CultureBotAI/MediaIngredientMech','path':o['path'],'role':'Actual baseline comparison owner; no complete-owner or release approval'} for o in d['owner_records']]
        else:
            target['ownership_note']='Source-only case. No actual baseline owner was established; proposed new owner paths are proposals, never fabricated maintained targets.'
        targets.append(target)
    T.mkdir(parents=True,exist_ok=True)
    target_path=T/'native-targets.yaml'
    if target_path.exists():raise FileExistsError(target_path)
    target_path.write_text(yaml.dump({'targets':targets},Dumper=PlainDumper,sort_keys=False,allow_unicode=True))
    checks_paths={
        'accounting':S/'validation/structural-final.json',
        'native-proposals':S/'validation/native-final/receipt.json',
        'labels':S/'validation/labels-final.json',
        'helper-tests':S/'validation/helper-tests-final.log',
        'overlap':S/'cross-shard-overlaps.json',
    }
    required=[S/p for p in ('decisions.json','evidence.json','proposals.json','succession.json','subagent-scopes.json','integration/independent-review-coverage.json','integration/shared-owner-composition.json')]
    inputs={relative(p) for p in required+list(checks_paths.values())+[PRIOR]}
    inputs|={'MAPPING_SEMANTICS.md','schema/record_review.yaml','conf/record_review.yaml','docs/record-review-profile.md','docs/stock_components.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','uv.lock'}
    inputs|={o['path'] for d in ds for o in d['owner_records']}
    inputs|={relative(R/e['capture']['path']) for e in es if e['capture']['root']=='artifact'}
    inputs|={relative(R/p['after_capture']['path']) for p in ps}
    command=[PY,'-B','scripts/record_review.py','inspect','--targets',str(target_path)]
    for path in sorted(inputs):command+=['--input',path]
    process=subprocess.run(command,capture_output=True,text=True)
    (S/'validation/native-inspect-v2.log').write_text(process.stderr)
    if process.returncode:raise RuntimeError(process.stderr)
    inspection=json.loads(process.stdout)
    (S/'validation/native-inspection-v2.json').write_text(json.dumps(inspection,indent=2)+'\n')
    kinds={'primary_source':'primary_source','source_snapshot':'record_content','ontology':'authority','native_record_review':'prior_review','independent_review':'prior_review','unsuccessful_search':'search','local_validation':'validation'}
    evidence=[]
    for e in es:
        cap=e['capture'];reference=relative(R/cap['path']) if cap['root']=='artifact' else 'Frozen queue preliminary-v5/'+cap['path']
        item={'evidence_id':e['evidence_id'],'kind':kinds[e['kind']],'reference':e.get('url') or reference,'locator':reference+'; '+e['locator'],'accessed_at':utc(e['accessed_at']) if e.get('accessed_at') else finish,'support':'context_only' if e['kind']=='unsuccessful_search' else 'partial','summary':e['supports_or_contradicts'],'snapshot_sha256':cap['sha256']}
        if item['kind']=='search':item['search_scope']=e['locator']+'; '+e['supports_or_contradicts']
        evidence.append(item)
    for name,path in checks_paths.items():
        evidence.append({'evidence_id':'w02-v2-check-'+name,'kind':'validation','reference':relative(path),'accessed_at':finish,'support':'context_only','summary':'Actual bounded validation/observation receipt; no scientific or release authority is conferred by a structural pass.','snapshot_sha256':sha(path)})
    ids=[d['case_id'] for d in ds];pid_targets=[d['case_id'] for d in ds if d['proposal_ids']]
    label_results=load(checks_paths['labels'])['results']
    unavailable=[r for r in label_results if r['status']=='UNAVAILABLE_ADAPTER']
    mismatches=[r for r in label_results if r['status'] not in ('UNAVAILABLE_ADAPTER','OK_CANONICAL','NO_ONTOLOGY_MAPPING','REGISTRY_SELF_CONSISTENT')]
    assert not mismatches, mismatches
    checks=[
        {'check_id':'full-shard-accounting','name':'188-case immutable accounting','status':'passed','required':True,'summary':'All188 frozen cases and original source/occurrence digests retained; every revised case and payload has separate skeptical review.','target_ids':ids,'command':'audit_worker_outcomes_v1.py; exact resolved argv and hashes retained in validation/structural-final.json','exit_code':0,'evidence_ids':['w02-v2-check-accounting']},
        {'check_id':'native-writer-partonomy','name':'Exact proposed owners and complete catalog overlay','status':'passed','required':True,'summary':f'{len(ps)} exact active payloads passed native closed-schema guarded writers and round trips; full proposed catalog overlay passed native partonomy; maintained catalog hashes unchanged. Unknown-field negative write rejected.','target_ids':pid_targets,'command':'validate_successor_proposals.py --proposals proposals.json --out validation/native-final; exact paths in receipt','exit_code':0,'evidence_ids':['w02-v2-check-native-proposals']},
        {'check_id':'canonical-labels','name':'Ontology labels and local registry consistency','status':'failed' if unavailable else 'passed','required':False,'summary':f'{len(label_results)} mappings checked. {len(unavailable)} unavailable ontology adapter(s) retained explicitly. Local registry self-row consistency does not establish source identity.','target_ids':pid_targets,'command':'validate_successor_labels.py validation/labels-final.json proposals.json','exit_code':int(bool(unavailable)),'evidence_ids':['w02-v2-check-labels']},
        {'check_id':'helper-negative-tests','name':'Successor/composition/reviewer guard tests','status':'passed','required':True,'summary':'Actual failure-case tests cover frozen-source changes, author self-review, changed scientific decisions, missing review reasoning and destructive composition.','target_ids':ids,'command':PY+' -B -m unittest discover -s '+relative(S)+" -p 'test_*.py'",'exit_code':0,'evidence_ids':['w02-v2-check-helper-tests']},
        {'check_id':'cross-shard-observation','name':'Read-only cross-shard conflict observation','status':'passed','required':True,'summary':'Exact observed peer ledgers/hashes retained as reconciliation leads. No winning owner, equivalence or peer review is inferred.','target_ids':pid_targets,'command':'observe_cross_shard.py --proposals proposals.json --out cross-shard-overlaps.json','exit_code':0,'evidence_ids':['w02-v2-check-overlap']},
        {'check_id':'maintained-release-gates','name':'Maintained synchronization and release','status':'not_applicable','required':False,'summary':'Worker proposal-only scope; no maintained writes or downstream rebuild authorized. Coordinator must integrate guarded changes and independently validate all released payloads.','target_ids':ids},
    ]
    previous_findings={f['finding_id']:f for f in prior['findings']}
    def previous(fid):return {'repository':'CultureBotAI/MediaIngredientMech','review_id':prior['review_id'],'finding_id':fid}
    assessments=[];findings=[];actions=[]
    for i,d in enumerate(ds):
        refs=list(dict.fromkeys(d['evidence_ids']+d['independent_review']['evidence_ids']))
        assessments.append({'assessment_id':f'case-{i:03d}','area':'identity','topic':d['source']['source_label'],'outcome':'unknown' if d['disposition']=='unresolved' else ('concern' if d['disposition'] in ('supplied_form_correction','malformed_or_nonchemical_token') else 'supported'),'summary':d['reasoning'],'details':d['applicability']+' Remaining scope: '+(d['missing_requirement'] or 'All explicit source, complete-owner and publication holds remain separate.'),'target_ids':[d['case_id']],'evidence_ids':refs})
        old_id=f'source-requirement-{i:03d}'
        if d['missing_requirement'] or old_id in previous_findings:
            f={'finding_id':old_id,'issue_key':f'w02-source-{d["case_id"].split(":")[1][:24]}','category':'identity','severity':'informational','status':'open' if d['proposal_ids'] else 'deferred','certainty':'confirmed','title':'Current bounded source assessment and remaining integration scope','description':d['missing_requirement'] or 'Source scope has an isolated proposal. Complete-owner, duplicate and release obligations remain as explicitly recorded in the decision and its evidence.','target_ids':[d['case_id']],'evidence_ids':refs,'ownership_note':'Exact frozen source case only. This successor records completed lookup/proposal work separately from unresolved scientific facts and complete-owner/release holds.','external_issues':d['issue_refs']}
            if f['status']!='open':f['disposition_reason']='The current reason names the case-specific scientific uncertainty or already represented identity. It does not defer feasible proposal work merely for missing ontology terms, later curation or receiving-medium unit repair.'
            if old_id in previous_findings:f['previous_occurrences']=[previous(old_id)]
            findings.append(f)
    old_by_pid={f['title']:f for f in prior['findings'] if f['finding_id'].startswith('proposal-')}
    for i,p in enumerate(ps):
        predecessors=[]
        if p['proposal_id'] in old_by_pid:predecessors=[old_by_pid[p['proposal_id']]]
        for fragment in p.get('supersedes_proposals',[]):
            pid=fragment['proposal_id']
            if pid in old_by_pid and old_by_pid[pid] not in predecessors:predecessors.append(old_by_pid[pid])
        fid=f'active-proposal-{i:03d}'
        f={'finding_id':fid,'issue_key':predecessors[0]['issue_key'] if predecessors else 'w02-v2-'+p['proposal_id'],'category':'grounding','severity':'major','status':'open','certainty':'confirmed','title':p['proposal_id'],'description':p['description']+' Exact isolated after payload '+p['after_capture']['path']+' SHA256 '+p['after_capture']['sha256']+'. This remains a proposed remedy, not an applied correction.','target_ids':p['case_ids'],'evidence_ids':p['evidence_ids'],'ownership_note':'Intended owner '+p['owner_path']+'; original before hashes and cross-shard conflicts must be reconciled before application.','rule_id':'MAPPING_SEMANTICS sections3/6 and add-media','native_severity':'P2','normalization_reason':'Unintegrated scoped curation requires coordinator action and independent full-owner release review.'}
        if predecessors:f['previous_occurrences']=[previous(x['finding_id']) for x in predecessors]
        findings.append(f)
        actions.append({'action_id':f'coordinator-proposal-{i:03d}','description':'Reconcile and, if supported, integrate '+p['proposal_id']+' through guarded maintained workflows.','finding_ids':[fid],'target_ids':p['case_ids'],'ownership_note':'Do not overwrite a changed baseline or select a competing worker proposal by ordering.','acceptance_checks':['Preserve source alternatives, raw provenance and all explicit source/owner/release holds.','Reconcile peer overlaps and any new owner/component dependencies against final published bytes.','Withdraw inherited approval for changed owners; synchronize maintained YAML/SSSOM and run required release gates only in coordinator integration.']})
    changed=sum(x['scope']=='successor_case' for x in coverage['cases'])
    review={'schema_version':'1.0.0','review_id':now.strftime('%Y%m%dT%H%M%SZ')+'-w02-issue1201-source-successor','kind':'batch','repository':'CultureBotAI/MediaIngredientMech','title':'Worker02 complete no-change cohort reassessment under issue1201','started_at':utc(load(S/'acceptance.json')['recorded_at']),'finished_at':finish,'reviewer':{'identity':'codex_worker02_root; per-case authors/reviewers retained in immutable review coverage','kind':'agent','independence':'self_review','independence_basis':'Root compiled the native bundle and authored integration. Distinct in-process reviewers inspected the exact changed source decisions and payloads; root does not claim independence from its own integration.'},'skill':'add-media; review-ingredients','completion':'completed','verdict':'needs_curation','scientific_review':True,'summary':f'All145 prior no-proposal cases reassessed against complete source contexts and current baseline owners; all188 cases remain accounted. {changed} exact successor decisions have new independent review, including explicit shared-owner backlink updates; unchanged predecessor decisions retain their prior independent evidence. {len(ps)} active isolated proposals remain. No maintained data or release status changed.','source':inspection['source'],'targets':targets,'scope':{'description':'Complete145-case no-proposal cohort, plus explicitly identified original proposal-case backlinks affected by combined successor payloads. Full188-case accounting retains unaffected predecessor conclusions.','selection':'Frozen shard02 SHA256993e393b8a50e6061e4a9863bd60b3ab2a48ee584907a97e3066c1cbc03d6db0; source-case ordering unchanged.','coverage':'full','population_size':188,'reviewed_target_ids':ids,'exclusions':[{'target':'Other worker case decisions, complete owner approval, roles, exports, release holds and downstream rebuild','reason':'Outside this source-review continuation; cross-shard observations are reconciliation leads only.'}]},'checks':checks,'evidence':evidence,'assessments':assessments,'findings':findings,'actions':actions,'limitations':['All prior published artifacts and reviews remain immutable. Successor findings explicitly reference affected predecessors and never silently retire source, owner or release obligations.','Source recipe headings are not assumed to be premixed ingredients; source-qualified preparation identities do not imply unqualified global aliases or equivalence between alternative species, formulations or versions.','Unstated solvent, final volume, exact hydrate, supplier version and undisclosed constituents remain unknown; schema validation never supplies those scientific facts.','Primary captures retain their actual original retrieval times. Unavailable downloads and approval-refused retrievals remain documented limitations, not evidence that a source does not exist.','Unchanged unavailable ontology adapters and registry consistency checks retain their stated limits; complete label/source/consumer compatibility remains a coordinator obligation.','No maintained data, canonical mappings, semantic/companion selectors or publication inputs were edited; no merges, external research sessions or downstream rebuilds were performed.'],'related_reviews':[{'repository':'CultureBotAI/MediaIngredientMech','review_id':prior['review_id'],'relationship':'Immutable source-case completeness successor; affected finding lineage explicit, all complete-owner and release holds retained.'}],'links':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1201','https://github.com/CultureBotAI/MediaIngredientMech/pull/1158']}
    dest=T/'native-review-final.yaml'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(yaml.dump(review,Dumper=PlainDumper,sort_keys=False,allow_unicode=True))
    receipt={'prepared_at':finish,'review_id':review['review_id'],'command':command,'exit_code':process.returncode,'target_count':188,'assessment_count':len(assessments),'findings':len(findings),'input_count':len(inputs),'prepared_document':str(dest),'saved':False}
    (S/'validation/native-preparation.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='command'}))


if __name__=='__main__':main()
