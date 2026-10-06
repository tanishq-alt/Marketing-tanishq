from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / 'README.md',
    root / 'SKILL.md',
    root / 'sources' / 'bibliography.md',
]
errors = []
for p in required:
    if not p.exists():
        errors.append(f'Missing: {p.relative_to(root)}')

skills = list((root / 'skills').glob('*/SKILL.md'))
if len(skills) < 10:
    errors.append('Expected at least 10 task skills.')

for p in root.rglob('*.md'):
    if p.stat().st_size == 0:
        errors.append(f'Empty file: {p.relative_to(root)}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {len(skills)} skills, {len(list(root.rglob("*.md")))} markdown files')
