from chess.game.scenario.scenarios import setup_scenario


def test_the_problem() -> None:
    scenario = setup_scenario
    actual = scenario()

    assert isinstance(actual, list)
