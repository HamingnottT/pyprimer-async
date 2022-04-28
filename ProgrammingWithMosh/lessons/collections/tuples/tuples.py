def intro():

    # tuples can be thought of as immutable lists
        # useful for preventing accidental modification
    numbers = (1, 2, 3)

def unpacking():
    # a method that can be used with tuples

    coordinates = (1, 2, 3)

    # we have these coordinates in a raw tuple but need to use them
    # one was to do this we can assign them to their own variable
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    x * y * z

    # there is an easier way but using the unpacking property/method
        # to do this declare x, y , and z on the same line and assign them to tuple coordinates
        # this works as the same method as above but more efficient
    x, y, z = coordinates
    

def main():
    pass

if __name__ == '__main__':
    main()