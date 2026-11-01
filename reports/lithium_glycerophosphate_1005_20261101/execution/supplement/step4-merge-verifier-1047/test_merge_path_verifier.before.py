"""Exercise the exact closure-verifier function on real Git trees; never run cleanup."""
from pathlib import Path
import ast
import subprocess
import pytest

SOURCE=Path(__file__).resolve().parent.parent/'verify_mim_merge_nul.py'
module=ast.parse(SOURCE.read_text())
function=next(n for n in module.body if isinstance(n,ast.FunctionDef) and n.name=='verified_changed_paths')
ns={'subprocess':subprocess}
exec(compile(ast.Module(body=[function],type_ignores=[]),str(SOURCE),'exec'),ns)
verify=ns['verified_changed_paths']

@pytest.mark.parametrize('name',['plain.yaml','Α-lipoic_Acid.yaml','line\nbreak.yaml','x[1].yaml',' leading.yaml'])
def test_exact_real_git_paths_and_different_merged_bytes(tmp_path,name):
 def git(*args):return subprocess.check_output(['git',*args],cwd=tmp_path)
 git('init','-q');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid')
 p=tmp_path/name;p.write_text('base\n');git('add','--',name);git('commit','-qm','base');base=git('rev-parse','HEAD').decode().strip()
 p.write_text('reviewed\n');git('commit','-qam','reviewed');head=git('rev-parse','HEAD').decode().strip()
 assert verify(tmp_path,base,head,head)==[name]
 p.write_text('wrong merge\n');git('commit','-qam','wrong');bad=git('rev-parse','HEAD').decode().strip()
 with pytest.raises(AssertionError,match='Merged files differ'):
  verify(tmp_path,base,head,bad)
