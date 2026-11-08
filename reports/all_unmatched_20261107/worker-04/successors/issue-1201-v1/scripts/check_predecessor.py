"""Fail if a published predecessor artifact or maintained input changed."""
import hashlib,json,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parents[1];R=Path(__file__).resolve().parents[6]
def check():
 manifest=json.loads((S/'provenance/published-predecessor-files.json').read_text());errors=[]
 for row in manifest['files']:
  p=R/row['path']
  if not p.is_file() or p.is_symlink() or hashlib.sha256(p.read_bytes()).hexdigest()!=row['sha256']:errors.append(row['path'])
 changed=subprocess.check_output(['git','diff','e000d66dd26ab053e9b17ce7bf8d3c873c3dde99','--name-only','--','data','mappings','UNIFIED_INGREDIENT_MAPPING.tsv','MAPPING_SEMANTICS.md','src','schema','scripts','conf'],cwd=R).decode().splitlines()
 untracked=subprocess.check_output(['git','ls-files','--others','--','data/ingredients','data/curated','mappings'],cwd=R).decode().splitlines()
 result={'predecessor_head':manifest['head'],'published_files_checked':len(manifest['files']),'changed_published_files':errors,'changed_maintained_inputs':changed,'untracked_maintained_inputs_including_ignored':untracked,'status':'FAIL' if errors or changed or untracked else 'PASS'}
 return result
if __name__=='__main__':
 result=check();print(json.dumps(result,indent=2));sys.exit(result['status']!='PASS')
