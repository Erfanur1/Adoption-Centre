class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adopted = False

    @property
    def type(self) -> str:

        return self.__class__.__name__

    def get_name(self):
        return self.name

    def is_already_adopted(self):
        return self.adopted

    def adopt(self):
        self.adopted = True

    def __str__(self):
        return f"{self.name} (Age: {self.age})"


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Rabbit(Animal):
    pass
