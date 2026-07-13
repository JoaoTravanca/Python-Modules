class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def show(self) -> str:
        height = round(self._height, 1)
        return f"{self.name}: {height}cm, {self._days} days old"

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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color

    def show(self) -> None:
        print("===Flower")
        print(f"{super().show()}")
        print(f"Color: {self.color}")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        if (self._days > 30):
            print(f"the {self.name} is blooming and its color is {self.color}")
        else:
            print(f"the {self.name} needs more days to bloom")


class Tree(Plant):
    def __init__(
          self, name: str, height: float,
          days: int, trunk_diameter: float):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        print("===Tree")
        print(f"{super().show()}")
        print(f"Trunk diameter: {self.trunk_diameter} cm")

    def produce_shade(self) -> None:
        shade_long = self.trunk_diameter * 40
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree Oak now produces a shade of {round(shade_long, 1)}"
              f"cm long and {round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            days: int, harvest_season: str):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        print("=== Vegetable")
        print(f"{super().show()}")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    Rose = Flower("Rose", 65, 25, "red")
    Rose.show()
    Rose.bloom()
    print("")
    Oak = Tree("Oak", 65, 25, 10.45)
    Oak.show()
    Oak.produce_shade()
    print("")
    Tomato = Vegetable("Rose", 65, 25, "red")
    Tomato.show()
