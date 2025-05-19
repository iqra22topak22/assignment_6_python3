# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
#   ya mujy roman urdu me  krwa do
# 20./# Step 1: Custom Exception banayi
class InvalidAgeError(Exception):
    pass

# Step 2: Function jo age check kare
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age 18 se kam hai, allowed nahi hai.")
    else:
        print("Welcome! Aap eligible hain.")

# Step 3: Try...Except block ke zariye exception handle karna
try:
    user_age = int(input("Apni age daalein: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Error:", e)

