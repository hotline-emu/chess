from chess.exceptions import ScenarioNotFoundError


def test_exception() -> None:
    scenario = "foo"
    exception = ScenarioNotFoundError(scenario)

    expected = f"Scenario by name '{scenario}' has not been configured."
    actual = str(exception)

    assert expected == actual
