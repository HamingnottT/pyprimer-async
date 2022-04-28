# How subclasses can inherit from a super class

# super class defined
    # This is the general blueprint in which other similar classes can  inherit from
    # you can think of the methods in these classes the default methods that subclasses can fall back on
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say...")

# sub classes defined
    # with inheritance the __init__ function is reserved for the super class
    # calling a Cat(Pet) is like calling 'class Cat extends Pet' in Scala
class Cat(Pet):
    def speak(self):
        print("Meow")
    
class Dog(Pet):
    def speak(self):
        print("Bark")

    # using 'pass' will cause this class to return the methods from the superclass
class Fish(Pet):
    pass

class Horse(Pet):

    # using this method, you can instantiate a new variable to call in __init__ for this particular class
        # The first line defines the subclass-specific __init__ function
        # calling super().__init__(name, age) predefines the name and age varables
        # finally you can set a new variable, in this case color
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Neigh")

    def show(self):
        print(f"My show name is {self.name} and I am {self.age} years old and I am {self.color}")
    

def main():
    print("\n")

    # superclass invocation
    # how to instantiate and show the values in class Pet
    p = Pet("Tim", 19)
    p.show()
    p.speak()
    print("\n")

    # subclass invocation
        # even though there is no explicit method to print(f"I am {self.name} and I am {self.age} years old"),
        # Cat inherits properties from Pet which allows Cat to return a method from the superclass
    c = Cat("Bill", 34)
    c.show()
    c.speak()
    print("\n")
    
    d = Dog("Jill", 25)
    d.show()
    d.speak()
    print("\n")

    f = Fish("Neptune", 2)
    f.show()
    f.speak()
    print("\n")

    h = Horse("Winds of Plague", 5, "Black") # for all you metalheads out there
    h.show()
    h.speak()
    print("\n")

if __name__ == '__main__':

    main()