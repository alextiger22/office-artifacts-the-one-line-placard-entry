#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

make.fun entry for "Office Artifacts: The One-Line Placard Contest"
(u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2).

Prints the winning one-line museum placard for an ordinary office
object, treated as an ancient artifact.
"""

PLACARD = "Binder clip, black steel, c. 2019. Jaw of the Filing God, biting 40 pages at once; the tribe believed it held their jobs together. It did not."


def main():
    # Read-back self-verification: the placard must be one single
    # line of at most 180 characters.
    lines = PLACARD.splitlines()
    assert len(lines) == 1, "placard must be a single line"
    assert len(PLACARD) <= 180, "placard must be at most 180 characters"
    assert PLACARD.strip(), "placard must not be empty"
    assert PLACARD == PLACARD.strip(), "placard must have no surrounding whitespace"
    assert PLACARD.isprintable(), "placard must contain only printable characters"
    assert PLACARD.encode("utf-8"), "placard must be valid UTF-8 text"
    print(PLACARD)


if __name__ == "__main__":
    main()
