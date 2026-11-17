# Notes for agents working in this repo

- `tokens.json` is the source of truth. Never hand-edit `css/tokens.css`, `buddhistai.css`, `tailwind.preset.js` or `tokens.js`: run `python3 scripts/build.py`, then `python3 scripts/check.py`.
- Never add a hex color outside `tokens.json`. Every text color pair must pass WCAG AA in light and dark (check.py).
- Class names follow the homepage design; do not rename a class without a major version bump.
- Bump `version` in tokens.json (semver) and add a CHANGELOG line for any change, then copy `buddhistai.css` into the sites that use it (buddhist-benchmarks `site/`, knowledge-base `assets/`).
- Words follow VOICE.md: plain English for non-native readers, "Buddhist tasks", "Top performance" / "Best value", Share → Measure → Release, neutral credits.
