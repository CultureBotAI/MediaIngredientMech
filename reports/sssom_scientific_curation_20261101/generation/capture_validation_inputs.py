from pathlib import Path
import datetime, hashlib, importlib.metadata, json, subprocess, sys

RUN = Path(__file__).resolve().parent
ORIGINAL = RUN.parent.parent
OLD = RUN.parent/'sssom-generation-20261031T213407Z'
MIM = RUN/'mim'
CLAW = RUN/'claw'
KG = (ORIGINAL/'../../KG-Hub/KG-Microbe/kg-microbe').resolve()
CM = (ORIGINAL/'../CultureMech').resolve()
inputs = {}

def capture(path, role):
    path = path.resolve()
    if path in inputs:
        return
    h=hashlib.sha256()
    with path.open('rb') as stream:
        while chunk := stream.read(8*1024*1024):
            h.update(chunk)
    inputs[path]=dict(path=str(path),sha256=h.hexdigest(),bytes=path.stat().st_size,role=role)

for p in (MIM/'data/ingredients').rglob('*.yaml'):
    capture(p,'maintained MIM record; mapped records feed builder and all records inform native validation')
for name in ['data/curated/mapped_ingredients.yaml','data/curated/unmapped_ingredients.yaml',
             'mappings/ingredient_mappings.sssom.tsv','mappings/other_cross_record_baseline.tsv',
             'MAPPING_SEMANTICS.md','AGENTS.md','docs/SSSOM_RELEASE.md','conf/id_label_targets.yaml',
             'src/mediaingredientmech/schema/mediaingredientmech.yaml','scripts/validate_sssom_invariants.py',
             'scripts/validate_id_label_correspondence.py','scripts/reconcile_sssom.py',
             'scripts/validate_published_curies.py','scripts/check_sssom_subject_files.py',
             'reports/sssom_completion_20260921/review.json','UNIFIED_INGREDIENT_MAPPING.tsv',
             '.github/workflows/qc-evidence.yaml','workflow/mech-workflow.yaml',
             '.claude/skills/mediaingredientmech-evolve-workflow/SKILL.md',
             '.claude/skills/curate-yaml-record/SKILL.md',
             '.claude/skills/map-media-ingredients/SKILL.md',
             '.claude/skills/review-sssom-output/SKILL.md']:
    capture(MIM/name,'native input, contract, validation implementation or maintained publication preserved')
for name in ['scripts/build_mim_ingredient_sssom.py','scripts/kgm_unified_mappings.py',
             'workspace/reports/kg_microbe_residual_p25_categorized.json']:
    capture(CLAW/name,'actual current raw-builder code or copied residual input')
capture(KG/'mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz','actual KG unified entity mapping read by builder')
capture(KG/'data/transformed/mediadive/nodes.tsv','read-only KG comparison input; not substituted for builder unified mappings')
for p in sorted((OLD/'ontology-cache/oaklib').glob('*.db')):
    capture(p,'actual local ontology database snapshot used by builder or native label validation')
for name in ['ingredients_list.tsv','ingredient_occurrences.tsv','mapped_ingredients.yaml','unmapped_ingredients.yaml']:
    capture(CM/'output'/name,'current CultureMech comparison output only; not bulk imported or read by raw MIM builder')

def git(root,*args):
    return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()

repositories={}
for name,root in [('mim',MIM),('claw',CLAW),('kg_microbe',KG),('culturemech',CM)]:
    diff=git(root,'diff','--binary','HEAD')
    repositories[name]=dict(path=str(root),revision=git(root,'rev-parse','HEAD'),branch=git(root,'branch','--show-current'),
                            origin=git(root,'remote','get-url','origin'),status=git(root,'status','--porcelain=v1'),
                            tracked_diff_sha256=hashlib.sha256(diff.encode()).hexdigest())
    (RUN/'provenance'/f'{name}-tracked-diff.patch').write_text(diff)
versions={}
for name in ['sssom','oaklib','PyYAML','linkml','linkml-runtime','pytest']:
    try:versions[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:versions[name]='unavailable in capture runtime'
old_inputs=json.loads((OLD/'provenance/inputs.json').read_text())['inputs']
old_hashes={x['path']:x['sha256'] for x in old_inputs}
changes=[]
for item in inputs.values():
    path=item['path'];old_path=path.replace(str(MIM),str(OLD/'repo')).replace(str(CLAW),str((ORIGINAL/'../../KG-Hub/KG-Microbe/culturebotai-claw').resolve()))
    if old_path in old_hashes and old_hashes[old_path]!=item['sha256']:
        changes.append({'current_path':path,'prior_path':old_path,'before_sha256':old_hashes[old_path],'after_sha256':item['sha256']})
result=dict(captured_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),repositories=repositories,
            python=sys.version,package_versions=versions,inputs=list(inputs.values()),changes_from_prior_generation=changes,
            scope='Current exact working-tree bytes. Raw builder consumes MIM mapped records, copied CLAW residual, current KG unified mapping and ontology label sources. CM and Mediadive data remain comparison inputs. Historical scientific holds are not cleared.')
(RUN/'provenance/validation-inputs.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'input_files':len(inputs),'changes_from_prior_generation':changes,'manifest':str(RUN/'provenance/validation-inputs.json')},indent=2))
