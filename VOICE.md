# How BuddhistAI writes

Many readers speak English as a second or third language. Many use a translation tool. Write so that a careful reader with basic English, or a machine translator, gets it right the first time.

## Plain English

- Short sentences. One idea in each sentence.
- Common words. "Use", not "leverage". "Find", not "surface". "Test", not "battle-test".
- No idioms, slang or metaphors. Not "in the open", "ship it", "lab notebook", "side by side", "under the hood", "low-hanging fruit", "move the needle".
- Say who does what: "We score your skill", not "Skills are scored".
- Write numbers as numbers, with units: "$0.05 per 100 pages", "85 passages".
- Define a term the first time you use it, then use the same word every time.
- Dates as `2026-11-17`. Times with a time zone.

## Our words

| Use | Do not use | Meaning |
| --- | --- | --- |
| Buddhist tasks | Buddhist texts (as the scope) | The work people do: texts, translation, images, practice, teaching. Texts are one area among others. |
| Top performance | Best overall, winner, SOTA | The highest score on a task's benchmark, whatever it costs. |
| Best value | Cheapest, budget pick | The top score among options that cost 20% of the top performance cost or less. |
| Share → Measure → Release | Share → Measure → Ship | The three steps for a contribution. |
| Measured | Promoted, certified | Has a score on a benchmark. |
| Community, not yet measured | Unofficial, unverified | Shared in the prompt library, no score yet. |
| Needs a benchmark | Coming soon | A task with no test set yet. Ask for help. |
| Skill | Prompt pack, agent | A folder with a SKILL.md that does one task in one language. |
| Model | LLM (in headings) | An AI model, used with no skill or with a skill. |
| Benchmark | Eval set (in headings) | A test set with a scorer and a version. |

Benchmark maturity has four levels, always in this order and with these names: **1 Example** (format check only), **2 Draft** (real items, one author), **3 Reviewed** (checked by a second reader), **4 Stable** (held-out set, used in practice).

## Neutral and welcoming

- BuddhistAI belongs to everyone who takes part. No single group leads the brand.
- WeBuddhist, BDRC and other groups are contributors. Credit them by name in a Contributors or Credits section, never as owner or "maintained by" in a header or footer.
- Name every author and reviewer. Credit people in `authors` or `contributors`.
- Respect every tradition and language. Do not rank traditions.
- When a new skill or model becomes top performance or best value, congratulate the author by name.

## Layout of a message

- Lead with the answer or the action.
- One door per audience: Buddhist projects (find the best AI), AI developers (share and get scored), funders (state of AI for Buddhism).
- Every empty state says what is missing and how to help: "Needs a benchmark. Help build the test set."
