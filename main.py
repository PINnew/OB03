#Базовый класс
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name}, {self.age} года")


#Подклассы
class Bird(Animal):
    def __init__(self, name, age, can_fly=True):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} поёт!")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит!")


class Reptile(Animal):
    def __init__(self, name, age, venomous=False):
        super().__init__(name, age)
        self.venomous = venomous

    def make_sound(self):
        print(f"{self.name} шипит!")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


#Класс Zoo
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} добавлен в зоопарк.")



