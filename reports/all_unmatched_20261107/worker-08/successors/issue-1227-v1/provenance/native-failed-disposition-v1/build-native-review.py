"""Prepare a native whole-selection review from exact final peer receipts.

This records the worker integration author's actual self-review with separately
identified scientific peers. It cannot turn a schema PASS into scientific or
export approval. Native validate/save remain separate explicit commands.
"""
from datetime import datetime, timezone
from pathlib import Path
import copy
import json
import yaml
from assemble import read, sha, checked_capture, SELECTION, SELECTION_CONFIG

ROOT = Path.cwd()
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-v1'
PRIVATE = ROOT / '.temp/all-unmatched-worker-08/issue-1227-v1'


class NoAliases(yaml.SafeDumper):
    def ignore_aliases(self, data): return True


def main():
    inspection = read(PRIVATE / 'native-inspection.json')
    for x in inspection['source']['inputs']:
        assert sha(ROOT / x['path']) == x['sha256'], ('stale native input', x['path'])
    structural = read(OUT / 'structural-audit.json')
    assert structural['structural_accounting'] == 'PASS' and structural['accounted_case_count'] == 188
    assert structural['independent_review_status_counts'] == {'complete': 188}
    validation = read(OUT / 'validation/combined-validation.json')
    assert validation['strict_exit_code'] == 0 and validation['guarded_replays'] == 113
    for key in ['baseline_partonomy_violations', 'overlay_partonomy_violations', 'label_errors']:
        assert validation[key] == []
    assert validation['preservation']['mismatches'] == []
    assert validation['bounded_correction_validation_status'] == 'PASS'
    assert validation['owner_admission_status'] == 'HELD' and len(validation['owner_admission_failures']) == 1
    assert validation['owner_admission_failures'][0]['gate_status'] == 'failed'
    identity = read(OUT / 'validation/identity-obligations.json')
    assert identity['selected_payload_count'] == 113 and not any(identity['native_failures'].values())
    assert identity['input_sha256'] == sha(SELECTION / 'proposals.json')
    ds = read(SELECTION / 'decisions.json')['decisions']; ps = read(SELECTION / 'proposals.json')['proposals']
    config = read(SELECTION_CONFIG)
    dispositions = read(OUT / 'issue-dispositions.json')['findings']
    assert len(dispositions) == 12
    now = datetime.now(timezone.utc); stamp = now.isoformat().replace('+00:00', 'Z')
    evidence, assessments = [], []
    def local_evidence(eid, path, kind, summary, locator):
        evidence.append(dict(evidence_id=eid, kind=kind, reference=str(path.relative_to(ROOT)),
            accessed_at=stamp, support='supports', snapshot_sha256=sha(path), locator=locator, summary=summary))
    for g in config['groups']:
        path = checked_capture(g['peer_capture'], ART)
        peer = read(path)
        assert peer['author'] == g['author'] and peer['reviewer'] == g['reviewer'] and g['author'] != g['reviewer']
        assert peer['full_payload_review'] is True and peer['open_blocking_findings'] == []
        local_evidence('peer-' + g['name'], path, 'prior_review',
            g['reviewer'] + ' inspected every full selected payload and assigned source outcome authored by ' + g['author'] + '. Exact peer scope/hashes and remaining holds are preserved.',
            'Complete per-case and per-payload appraisals, final hashes, primary capture read log, findings and re-review dispositions')
    local_evidence('source-index', SELECTION / 'evidence.json', 'record_content',
        'Full retained evidence index, plus truthful successor additions. This timestamp is index inspection; nested primary captures keep original acquisition times.', 'Evidence IDs cited by each exact source decision/proposal')
    for eid, rel, text in [('accounting','structural-audit.json','All188 frozen source cases and all113 selected proposals, original occurrences, evidence captures and exact backlinks.'),
                          ('native','validation/combined-validation.json','Guarded writer replay, strict closed schema, full overlay partonomy, native labels/registry identity, literal alias checks and historical preservation.'),
                          ('identity','validation/identity-obligations.json','Native B1/B2/B3/B5/D on explicit identity obligations and exact private payload fixtures; meaningful failure controls. No maintained SSSOM or downstream export was generated or validated.'),
                          ('dispositions','issue-dispositions.json','All12 original findings retain exact severity, reviewer identity, routing, predecessor targets and bounded successor disposition.'),
                          ('selection','final-v2/assembly-provenance.json','Disjoint actual author/reviewer scopes and exact changed/unchanged payload accounting; original owner beforeimages preserved.')]:
        local_evidence(eid, OUT / rel, 'validation' if eid != 'dispositions' else 'prior_review', text, 'Full exact receipt')
    local_evidence('prior-external', OUT / 'inputs/external-review/review.yaml', 'prior_review',
        'Sealed worker03 independent review of b90; preserved unchanged, with all twelve findings and original reviewers.', 'All findings and original affected targets')
    local_evidence('new-findings', OUT / 'new-finding-dispositions.json', 'prior_review',
        'Six distinct new findings were routed before correction and bound to exact final payloads or metadata and separate review receipts. Raw severities and failed inputs are preserved in their referral packets.', 'All six exact finding dispositions')
    local_evidence('tsb-admission', OUT / 'independent-review/final_assembly/trypticase-admission-review-v1.json', 'prior_review',
        'Separate reviewer confirmed the exact preexisting Trypticase/Bacto collision, full owner bytes and prior/current identity. The failed owner-admission gate remains HELD; only bounded grade/evidence correction is assessed.',
        'Entire independent appraisal, exact owner/payload/input hashes and primary OLS annotation')
    for n, d in enumerate(ds):
        g = next(g for g in config['groups'] if d['case_id'] in g['case_ids'])
        assessments.append(dict(assessment_id=f'case-{n:03}', area='scope', topic='Complete frozen source-case outcome with preserved occurrence limits', outcome='supported',
            target_ids=[d['case_id']], evidence_ids=['source-index', 'peer-' + g['name']],
            summary=d['reasoning'], details=d['applicability'] + '\nRemaining requirement: ' + str(d.get('missing_requirement')) + '\nThis positive assessment supports the bounded disposition, including explicit unresolved facts; it does not approve an unresolved identity or release its holds.'))
    for n, p in enumerate(ps):
        g = next(g for g in config['groups'] if p['proposal_id'] in g['proposal_ids'])
        assert read(checked_capture(g['peer_capture'], ART))['payload_hashes'][p['proposal_id']] == p['after_capture']['sha256']
        assessments.append(dict(assessment_id=f'payload-{n:03}', area='identity', topic='Complete selected isolated payload and source applicability', outcome='supported',
            target_ids=[p['proposal_id']], evidence_ids=['source-index','peer-' + g['name']], summary=p['description'],
            details='Peer review inspected all fields, evidence and inherited scope in the exact payload, not only correction deltas. Identity/alias consequences: ' + str(p.get('identity_predicate_alias_consequences')) + '\nRemaining integration obligations: ' + str(p.get('publication_review_obligations')) + '\nNo role, complete-owner release, cross-shard winner or source-hold approval.'))
    assessments.extend([
        dict(assessment_id='tsb-existing-owner-admission-hold', area='identity', topic='Preexisting Trypticase promotion collides with active Bacto owner', outcome='concern',
            target_ids=['op1201-trypticase-soy-broth'], evidence_ids=['tsb-admission', 'native'],
            summary='Maintained owner admission fails: active data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml already owns MICRO:0000113. The predecessor and selected Trypticase proposal share that ID; this correction changes only grade, evidence category and history.',
            details='W08-1227-TSB-OWNER-RECONCILIATION is an explicit coordinator dependency. The exact candidate and collider hashes are bound in the independent receipt. Neither a duplicate owner, a product equivalence nor a merge winner is approved. The private structural overlay does not constitute maintained admission.'),
        dict(assessment_id='retained-valerate-owner-hold', area='identity', topic='Inherited neutral-acid versus pentanoate alias boundary', outcome='concern',
            target_ids=['op-valeric-alias'], evidence_ids=['peer-organic_products', 'prior-external'],
            summary='The source-supported n-/n--valeric acid aliases remain bounded planning candidates. Inherited n-Pentanoate/Pentanoate aliases do not establish neutral-acid identity and receive no scientific or release approval.',
            details='This is the earlier external reviewer A whole-owner limitation confirmed again, not a new finding or a removal of its hold. No inherited alias is approved merely because the isolated source alias delta is supported.'),
        dict(assessment_id='retained-thauer-stereo-owner-hold', area='identity', topic='Inherited calcium-pantothenate stereochemistry', outcome='concern',
            target_ids=['vm1201-prop-thauers-source-comparison'], evidence_ids=['peer-vitamins_mixtures', 'prior-external'],
            summary='The CultureBotHT versus TOGO provenance comparison remains supported. CultureBotHT does not establish pantothenate stereochemistry; inherited components[6] CHEBI:31345 is not scientifically approved by this review.',
            details='The prior external reviewer C explicitly retained this component-grounding hold. Preserve CultureBotHT-specific cyanocobalamin, the distinct TOGO comparison and original amounts; no source-form equivalence or whole-owner release follows.')])
    for aid, pid, summary in [
        ('retained-soy-family-hold', 'op1201-soy-family-source-boundary',
         'The notes-only source boundary does not approve the whole soy hydrolysate family, active duplicates or rejected Bacto Soytone tombstone. Coordinated source-specific owner review remains.'),
        ('retained-tpp-referenced-owner-hold', 'vm-prop-new-110',
         'The source TPP component reference does not import or approve conflicting chloride formula/CAS/SMILES/aliases on its existing referenced owner. Existing319/320/268 and WITHHOLD2792 remain.'),
        ('retained-jcm403-class-relation-limit', 'vm-prop-jcm403-vitamin',
         'The inherited CLOSE_MATCH to generic MICRO0000460 vitamin solution is not exact whole-formulation equivalence and receives no new release approval. Source-qualified preparation and raw pointer rejection remain distinct claims.'),
        ('retained-menadione-owner-scope', 'vm-prop-menadione',
         'The bounded ATCC solute-name assertion does not independently validate inherited commercial brand aliases or role facets. This unchanged planning payload gains no whole-owner or export approval.'),
        ('retained-thauer-evidence-limit', 'vm1201-prop-thauers-source-comparison',
         'Legacy DATABASE_MATCH source attribution and universal ontology-absence rationale are not approved anew by the source comparison. Historical claims remain preserved, while actual source comparison is separately supported.')]:
        group = next(g for g in config['groups'] if pid in g['proposal_ids'])
        assessments.append(dict(assessment_id=aid, area='scope', topic='Explicit retained whole-owner or referenced-owner limitation', outcome='concern',
            target_ids=[pid], evidence_ids=['peer-' + group['name'], 'source-index'], summary=summary,
            details='This is a preserved predecessor limitation, not a newly fixed field or a new finding. The bounded correction acceptance does not erase it.'))
    previous = yaml.safe_load((OUT / 'inputs/external-review/review.yaml').read_text())
    original = {f['finding_id']: f for f in previous['findings']}
    findings = []
    for disposition in dispositions:
        old = original[disposition['finding_id']]; f = copy.deepcopy(old)
        assert disposition['severity'] == old['severity']
        f.update(status='resolved', evidence_ids=['dispositions', 'prior-external', 'native', *['peer-' + g['name'] for g in config['groups']]],
            disposition_reason=disposition['bounded_disposition'] + ' Resolution describes only the isolated successor correction; the linked GitHub issue, maintained owner admission and remaining scientific holds are not closed or approved.',
            previous_occurrences=[dict(repository='CultureBotAI/MediaIngredientMech', review_id=previous['review_id'], finding_id=old['finding_id'])],
            external_issues=[f"https://github.com/CultureBotAI/MediaIngredientMech/issues/{disposition['issue']}"])
        findings.append(f)
    for f in read(OUT / 'new-finding-dispositions.json')['findings']:
        findings.append(dict(finding_id=f['finding_id'], issue_key='w08-1227-' + f['finding_id'].lower(),
            category='identity' if f['finding_id'] == 'VM1227-PEER-001' else 'scope',
            severity=f['normalized_severity'], status='resolved', certainty='confirmed', title=f['title'],
            description='Original reviewer severity: ' + f['original_severity'] + '. ' + f['bounded_disposition'],
            target_ids=f['proposal_ids'], evidence_ids=['new-findings', 'source-index', *['peer-' + g['name'] for g in config['groups']]],
            ownership_note='Isolated exact source proposal correction. Coordinator retains GitHub disposition and whole-owner/cross-shard acceptance.',
            disposition_reason=f['bounded_disposition'] + ' All maintained, source-specific and release holds remain; no issue closure is asserted.',
            external_issues=[f"https://github.com/CultureBotAI/MediaIngredientMech/issues/{f['issue']}"]))
    ids = [t['target_id'] for t in inspection['targets']]
    assert len(ids) == 301 and {t for a in assessments for t in a['target_ids']} == set(ids)
    checks = [dict(check_id='accounting', name='Frozen shard/evidence/proposal accounting', status='passed', required=True, exit_code=0,
        summary='188 cases/113 payloads; all occurrences and exact beforeimage bindings preserved.', target_ids=ids, evidence_ids=['accounting']),
        dict(check_id='native', name='Native schema, guarded writer, labels, identity and full overlay partonomy', status='passed', required=True, exit_code=0,
        command=' '.join(validation['validation_command']), summary='Every selected payload passed guarded/schema/label/partonomy and proposed-identity checks; the separate maintained owner-admission failure remains HELD. These checks do not confer scientific approval.', target_ids=ids, evidence_ids=['native']),
        dict(check_id='identity', name='Native proposed-identity obligations and negative controls', status='passed', required=True, exit_code=0,
        summary='All113 payloads assessed; native asymmetric/registry/own-identifier invariants apply to explicit proposed obligations in a private fixture. This is not a maintained SSSOM export check.', target_ids=ids, evidence_ids=['identity']),
        dict(check_id='peer', name='Authorship-separated whole-payload and source-outcome review', status='passed', required=True, exit_code=0,
        summary='All three disjoint cohorts have actual final-byte independent peer receipts. Root is an integration author, not an independent scientific reviewer of its own assembly.', target_ids=ids, evidence_ids=['peer-' + g['name'] for g in config['groups']]),
        dict(check_id='release', name='Maintained integration and release gates', status='not_applicable', required=False,
        summary='No maintained corpus application or downstream rebuild. Coordinator final-head review, cross-shard reconciliation and complete-owner/export admission remain separate.', target_ids=ids)]
    checks.append(dict(check_id='tsb-owner-admission', name='Existing-owner collision admission', status='failed', required=False, exit_code=1,
        summary='Real admission failure retained: the preexisting Trypticase promotion duplicates the active Bacto MICRO:0000113 owner. Not required to assess this isolated grade/evidence correction, but mandatory coordinator reconciliation before any maintained admission. No exemption or gate PASS is asserted.',
        target_ids=['op1201-trypticase-soy-broth'], evidence_ids=['tsb-admission', 'native']))
    review = dict(schema_version='1.0.0', review_id=now.strftime('%Y%m%dT%H%M%SZ') + '-w08-issue1227-complete-successor',
        kind='batch', repository='CultureBotAI/MediaIngredientMech', title='Worker08 issue1227: complete selected payload and source-outcome correction review',
        started_at=read(OUT / 'acceptance.json')['accepted_at'].replace('+00:00','Z'), finished_at=stamp,
        reviewer=dict(identity='worker08:/root integration author', kind='agent', independence='self_review',
            independence_basis='Root authored assembly and deterministic checks. Separate actual reviewers are named in bound peer receipts and have no authorship of their reviewed cohort. Final coordinator review is outstanding.'),
        skill='add-media; review-yaml-category; native record-review profile', completion='completed', verdict='pass_with_limitations', scientific_review=True,
        summary='All188 source outcomes and all113 complete selected isolated payloads were assessed through disjoint authors and separate skeptical reviewers. Original twelve findings are addressed within exact proposal scope; unknown scientific facts, inherited roles and all release/source holds remain explicit. No maintained owner or export is approved.',
        source=inspection['source'], targets=inspection['targets'], scope=dict(description='188 frozen source-case outcomes plus113 complete isolated selected owner payloads; these are two distinct accounting populations.',
            selection='Complete immutable successor selection with preserved original cases, occurrences and beforeimages; no sampling.', coverage='full', population_size=301, reviewed_target_ids=ids,
            exclusions=[dict(target='Cross-shard final owner selection, maintained application, roles and release', reason='Coordinator integration/admission scope; native or source review does not confer it.')]),
        checks=checks, evidence=evidence, assessments=assessments, findings=findings, actions=[],
        related_reviews=[dict(repository='CultureBotAI/MediaIngredientMech', review_id=previous['review_id'], relationship='Exact full-scope successor to the preserved independent b90 review; all twelve finding targets retained.')],
        limitations=['NBRC1314/TOGOM2023 remains explicitly unread/source-held; supported NBRC1301 identity is retained.',
            'Trypticase/Bacto MICRO:0000113 duplicate-owner admission failed and remains HELD. Only the already-proposed source identity and bounded lookup-grade/evidence correction are supported, with exact coordinator reconciliation required.',
            'Unknown B12 vitamer, pantothenate stereochemistry, unresolved hydrate, carrier, quantity and nested-stock facts remain unknown; literal COMPLETE lists do not assert final molecular composition.',
            'W03-shared phosphate and all cross-shard duplicate preparations require coordinator reconciliation; no reviewer approves its own competing owner.',
            'Sealed W05 independent review and all previous W08 artifacts are preserved. New coordinator referrals and their bounded execution are recorded separately; this review does not mutate GitHub issue state.'])
    path = PRIVATE / 'native-review.yaml'; assert not path.exists()
    path.write_text(yaml.dump(review, Dumper=NoAliases, sort_keys=False, allow_unicode=True))
    (PRIVATE / 'native-review-id.txt').write_text(review['review_id'] + '\n')
    print(review['review_id'])


if __name__ == '__main__': main()
