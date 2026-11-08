"""Inspect all188 source outcomes and all113 final isolated payloads, 2026-11-08.

This captures native input provenance, not a scientific verdict. Run only after
final assembly and exact independent review are complete.
"""
from pathlib import Path
import json
import subprocess
import sys
import yaml
from assemble import read, sha, checked_capture, SELECTION, SELECTION_CONFIG

ROOT = Path.cwd()
ART = ROOT / 'reports/all_unmatched_20261107/worker-08'
OUT = ART / 'successors/issue-1227-v1'
PRIVATE = ROOT / '.temp/all-unmatched-worker-08/issue-1227-v1'


def main():
    ds = read(SELECTION / 'decisions.json')['decisions']
    ps = read(SELECTION / 'proposals.json')['proposals']
    targets = []
    for d in ds:
        targets.append(dict(target_id=d['case_id'], path=str((SELECTION / 'decisions.json').relative_to(ROOT)),
            selector='decisions[case_id=' + d['case_id'] + ']', label=d['source']['source_label'] or d['case_id'],
            kind='source', ownership_note='Exact successor decision of the unchanged frozen source case/occurrences. Source-only assessment does not invent a maintained owner or approve a scientific identity beyond its stated scope.'))
    inputs = set(['AGENTS.md', 'MAPPING_SEMANTICS.md', 'src/mediaingredientmech/schema/mediaingredientmech.yaml',
        '.claude/skills/add-media/SKILL.md', 'docs/record-reviews.md', 'docs/record-review-profile.md',
        'src/mediaingredientmech/validation/component_partonomy.py', 'src/mediaingredientmech/validation/write_validated.py',
        'scripts/validate_sssom_invariants.py', 'src/mediaingredientmech/sssom_grading.py',
        'src/mediaingredientmech/synonym_policy.py', str((ART / 'provenance/shard-08.json').relative_to(ROOT))])
    for p in ps:
        path = checked_capture(p['after_capture'], ART)
        record = yaml.safe_load(path.read_text())
        t = dict(target_id=p['proposal_id'], path=str(path.relative_to(ROOT)), label=record['preferred_term'], kind='source', record_class='IngredientRecord')
        if p['kind'] == 'edit_existing_owner':
            inputs.add(p['owner_path'])
            t['owner_paths'] = [dict(repository='CultureBotAI/MediaIngredientMech', path=p['owner_path'], role='Exact frozen maintained beforeimage; isolated successor bytes are not applied')]
        else:
            t['ownership_note'] = 'Unapplied new-owner proposal for ' + p['owner_path'] + '; no existing owner is fabricated. Coordinator duplicate reconciliation and final-head review required.'
        targets.append(t)
    for e in read(SELECTION / 'evidence.json')['evidence']:
        if e['capture']['root'] == 'artifact':
            inputs.add(str(checked_capture(e['capture'], ART).relative_to(ROOT)))
    inputs.add(str(SELECTION_CONFIG.relative_to(ROOT)))
    inputs.update(str((SELECTION / n).relative_to(ROOT)) for n in ['decisions.json','proposals.json','evidence.json','assembly-provenance.json'])
    for n in ['structural-audit.json', 'validation/combined-validation.json', 'validation/identity-obligations.json',
              'issue-dispositions.json', 'new-finding-dispositions.json',
              'independent-review/preservation-final/receipt.json', 'independent-review/preservation-final/checks.json',
              'independent-review/preservation-final/inventories.json', 'provenance/preservation-coverage-refinement.json',
              'provenance/assembly-controls-v4.log', 'provenance/validation-controls-v6.log',
              'COORDINATOR-TSB-OWNER-DEPENDENCY-v1.json',
              'independent-review/final_assembly/trypticase-admission-review-v1.json',
              'independent-review/final_assembly/promotion-collision-inventory.json',
              'provenance/native-validation-command-v1.log']:
        inputs.add(str((OUT / n).relative_to(ROOT)))
    inputs.add('data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml')
    inputs.update(str(p.relative_to(ROOT)) for p in (OUT / 'scripts').glob('*.py'))
    assert len(targets) == len({t['target_id'] for t in targets}) == 301
    targetpath = PRIVATE / 'native-targets.yaml'
    targetpath.write_text(yaml.safe_dump({'targets': targets}, sort_keys=False, allow_unicode=True))
    cmd = [sys.executable, 'scripts/record_review.py', 'inspect', '--targets', str(targetpath)]
    for p in sorted(inputs): cmd.extend(['--input', p])
    run = subprocess.run(cmd, capture_output=True, text=True)
    (PRIVATE / 'native-inspection.json').write_text(run.stdout)
    (PRIVATE / 'native-inspection.stderr').write_text(run.stderr)
    (OUT / 'validation/native-inspection-receipt.json').write_text(json.dumps(dict(command=cmd,
        exit_code=run.returncode, targets=len(targets), inputs=len(inputs), inspection_sha256=sha(PRIVATE / 'native-inspection.json'),
        description='Source cases and complete selected payloads, not only changed fields. Inspect captures bytes; peer assessments provide scientific review.'), indent=2) + '\n')
    assert run.returncode == 0, run.stderr
    print(json.dumps(dict(targets=len(targets), inputs=len(inputs), exit_code=run.returncode)))


if __name__ == '__main__': main()
