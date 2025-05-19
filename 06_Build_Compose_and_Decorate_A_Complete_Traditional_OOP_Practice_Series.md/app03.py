
# 3. Public Variables and Methods
#    Assignment:
#    Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

# Define the Car class


class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"the {self.brand} car is starting...")

my_car = Car("Tayota")
my_car2 = Car("Honda")
print("brand:", my_car2.brand)
print("Brand:", my_car.brand)
my_car.start()
my_car2.start()