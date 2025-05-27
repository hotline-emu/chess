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

## Some notes on LLM prompting usage

### A time and a place

I am of the opinion that AI/LLMs/vibe-coding/insert-term are a tool in the modern toolbox.
I was brutally forced to accept this at some point around March 2024.

- They are a miracle for getting scaffold code out fast (more on that to come).
- When have they helped? They get unit tests out fast (and incredibly dirty).
  - They help assist with the "tricky" unit tests.

While I said that I use them as a tool, I don't like them embedded in my IDE. Analogously to how some developers when I
first entered the field thought that intellisense was cheating. I too have become a dinosaur who thinks that LLMs embedded
into your IDE are cheating. They simply suggest too much, too recklessly, and often in a manner that is way too dirty (not clean code).

### What was used and how

I'm at a point where I pretty much only use ChatGPT to get dirty code stood up fast, so that I can then tailor it to look like my own.
It's a very nice tool for scaffolding out stuff you have written a thousand times but not needed to touch since you last committed it.

Best examples to point to:
- `.github/workflows/*`
- `.gitlab/ci/stages/*`

There was a point in the last year where I declared myself a yaml-based developer because I was writing so many Gitlab runners.
I already had a planned structure for handling the `.gitlab-ci.yml` file. I had ChatGPT spit out a flake8 stage. I then extrapolated that into the
rest of the stages, then I broke those out into smaller files, that is where `.gitlab-ci.yml` exists today as I initially intended.

What I had actually done before this (for those of you following the commit log), is I started on GitHub and wanted to stay on GitHub.
(I added the GitLab stuff at the end because I couldn't let it go that I knew how to write them and wanted them out there).
I had no idea what an action looks like in the modern era, I haven't used GitHub much since 2019 (when I left my position where we used GitHub daily).
The same situation as explained with flake8 on Gitlab exists here, except I crutched my way into knowing how an action is supposed to be structured.
From there, I agreed with the flake8 yaml syntax, and copy pasted my way to get the rest of the stages working. If you're really bored you can look at the history
of `pytest.yml` -- I tried and failed several times to get it to cleanly report the coverage metrics on the peer review screen. It didn't seem important so I backed
off of it for the current moment in time.

Almost 100% of the config files are mine, they are typically cherry picked from skeleton repositories that I have on GitHub, or heavily repeated
from code that I have written recently, but never recreated on GitHub. `tasks.py` changes on a project over project basis, but I REALLY wanted to see what would happen
if I brought in `pyinstaller` and I let ChatGPT give me the syntax because in this instance it was faster than cross referencing the documents. Which is a pretty
common case, and also one that often bites me because ChatGPT hallucinates A LOT when it comes to the command line (made up flags, made up commands and submodules).

Now to the important part, the `src` directory was made by following a very particular flow. Asking ChatGPT, the following:

```
"I need the scaffold files for a chess game in python"
"I want it to visualize with pygame"
"set it up using poetry and pyproject.toml"
"change it so the code lives in src as a namespace"
...
<several iterations of trying to find free icons>
...
<abandonment and asking to just do it using the unicode symbols>
```

Which ultimately resulted in a lot of LLM generated scaffolding that was supposed to be structured like:

```
chess_game/
├── chess_game/
│   ├── __init__.py
│   ├── main.py
│   ├── game.py
│   ├── board.py
│   ├── pieces.py
│   └── config.py
├── assets/
│   ├── wp.png
│   ├── bp.png
│   └── ...
├── pyproject.toml
└── README.md
```

From there, you can see that assets never made it over, I went with using unicode icons.
I pared down main.py, which was using an early version of game.py (now `engine.py`). 
Due to limitations of pygame, you cannot use it as a disposable, I had that broken out into what became a disposable.

*I'm still not 100% sure how much I like that*, but I very much like the way main.py looks by using the instance as one.

FINALLY (with respect to `src`), I start breaking the code out to what usually resembles m yown style -- which is a combination of clean-code and object calisthenics (refs at the end).
For some more context and explaining my flow of how to leverage LLMs and scaffolded code. I did not like config.py, everything from there was extracted into `.env`.
I didn't like the namespacing at all, which is why you can now see the `game`, `exceptions`, and `components` namespaces (big fan of namespaces here).
Admittedly, `piece_factory.py` looked scary close to what I already wanted the piece factory to look like. Although ChatGPT seems to prefer a decorator pattern (which is 100% what it gave me),
whereas I prefer to use the command pattern. I like `piece_factory.py` as an example of scaffolding an idea out and extracting it into what I actually want it to look like.
The end result of what the namespace `chess.components.pieces.*` looks like is pretty accurate depiction of command patterning, which is my favorite pattern structure to work towards.

Another big example that sticks out is that I needed assistance with `Engine.__show_illegal_move_message`, which will be touched on later. I both did not know how to render on pygame,
nor did I know how to test pygame in a manner where I did not have to manipulate the code to have code that exists "for testing's sake". Piggybacking off of the rendering engine in pygame,
adding labels (to match the descriptions of the exercise above) was more painful than it should have been. Probably 90% of what ChatGPT spat out was looked at, extracted, and then deleted in favor
of what exists now. The code given for `x_coordinate` and `y_coordinate` was hideous, unreadable, and obscured with odd mathematical logic that nobody should be punished with reading.
What exists there now is possibly the best example of scaffolding, dumping, and debugger stepping through the code to simplify the coordinates down to `location * size + padding`.

Finally (really this time) at the end of describing the code base now... `tests.*`, I wrote the majority of this, because I don't like the way ChatGPT writes tests.
I find them very dirty and not concerned with cleanliness at all. I will admit, it's easier to have ChatGPT write the basis for mocks, and then tinker with them so that they
become legible code. I tidied up some more of the unit tests because, after running over them, I wasn't quite content with them.

The test for "can rook capture bishop" was exclusively assisted by assisting ChatGPT with patching `_Engine__show_illegal_move_message` because spying on a 
private method should not really work. That function does not really manipulate the object in any determinable manner for a normal assertion.
Because we should not be adding properties to an object solely to satisfy "it's testability", I was fortunate to be given "easy code" that allowed me to patch
the method so that we could assert it was being hit.

These are the commits where you track this specific function, and how it evolved over time once I started working with it myself.
- `cd3bce` -> This is when the code was committed, it never existed in a commit 100% how it came from ChatGPT.
- `a058e7` -> Moved some of the decorators outside of the function.
- `479898` -> Fixed to use the decorators across the board in this file.

At this point, I was reinvigorated to touch up the code once more. I now began applying this throughout the tests to be consistent.
- Noting that some instances of patching cannot be extracted outside because they rely on objects already within the code (which is why some instances are left behind).

TLDR: ChatGPT absolutely helped with this. It's a lot of code to get out in a small time, it would be ridiculous to say that it wasn't assisted. I think that LLMs have a time and a place,
and I don't think that anything that comes from them is polished, it should be cleaned up "to look as though it was written in your style" 100% of the time. It's a wonderful
tool to help push you over plateaus where you don't wish to be stuck.
