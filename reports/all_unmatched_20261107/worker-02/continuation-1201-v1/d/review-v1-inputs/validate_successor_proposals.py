"""Validate exact isolated payloads and a read-only catalog overlay.

No maintained input is written. Overlay validation is not integration approval.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0,str(Path.cwd()/'src'))
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient, ValidationFailedError
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy

ARTIFACT = Path(__file__).resolve().parent.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--proposals',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    args.out.mkdir(parents=True)
    proposal_bytes=args.proposals.read_bytes()
    proposal_input_sha256=hashlib.sha256(proposal_bytes).hexdigest()
    proposals=json.loads(proposal_bytes)['proposals']
    catalog={str(p):yaml.safe_load(p.read_text()) for p in sorted(Path('data/ingredients').glob('*/*.yaml'))}
    original_hashes={p:sha(Path(p)) for p in catalog}
    before_violations=validate_component_partonomy(catalog.values())
    overlay=dict(catalog); payloads=[]; seen_paths=set(); new_ids={}; errors=[]
    scratch=Path('.temp/all-unmatched-worker-02/continuation-1201-v1/guarded-roundtrip')/args.out.name
    scratch.mkdir(parents=True,exist_ok=False)
    for p in proposals:
        owner=p['owner_path']; capture=p['after_capture']
        if capture['root']!='artifact':raise ValueError('Unexpected after root')
        after=ARTIFACT/capture['path']
        if sha(after)!=capture['sha256']:raise ValueError('Changed after payload: '+str(after))
        if owner in seen_paths:raise ValueError('Conflicting active payloads for owner: '+owner)
        seen_paths.add(owner)
        if p['kind']=='edit_existing_owner':
            if owner not in catalog or original_hashes[owner]!=p['before_sha256']:raise ValueError('Original owner hash mismatch: '+owner)
        elif p['kind']=='new_owner':
            if Path(owner).exists() or p['before_sha256'] is not None:raise ValueError('New owner already exists or has a before hash')
        else:raise ValueError('Unknown proposal kind')
        value=yaml.safe_load(after.read_text())
        previous_history=(catalog.get(owner) or {}).get('curation_history',[])
        history=value.get('curation_history',[])
        if len(history)<=len(previous_history):
            raise ValueError('Material proposal lacks a new curation event: '+owner)
        if history[:len(previous_history)]!=previous_history:
            raise ValueError('Existing curation history changed: '+owner)
        if not all(event.get('llm_assisted') is True for event in history[len(previous_history):]):
            raise ValueError('New assisted curation event omits truthful LLM provenance: '+owner)
        destination=scratch/(p['proposal_id']+'.yaml')
        try:
            write_validated_ingredient(value,destination)
            if yaml.safe_load(destination.read_text())!=value:raise ValueError('Guarded write changed content')
            status='passed'
        except ValidationFailedError as exc:
            status='failed';errors.append({'proposal_id':p['proposal_id'],'error':exc.summary()})
        overlay[owner]=value
        payloads.append({'proposal_id':p['proposal_id'],'owner_path':owner,'after_capture':capture,'native_guarded_write':status,'roundtrip_path':str(destination),'identifier':value['identifier']})
        new_ids.setdefault(value['identifier'],[]).append(owner)
    violations=validate_component_partonomy(overlay.values())
    baseline_collisions={identifier:sorted(p for p,v in catalog.items() if v.get('identifier')==identifier) for identifier in new_ids}
    collisions=[]
    for identifier in new_ids:
        paths=sorted(p for p,v in overlay.items() if v.get('identifier')==identifier)
        if len(paths)>1:collisions.append({'identifier':identifier,'after_paths':paths,'baseline_paths':baseline_collisions[identifier],'new_collision':paths!=baseline_collisions[identifier]})
    referenced_parts={}
    for p in proposals:
        for component in overlay[p['owner_path']].get('components',[]):
            if component.get('reference_scope')=='MIM_CATALOG':
                referenced_parts.setdefault(component['component_id'],[]).append({'proposal_id':p['proposal_id'],'component_name':component['component_name']})
    component_owner_collisions=[]
    for identifier,uses in referenced_parts.items():
        matches=[{'path':path,'preferred_term':value.get('preferred_term'),'mapping_status':value.get('mapping_status')} for path,value in overlay.items() if value.get('identifier')==identifier and value.get('mapping_status')!='REJECTED']
        if len(matches)>1:component_owner_collisions.append({'identifier':identifier,'active_owner_candidates':matches,'uses':uses,'coordinator_reconciliation_required':True,'owner_selected':False})
    # Demonstrate rejection before writing, without modifying a proposal.
    probe=dict(next(iter(overlay.values())));probe['unexpected_worker_probe']='must be rejected'
    rejected=scratch/'invalid-probe.yaml'
    try:write_validated_ingredient(probe,rejected)
    except ValidationFailedError:negative_ok=not rejected.exists()
    else:negative_ok=False
    if not negative_ok:raise AssertionError('Guarded writer accepted an unknown field')
    if any(sha(Path(p))!=h for p,h in original_hashes.items()):raise AssertionError('Maintained catalog changed during validation')
    if sha(args.proposals)!=proposal_input_sha256:raise AssertionError('Proposal ledger changed during validation; rerun a stable revision')
    for p in payloads:
        if sha(ARTIFACT/p['after_capture']['path'])!=p['after_capture']['sha256']:raise AssertionError('Proposal payload changed during validation')
    report={'checked_at':datetime.now(timezone.utc).isoformat(),'proposal_input':str(args.proposals),'proposal_input_sha256':proposal_input_sha256,'catalog_file_count':len(catalog),'catalog_hashes':original_hashes,'payloads':payloads,'guarded_writer_errors':errors,'negative_unknown_field_write_rejected':negative_ok,'baseline_partonomy_violations':[str(x) for x in before_violations],'overlay_partonomy_violations':[str(x) for x in violations],'identifier_collisions':collisions,'component_owner_collisions':component_owner_collisions,'maintained_catalog_unchanged':True,'scientific_or_release_approval':False,'scope':'Exact isolated after payloads validated by maintained closed-schema writer; native partonomy run over all actual catalog files with those proposals substituted in memory. Native duplicate families are reported separately, never merged; MIM_CATALOG references identify substances and do not choose among competing owner documents.'}
    (args.out/'receipt.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'payloads':len(payloads),'writer_errors':len(errors),'baseline_partonomy_violations':len(before_violations),'overlay_partonomy_violations':len(violations),'new_identifier_collisions':sum(x['new_collision'] for x in collisions),'invalid_write_rejected':negative_ok}))
    return bool(errors or violations or any(x['new_collision'] for x in collisions))


if __name__=='__main__':raise SystemExit(main())
