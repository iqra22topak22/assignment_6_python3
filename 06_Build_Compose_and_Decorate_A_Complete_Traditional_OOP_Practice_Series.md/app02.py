# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.




class Varibale:
    count = 0 

    def __init__(self):
        Varibale.count += 1

    @classmethod
    def display_count(self):
        print(f"total count is {self.count}")

obj = Varibale()
obj1 = Varibale()

Varibale.display_count()

