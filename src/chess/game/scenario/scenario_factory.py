from chess.game.scenario.scenarios import problem_scenario
from chess.exceptions import ScenarioNotFoundError


class ScenarioFactory:
    SCENARIO_MAP = {
        "the_problem": problem_scenario,
    }

    @staticmethod
    def get(scenario: str):
        scenario_callable = ScenarioFactory.SCENARIO_MAP.get(scenario)
        if scenario_callable is None:
            raise ScenarioNotFoundError(scenario)

        return scenario_callable
