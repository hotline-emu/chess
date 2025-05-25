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
