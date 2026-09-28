#!/usr/bin/env python3
"""Run only AFTER committing the initial repository state; creates PR edits."""
from pathlib import Path
import sys
root = Path(__file__).resolve().parent
target = root/'force-app/main/default/profiles'
files = sorted(target.glob('*.profile-meta.xml'))
if not files:
    sys.exit('No profiles found')
for p in files:
    s = p.read_text(encoding='utf-8')
    a = '  <classAccesses>\n    <apexClass>QA_DeleteMe</apexClass>\n    <enabled>true</enabled>\n  </classAccesses>\n'
    if a not in s:
        sys.exit(f'Missing expected class access: {p}')
    p.write_text(s.replace(a, '', 1), encoding='utf-8')
for p in (root/'force-app/main/default/classes').glob('QA_DeleteMe.cls*'):
    p.unlink()
print(f'Changed {len(files)} profiles and deleted one Apex class + metadata. Commit on a new branch.')
