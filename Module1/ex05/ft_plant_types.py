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
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom() -> None:
        print(f"the {self.name} is blooming and its color is {self.color}")

class Tree:
    pass
class Vegetable:
    pass


if __name__ == "__main__":

