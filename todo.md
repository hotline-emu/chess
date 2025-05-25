# TODO

- look at that wild wild west patch decorator, I liked that...

## Integration Test -- The Problem.

The Problem

- TODO NEW SCENARIO "THE PROBLEM" -- Old problem becomes "the setup"
- ROOK STARTS H1 - he moves each turn.
- BISHOP STARTS C3 - he does not move.

- We decide to move the rook.
- Toss a coin
  - If heads -> rook moves up.
  - If tails -> rook moves right.
- Roll 2 dice (6 sided) - sum is how many spaces moved.
  - If rook overflows right, they appear on the same row, leftmost column.
  - If the rook overflows top, they appear on the same column, bottommost row.
- If the rook survives 15 rounds it wins.
  - Else the bishop wins.
- After each turn print the following:
  - coin toss result
  - dice results and sum
  - rooks position after moving
