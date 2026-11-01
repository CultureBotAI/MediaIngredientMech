from pathlib import Path
import copy, hashlib, json, sys
import yaml
run = Path(__file__).resolve().parent
phase = sys.argv[1] if len(sys.argv) > 1 else 'final'
assert phase in {'final', 'ready'}
source = run/'mim/conf/id_label_targets.yaml'
config = yaml.safe_load(source.read_text())
original = copy.deepcopy(config)
config['targets'] = [x for x in config['targets'] if x['name'] == 'sssom']
assert len(config['targets']) == 1
config['targets'][0]['glob'] = f'output/sssom-scientific-audit/{phase}.sssom.tsv'
for key in original.keys() - {'targets'}:
    assert original[key] == config[key]
out = run/f'provenance/{phase}-candidate-id-label-config.yaml'
out.write_text(yaml.safe_dump(config, sort_keys=False))
receipt = dict(source_config=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
               derived_config=str(out),derived_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
               changes=['targets restricted to native sssom target','only target glob redirected to diagnostic candidate'],
               all_other_configuration_identical=True)
(run/f'provenance/{phase}-candidate-id-label-config.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
