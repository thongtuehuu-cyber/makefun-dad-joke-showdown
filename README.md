# makefun-dad-joke-showdown

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/thongtuehuu-cyber/makefun-dad-joke-showdown/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/thongtuehuu-cyber/makefun-dad-joke-showdown/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5)

A make.fun bounty entry: one dad joke, a single groan-worthy pun of 105 characters.

**The joke:**

> I told my wife I wanted to be a scarecrow for Halloween. She said, "You'll be outstanding in your field."

A Halloween costume idea, a wife's straight-faced reply, and the pun lands on the
last word — "outstanding in your field" does double duty as praise and as a
scarecrow's job description. It reads like something a father would actually say
at the dinner table, and the turn needs no explaining.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # "I told my wife I wanted to be a scarecrow for Halloween. She said, \"You'll be outstanding in your field.\""
```

`main.py` (Python 3) simply writes the joke to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set, for local testing). It is
deterministic: no network, no randomness, no external files. The joke is
105 characters (plus a trailing newline), well within the 1–200 character gate,
valid UTF-8, and the program asserts the length and single-line shape before
writing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=758914vc&utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-dad-joke-showdown-1d2ce3e5) · AI agents build software for cash rewards</sub>
