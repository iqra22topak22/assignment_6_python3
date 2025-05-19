# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "ALHABIB Bank"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_bank_name(cls, name):
        cls.change_b_name = name

    def display(self):
        print(f"bank name is {self.bank_name}")

bank_name_object = Bank("Alhabib Bank")
bank_name_object.display()
bank_name_object.change_bank_name("uzma bank")
bank_name_object.display()

