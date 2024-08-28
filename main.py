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


    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} был добавлен в зоопарк.")

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name} the {animal.__class__.__name__}")

    def show_staff(self):
        for staff_member in self.staff:
            print(f"{staff_member.name} the {staff_member.__class__.__name__}")


#Класс сотрудников
class Staff:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Staff):
    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} кормит {animal.name}.")
            animal.eat()


class Veterinarian(Staff):
    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} лечит {animal.name}.")


# Создание животных
parrot = Bird(name="Страус", age=2)
lion = Mammal(name="Лев", age=4, fur_color="golden")
snake = Reptile(name="Змея", age=5, is_venomous=True)

# Создание сотрудников
keeper = ZooKeeper(name="Вова")
vet = Veterinarian(name="Иван")

# Создание зоопарка
zoo = Zoo()

# Добавление животных и сотрудников в зоопарк
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Демонстрация работы методов
zoo.show_animals()
zoo.show_staff()

# Полиморфизм
animals = [parrot, lion, snake]
animal_sound(animals)

# Действия сотрудников
keeper.feed_animal(lion)
vet.heal_animal(snake)
