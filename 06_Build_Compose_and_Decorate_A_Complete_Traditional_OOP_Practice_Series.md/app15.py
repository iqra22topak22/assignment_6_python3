# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def method(self):
        print("A")

class B(A):
     def method(self):
          print("B")

class C(A):
     def method(self):
        print("C")

class D(B, C):
    pass

object1 = D()      
object1.method()    

print(D.__mro__)