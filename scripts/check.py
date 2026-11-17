#!/usr/bin/env python3
"""Check the design system: generated files are up to date and text colors pass WCAG AA (4.5:1)."""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
T = json.loads((ROOT / 'tokens.json').read_text())

# (text, background) pairs used in the components
PAIRS = [('ink', 'bg'), ('ink', 'surface'), ('muted', 'bg'), ('muted', 'surface'), ('muted', 'sunk'),
         ('lapis', 'bg'), ('lapis', 'surface'), ('lapis', 'lapis-soft'),
         ('saffron', 'surface'), ('saffron', 'saffron-soft'), ('saffron', 'bg'),
         ('good', 'good-soft'), ('good', 'surface'), ('bad', 'surface'), ('bad', 'bad-soft'),
         ('bg', 'lapis'), ('bg', 'ink')]


def lum(h):
    h = h.lstrip('#')
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def ratio(a, b):
    a, b = lum(a), lum(b)
    return (max(a, b) + .05) / (min(a, b) + .05)


def main():
    errors = []
    r = subprocess.run([sys.executable, str(ROOT / 'scripts/build.py'), '--check'], capture_output=True, text=True)
    if r.returncode:
        errors.append(r.stderr.strip() or r.stdout.strip())
    for mode in ('light', 'dark'):
        c = {k: v['value'] for k, v in T['color'][mode].items()}
        if set(c) != set(T['color']['light']):
            errors.append(f'{mode}: colors differ from light')
        for fg, bg in PAIRS:
            x = ratio(c[fg], c[bg])
            if x < 4.5:
                errors.append(f'{mode}: {fg} on {bg} is {x:.2f}:1, needs 4.5:1')
    # saffron button text (bg on saffron) is 14px bold: large-text rule 3:1
    for mode in ('light', 'dark'):
        c = {k: v['value'] for k, v in T['color'][mode].items()}
        if ratio(c['bg'], c['saffron']) < 3:
            errors.append(f'{mode}: button text on saffron below 3:1')
    if errors:
        sys.exit('\n'.join(errors))
    print('ok')


if __name__ == '__main__':
    main()
