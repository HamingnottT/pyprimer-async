class Person:

    def __init__(self, name):
        self.name = name    # this arguement is to reference the current object - we set the name object to the name arguement passed in the method

    def talk(self):
        print(f"Hello my name is {self.name}")

def main():
    name = input("Name? ")
    person = Person(name)   # it seems to be important to declare a variable when instantiating a class object
    person.talk()           # this variable then is what you can call methods on

    bob = Person("Bob Smith")
    bob.talk()