"""Author a bounded native review from exact inspected proposal inputs."""
from pathlib import Path
import json
import hashlib
from datetime import datetime, timezone
import yaml

class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'reports/all_unmatched_20261107/worker-08'
PRIVATE = ROOT / '.temp/all-unmatched-worker-08'
inspect = json.loads((PRIVATE / 'native-inspection-final.json').read_text())
proposals = json.loads((OUT / 'proposals.json').read_text())['proposals']
decisions = {d['case_id']: d for d in json.loads((OUT / 'decisions.json').read_text())['decisions']}
now = datetime.now(timezone.utc)
stamp = now.isoformat().replace('+00:00', 'Z')
ids = [p['proposal_id'] for p in proposals]
groups = json.loads((PRIVATE / 'final-fragment-selection.json').read_text())['groups']
evidence = []
assessments = []
for g in groups:
    path = OUT / g['final_review_paths'][0]
    evidence.append(dict(evidence_id='peer-'+g['name'], kind='prior_review',
        reference=str(path.relative_to(ROOT)), accessed_at=stamp, support='supports',
        snapshot_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        locator='Per-case and per-proposal reviews, final input hashes, findings and dispositions',
        summary='Separate skeptical review by '+g['reviewer']+' of primary work by '+g['primary_author']+'. Scientific acceptance is bounded to each stated delta and preserved source limits.'))
for index,p in enumerate(proposals,1):
    g = next(g for g in groups if set(p['case_ids']) <= set(g['reviewed_case_ids']))
    eid = f'proposal-evidence-{index:03}'
    evidence.append(dict(evidence_id=eid, kind='record_content',
        reference=str((OUT/'evidence.json').relative_to(ROOT)), accessed_at=stamp,
        support='supports', snapshot_sha256=hashlib.sha256((OUT/'evidence.json').read_bytes()).hexdigest(),
        locator='Evidence IDs: '+', '.join(p['evidence_ids']),
        summary='Content-bound evidence index for this proposal; each nested source retains its original URL, capture bytes, retrieval time and applicability in the case decisions. This timestamp records inspection of the index, not source recapture.'))
    scientific = '\n\n'.join(c+': '+decisions[c]['reasoning'] for c in p['case_ids'])
    consequences = p.get('identity_predicate_alias_consequences', p.get('source_scope','Source-defined distinct proposed formulation; preserve component qualifiers.'))
    obligations = p.get('publication_review_obligations',p.get('integration_requirements',[]))
    if isinstance(obligations,list): obligations='; '.join(obligations)
    assessments.append(dict(assessment_id=f'proposal-{index:03}',area='identity',
        topic=p['proposal_id']+' — bounded isolated delta',outcome='supported',
        target_ids=[p['proposal_id']], evidence_ids=[eid,'peer-'+g['name']],
        summary=p['description']+' '+consequences,
        details=scientific+'\n\nApplication/publication conditions: '+obligations+'\n'+p.get('cross_shard_conflict','Reconcile equivalent recipes and shared owner proposals before integration.')))
for eid,path,summary in [
    ('structural','structural-audit-v2.json','Whole-shard exact accounting PASS for all 188 cases after bounded archive extraction. This is structural validation only.'),
    ('combined','validation/combined-validation.json','All 46 selected payloads pass closed schema; 2956-record baseline and 2985-record memory overlay have zero partonomy violations; 3043 maintained files unchanged.')]:
    file=OUT/path
    evidence.append(dict(evidence_id=eid,kind='validation',reference=str(file.relative_to(ROOT)),
        accessed_at=stamp,support='supports',summary=summary,snapshot_sha256=hashlib.sha256(file.read_bytes()).hexdigest()))
review=dict(schema_version='1.0.0',review_id=now.strftime('%Y%m%dT%H%M%SZ')+'-w08-final-isolated-proposals',
    kind='batch',repository='CultureBotAI/MediaIngredientMech',title='Worker 08: bounded review of 46 isolated source-backed proposals',
    started_at='2026-11-08T05:08:49.272907Z',finished_at=stamp,
    reviewer=dict(identity='/root (worker08 integration reviewer)',kind='agent',independence='self_review',
        independence_basis='Root assembles and validates the bundle. Scientific primary authors and separate skeptical reviewers are explicitly identified in three hashed peer receipts; root does not claim independence from its own assembly.'),
    skill='map-media-ingredients; add-media; review-sssom-output; native record-review profile',
    completion='completed',verdict='pass_with_limitations',scientific_review=True,
    summary='All 46 isolated proposed deltas (17 existing owners, 29 proposed new owners) have evidence-backed case assessments and separate skeptical review. Proposed source-qualified identities and alias/provenance corrections are supported within the stated limits. This observation neither applies the proposals nor approves inherited whole records, roles, mapping rows or publication. The complete 188-case campaign remains authoritative for source-only holds and no-change outcomes.',
    source=inspect['source'],targets=inspect['targets'],
    scope=dict(description='Exact final 46 proposed payload deltas selected by proposals.json, with original maintained preimages and source-qualified new-owner boundaries. Unchanged inherited owner claims are outside approval.',
        selection='Every proposal in the assembled worker08 proposals.json; no sampling.',coverage='full',population_size=46,reviewed_target_ids=ids,
        exclusions=[dict(target='Source cases without a proposal',reason='Their exact frozen source objects are assessed in decisions.json and independent receipts. The local ingredient review profile does not create a maintained MIM owner for a source-only hold.'),
                    dict(target='Maintained whole-record and export admission',reason='All data remain unchanged. Integration, inherited claim withdrawal and content-bound publication admission belong to the coordinator.')]),
    checks=[dict(check_id='strict',name='Native closed schema for all 46 exact payloads',status='passed',required=True,
        command='Python scripts/validate_strict.py --workers 2 --out validation/final-proposals-strict.tsv <46 exact selected payload paths; complete argv in combined-validation.json>',
        exit_code=0,summary='46 payloads, zero schema failures.',target_ids=ids,evidence_ids=['combined']),
        dict(check_id='partonomy-and-preimages',name='Read-only combined native partonomy and exact preimage validation',status='passed',required=True,
        command='.temp/all-unmatched-worker-08/venv/bin/python .temp/all-unmatched-worker-08/validate_final_bundle.py',exit_code=0,
        summary='Baseline 2956 and in-memory overlay 2985 records: zero violations; original before hashes verified; new paths/identifiers unused; 3043 maintained files unchanged including ignored files.',target_ids=ids,evidence_ids=['combined']),
        dict(check_id='source-accounting',name='Whole-shard campaign audit',status='passed',required=True,exit_code=0,
        command='audit_worker_outcomes_v1.py --shard shard-08.json --decisions decisions.json --evidence evidence.json --proposals proposals.json --artifact-root worker08 --source-root preliminary-v5 --mim-root assigned-worktree --output structural-audit-v2.json',
        summary='188/188 exact cases; 736 evidence entries; all46 proposal references and capture hashes accounted. Structural pass is not scientific approval.',target_ids=ids,evidence_ids=['structural']),
        dict(check_id='maintained-release-gates',name='Post-application synchronization and publication gates',status='not_applicable',required=False,
        summary='No maintained data changes applied; sync, full-data QC, SSSOM generation, companion/semantic approval and downstream rebuilds are not run in this proposal-only shard.',target_ids=ids)],
    evidence=evidence,assessments=assessments,findings=[],actions=[],
    related_reviews=[dict(repository='CultureBotAI/MediaIngredientMech',review_id='20261108T053047Z-w08-isolated-proposal-review',relationship='Successor after replacing two full literature archives and a derivative extraction log with bounded factual captures. All scientific decisions and proposal payloads remain unchanged; earlier exact assembled inputs are retained under review-history/assembly-before-archive-remediation, and full archive bytes remain privately preserved.')],
    limitations=['Pass applies only to reviewed isolated deltas, not authorization to apply or export. Full inherited record claims and roles remain unapproved.',
      'Source-specific WITHHOLD/REJECTED decisions and exact missing requirements remain in all188 case decisions. No hold release follows from native validation.',
      'Issue758 phosphate proposals require coupled alias/override/membership/count integration. Sodium dithionite owner overlaps worker07 issue1169. Preserve original before hashes.',
      'New-owner positive content-bound SSSOM admission limitations in issue1165 remain. Source-qualified stock names do not justify globally resolving generic aliases.',
      'The source-only Na and CO cases remain held under issues1172 and1178; CO alias was withdrawn after native resolver casefold reproduction.',
      'JCM149 Hutner and worker01NBRC943 are distinct source formulations; no worker01 case approval is claimed.',
      'Zero native finding objects means no residual defect in this narrowly reviewed proposal delta scope; open integration and source findings remain in the campaign decisions and issue ledger.'])
(PRIVATE/'native-final-review.yaml').write_text(yaml.dump(review,Dumper=NoAliasDumper,sort_keys=False,allow_unicode=True))
(PRIVATE/'native-final-review-id.txt').write_text(review['review_id']+'\n')
print(review['review_id'])
