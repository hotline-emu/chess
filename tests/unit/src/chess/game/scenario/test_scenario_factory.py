# Like all abstractions MyPy will complain about comparing scenario_callable to a Callable.
# I disagree, I believe that this is a perfectly sane comparison, and their linter is being
# overly strict. Which is fine, because it has been set to act that way.
# mypy: disable-error-code=arg-type

from typing import Callable
import pytest
from chess.game.scenario import ScenarioFactory
from chess.exceptions import ScenarioNotFoundError


def test_factory_scenario_found() -> None:
    scenario = "the_problem"
    scenario_callable = ScenarioFactory.get(scenario)

    assert isinstance(scenario_callable, Callable)


def test_factory_scenario_not_found() -> None:
    scenario = "el_problemo"
    with pytest.raises(ScenarioNotFoundError):
        _ = ScenarioFactory.get(scenario)
