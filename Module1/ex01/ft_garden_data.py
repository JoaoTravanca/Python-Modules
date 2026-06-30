class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = f"{age} days old"

    def show(self):
        print(self.name, end=" ")
        print(self.height, end=" ")
        print(self.age)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant1 = Plant("Rose:", "25cm,", "30")
    Plant2 = Plant("Sunflower:", "80cm,", "45")
    Plant3 = Plant("Cactus:", "15cm,", "120")
    Plant1.show()
    Plant2.show()
    Plant3.show()
