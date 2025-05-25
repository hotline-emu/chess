class ScenarioNotFoundError(Exception):
    def __init__(self, scenario: str) -> None:
        message = f"Scenario by name '{scenario}' has not been configured."
        super().__init__(message)
