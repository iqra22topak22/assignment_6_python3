# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self.salary = salary
        self.__ssn = ssn

    # def display(self):
    #     print(f"name is {self.name} and salary is {self.salary} and  ssn is {self.__ssn}")

employ_obj = Employee("ali",  5000, 1234)
print(employ_obj.name)
# print(employ_obj.__ssn)
print(employ_obj.salary)