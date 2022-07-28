class Animal:
    def __init__(self, name, appetite: int, is_hungry=True):
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self):
        return print(f"Hello, I'm {self.name}")

    def feed(self):
        if self.is_hungry:
            self.is_hungry = False
            print(f"Eating {self.appetite} food points...")
            return self.appetite
        else:
            return 0


class Cat(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(
            appetite=3,
            name=name,
            is_hungry=is_hungry
        )

    @staticmethod
    def catch_mouse():
        return print("The hunt began!")


class Dog(Animal):
    def __init__(self, name, is_hungry=True):
        super().__init__(
            appetite=7,
            name=name,
            is_hungry=is_hungry
        )

    @staticmethod
    def bring_slippers():
        return print("The slippers delivered!")


def feed_animals(animals: list):
    food_points = []
    for animal in animals:
        food_points.append(animal.feed())
    return sum(food_points)
