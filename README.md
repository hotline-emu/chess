# Chess
A chess POC in python

## Environment setup

Requires Python `python = ">=3.12,<3.14"`  
Developed on Python `3.13.3`  

CLI steps:

```bash
pip install poetry invoke
```

## Using Invoke

The repository was developed with the intent of using Invoke to run everything.  
As of the time of documentation (24MAY25), the current list of commands is:  

```
build
coverage
flake8
lint
mypy
pylint
run
test
integration
```

This can be revealed via the command `invoke --list` from the CLI.

## Running the program

The program can be ran using the command `invoke run`

## Building the program

The program can be built using the command `invoke build`  
From there, the program can be ran from `chess.exe`, found in the `dist/` directory.

## Linting the code base

The code base is linted using a combination of flake8, pylint, and mypy.  

While this is somewhat overkill, collectively they enforce a cohesive list of automation discoverable best practices.  
Note: There are some lints that were disabled. There is a fine mix of some that I would have disabled always.  
There are also some lints that were disabled because they force the code to follow patterns that don't benefit anyone,  
and exist for "beating the linter". Which is against the spirit of intent as to why the code is being linted in the first place.  

You can lint the application with the following:

```bash
invoke flake8
invoke pylint
invoke mypy
```

Alternatively, a one-shot command exists in `tasks.py`:

```bash
invoke lint
```

## Testing the code base

The code base can be tested via the following two commands:

```bash
invoke test
invoke coverage
invoke integration
```

`test` and `coverage` do the same thing, with the caveat that coverage outputs a coverage report.  
`integration` bypasses `pytest.ini` and informs pytest to look at `tests/integration` as opposed to `tests/unit`.  

## The Impetus

Why does this exist in the first place?

This repository was started in order to fill in as a showcase of development standards, best practices,  
and general coding styles -- in-lieu of having anything substantial that I would be able to share after a 5 year  
period working of working in the public sector (everything worth looking at is redacted).  

### The Prompt

We are looking at a 'special' game of chess where each player only has one piece.  
Player with white pieces only has a bishop while player with black pieces only has a rook.  
- In chess, the columns (called Files) are denoted as alphabets(a-h) and rows (called Ranks) are denoted as numbers (1-8).
- Any given square is a combination of file and rank. 
- In the above figure the position of bishop is c3 while that of the rook is f6.
- Bishop only moves diagonally from its position, in all 4 directions (top-right, top-left, bottom-right, bottom-left).
- Rook moves either vertically (up and down) or horizontally (left and right) from its given position.
- Both rook and bishop can capture one another only if the other piece falls in the valid motion path.

#### Set Up

In the object-oriented language of your choosing
1. Create classes/objects for the two pieces
2. Create an appropriate representation of board state
3. Given a board state, write code to determine whether the rook can capture the bishop.
4. Write code to determine whether the bishop can capture the rook.

#### The Problem

We decide to move the black rook and play for its survival. The move happens as follows:
1. Toss a coin, if it's heads, the rook moves up. If it's tails, the rook moves to the right.
2. Roll 2 dice (6 sided). The sum of numbers on the face up side of both the dice will be the number of squares the rook moves.
3. If the rook reaches the right most column on the board, it emerges again from the left most column.
4. If the rook reaches the top most row, it emerges again from the bottom most row.
  - Move the rook as described above for 15 rounds. 
  - If it manages to survive from being captured by the bishop, the player with the rook wins. Else the player with bishop wins.
  - The starting position for rook is h1 square and bishop remains stationary on c3.

Write code to determine which player won, given the above constraints.  
Make sure to record (or print) the result of coin toss, dice and rook's position after every move.  
