# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Longer :
    def __init__(self):
        print("object is created")

    def __del__(self):
        print("object is destroyed")

my_obj = Longer()

del my_obj

