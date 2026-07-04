class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def show(self) -> str:
        return f"{self.name}: {round(self._height, 1)}cm, {self._days} days old"

    def set_height(self, new_height) -> None:
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {round(new_height)} cm")

    def set_age(self, new_days) -> None:
        if (new_days < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_days
            print(f"Age updated: {new_days} days")

    def get_age(self) -> int:
        return self._days

    def get_height(self) -> float:
        return self._height


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {plant.show()}")
    plant.show()
    print("")
    plant.set_height(25.0)
    plant.set_age(30)
    print("")
    plant.set_height(-25)
    plant.set_age(-30)
    print("")
    print(f"Current state: {plant.show()}")
