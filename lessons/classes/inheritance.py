# class inheritance

class Mammal:
    def walk(self):
        print("walk")

"""
to have a class inherit from another class, pass the superclass
inside of the class that is inheriting from
"""

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def eat_catnip(self):
        print("I can taste colors!")

def main():
    dog1 = Dog()
    dog1.walk()
    dog1.bark()

    cat1 = Cat()
    cat1.eat_catnip()