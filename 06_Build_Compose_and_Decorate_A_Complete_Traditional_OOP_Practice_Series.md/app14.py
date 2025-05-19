# 4. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.


# Employee class banai gayi
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

# Department class banai gayi jisme employee ka reference hai
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference liya hai

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()

# Pehle aik employee banaya (ye independent hai)
emp = Employee(101, "Alice")

# Phir us employee ko department ke sath link kiya
dept = Department("HR", emp)

# Department ka info dikhaya
dept.show_department_info()
