"""Issue-scoped isolated proposal writer. No maintained/source writes.

All metadata entries are rebound by owner, mapping attachment, full object and
duplicate ordinal before mutation. Native closed-schema writer and history
helper are unchanged. Existing output is refused; no atomicity claim is made.
"""
import copy, datetime, hashlib, json, shutil
from collections import defaultdict
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event

R=Path('reports/all_unmatched_20261107/worker-07')
S=R/'successors/issues1226-1237-v1'
P=Path('.temp/worker07-issues1226-1237-v1')
OLD=R/'successors/issue1203-v1'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def objsha(x):return hashlib.sha256(canonical(x)).hexdigest()
def put(p,b):
    assert not p.exists(), f'refuse overwrite: {p}'
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def jp(p,x):put(p,(json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode())
def cap(p):return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)}
def rebind(before, digest, row):
    assert digest==row['payload']['sha256'],'stale owner'
    assert row['enum']=='EvidenceTypeEnum' and row['type_pointer']==f"/ontology_mapping/evidence/{row['index']}/evidence_type",'wrong enum or locator'
    mapping=before['ontology_mapping']; context={k:v for k,v in mapping.items() if k!='evidence'}
    assert context==row['mapping_context'] and objsha(context)==row['mapping_context_sha256'],'stale mapping attachment'
    objects=mapping['evidence']; o=objects[row['index']]
    assert o==row['full_object'] and objsha(o)==row['full_object_sha256'],'stale complete object'
    matches=[i for i,v in enumerate(objects) if v==o]
    assert len(matches)==row['duplicate_total'] and matches.index(row['index'])+1==row['duplicate_ordinal_1based'],'duplicate ambiguity'
    assert row['baseline_match_index'] is None,'inherited evidence excluded'
    assert o['evidence_type']==row['before_value']=='MANUAL_CURATION'
    assert row['suggested_value']=='LLM_SUGGESTION','unsupported suggestion'

TRIS='A-PROPOSAL-NBRC1507_Tris_HCl_01M_pH75_Buffer'
CYS='B-PROPOSAL-jcm_1479_l_cysteine_hcl_monohydrate_5_percent_ph7'
HUT='W07-COMBINED-JCM900-JCM979-Hutner'
DSM=['A-PROPOSAL-DSM590_Hutner_Basal_Salts','B-PROPOSAL-dsmz_1144_hutner_basal_salts']
SCI={
TRIS:'Issue1237 W01-PREP-B-001: NBRC1507 names 0.1 M Tris/HCl (pH7.5) as a supplied buffer. It does not enumerate free hydrochloric acid as a separately added component. Retain the named buffer moiety and nominal strength; the complete constituent list, solvent, preparation and neutralization ratio remain unknown. No dry Tris-HCl substitution or neutralization chemistry is inferred.',
CYS:'Issue1237 W01-PREP-B-002/CHEM-COMP-003: JCM1479 explicitly specifies the L-cysteine hydrochloride monohydrate 5% stock at pH7.0. It is a preparation, separate from solid solute. Unreported pH in another 5% stock establishes neither difference nor equivalence. Percentage basis, carrier and titrant/preparation remain unreported; a common-stock relationship requires affirmative source evidence.',
HUT:'Issue1237 MIN-F02: Comparison with DSM590/1144 remains unresolved at complete chemical/preparation scope. JCM149 Metals44 prints EDTA·2Na and MnSO4·xH2O; DSM prints Na-EDTA and MnSO4·H2O plus a few drops of concentrated H2SO4. Unspecified hydration, salt detail or an unreported acid step does not prove incompatibility or equivalence. The historical malformed molybdate strings remain literal unresolved assertions. Positively different JCM149 outer Hutner mineral base has MgSO4·7H2O 14.45 g versus 29.7 g in JCM900/979; that outer recipe is distinct from the nested Metals44 reference. JCM631 also retains its positively different Mg/Ca quantities and vitamin inputs. All present immediate inputs remain unchanged; COMPLETE is source-list completeness, not resolved molecular identity.'
}
HOLD='Issue1237 MIN-F01: DSM590/1144 support one nominal Hutner preparation. Both source origins and histories remain retained inputs to the coordinator root C union. Neither is selected as a winner here and these two candidates are not independently co-installable. Preserve CaCl2·2H2O 3.335 g versus 3.34 g rounding, both malformed molybdate literals and both Metals44/process accounts. Historical molecular clarification is a separate requirement from the settled nominal union; no new union is composed by W07.'

def main():
    allow=json.loads((P/'provenance-author/allowlist-v1.json').read_text())
    by=defaultdict(list)
    for row in allow['rows']:by[row['proposal_id']].append(row)
    d=json.loads((OLD/'decisions.json').read_text()); e=json.loads((OLD/'evidence.json').read_text()); p=json.loads((OLD/'proposals.json').read_text())
    assert len(d['decisions'])==188 and len(e['evidence'])==1498 and len(p['proposals'])==100
    originals={x['proposal_id']:copy.deepcopy(x) for x in p['proposals']}
    prepared=[]; mutations=[]
    for prop in p['proposals']:
        pid=prop['proposal_id']; f=R/prop['after_capture']['path']; digest=sha(f)
        assert digest==prop['after_capture']['sha256']
        old=yaml.safe_load(f.read_text()); new=copy.deepcopy(old)
        rows=by.get(pid,[])
        for row in rows:rebind(old,digest,row)
        for row in rows:new['ontology_mapping']['evidence'][row['index']]['evidence_type']=row['suggested_value']
        if pid==TRIS:
            assert old['components'][1]=={'component_name':'Hydrochloric acid','reference_scope':'UNMAPPED'} and len(old['components'])==2
            new['components']=new['components'][:1]
            new['component_assertion']['notes']+=' '+SCI[pid]
        if pid in SCI:new['notes']+=' '+SCI[pid]
        if not rows and pid not in SCI:continue
        changes=[]
        if rows:changes.append('Issue1226: Reclassify only ontology_mapping.evidence indices '+','.join(str(x['index']) for x in rows)+' from MANUAL_CURATION to LLM_SUGGESTION. Exact complete objects were rebound to the frozen provenance audit; these entries record documented agent interpretation, not human-supplied evidence. Sources, claim notes and historical entries are retained; ComponentEvidenceTypeEnum and canonical SSSOM ManualMappingCuration are unchanged.')
        if pid in SCI:changes.append(SCI[pid])
        if pid==TRIS:changes.append('Remove the unsupported separate Hydrochloric acid has-part assertion; preserve UNKNOWN completeness and the first named buffer moiety at 0.1 M.')
        changes.append('Isolated report-only successor; no owner, role, source gate or release approval.')
        record_curation_event(new,curator='all-unmatched-20261107-worker07-root',action='CORRECT_ISOLATED_PROPOSAL_EVIDENCE',changes=' '.join(changes),llm_assisted=True)
        assert not validate_ingredient(new)
        dest=S/'proposed_owners'/f.name
        assert dest.resolve().is_relative_to((S/'proposed_owners').resolve()) and not dest.exists()
        prepared.append((prop,f,old,new,dest,rows))
    assert len(prepared)==len(by)==74
    # Preflight above is complete before any candidate output is written.
    for prop,f,old,new,dest,rows in prepared:
        before=S/'before'/f.name;put(before,f.read_bytes())
        write_validated_ingredient(new,dest,yaml_kwargs={'width':80})
        assert yaml.safe_load(dest.read_text())==new
        prop['supersedes_payload']={'publication_head':'ddef7355bf7814bd3b1a23b9d61327bea3ac75fe','after_capture':copy.deepcopy(prop['after_capture']),'reason':'Bounded issue1226 provenance correction'+(' and issue1237 source correction' if prop['proposal_id'] in SCI else '')}
        prop['after_capture']=cap(dest)
        prop['current_payload_review_scope']='New exact bytes require current independent review. Prior source-case outcomes/old native reviews remain historical scoped evidence, not approval of this successor owner.'
        if prop['proposal_id'] in SCI:prop['limitations']+=' '+SCI[prop['proposal_id']]
        mutations.append({'proposal_id':prop['proposal_id'],'owner_path':prop['owner_path'],'before':cap(before),'after':cap(dest),'metadata_entries':[{'audit_row_id':x['audit_row_id'],'pointer':x['type_pointer'],'before_object_sha256':x['full_object_sha256'],'after_object_sha256':objsha(new['ontology_mapping']['evidence'][x['index']]),'before':'MANUAL_CURATION','after':'LLM_SUGGESTION'} for x in rows],'science_correction':SCI.get(prop['proposal_id']),'old_history_count':len(old.get('curation_history',[])),'history_appended':new['curation_history'][-1]})
    for prop in p['proposals']:
        if prop['proposal_id'] in DSM:prop['installation_hold']=HOLD
    changed=[]
    science_cases={pid:originals[pid]['case_ids'] for pid in [TRIS,CYS,HUT]+DSM}
    for dec in d['decisions']:
        scope=[pid for pid,cases in science_cases.items() if dec['case_id'] in cases]
        if not scope:continue
        old=copy.deepcopy(dec); pid=scope[0]
        # The new scope supplement is explicit; old assertions are not erased.
        dec['issue1237_scope_correction']=SCI.get(pid,HOLD)
        if pid==CYS:
            dec['reasoning']=SCI[pid]
            dec['applicability']='Exact frozen source occurrence only. '+SCI[pid]
            dec['missing_requirement']='Percentage basis, carrier and pH-adjustment/preparation evidence or an authoritative common-stock relationship are needed for stronger formulation equivalence. The stated 5%, L-form, monohydrate and pH7 remain supported.'
        if pid==TRIS:dec['missing_requirement']='Complete preparation composition, solvent and neutralization recipe are unreported. These do not prevent retaining the literal named 0.1 M Tris/HCl pH7.5 buffer; no separate free HCl input is asserted.'
        if pid in DSM:dec['integration_hold']=HOLD
        if pid==HUT:dec['integration_hold']='MIN-F02 complete chemical/preparation comparison with DSM remains unresolved; no proved incompatibility or co-installation approval. Existing positive differences with JCM149/JCM631 remain. '+('Historical PARTIAL/separate-draft wording above is preserved pending issue-first coordinator triage; it does not override the selected complete immediate-input list.' if 'PARTIAL assertion' in old['reasoning'] else '')
        dec['issue_refs']=list(dict.fromkeys(dec.get('issue_refs',[])+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1237']))
        dec['predecessor_independent_review']=copy.deepcopy(dec.get('independent_review'))
        dec['independent_review']={'status':'pending','evidence_ids':[]}
        dec['evidence_ids']=list(dict.fromkeys(dec['evidence_ids']+['W07-I1237-FAMILY','W07-I1237-SOURCE-INDEX']))
        changed.append({'case_id':dec['case_id'],'before_object_sha256':objsha(old),'after_object_sha256':objsha(dec),'before':old,'scoped_correction':dec['issue1237_scope_correction']})
    for name in ['allowlist-v1.json','exclusions-v1.json','all-current-payload-scopes-v1.json','input-bindings-v1.json','summary-v1.json']:
        put(S/'provenance'/name,(P/'provenance-author'/name).read_bytes())
    put(S/'review/source-primary-index-v1.json',(P/'science-review/primary-index-v1.json').read_bytes())
    put(S/'review/source-supplementary-primary-index-v1.json',(P/'science-review/supplementary-primary-index-v1.json').read_bytes())
    caseids=[x['case_id'] for x in changed]
    for eid,path,kind,loc,support in [
      ('W07-I1237-FAMILY',S/'captures/findings-matrix-v2.json','source_snapshot','findings for entries619,624,657,669,705 and exact origin/capture bindings','Filed bounded family correction and retained missing-evidence/union scope; not source or release approval.'),
      ('W07-I1237-SOURCE-INDEX',S/'review/source-primary-index-v1.json','source_snapshot','primary_captures and original_finding_context','Rehash and exact source applicability; original capture timestamps preserved.')]:
        e['evidence'].append(dict(evidence_id=eid,capture=cap(path),kind=kind,locator=loc,supports_or_contradicts=support,url=None,case_ids=caseids))
    jp(S/'mutation-ledger.json',{'author':'/root','provenance_allowlist_author':'/root/provenance1226_analysis','issues':[1226,1237],'metadata_entry_count':sum(len(x['metadata_entries']) for x in mutations),'changed_payloads':mutations,'changed_cases':changed,'no_approval_transfer':True,'pending_union':{'proposal_ids':DSM,'hold':HOLD}})
    for name,obj in [('decisions.json',d),('evidence.json',e),('proposals.json',p)]:jp(S/'draft-v1'/name,obj)
    jp(S/'retention.json',{'predecessor_head':'ddef7355bf7814bd3b1a23b9d61327bea3ac75fe','original_case_ids':[x['case_id'] for x in d['decisions']],'original_proposals':list(originals.values()),'retained_evidence_count':1498,'retained_evidence_capture':cap(OLD/'evidence.json'),'changed_case_ids':caseids,'changed_payload_ids':[x['proposal_id'] for x in mutations],'unchanged_payload_ids':[x['proposal_id'] for x in p['proposals'] if x['proposal_id'] not in by],'hold_count_not_identity_count':2,'pending_union':HOLD,'prior_packets':'All original scientific cores, captures, drafts, failed attempts, issue1203/1223 supplements, native reviews, sealed W10 and FAC/Polypeptone packets retained byte-identically.'})
    print(json.dumps({'cases':len(d['decisions']),'changed_scoped_cases':len(changed),'proposals':len(p['proposals']),'changed_payloads':len(mutations),'evidence':len(e['evidence']),'metadata_entries':sum(len(x['metadata_entries']) for x in mutations)}))
if __name__=='__main__':main()
