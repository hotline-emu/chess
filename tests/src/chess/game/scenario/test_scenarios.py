from chess.game.scenario.scenarios import problem_scenario


def test_the_problem() -> None:
    scenario = problem_scenario
    actual = scenario()

    assert isinstance(actual, list)
