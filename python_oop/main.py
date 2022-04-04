# Tech With Tim source https://www.youtube.com/watch?v=JeznW_7DlB0

# built-in types example
def hello():
    print("\n")
    print("python_oop.hello running. . .")
    x = 1

    print("\nEach data type has a class of its own:")
    print(f"This variable x is the following class type: {type(x)}")
    print(f"This function hello() is the following class type: {type(hello)}")

#  string mainpulation
def str_manip_examples():
    print("\n")
    print("python_oop.str_manip_examples running. . .")
    string = "hello"
    print(string.upper())

# class builder example
class Dog:
    # method of this class - calling type() returns <class: 'function'>

    #  __init__(self):
    # This method instantiates the class object when its created
    # using this you can pass arguemnts to the class itself
    def __init__(self, name, age):
        # using '.self.' before variable creation, creates an attribute to the class
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

def class_example():
    print("\n")
    print("python_oop.class_example. . .")
    
    d = Dog("Charlie", 11)
    d.bark()
    
    print(type(d))
    print(d.add_one(5))

    d = Dog("Max", 2)
    d2 = Dog("Beethoven", 14)
    print(d.get_name(), d.get_age())
    print(d2.get_name(), d2.get_age())


def main():
    print("python_oop.main running. . .")
    hello()
    str_manip_examples()
    class_example()

if __name__ == '__main__':
    main()
    