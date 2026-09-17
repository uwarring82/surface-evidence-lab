"""Check preserved source bytes against the manifest; no network or dependencies."""
import argparse
import hashlib
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--require-local-archive', action='store_true',
                        help='Require the two files excluded from the default Git commit.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'literature/source-manifest.json').read_text(encoding='utf-8'))
    passed = skipped = failed = 0
    for source in manifest['sources']:
        for record in source.get('archived_files', []):
            relative = record['path']
            path = (root / relative).resolve()
            if root not in path.parents:
                print('FAIL unsafe path:', relative)
                failed += 1
                continue
            if not path.is_file():
                optional = record.get('optional_in_repository', False)
                if optional and not args.require_local_archive:
                    print('OPTIONAL absent:', relative)
                    skipped += 1
                else:
                    print('FAIL missing:', relative)
                    failed += 1
                continue
            data = path.read_bytes()
            if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
                print('FAIL size/hash:', relative)
                failed += 1
            else:
                print('PASS:', relative)
                passed += 1
    print(f'{passed} passed; {skipped} optional absent; {failed} failed. {len(manifest["sources"])} source records.')
    return 1 if failed else 0

if __name__ == '__main__':
    raise SystemExit(main())
