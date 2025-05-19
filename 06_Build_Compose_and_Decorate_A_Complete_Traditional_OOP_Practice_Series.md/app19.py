# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value


# Create an instance of Multiplier
double = Multiplier(2)

# Test if the object is callable
print("Is 'double' callable?", callable(double))  # Output: True

# Use the object like a function
result = double(10)
print("double(10) =", result)  # Output: 20


