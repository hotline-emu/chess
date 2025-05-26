from chess.game.scenario.scenarios import setup_scenario, problem_scenario


def test_the_setup() -> None:
    scenario = setup_scenario
    actual = scenario()

    assert isinstance(actual, list)


def test_the_problem() -> None:
    scenario = problem_scenario
    actual = scenario()

    assert isinstance(actual, list)
