class GardenError(Exception):
    """Basic error for garden problems."""
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name) -> None:
    try:
        if (plant_name):
            print(f"Watering {str.capitalize(plant_name)}: [OK]")
        else:
            raise PlantError(f" Invalid plant name to water: {plant_name}")
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_watering_system() -> None:
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")
    print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
