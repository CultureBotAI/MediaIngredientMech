"""Assemble the explicit Step4 selection only after all native groups finish."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
RUN=HERE.parent
x=json.loads((HERE/'selection.draft.json').read_bytes())
x['execution_groups']=[f'step4-native-chain-plan/executions/{name}' for name in ('step4-chain-v2-build','step4-exports-v1-exports','step4-gates-v1-gates')]
for name in x['execution_groups']:
 c=json.loads((RUN/name/'complete.json').read_bytes());assert c['complete'] is True

def add(path,destination=None,classification='completed_execution_evidence'):
 if any(i['path']==path for i in x['files']):return
 p=RUN/path;assert p.is_file(),path
 x['files'].append({'path':path,'destination':destination or 'supplement/'+path,'classification':classification})
def command(name,expected=0,disposition=None,rerun=None):
 path=f'logs/{name}.json'
 if any(i['receipt']==path for i in x['commands']):return
 value=json.loads((RUN/path).read_bytes());assert value['exit_code']==expected
 item={'receipt':path,'expected_exit':expected}
 if expected:item.update(disposition=disposition,successful_rerun=f'logs/{rerun}.json')
 x['commands'].append(item)
for name in ('step4-dispatch-chain-build-fixed','step4-dispatch-exports','step4-dispatch-gates','step4-unified-generation'):
 command(name)
for name in ('step4-independent-actual-chain-v1','step4-independent-generated-surfaces-v1'):
 command(name)
command('step4-dispatch-chain-build',1,'#1045: quoted Unicode paths caused a false preflight refusal before native commands; NUL parser and independent regressions repaired it.','step4-dispatch-chain-build-fixed')
for name in ('step4-independent-1046-mim-only','step4-independent-1046-native','step4-independent-actual-proposal-v1','step4-independent-author-focused','step4-independent-chain-1045-actual','step4-independent-chain-1045-v1','step4-independent-chain-controls-v1','step4-independent-merge-1047-v1','step4-independent-merge-nul-v1','step4-independent-native-contract','step4-independent-native-gates','step4-independent-receipt-fix-v1','step4-independent-receipt-wrapper-v1','step4-independent-unified-wrapper-v2'):
 command(name)
command('step4-independent-unified-wrapper-v1',1,'Independent tiny fixture omitted bump_sssom_header.py; setup failure preserved, dependency supplied in v2 with all controls passing.','step4-independent-unified-wrapper-v2')
for index_path in ('step4-independent/preapplication-evidence-index.json','step4-independent/preapplication-addendum-index.json','step4-native-chain-plan/revision-1045/version-index.json'):
 index=RUN/index_path;data=json.loads(index.read_bytes());add(index_path)
 for name,item in data['files'].items():
  p=index.parent/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256'],str(p)
  add(str(p.relative_to(RUN)))
for path in ('approved-plan.txt','plan-context.json','workflow-audit.md','step4-context.json','step4-workflow-context.json','step4-baseline-inputs.json','step4-baseline-inputs-v2.json','step4-chain-retry-disposition.json','step4-application/assemble_review.before.py','step4-independent/probe_merge_rename.py','step4-independent/merge-rename-proof.json','step4-independent/finding-merge-rename-paths.md','step4-independent/merge-helper-independent-review.json','step4-merge-verifier-1047/verify_mim_merge_nul.before.py','step4-merge-verifier-1047/test_merge_path_verifier.before.py','step4-merge-verifier-1047/tests.log','step4-merge-verifier-1047/receipt.json','step4-final-validation.json'):
 add(path)
for path in ('step4-independent/actual-generated-state.json','step4-independent/check_generated_state.py','prepare_step4_validation.py','step4-execution-packaging/prepare_final_selection.py','step4-remote-refresh-1116/main.json','step4-remote-refresh-1116/prs.json','step4-remote-refresh-1116/observed-at.txt'):
 add(path)
for number in (1005,1043,1044,1045,1046,1047):
 add(f'step4-remote-refresh-1116/issue{number}.json',classification='observed_issue_state_before_publication')
for path in ('unified-candidate.tsv','unified-before.tsv','unified-provenance-before.json','unified-provenance-candidate.json'):
 add('step4-unified-evidence/'+path,'unified/'+path,'actual_zero_change_unified_rebuild')
x['completion_receipts'].append({'path':'step4-unified-evidence/unified-generation-receipt.json','destination':'unified/unified-generation-receipt.json'})
for folder,name in (('mim-kgx-710-full','complete-kgx'),('mim-reviewed-sssom','reviewed-sssom'),('step4-supported-kgx','supported-kgx'),('step4-ingredient-bundle','companion')):
 add(f'step4-mim/output/{folder}/manifest.json',f'product-manifests/{name}.json','manifest_only_rebuildable_native_product')
refs=['AGENTS.md','MAPPING_SEMANTICS.md','justfile','docs/MERGE_QUEUE.md','workflow/mech-workflow.yaml','workflow/parent/mech-cycle.yaml','workflow/parent/workflow.yaml','.claude/skills/mediaingredientmech-evolve-workflow/SKILL.md','.github/workflows/qc-evidence.yaml','.github/workflows/qc-reviewed-sssom.yaml','tests/test_ingredient_bundle.py','docs/SSSOM_RELEASE.md','docs/INGREDIENT_BUNDLE.md']
refs.extend('reports/ingredient_bundle_20261101_lithium1005/'+p for p in ('review.json','prior-review.json','dependency-refresh.json','README.md'))
x['repository_references']=list(dict.fromkeys(x['repository_references']+refs))
x['repository_references'].append('reports/lithium_glycerophosphate_1005_20261101/README.md')
x['scope_exclusions'].append('Final committed-head and merge-group attestations follow the frozen content and are retained separately; no circular self-attestation is asserted.')
x['observed_limitations'].append('Hermetic MIM-only lithium module:16 passed/33 optional native integration skips; native-enabled independent module:49 passed. Full suite and current QC are separately bound below.')
x['pending_final_inputs']=[];x['state']='final'
with (HERE/'selection.final.json').open('x') as f:json.dump(x,f,indent=2);f.write('\n')
print(len(x['files']),len(x['commands']),len(x['repository_references']))
