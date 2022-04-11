
# class is just for organization of example code
class StringDecorator:

    """
    This is our decorator function. This function 'start_end_decorator' takes an object function 'func',
    and wraps console print statements start and end around the object function 'func'
    """
    def start_end_decorator(func):

        def wrapper():
            print("start")
            func()
            print("end")
        
        return wrapper

    """
    This is the example function that will have a decorator added to it. 
    In this case, using the decorator function 'start_end_decorator' with a wrapper function surrounding object function 'print_name'
    """

    @start_end_decorator
    def print_name():
        print("Alex")


    # ~ Explaination ~
    # NOTE: to run explaination, comment out decorator call '@start_end_decorator' and then uncomment code starting at variable 'd'
    # this is the block of code that represents the desired output of the decorator
    # the output in the console should look like the following:
    #   start
    #   Alex
    #   end

# since this example uses a class as a container, I'm reassigning the class name to alias 'd' for readability
# d = StringDecorator

# print("-"*48, "\nDesired output:")

# d.print_name = d.start_end_decorator(d.print_name)
# d.print_name()

# print("-"*48)


import functools        # This is a critical import to get the desired output for the example below

""" 
/!\ Needs attention: example from python course is not producing expected output
source: YT - Intermediate Python Programming Course FreeCodeCampe at 3:20.00
"""
class ArgDecorator:
    # This is a similar example as above but instead wrapping a function with arguements

    def start_end_decorator(func):

        # defining the wrapper function without adding '*args' and '**kwargs' will throw a TypeError
            # this happens when the function that you are using a decorator on takes an arguement
            # *args and **kwargs allows the wrapper to take unlimited arguements and keyword arguements
        @functools.wraps(func) # this functools decorator preserves the target function in the wrapper function
        def wrapper(*args, **kwargs):
            print("start")
            result = func(*args, **kwargs)
            print("end")
            return result
        
        return wrapper

    @start_end_decorator
    def add5(x):
        return x + 5             #added print() for visibility on console


def main():
    print("\ndecorators.py running. . .\n")
    
    # example 1: decorating a function that has no arguements
    # since this example uses a class as a container, I'm reassigning the class name to alias 'd' for readability
    d = StringDecorator
    
    d.print_name()
    # the output in the console should look like the following:
    #   start
    #   Alex
    #   end

    print("\n")

    # example 2: decorating a function that takes arguements
    a = ArgDecorator
    # result = a.add5(10)
    # print(result)

    print(help(a.add5))
    print(a.add5.__name__)

    print(a.add5(10))


if __name__ == '__main__':
    main()