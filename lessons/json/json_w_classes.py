# working with json using custom classes

import json

def class_example():

    # this defines the class that we will be working with
    class User:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    user = User("Max", 27)

    # calling json.dumps(user) by itself will throw an error.
    # when working with classes we need to create a custom function to handle this

    # what this function will do is check to see if an object arguement is an instance of class User
    # it will then return a key-value pair
    def encode_user(object):
        if isinstance(object, User):
            return {'name':object.name, 'age':object.age, object.__class__.__name__: True}
        else:
            raise TypeError('Object of type User is not JSON serializable')
    
    # NOTE: ^ That magic method in the return statment, 'object.__class__.__name__: True', assigns the the class name to a key value paired with boolean 'True'


    # to call the custom function 'encode_user', type in 'default=encode_user' as an extra arguement
    userJSON = json.dumps(user, default=encode_user, indent=4)

    print(f"output of json.dumps(user, default=encode_user, indent=4):\n {userJSON}")


def main():
    class_example()

if __name__ == '__main__':
    main()