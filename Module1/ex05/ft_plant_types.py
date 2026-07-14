class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def show(self) -> None:
        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._days} days old")

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
        self.is_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if (self.is_bloomed):
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self, bloom: bool) -> None:
        print(f"[asking the {Rose.name} to bloom]")
        if (bloom):
            self.is_bloomed = True
        else:
            self.is_bloomed = False


class Tree(Plant):
    def __init__(
          self, name: str, height: float,
          days: int, trunk_diameter: float):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter} cm")

    def produce_shade(self) -> None:
        shade_long = self._height
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of"
              f" {round(shade_long, 1)}"
              f"cm long and {round(self.trunk_diameter, 1)}cm wide.")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            days: int, harvest_season: str):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age(self, aged) -> None:
        self._days += aged
        self.nutritional_value += aged
        print(f"[make {self.name} grow and age for {aged} days]")

    def grow(self) -> None:
        self._height += self.nutritional_value * 2.1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red")
    Rose.show()
    Rose.bloom(True)
    Rose.show()
    print("")
    print("=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    Oak.produce_shade()
    print("")
    print("=== Vegetable")
    Tomato = Vegetable("Tomato", 5.0, 10, "April")
    Tomato.show()
    Tomato.age(20)
    Tomato.grow()
    Tomato.show()
