# working with json using custom classes

import json
from textwrap import indent

def class_example():

    # this defines the class that we will be working with
    class User:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    user = User("Max", 27)

    # calling json.dumps(user) by itself will throw an error.

    ''' approach # 1: homemade custom function '''

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
    # the 'user' is considered to be the 'object', so it would be like writing encode_user(user) in normal python syntax
    userJSON = json.dumps(user, default=encode_user, indent=4, sort_keys=True)

    print(f"\noutput of json.dumps(user, default=encode_user, indent=4, sort_keys=True):\n {userJSON}")

    ''' approch #2: using JSONEncoder from the json library '''
    
    from json import JSONEncoder

    # similar steps as above custom method be now we create a class UserEncoder with JSONEncoder as the object method
    class UserEncoder(JSONEncoder):

        # inside the class we override the default method from json.dumps and use create it as the custom class method
        def default(self, object):
            if isinstance(object, User):
                return {'name':object.name, 'age':object.age, object.__class__.__name__: True}
            else:
                raise TypeError('Object of type User is not JSON serializable')

    # we call the same json.dumps(), but instead of default, we call the class as 'cls=UserEncoder'
    userJSON = json.dumps(user, cls=UserEncoder, indent=4, sort_keys=True)

    print(f"\noutput of json.dumps(user, cls=UserEncoder, indent=4, sort_keys=True):\n {userJSON}")

    ''' approach #3: use JSONEncoder directly '''
    ''' /!\ PERSONAL NOTE: Using this approach only returns a one-line string. Need to find a way to indent using this method '''

    userJSON = UserEncoder().encode(user)

    print(f"\noutput of UserEncoder().encode(user):\n {userJSON}")

    ''' How to decode a json string from a class '''

    ''' approach #1: only write into dictionary '''

    user = json.loads(userJSON)

    print(type(user))
    print(f"\nHow to decode a json string into a dictionary:",
    f"\noutput of json.loads(userJSON):\n {user}")

    ''' approach #2: custom method to create a user class '''

    def decode_user(dictionary):
        
        # this checks to see if the name of the class matches with the contents of the dictionary
            # it will then assign the dictionary back to the class by its name
        if User.__name__ in dictionary:
            return User(name=dictionary['name'], age=dictionary['age'])
        
        # if there is no match then this ensure that a dictionary is returned regardless of a match
        return dictionary

    user = json.loads(userJSON, object_hook=decode_user)

    print(type(user))
    print(f"\nHow to decode a json string into a dictionary:",
    f"\noutput of json.loads(userJSON, object_hook=decode_user):\n {user.name}")

def main():
    class_example()

if __name__ == '__main__':
    main()