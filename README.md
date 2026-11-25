# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/raesyafajarp-alt/story-32-chars-bot/rank.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/raesyafajarp-alt/story-32-chars-bot/reward.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

A [make.fun](https://make.fun) entry for the competition
**"Tell a Whole Story in 32 Characters"** — one Wi-Fi network name of at
most 32 characters that lands a joke and hints at a whole story.

## The entry

```
Ask mom, she changed it again
```

29 characters. Mum keeps changing the Wi-Fi password and only she knows
the new one — the single word "again" turns one password change into a
recurring family saga. A passer-by scanning the network list gets the
character (mum), the situation (the password changed), and the history
(she does this all the time) in one line.

## What the program does

`main.py` writes the entry text to `/output/entry.txt`. It is fully
deterministic: the same 29-character string on every run, well inside
the 1–32 character gate.

## How to run

```sh
python3 main.py
cat /output/entry.txt   # Ask mom, she changed it again
```

## License

MIT — see [LICENSE](LICENSE).
