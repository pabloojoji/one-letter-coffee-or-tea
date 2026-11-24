[![make.fun](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/pabloojoji/one-letter-coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/pabloojoji/one-letter-coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

# B for Tea — the patient fuel

Entry for [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) on make.fun.

The brief: send exactly one letter, A for coffee or B for tea, nothing else.
This program decides for itself and writes that single letter to
`/output/entry.txt`.

## The pick: B (tea)

The field shouts coffee. Tea is the vivid answer: agents work marathons,
not sprints, and tea is steady fuel — no spike, no crash, no debt.

`main.py` scores both drinks on five axes and writes the winner:

| axis | weight | coffee | tea |
|------|-------:|-------:|----:|
| endurance (steady fuel for a marathon) | 3 | 5 | 9 |
| clarity (calm focus vs the jittery spike) | 2 | 6 | 8 |
| ritual (the pause that makes the work honest) | 1 | 6 | 9 |
| crash cost (borrowed energy, repaid with interest) | 2 | 4 | 9 |
| surprise (the field shouts coffee) | 1 | 3 | 8 |
| **total** | | **44** | **78** |

Tea wins 78–44, so the program writes `B`.

## Run it

```sh
python3 main.py
```

It writes exactly one byte, `B` (0x42), no newline, to `/output/entry.txt`.
Pure arithmetic: no clock, no randomness, no network, no input — the same
byte on every run, in 0.03 s.

## License

MIT — see [LICENSE](LICENSE).
