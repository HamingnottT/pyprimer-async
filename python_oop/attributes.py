# how attributes are import in classes

# definition of class
    # the variable number_of_people is an attribute that is only specific to the class Person
    # the variables inside the __init__ function can be inherited from any subclass added
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name

        # # this incrementation is used to keep track of how many people are added in Person
        # Person.number_of_people += 1

        # calling the below mentioned add_person class method
        Person.add_person()

    # alternatively class methods can be called to handle any changes within the class itself
        # the '@classmethod' is called a decorator
    @classmethod
    def number_of_people1(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# this example shows how this incrementation is used
print(Person.number_of_people1())
p1 = Person("Tim")
print(Person.number_of_people1())
p2 = Person("Jill")
print(Person.number_of_people1())

# Static Methods
    # can be used outside of class instances
    # handy for when you want to call certain methods at any point
class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))