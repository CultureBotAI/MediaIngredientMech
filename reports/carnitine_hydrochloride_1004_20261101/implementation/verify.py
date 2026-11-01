"""Read-only byte verification of this bounded evidence package and referenced inputs."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked(path, entry):
    assert path.is_file() and not path.is_symlink(), path
    data = path.read_bytes()
    assert digest(data) == entry['sha256'], path
    assert len(data) == entry['bytes'], path
    return data


def main():
    package = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repository-root', type=Path, default=package.parents[2])
    args = parser.parse_args()
    repo = args.repository_root.resolve()
    manifest = json.loads((package / 'manifest.json').read_text())
    actual = {str(p.relative_to(package)) for p in package.rglob('*') if p.is_file()}
    assert actual == set(manifest['files']) | {'manifest.json'}, 'Package inventory drift'
    for name, entry in manifest['files'].items():
        checked(package / name, entry)
    references = {}
    for name in ['repository-references.json', 'maintained-source-references.json']:
        for relative, entry in json.loads((package / name).read_text())['files'].items():
            checked(repo / relative, entry)
            references[relative] = entry
    for name in ['preimage-references.json', 'promotion-preimage-references.json']:
        data = json.loads((package / 'application' / name).read_text())
        for entry in data['large_preimages']:
            compressed = (repo / entry['repository_gzip_path']).read_bytes()
            assert digest(compressed) == entry['gzip_sha256'], entry
            raw = gzip.decompress(compressed)
            assert digest(raw) == entry['raw_sha256'], entry
            assert len(raw) == entry['raw_bytes'], entry
        journal = data['journal']
        filename = 'source-apply-native-journal.json.gz' if name == 'preimage-references.json' else 'mapping-promotion-native-journal.json.gz'
        compressed = checked(package / 'application' / filename, journal)
        raw = gzip.decompress(compressed)
        assert digest(raw) == journal['uncompressed_sha256'], filename
        assert len(raw) == journal['uncompressed_bytes'], filename
    print(json.dumps({'status': 'PASS', 'package_files': len(manifest['files']),
                      'repository_references': len(references),
                      'manifest_sha256': digest((package / 'manifest.json').read_bytes())}, indent=2))


if __name__ == '__main__':
    main()
