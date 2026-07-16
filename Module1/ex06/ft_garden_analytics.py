class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = self.validate_height(height)
        self._days = self.validate_days(days)
        self.stats = self.Statistics()

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

    def show(self) -> None:
        height = round(self._height, 1)
        print(f"{self.name}: {height}cm, {self._days} days old")
        self.stats.increment_show()

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

    @staticmethod
    def check_year(age) -> None:
        result = age > 366
        print(f"Is {age} days more than a year? -> {result}")

    @classmethod
    def anonymous_obj(cls) -> object:
        return cls(name="Unknown plant", height=0, days=0)

    def age(self, aged) -> None:
        self.stats.increment_age()
        self._days += aged

    def grow(self, grow_value) -> None:
        self.stats.increment_grow()
        self._height += grow_value

    class Statistics:
        def __init__(self):
            self._show_call = 0
            self._age_call = 0
            self._grow_call = 0

        def increment_show(self) -> None:
            self._show_call += 1

        def increment_age(self) -> None:
            self._age_call += 1

        def increment_grow(self) -> None:
            self._grow_call += 1

        def show(self) -> None:
            print(f"Stats: {self._grow_call} grow, {self._age_call} age, "
                  f"{self._show_call} show")


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
        print(f"[asking the {self.name} to bloom]")
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
        self.stats: "Tree.Statistics" = self.stats

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter} cm")

    def produce_shade(self) -> None:
        shade_long = self._height
        print(f"Tree {self.name} now produces a shade of"
              f" {round(shade_long, 1)}"
              f"cm long and {round(self.trunk_diameter, 1)}cm wide.")
        self.stats.increment_shade()

    class Statistics(Plant.Statistics):
        def __init__(self):
            super().__init__()
            self._shade_call = 0

        def increment_shade(self) -> None:
            self._shade_call += 1

        def show(self) -> None:
            super().show()
            print(f"{self._shade_call} shade")


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
        super().age(aged)
        self.nutritional_value += aged
        print(f"[make {self.name} grow and age for {aged} days]")

    def grow(self) -> None:
        super().grow()
        self._height += self.nutritional_value * 2.1


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds:{self.seeds}")

    def bloom(self, bloom: bool) -> None:
        super().bloom(bloom)
        if bloom:
            self.seeds += 42


def display_stats(plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year(30)
    Plant.check_year(400)
    print("")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    flower.stats.show()
    print("[asking the rose to grow and bloom]")
    flower.grow(8.0)
    flower.bloom(True)
    flower.show()
    display_stats(flower)
    print("")
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    display_stats(tree)
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    display_stats(tree)
    print("")
    print("=== Seed")
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.age(20)
    seed.grow(30.0)
    seed.bloom(True)
    seed.show()
    display_stats(seed)
    print("")
    print("=== Anonymous")
    anonymous = Plant.anonymous_obj()
    anonymous.show()
    display_stats(anonymous)
