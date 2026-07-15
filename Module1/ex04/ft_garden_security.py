class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = self.validate_height(height)
        self._days = self.validate_days(days)

    def validate_height(self, height) -> float:
        if (height < 0):
            print(f"{self.name}: Error, height can't be negative")
            return 0.0
        else:
            return height

    def validate_days(self, days) -> int:
        if (days < 0):
            print(f"{self.name}: Error, age can't be negative")
            return 0
        else:
            return days

    def show(self) -> str:
        height = round(self._height, 1)
        return f"{self.name}: {height}cm, {self._days} days old"

    def set_height(self, new_height) -> None:
        if (new_height < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {round(new_height)}cm")

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
    print("")
    plant.set_height(25.0)
    plant.set_age(30)
    print("")
    plant.set_height(-25)
    plant.set_age(-30)
    print("")
    print(f"Current state: {plant.show()}")
