class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        self.grow_rate = (self.height * 1.032) - self.height

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def age(self):
        self.days = self.days + 1

    def grow(self):
        self.height = self.height + self.grow_rate


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    Plant1 = Plant("Rose", 25.0, 30)
    initial_height = Plant1.height
    Plant1.show()
    day = 1
    for day in range(1, 8):
        print("=== Day", day, "===")
        Plant1.grow()
        Plant1.age()
        Plant1.show()
    total_grow = Plant1.height - initial_height
    print(f"Growth this week: {round(total_grow, 1)}cm")
