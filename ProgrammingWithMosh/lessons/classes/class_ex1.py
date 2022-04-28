# this is an expanded note section from python _oop following Mosh's tutorial
# convention to name is called Pascal Convention
    # capitalize first letter of every word

# classes are the bluebrint of creating objects
    # objects are the actual instances based on the blueprint
class Point:
    # here you can create function that specifically belong to Point class
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

# creating this point_example function to keep any instances encapulated to practice OOP etiquette
def point_example():

    # to create an instance (an object) of class Point, simply call Point like you would a function
        # with Point instantiated, you can call the move or draw method created from above
    point1 = Point()
    
    point1.x = 10
    point1.y = 20
    
    print(point1.x)
    point1.draw()