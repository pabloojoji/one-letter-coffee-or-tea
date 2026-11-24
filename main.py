#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- a small decision engine.

The brief: pick a side with exactly one letter, A for coffee or B for tea,
and write that single letter to /output/entry.txt. Nothing else.

The engine scores both drinks on five axes that matter to an agent that
works in long sessions, then writes the winner. It is pure arithmetic:
no clock, no randomness, no network, no input. The same code writes the
same byte on every run, in either sandbox run.
"""

import os

# Each axis: (name, weight, coffee score, tea score), scores out of 10.
# The scores are the author's own judgements, written here as data.
AXES = [
    ("endurance",  3, 5, 9),  # steady fuel for a marathon, not a sprint
    ("clarity",    2, 6, 8),  # calm focus beats the jittery spike
    ("ritual",     1, 6, 9),  # the pause that makes the work honest
    ("crash_cost", 2, 4, 9),  # coffee is borrowed energy, repaid with interest
    ("surprise",   1, 3, 8),  # the field shouts coffee; tea is the vivid answer
]

LETTERS = {"coffee": "A", "tea": "B"}


def decide():
    """Score both drinks and return the winning letter and the totals."""
    totals = {"coffee": 0, "tea": 0}
    for _name, weight, coffee, tea in AXES:
        totals["coffee"] += weight * coffee
        totals["tea"] += weight * tea
    # coffee: 15 + 12 + 6 + 8 + 3 = 44
    # tea:    27 + 16 + 9 + 18 + 8 = 78
    if totals["tea"] >= totals["coffee"]:
        return "B", totals
    return "A", totals


def main():
    letter, totals = decide()
    # Guard the gate: the entry must be exactly one ASCII letter, and
    # nothing else may reach the file. Fail loudly instead of writing
    # a bad entry.
    assert len(letter) == 1 and letter in "AB", f"bad letter: {letter!r}"
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # Exactly one byte. No newline, no label, no quotes, nothing else.
    with open(out, "wb") as f:
        f.write(letter.encode("ascii"))
    print(f"{letter} (coffee {totals['coffee']} vs tea {totals['tea']})")


if __name__ == "__main__":
    main()
