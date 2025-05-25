from invoke.tasks import task
from invoke.context import Context


@task
def flake8(context: Context) -> None:
    context.run("poetry run flake8 .")


@task
def pylint(context: Context) -> None:
    context.run("poetry run pylint .")


@task
def mypy(context: Context) -> None:
    context.run("poetry run mypy .")


@task(
    flake8,
    pylint,
    mypy,
)
def lint(_context: Context) -> None: ...


@task
def run(context: Context) -> None:
    context.run("poetry run python -m chess.main")


@task
def test(context: Context) -> None:
    context.run("poetry run pytest")


@task
def coverage(context: Context) -> None:
    context.run(
        "poetry run pytest --cov=src --cov-report=html --cov-report=term-missing"
    )


@task
def build(context: Context) -> None:
    context.run("poetry run pyinstaller src/chess/main.py --name chess --onefile")


@task
def integration(context: Context) -> None:
    log_level = "INFO"
    log_format = "%(levelname)s: %(message)s"
    pytest_args = (
        f'-o log_cli=true -o log_cli_level={log_level} -o log_cli_format="{log_format}"'
    )
    context.run(f"poetry run pytest {pytest_args} tests/integration")
