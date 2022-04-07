# from example 1 but now with contructors

class Point:
    # this __init__ function is a contructor
        # it instantiates the class as soon as it is called
        # passing in arguements x and y is handy in creating a reuseable object
    def __init__(self, x, y):
        self.x = x # same as Point.x = 10
        self.y = y # same as Point.y = 20

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

def point_example():

    # because of the above constructor we can now pass in arguements like a function
    point = Point(10, 20)

    # returns value of self.x from the contructor
    print(point.x)
    point.draw()

    # as you can see, this is a way more efficiant way of working with classes and objects

    # reassign the value of x
    point.x = 11
    print(point.x)