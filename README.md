# BuddhistAI design system

<img src="assets/logo-128.png" width="64" align="right" alt="">

One look for every BuddhistAI site: the homepage, the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/), the [knowledge base](https://buddhistai.github.io/knowledge-base/), the arena and the org profile. It comes from the homepage design of 2026-11-17.

**See it:** https://buddhistai.github.io/design/ (style guide with every part).

## What is in it

| File | What it is |
| --- | --- |
| `tokens.json` | Colors (light and dark), fonts, sizes, spacing, radius. **The source of truth.** |
| `css/base.css`, `css/components.css` | Page styles and parts: buttons, chips, cards, Top performance / Best value picks, badges, status labels, tables, maturity ladder, paste-a-repo box, header, footer. |
| `buddhistai.css` | Tokens + base + components in one file. Link or copy this. |
| `tailwind.preset.js` | Tailwind preset (colors, fonts, radius as CSS variables). |
| `tokens.js` | Tokens as a JS module, for React code and charts. |
| `assets/` | Logo in ink (`logo.png`) and for dark backgrounds (`logo-dark.png`), 128px versions, org avatar. |
| `VOICE.md` | Writing rules: plain English, our words, neutral credits. |
| `index.html` | The style guide page. |

## Use it

**Static site (GitHub Pages, Jekyll, a Python generator).** Copy `buddhistai.css` and the logo files into the site. Add the fonts and the CSS:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Noto+Serif+Tibetan:wght@400&display=swap">
<link rel="stylesheet" href="/buddhistai.css">
```

Put site-only rules in a second CSS file that uses the variables (`var(--lapis)`, `var(--r-md)`), never new hex colors.

**React + Tailwind (the FastAPI + React leaderboard).** Copy `buddhistai.css` and `tailwind.preset.js`:

```js
// tailwind.config.js
module.exports = { presets: [require('./tailwind.preset.js')], content: ['./src/**/*.{ts,tsx}'] };
```

```tsx
import './buddhistai.css';            // tokens + parts; dark mode follows the system
<div className="bg-surface text-ink border border-line rounded-md font-display">…</div>
<div className="pick top"><span className="lab">Top performance</span>…</div>
```

Without Tailwind, `import { tokens } from './tokens.js'` gives the same values.

**Which sites use it now:** buddhist-benchmarks (leaderboard site, `site/buddhistai.css`), knowledge-base (`assets/buddhistai.css`). Org profile banners use the same ink and paper colors.

## Rules

- Colors mean one thing each. **Lapis** = links, primary action, Top performance. **Saffron** = contribute, Best value, labels above headings. **Green** = measured, new leader, gains. **Red** (`--bad`) = losses and errors only.
- Every color pair passes WCAG AA for normal text in light and dark mode. Check with `python3 scripts/check.py` after a change.
- Respect dark mode: use the variables, never fixed colors. `data-theme="light"` or `"dark"` on `<html>` forces a theme.
- Tibetan text gets `lang="bo"` (font and size come from the CSS).
- Layout works at 360px wide with a 16px side gutter and no sideways scroll.
- Words follow [VOICE.md](VOICE.md).

## Change it

1. Edit `tokens.json` or `css/*.css`.
2. Run `python3 scripts/build.py`, then `python3 scripts/check.py`.
3. Bump `version` in `tokens.json` (semver: new token or part = minor, changed value = patch, renamed or removed = major) and add a line to `CHANGELOG.md`.
4. Copy `buddhistai.css` into the sites that use it.

MIT license. Contributors: NT, Claude, and everyone who reviews it.
