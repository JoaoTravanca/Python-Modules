class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        self.grow_rate = (float(self.height) * 1.032) - float(self.height)

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")

    def age(self):
        self.days = int(self.days) + 1

    def grow(self):
        self.height = self.height + self.grow_rate


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant1 = Plant("Rose", 25.0, 30)
    Plant2 = Plant("Oak", 200.0, 365)
    Plant3 = Plant("Cactus", 5.0, 90)
    Plant4 = Plant("Sunflower", 80.0, 45)
    Plant5 = Plant("Fern", 15.0, 120)
    print("Created:", end=" ")
    Plant1.show()
    print("Created:", end=" ")
    Plant2.show()
    print("Created:", end=" ")
    Plant3.show()
    print("Created:", end=" ")
    Plant4.show()
    print("Created:", end=" ")
    Plant5.show()
