class GardenError(Exception):
    """Basic error for garden problems."""
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def custom_error() -> None:
    try:
        print("Testing PlantError...")
        raise PlantError("The Tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    try:
        print("\nTesting WaterError...")
        raise WaterError("Not enought water in the tank")
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The Tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise WaterError("Not enought water in the tank")
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    custom_error()
    print("\nAll custom error types work correctly!")
