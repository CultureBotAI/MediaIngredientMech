"""Read-only worker overlap leads against explicitly configured peer ledgers.

The worker2 successor is selected explicitly. Peer paths are coordinator-selected
observations, not assertions that a concurrently running peer has finalized work.
No winning owner, identity equivalence or application is selected.
"""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import yaml

ROOT = Path(__file__).resolve().parent
CAMPAIGN = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--proposals', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    reads = {}
    def read(p):
        p = Path(p)
        raw = p.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if str(p) in reads and reads[str(p)] != digest:
            raise ValueError('Input changed during repeated read: ' + str(p))
        reads[str(p)] = digest
        return raw, digest
    config = json.loads(read(CAMPAIGN/'preflight/campaign-accounting-v1/active-bundles-v2.json')[0])
    groups = {k: defaultdict(list) for k in ('owner_path','identifier','preferred_term')}
    source_documents = defaultdict(list)
    errors, heads, observations = [], {}, []
    for bundle in config['bundles']:
        slot = bundle['worker_slot']
        tree = Path(bundle['mim_root'])
        heads[str(slot)] = subprocess.check_output(['git','-C',str(tree),'rev-parse','HEAD'],text=True).strip()
        ledger = args.proposals.resolve() if slot == 2 else Path(bundle['proposals'])
        artifact = ROOT.parent if slot == 2 else Path(bundle['artifact_root'])
        try:
            raw, ledger_hash = read(ledger)
            ps = json.loads(raw)['proposals']
        except (OSError, ValueError, KeyError) as exc:
            errors.append({'worker':slot,'ledger':str(ledger),'error':str(exc)})
            continue
        for p in ps:
            try:
                cap = p['after_capture']
                rel = Path(cap['path'])
                if cap['root'] != 'artifact' or rel.is_absolute() or '..' in rel.parts:
                    raise ValueError('Invalid artifact path')
                raw, actual = read(artifact/rel)
                if actual != cap['sha256']:
                    raise ValueError('Payload differs from ledger pin')
                value = yaml.safe_load(raw)
                observation = {'worker':slot,'head_at_observation':heads[str(slot)],
                    'proposal_id':p['proposal_id'],'case_ids':p['case_ids'],
                    'owner_path':p['owner_path'],'before_sha256':p.get('before_sha256'),
                    'kind':p['kind'],'payload':str(artifact/rel),'payload_sha256':actual,
                    'ledger':str(ledger),'ledger_sha256':ledger_hash,
                    'identifier':value.get('identifier'),'preferred_term':value.get('preferred_term'),
                    'description':p.get('description'),
                    'review_scope':'Observed proposal bytes only; no peer science or review attested'}
                observations.append(observation)
                # Shared primary recipe documents are weaker leads than equal
                # owner IDs: one recipe can contain many distinct stocks.
                urls = set(re.findall(r'https?://[^\s\"<>]+', raw.decode('utf-8')))
                recipe_urls = sorted(u.rstrip("',.;)") for u in urls if any(marker in u for marker in ('DSMZ_Medium','GRMD=','NBRCMediumDetail','/rest/medium/','/rest/solution/')))
                observation['primary_recipe_urls_observed'] = recipe_urls
                for url in recipe_urls:
                    source_documents[url].append(observation)
                for field, group in groups.items():
                    if observation[field]:
                        key = observation[field] if field == 'owner_path' else observation[field].casefold()
                        group[key].append(observation)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                errors.append({'worker':slot,'proposal_id':p.get('proposal_id'),'error':str(exc)})
    def relevant(rows):
        return any(r['worker']==2 for r in rows) and any(r['worker']!=2 for r in rows)
    changed = [p for p,h in reads.items() if not Path(p).is_file() or hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h]
    report = {'at':datetime.now(timezone.utc).isoformat(),'worker_heads':heads,
        'worker02_proposal_ledger':str(args.proposals),'proposal_count_observed':len(observations),
        'same_owner_path':{k:v for k,v in groups['owner_path'].items() if relevant(v)},
        'identifier_leads':{k:v for k,v in groups['identifier'].items() if relevant(v)},
        'preferred_term_leads':{k:v for k,v in groups['preferred_term'].items() if relevant(v)},
        'shared_recipe_document_leads':{k:v for k,v in source_documents.items() if relevant(v)},
        'unreadable_or_in_progress':errors,'changed_during_read':changed,'input_sha256':reads,
        'observer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'reconciliation_required':True,'owner_or_payload_selected':False,
        'limitations':'Only coordinator-configured peer ledgers were observed; unselected newer peer continuations are outside this mechanical pass. Exact paths, identifiers and labels are conflict leads, never substance equivalence. Final peer payloads and all source scopes require coordinator reconciliation.'}
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:len(report[k]) for k in ('same_owner_path','identifier_leads','preferred_term_leads','unreadable_or_in_progress','changed_during_read')}))


if __name__ == '__main__':
    main()
