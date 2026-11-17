# Notes for agents working in this repo

## Start here (every BuddhistAI repo)

- Read the maintainer handbook first: https://buddhistai.github.io/knowledge-base/handbook/ (source: BuddhistAI/knowledge-base `handbook/`). Follow its rules and conventions.
- Check the Development board for cards assigned to you: https://github.com/orgs/BuddhistAI/projects/3. Status and next steps: `handbook/status.md`.
- Rules: plain English for non-native readers, no idioms. "Buddhist tasks", not only texts. "Top performance" and "Best value". Neutral credits: WeBuddhist is one contributor among others. Never invent data, scores, votes or links. Never edit generated files by hand.
- buddhist-benchmarks stays clean (short `result.json`, outputs, scores). Provenance records (`buddhistai/provenance@1`) live in the skill's own repo.
- When you change something the handbook describes, update the handbook in the same pull request.
- This repo: the design system. `tokens.json` is the source of truth. Run `python3 scripts/build.py`, then `python3 scripts/check.py`, then copy `buddhistai.css` into the sites.

## This repo

- `tokens.json` is the source of truth. Never hand-edit `css/tokens.css`, `buddhistai.css`, `tailwind.preset.js` or `tokens.js`: run `python3 scripts/build.py`, then `python3 scripts/check.py`.
- Never add a hex color outside `tokens.json`. Every text color pair must pass WCAG AA in light and dark (check.py).
- Class names follow the homepage design; do not rename a class without a major version bump.
- Bump `version` in tokens.json (semver) and add a CHANGELOG line for any change, then copy `buddhistai.css` into the sites that use it (buddhist-benchmarks `site/`, knowledge-base `assets/`).
- Words follow VOICE.md: plain English for non-native readers, "Buddhist tasks", "Top performance" / "Best value", Share → Measure → Release, neutral credits.
