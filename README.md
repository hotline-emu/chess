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
