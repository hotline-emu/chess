from typing import Callable, Any
from chess.game.scenario.scenarios import setup_scenario, problem_scenario
from chess.exceptions import ScenarioNotFoundError


class ScenarioFactory:
    SCENARIO_MAP = {
        "the_setup": setup_scenario,
        "the_problem": problem_scenario,
    }

    @staticmethod
    def get(scenario: str) -> Callable[[], list[list[Any]]]:
        scenario_callable = ScenarioFactory.SCENARIO_MAP.get(scenario)
        if scenario_callable is None:
            raise ScenarioNotFoundError(scenario)

        return scenario_callable
