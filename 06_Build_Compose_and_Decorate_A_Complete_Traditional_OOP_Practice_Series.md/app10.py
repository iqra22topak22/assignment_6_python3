# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed

    def bark(self):
      
        print(f"{self.name} is a {self.breed}")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()