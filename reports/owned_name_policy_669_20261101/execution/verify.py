"""Explicit Step5 evidence freeze/publication and history-independent verification.

Historical originals are keyed by (identity, raw SHA256), never current paths or
feature Git objects. Only publish writes an exclusively new production package.
"""
from pathlib import Path
from datetime import datetime,timezone
from contextlib import ExitStack
import argparse,gzip,hashlib,io,json,os,stat,subprocess,tarfile

HERE=Path(__file__).resolve().parent
RUN=HERE.parent
ROOT=RUN/'step5-mim'
DEST=Path('reports/owned_name_policy_669_20261101/execution')
BASE='be7170deb00a7c5490f8ade82facf86d45a852a4'
GROUPS={'primary','decisions','source','generation','acceptance','promotion','receipt_chain','chain','unified','checks','independent_review'}
DENIED={'.git','__pycache__','.pytest_cache','.mypy_cache','.venv'}


def require(ok,message):
 if not ok:raise ValueError(message)

def digest(data):return hashlib.sha256(data).hexdigest()
def encoded(value):return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()
def hexsha(value):return isinstance(value,str) and len(value)==64 and all(c in '0123456789abcdef' for c in value)
def key(ref):return ref['identity'],ref['sha256']

def safe(path):
 p=Path(path)
 require(p.parts and '..' not in p.parts and not any(part.casefold() in DENIED for part in p.parts),'Unsafe/excluded path: '+str(p))
 return p

def relative(path):
 p=safe(path);require(not p.is_absolute(),'Expected relative member');return p

def read(path):
 p=safe(path).absolute()
 require(p.is_file() and not any(member.is_symlink() for member in (p,*p.parents)),'Nonregular/aliased file: '+str(p))
 require(p.suffix not in {'.pyc','.db','.sqlite','.sqlite3'},'Excluded cache/database payload')
 return p.read_bytes()

def pointer(value,path):
 for item in path.strip('/').split('/') if path else []:
  item=item.replace('~1','/').replace('~0','~');value=value[int(item)] if isinstance(value,list) else value[item]
 return value


def selection_valid(plan,allow_draft=False):
 require(plan['schema_version']==1 and (plan['state']=='draft' and allow_draft or plan['state']=='final' and not plan['pending']),'Draft/incomplete selection')
 require(not plan.get('unresolved_graph_inputs',[]),'Unresolved selected provenance graph')
 require(plan['base']==BASE and plan['destination']==str(DEST),'Wrong package scope')
 require(set(plan['groups'])==GROUPS,'Incomplete evidence categories')
 require(isinstance(plan['package_readme'],str) and plan['package_readme'].strip(),'Missing selected README')
 require(plan['files'] and plan['commands'] and plan['assertions'] and plan['graphs'] and plan['publications'] and plan['receipt_chain'],'Missing required evidence bindings')
 identities=set()
 for item in plan['files']:
  require(Path(item['identity']).is_absolute() and Path(item['source_path']).is_absolute() and hexsha(item['sha256']) and type(item['bytes']) is int and item['bytes']>=0,'Invalid original identity/hash/size')
  safe(item['identity']);require(key(item) not in identities,'Duplicate original version');identities.add(key(item))
  require(item['group'] in GROUPS,'Unknown evidence category')
 require({item['group'] for item in plan['files']}==GROUPS,'Required group has no archived evidence')
 for omission in plan['omissions']:
  require(omission['kind'] in {'ontology_database','comparison_only','unified_culture_source','rebuildable_product'} and omission['reason'] and hexsha(omission['sha256']),'Unqualified omission')
  require(key(omission) not in identities,'Archived original also marked omitted')
 require(len({key(x) for x in plan['omissions']})==len(plan['omissions']),'Duplicate omission')


def originals_from_sources(plan):
 originals={}
 for item in plan['files']:
  data=read(Path(item['source_path']))
  require(digest(data)==item['sha256'] and len(data)==item['bytes'],'Selected original changed: '+item['identity'])
  originals[key(item)]=data
 return originals


def validate_bindings(plan,originals,allow_draft=False):
 selection_valid(plan,allow_draft=allow_draft)
 expected={key(item) for item in plan['files']}
 require(set(originals)==expected,'Original version set differs')
 for item in plan['files']:
  data=originals[key(item)];require(digest(data)==item['sha256'] and len(data)==item['bytes'],'Original bytes differ')
 omitted={key(item):item for item in plan['omissions']};absent=set(plan['absent_inputs'])
 def raw(identity,sha,allow_omitted=False):
  if (identity,sha) in originals:return originals[identity,sha]
  require(allow_omitted and (identity,sha) in omitted,'Unresolved original version: '+identity+' @ '+str(sha));return None
 def obj(ref):return json.loads(raw(*key(ref)))
 for omission in plan['omissions']:
  if omission['kind']=='ontology_database':
   require(omission.get('label_evidence'),'Ontology omission lacks captured labels')
   for ref in omission['label_evidence']:raw(*key(ref))
 for command in plan['commands']:
  receipt=obj(command['receipt'])
  require(receipt.get('finished_at') and type(receipt.get('exit_code')) is int and receipt.get('argv'),'Unfinished command')
  require(receipt['exit_code']==command['expected_exit'],'Command outcome differs')
  require(command.get('classification') in {'successful_check','expected_negative_control','failed_attempt','interrupted_attempt'},'Missing command classification')
  if receipt['exit_code']:require(command.get('disposition'),'Nonzero command lacks disposition')
  raw(receipt['log'],receipt['log_sha256'])
 for check in plan['assertions']:
  actual=pointer(obj(check['document']),check['pointer'])
  expected_value=check['target']['sha256'] if 'target' in check else check['equals']
  if 'target' in check:raw(*key(check['target']))
  require(actual==expected_value,'JSON evidence assertion differs: '+check['pointer'])
 for graph in plan['graphs']:
  value=pointer(obj(graph['document']),graph['pointer']);shape=graph['shape']
  if shape=='path_hash':entries=[(p,h,None) for p,h in value.items()]
  elif shape=='path_record':entries=[(p,item['sha256'],item.get('bytes')) for p,item in value.items()]
  elif shape=='path_list':entries=[(item['path'],item['sha256'],None) for item in value]
  else:raise ValueError('Unknown graph shape')
  for identity,sha,size in entries:
   if not Path(identity).is_absolute():
    require(graph.get('root_identity') and Path(graph['root_identity']).is_absolute(),'Relative graph input lacks original root')
    identity=str(Path(graph['root_identity'])/relative(identity))
   if sha is None:require(identity in absent,'Missing explicit absence receipt');continue
   data=raw(identity,sha,graph.get('allow_omitted',False))
   if data is not None and size is not None:require(len(data)==size,'Graph original size differs')
 for publication in plan['publications']:
  receipt=obj(publication['receipt']);transaction=receipt['transaction']
  require(receipt['state']=='complete' and receipt['applied'] is True and transaction['applied'] is True,'Publication incomplete')
  require(str(receipt.get('approval','NONE')).startswith('NONE'),'Publication implies approval')
  outputs=receipt['output_sha256'] if 'output_fields' not in publication else {name:receipt[field] for name,field in publication['output_fields'].items()}
  if 'output_fields' in publication:require(receipt['status']=='PASS' and receipt['scientific_approval_added'] is False,'Qualified publication status differs')
  require(len(outputs)==publication['output_count'],'Publication output count differs')
  expected_paths=set()
  for name,sha in outputs.items():
   identity=str(Path(publication['root_identity'])/relative(name));raw(identity,sha);expected_paths.add(identity)
  changed,created=set(transaction['changed']),set(transaction['created'])
  require(not changed&created and changed|created==expected_paths,'Publication transaction scope differs')
  journal=obj(publication['journal']);require(transaction['journal']==publication['journal']['identity'],'Journal identity differs')
  require(journal['status']=='complete' and set(journal['changed'])==changed and set(journal['created'])==created,'Native journal differs')
 links=[obj(ref) for ref in plan['receipt_chain']['receipts']]
 require([item['sequence'] for item in links]==list(range(1,20)),'Expected exact eighteen predecessors and successor19')
 for before,after in zip(links,links[1:]):require(before['after_sha256']==after['before_sha256'],'Receipt chain hash gap')
 final=links[-1];source=obj(plan['receipt_chain']['source_receipt'])
 require(final['records']==source['records'] and str(final['approval']).startswith('NONE'),'Receipt19 source/approval differs')
 raw(*key(plan['receipt_chain']['before']));raw(*key(plan['receipt_chain']['after']))
 require(final['before_sha256']==plan['receipt_chain']['before']['sha256'] and final['after_sha256']==plan['receipt_chain']['after']['sha256'],'Receipt19 canonical hashes differ')
 require(len(final['position_map'])==final['before_row_count'],'Receipt19 position map length differs')
 require(final['changed_rows']==sum(c['kind']=='changed' for c in final['changes']) and final['added_rows']==sum(c['kind']=='added' for c in final['changes']) and final['removed_rows']==sum(c['kind']=='removed' for c in final['changes']),'Receipt19 delta counts differ')
 return {'selection_state':plan['state'],'original_versions':len(originals),'omitted_historical_inputs':len(omitted),'receipt_links':len(links)}


def bound_selection(frozen,selection):
 require(frozen['kind']=='step5_mim_execution_evidence','Wrong frozen package kind')
 require(digest(selection)==frozen['selection_sha256'],'Selection hash differs')
 plan=json.loads(selection);require(plan==frozen['plan'],'Frozen plan differs semantically from selected plan')
 require(plan['run_root']==frozen['run_root'],'Recorded run root differs');selection_valid(plan);return plan


def freeze(selection,output):
 data=read(selection);plan=json.loads(data);selection_valid(plan)
 require(plan['run_root']==str(RUN) and output.parent==HERE and not output.exists(),'Wrong/frozen author output')
 originals=originals_from_sources(plan);validate_bindings(plan,originals)
 # Historical source revisions remain attributes. Author-selected present sources
 # and their exact bytes, not old Git objects, are the freeze authority.
 require(originals_from_sources(plan)==originals,'Input changed during freeze')
 frozen={'kind':'step5_mim_execution_evidence','captured_at':datetime.now(timezone.utc).isoformat(),'run_root':str(RUN),'selection_path':str(selection),'selection_sha256':digest(data),'packager_sha256':digest(read(Path(__file__))),'plan':plan}
 with output.open('xb') as stream:stream.write(encoded(frozen))
 return {'frozen':str(output),'sha256':digest(read(output)),**validate_bindings(plan,originals)}


def payload_archive(originals):
 by_hash={digest(data):data for data in originals.values()};raw_container=io.BytesIO();separate={}
 with tarfile.open(fileobj=raw_container,mode='w',format=tarfile.USTAR_FORMAT) as archive:
  for sha,data in sorted(by_hash.items()):
   if data.startswith(b'\x1f\x8b') and len(data)>1_000_000:
    separate['blobs/'+sha+'.bin']=data;continue
   item=tarfile.TarInfo(sha);item.size=len(data);item.mtime=0;item.mode=0o644;item.uid=item.gid=0;item.uname=item.gname='';archive.addfile(item,io.BytesIO(data))
 decoded=raw_container.getvalue();packed=gzip.compress(decoded,mtime=0)
 return {'payloads.tar.gz':packed,**separate},{'decoded_sha256':digest(decoded),'decoded_bytes':len(decoded)},set(by_hash)


def write_new_package(destination,payloads,manifest_bytes,final_input_check):
 """Create through retained directory handles; never follow a late path alias.

 Failed owned output is retained. Existing/replacement paths are never removed.
 Route and inode checks detect concurrent replacement; retained file handles
 prevent a replacement from redirecting bytes even between those checks.
 """
 destination=safe(destination).absolute();root=safe(ROOT).absolute()
 require(destination.is_relative_to(root),'Package destination is outside owned root')
 flags=os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW
 with ExitStack() as stack:
  directories={};opened_files=[]
  def retain(fd):stack.callback(os.close,fd);return fd
  directories[Path('/')]=retain(os.open('/',flags))
  def identity(status):return status.st_dev,status.st_ino
  def check():
   for path,fd in directories.items():
    actual=os.stat(path,follow_symlinks=False)
    require(stat.S_ISDIR(actual.st_mode) and identity(actual)==identity(os.fstat(fd)),'Publication directory route changed: '+str(path))
   for parent,name,fd in opened_files:
    actual=os.stat(name,dir_fd=directories[parent],follow_symlinks=False)
    require(stat.S_ISREG(actual.st_mode) and identity(actual)==identity(os.fstat(fd)),'Publication file reservation changed: '+name)
  def directory(path,*,exclusive=False):
   if path in directories:return directories[path]
   parent_fd=directory(path.parent);check()
   if exclusive:os.mkdir(path.name,0o755,dir_fd=parent_fd)
   else:
    try:fd=os.open(path.name,flags,dir_fd=parent_fd)
    except FileNotFoundError:
     require(path.is_relative_to(root),'Owned repository root/ancestor is absent')
     os.mkdir(path.name,0o755,dir_fd=parent_fd);fd=os.open(path.name,flags,dir_fd=parent_fd)
    directories[path]=retain(fd);check();return fd
   directories[path]=retain(os.open(path.name,flags,dir_fd=parent_fd));check();return directories[path]
  directory(destination,exclusive=True)
  def write(name,data):
   target=destination/relative(name);parent_fd=directory(target.parent);check()
   fd=retain(os.open(target.name,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o644,dir_fd=parent_fd));opened_files.append((target.parent,target.name,fd));check()
   with os.fdopen(os.dup(fd),'wb') as stream:stream.write(data);stream.flush()
   check()
  for name,data in payloads.items():write(name,data)
  final_input_check();check();write('manifest.json',manifest_bytes);check()


def publish(inputs):
 frozen_bytes=read(inputs);frozen=json.loads(frozen_bytes)
 require(frozen['kind']=='step5_mim_execution_evidence' and frozen['run_root']==str(RUN),'Wrong frozen author scope')
 require(digest(read(Path(__file__)))==frozen['packager_sha256'],'Packager changed since freeze')
 selection=read(Path(frozen['selection_path']));plan=bound_selection(frozen,selection)
 originals=originals_from_sources(plan);validate_bindings(plan,originals)
 payloads,container,hashes=payload_archive(originals)
 payloads.update({'selection.final.json':selection,'final-inputs.json':frozen_bytes,'README.md':plan['package_readme'].encode(),'verify.py':read(Path(__file__))})
 manifest={'schema_version':1,'files':{name:{'sha256':digest(data),'bytes':len(data)} for name,data in payloads.items()},'container':container,'originals':[{'identity':i,'sha256':h,'bytes':len(data),'storage':('blobs/'+h+'.bin') if 'blobs/'+h+'.bin' in payloads else 'payloads.tar.gz','member':h} for (i,h),data in sorted(originals.items())],'unique_payloads':sorted(hashes),'scientific_approval_added':False}
 destination=ROOT/DEST
 require(not destination.exists() and not destination.is_symlink() and not any(p.is_symlink() for p in destination.parents),'Publication requires a fresh unaliased directory')
 def final_input_check():
  require(originals_from_sources(plan)==originals and read(Path(frozen['selection_path']))==selection,'Input changed during publication; partial evidence retained')
 write_new_package(destination,payloads,encoded(manifest),final_input_check)
 return verify(destination)


def verify(package,repository=None,require_tracked=False,current_scope=False):
 package=package.absolute();manifest=json.loads(read(package/'manifest.json'))
 require(manifest['schema_version']==1 and manifest['scientific_approval_added'] is False,'Wrong package version/scope')
 require(not any(p.is_symlink() for p in package.rglob('*')),'Aliased package entry')
 actual={str(p.relative_to(package)) for p in package.rglob('*') if p.is_file()}
 require(actual==set(manifest['files'])|{'manifest.json'},'Package membership differs')
 for name,item in manifest['files'].items():
  data=read(package/relative(name));require(digest(data)==item['sha256'] and len(data)==item['bytes'],'Package bytes differ: '+name)
 frozen=json.loads(read(package/'final-inputs.json'));plan=bound_selection(frozen,read(package/'selection.final.json'))
 require(read(package/'README.md')==plan['package_readme'].encode(),'README differs from selected text')
 require(digest(read(package/'verify.py'))==frozen['packager_sha256'],'Verifier identity differs')
 decoded=gzip.decompress(read(package/'payloads.tar.gz'))
 require(digest(decoded)==manifest['container']['decoded_sha256'] and len(decoded)==manifest['container']['decoded_bytes'],'Decoded container differs')
 blobs={}
 with tarfile.open(fileobj=io.BytesIO(decoded),mode='r:') as archive:
  for item in archive:
   require(item.isfile() and hexsha(item.name) and item.name not in blobs,'Unsafe/duplicate archive member')
   data=archive.extractfile(item).read();require(digest(data)==item.name,'Container member identity differs');blobs[item.name]=data
 originals={}
 for item in manifest['originals']:
  identity=key(item);require(identity not in originals,'Duplicate archived original version')
  require(item['member']==item['sha256'],'Original/member SHA differs')
  if item['storage']=='payloads.tar.gz':data=blobs[item['member']]
  else:
   require(item['storage']=='blobs/'+item['sha256']+'.bin','Unexpected raw blob locator');data=read(package/relative(item['storage']))
  require(digest(data)==item['sha256'] and len(data)==item['bytes'],'Archived original bytes differ');originals[identity]=data
 require({digest(data) for data in originals.values()}==set(manifest['unique_payloads']),'Payload index differs')
 require(set(blobs)=={item['sha256'] for item in manifest['originals'] if item['storage']=='payloads.tar.gz'},'Unreferenced container payload')
 require({name for name in manifest['files'] if name.startswith('blobs/')}=={item['storage'] for item in manifest['originals'] if item['storage']!='payloads.tar.gz'},'Unreferenced standalone blob')
 result=validate_bindings(plan,originals)
 require(not (require_tracked or current_scope) or repository is not None,'Repository required for requested scope check')
 if current_scope:
  for name,expected in plan['current_scope'].items():
   data=read(repository/relative(name));require(digest(data)==expected,'Current publication scope differs')
 if require_tracked:
  for name in sorted(actual):
   relative_name=(package/relative(name)).relative_to(repository).as_posix()
   committed=subprocess.check_output(['git','show','HEAD:'+relative_name],cwd=repository)
   require(committed==read(package/relative(name)),'Current committed package blob differs')
 return {'status':'PASS',**result,'archive_members':len(actual),'tracked_checked':require_tracked,'current_scope_checked':current_scope,'scientific_approval_added':False}


def main():
 parser=argparse.ArgumentParser(description=__doc__);modes=parser.add_subparsers(dest='mode',required=True)
 f=modes.add_parser('freeze');f.add_argument('--selection',type=Path,required=True);f.add_argument('--output',type=Path,required=True)
 p=modes.add_parser('publish');p.add_argument('--inputs',type=Path,required=True)
 v=modes.add_parser('verify');v.add_argument('--package',type=Path,required=True);v.add_argument('--repository',type=Path);v.add_argument('--require-tracked',action='store_true');v.add_argument('--current-scope',action='store_true')
 args=parser.parse_args()
 if args.mode=='freeze':result=freeze(args.selection.absolute(),args.output.absolute())
 elif args.mode=='publish':result=publish(args.inputs.absolute())
 else:result=verify(args.package.absolute(),args.repository.absolute() if args.repository else None,args.require_tracked,args.current_scope)
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
