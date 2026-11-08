"""Bounded W02 evidence-status and active-owner proposal fragments.

Does not write maintained data. Review is independently authored after composition.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib, json, subprocess, sys
from pathlib import Path

W = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(W / 'src'))
import yaml
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import FrozenFile, no_alias
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.validation.write_validated import write_validated_ingredient

R = Path(__file__).resolve().parent
A = R.parent
OLD = A / 'continuation-1201-v1'
O = W / '.temp/w02-final-corrections-v1'
B = O / 'frozen-w04-review'
P = R / 'context/w02-final-issue-plan-v1'
OUT = R / 'root'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x): return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
def load(p): return json.loads(p.read_text())
def save(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('x') as f: json.dump(value, f, indent=2, ensure_ascii=False); f.write('\n')
def cap(p): return {'root':'artifact','path':str(p.relative_to(A)), 'sha256':sha(p)}
def copy_exact(p, to):
    to.parent.mkdir(parents=True, exist_ok=True)
    with to.open('xb') as f:f.write(p.read_bytes())
    assert sha(p)==sha(to)
    return cap(to)

def main():
    OUT.mkdir(exist_ok=False)
    snapshots=[FrozenFile.capture(OLD/(n+'.json')) for n in ['decisions','proposals','evidence']]
    decisions=load(OLD/'decisions.json')['decisions']
    props=load(OLD/'proposals.json')['proposals']
    evidence={e['evidence_id']:e for e in load(OLD/'evidence.json')['evidence']}
    original_cases=load(A/'decisions.json')['decisions']
    by_index={i:next(d for d in decisions if d['case_id']==x['case_id']) for i,x in enumerate(original_cases)}
    changes={}; extra=[]; rebound={}; proofs=[]
    for failure in load(P/'failed-capture-reproduction.json'):
        old=deepcopy(evidence[failure['evidence_id']]); path=A/old['capture']['path']
        assert sha(path)==failure['sha256']==old['capture']['sha256']
        assert 'Nothing found' in path.read_text(errors='replace')
        new=deepcopy(old); new['evidence_id']='w02-final-status-'+old['evidence_id']
        new['kind']='unsuccessful_search'
        new['locator']='Complete captured response contains Nothing found; no original recipe was returned by this exact route at this time.'
        new['supports_or_contradicts']='Failed retrieval only. No reagent, quantity, identity or preparation assertion is supported by these bytes. Later successful captures have separate source URLs, timestamps and hashes.'
        new['supersedes_evidence_id']=old['evidence_id']
        new['classification_author']='worker02 /root'
        extra.append(new); rebound[old['evidence_id']]=new['evidence_id']
        proofs.append({'old_evidence':old,'new_evidence':new,'reason':'Literal Nothing found response independently read; capture bytes/time unchanged.'})
    for eid,kind,reason in [
        ('c2-phc-commonchem-html','unsuccessful_search','The captured detail page renders Get detail failed and provides no CAS substance detail. It supports retrieval failure only, not identity.'),
        ('b2-chebi-30729','ontology','The response is the ChEBI phenanthroline ontology entry. It can support that ontology concept; it is not an original recipe or evidence identifying a named ammonium reagent.')]:
        old=deepcopy(evidence[eid]);path=A/old['capture']['path']; assert sha(path)==old['capture']['sha256']
        if 'commonchem' in eid: assert 'Get detail failed' in path.read_text()
        else:
            data=load(path);assert 'phenanthroline' in json.dumps(data).lower()
        new=deepcopy(old);new.update(evidence_id='w02-final-status-'+eid,kind=kind,locator=reason,supports_or_contradicts=reason,supersedes_evidence_id=eid,classification_author='worker02 /root')
        extra.append(new);rebound[eid]=new['evidence_id'];proofs.append({'old_evidence':old,'new_evidence':new,'reason':reason})
    # Exact prior independent primary recoveries, with original access times.
    for number,case_indices,reason in [
        (1033,[2,30],'Complete two-page JCM1033 bacmedia rendering: trace-elements section explicitly lists SrSO4 0.92 mg and CrK(SO4)2 x12H2O 0.50 mg. Separate recovered source; old JCM HTML remains unsuccessful.'),
        (1137,[152],'Complete two-page JCM1137 bacmedia rendering repeats Ca(NO3)2 x6H2O 49.40 mg in trace element solution. It confirms printed source scope, not the actual physical six-water reagent, procurement or a correction to tetrahydrate.')]:
        source=B/f'science/reviewer-b/captures/jcm{number}-bacmedia.body'
        receipt=load(source.with_suffix('.receipt.json'))
        assert sha(source)==receipt['sha256']
        captured=copy_exact(source, OUT/f'captures/jcm{number}-bacmedia.pdf')
        copy_exact(source.with_suffix('.receipt.json'),OUT/f'captures/jcm{number}-original-receipt.json')
        text=subprocess.check_output(['pdftotext','-layout',str(source),'-'])
        with (OUT/f'captures/jcm{number}-text.txt').open('xb') as f:f.write(text)
        extra.append({'evidence_id':f'w02-final-jcm{number}-recovered','kind':'primary_source','capture':captured,'url':receipt['url'],'accessed_at':receipt['started_at'],'locator':reason,'supports_or_contradicts':reason,'case_ids':[by_index[i]['case_id'] for i in case_indices],'original_capturer':'W04 /root/reviewer-b','current_assessor':'worker02 /root'})
    for i,d in by_index.items():
        revised=deepcopy(d)
        revised['evidence_ids']=[rebound.get(e,e) for e in d['evidence_ids']]
        if revised!=d:
            revised['applicability']+=' Successor #1241 evidence-status correction: failed captures are retained as unsuccessful searches, and ontology captures are distinguished from original recipes. Their raw bytes and access times are unchanged.'
            revised['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1241']))
            changes[d['case_id']]=revised
    for i in [2,30]:
        d=changes[by_index[i]['case_id']]
        d['evidence_ids'].append('w02-final-jcm1033-recovered')
        d['reasoning']+=' The original JCM1033 HTML attempt returned Nothing found; the separately captured complete bacmedia JCM1033 PDF corroborates the trace-element spelling. This later recovery does not change the old capture classification or approve receiving-medium quantities.'
    d=changes[by_index[152]['case_id']]
    d['reasoning']='MediaDive2013/JCM1137 print calcium nitrate hexahydrate. The old JCM HTML returned Nothing found; a separate complete bacmedia JCM1137 PDF recovered by W04 repeats Ca(NO3)2 x6H2O at49.40mg in the trace solution. Thus source text is now available and agrees on the printed six-water claim. Neither recipe supplies a supplier/CAS/structure or correction establishing the actual unusual six-water reagent; anhydrous and tetrahydrate owners remain distinct. No physical-form substitution is justified.'
    d['applicability']='Exact frozen ingredient2013 source context is retained. Separate successful original-recipe rendering confirms the printed claim, while the failed old capture remains unsuccessful. This is a source-availability correction; physical reagent verification and all original export/form holds remain.'
    d['evidence_ids'].append('w02-final-jcm1137-recovered')
    d['missing_requirement']=d['no_change_reason']='A primary reagent specification, supplier/registry structure, or explicit provider corrigendum establishing the actual calcium nitrate physical form is still required; repeating the printed six-water formula is insufficient to substitute tetrahydrate or authorize a physical identity.'
    # Bind active nickel owner after all-file lookup; preserve rejected historical pointer.
    catalog={str(p.relative_to(W)):yaml.safe_load(p.read_text()) for p in sorted((W/'data/ingredients').glob('*/*.yaml'))}
    matches=[{'path':p,'sha256':sha(W/p),'record':v} for p,v in catalog.items() if v.get('identifier')=='CHEBI:53437' or v.get('chemical_properties',{}).get('cas_rn')=='10101-97-0']
    active=[x for x in matches if x['record']['mapping_status']!='REJECTED']
    assert len(active)==1 and active[0]['path']=='data/ingredients/mapped/Nickel_II_sulfate_hexahydrate.yaml'
    owner=active[0];snapshots.append(FrozenFile.capture(W/owner['path']))
    active_capture=copy_exact(W/owner['path'],OUT/'before/Nickel_II_sulfate_hexahydrate.yaml')
    source=load(A/'b/captures/retry-togo-M2284.json')
    rows=[x for group in source['components'] for x in group['items'] if x.get('component_name')=='Ni2SO4x 6 H2O' or ('nickel' in x.get('label','').lower())]
    assert len(rows)==1 and 'hexahydrate' in rows[0]['label'].lower()
    save(OUT/'nickel-owner-comparison.json',{'author':'worker02 /root','searched':'Every direct data/ingredients mapped/unmapped YAML, including ignored files via pathlib; no filename filters','catalog_count':len(catalog),'matches':matches,'source_rows':rows,'source_capture':evidence['b-togo-e7e73dddba82b9cf'],'disposition':'Bind the existing active hexahydrate owner as source-scoped corrected-identity context. Retain rejected tombstone and prior EXCLUDED_REJECTED review as historical evidence. No global malformed alias, owner promotion, role or release approval.'})
    ni_eid='w02-final-nickel-active-owner-comparison'
    extra.append({'evidence_id':ni_eid,'kind':'local_validation','capture':cap(OUT/'nickel-owner-comparison.json'),'url':None,'locator':'Whole catalog identifier/CAS lookup and full active/rejected record comparison; exact TOGO M2284 raw-name versus named-GMO row','supports_or_contradicts':'Only the active Nickel_II_sulfate_hexahydrate owner is used as the current candidate identity. Ni2SO4 raw formula remains malformed source provenance.','case_ids':[by_index[115]['case_id']]})
    d=deepcopy(by_index[115]);d['owner_records']=[{'path':owner['path'],'sha256':owner['sha256']}]+d['owner_records'];d['evidence_ids'].append(ni_eid)
    d['reasoning']+=' Current whole-catalog lookup identifies active Nickel_II_sulfate_hexahydrate.yaml, CHEBI:53437/CAS10101-97-0, with matching six-water properties and explicit exact named synonym. Niso4_X_6_H2o.yaml is a REJECTED tombstone retained only as historical context. No malformed Ni2SO4 global alias is approved.'
    d['no_change_reason']='The active exact six-water nickel sulfate owner already exists and is now bound by current bytes; no owner mutation is needed for this source-scoped correction. The rejected duplicate and its EXCLUDED_REJECTED review remain historical. Original recipe/provider disagreement still requires occurrence-specific publication correction.'
    d['issue_refs']=list(dict.fromkeys(d['issue_refs']+['https://github.com/CultureBotAI/MediaIngredientMech/issues/1241']))
    changes[d['case_id']]=d
    # Correct active Strontium provenance while preserving all authored history.
    oldp=next(p for p in props if p['proposal_id']=='a-proposal-strontium-sulfate');source=A/oldp['after_capture']['path']
    assert sha(source)==oldp['after_capture']['sha256'];snapshots.append(FrozenFile.capture(source))
    record=yaml.safe_load(source.read_text());history=deepcopy(record['curation_history'])
    clarification='JCM1030-1032 and MediaDive solution5083 supply the trace SrSO4 scope. The old JCM1033 HTML capture returned Nothing found; a separately recovered complete bacmedia JCM1033 PDF lists SrSO4 0.92mg in the trace-elements section. CHEBI747199 provides the strontium sulfate ontology identity; neither source establishes a corrected receiving-medium dose. Preserve the frozen0.92G_PER_L versus source0.92mg discrepancy and all publication holds.'
    record['ontology_mapping']['evidence'][0]['notes']=clarification
    record['notes']=clarification
    record_curation_event(record,curator='worker02 /root',action='CORRECTED',changes='Under #1241, distinguish failed JCM1033 HTML from separate successful PDF evidence in active strontium provenance; retain all quantities, scientific fields, previous events and dose/form/release holds.',llm_assisted=True)
    assert record['curation_history'][:len(history)]==history
    stage=O/'root-stage/strontium.yaml';stage.parent.mkdir(parents=True,exist_ok=True);assert not stage.exists()
    write_validated_ingredient(record,stage)
    dest=OUT/'after/Strontium_sulfate.yaml';dest.parent.mkdir(parents=True,exist_ok=True)
    def verify():
        for s in snapshots:s.verify()
    publish_new_files([(dest,stage.read_bytes())],verify);verify()
    proposed=deepcopy(oldp);proposed['after_capture']=cap(dest);proposed['evidence_ids']=[rebound.get(e,e) for e in proposed['evidence_ids']]+['w02-final-jcm1033-recovered'];proposed['description']+=' Active source provenance now distinguishes failed HTML from separately captured original-recipe PDF; no quantity or identity change.'
    save(OUT/'evidence-classification-proof.json',{'author':'worker02 /root','entries':proofs,'old_evidence_ledger_sha256':sha(OLD/'evidence.json'),'historical_bytes_and_timestamps_preserved':True,'successor_ids':rebound})
    save(OUT/'fragments.json',{'author':'worker02 /root','created_at':datetime.now(timezone.utc).isoformat(),'decisions':list(changes.values()),'proposals':[proposed],'evidence':extra,'evidence_id_replacements':rebound,'superseded_proposal_ids':[],'proposal_authors':{proposed['proposal_id']:['worker02 /root']},'case_authors':{cid:['worker02 /root'] for cid in changes},'scientific_approval':False})
    print(json.dumps({'decision_fragments':len(changes),'proposal_fragments':1,'evidence_successors':len(extra),'classifications':len(proofs),'nickel_catalog_count':len(catalog)}))

if __name__=='__main__':main()
