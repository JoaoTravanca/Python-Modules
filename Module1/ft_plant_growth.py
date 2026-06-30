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
