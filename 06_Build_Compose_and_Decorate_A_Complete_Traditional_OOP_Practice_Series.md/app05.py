# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.




class MathUatils:

    @staticmethod

    def add( a, b):
        return  a + b
    
result = MathUatils.add(5, 3)
print("sum", result)