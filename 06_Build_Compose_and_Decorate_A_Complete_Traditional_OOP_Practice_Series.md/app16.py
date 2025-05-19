# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# Define the decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Apply the decorator to a function
@log_function_call
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()

# ----------------------------------------------------
def tea_time(func):
    def wraaper(*args, **kwargs):
        print("chay ka liya pani rakh do ")
        result = func(*args, **kwargs)
        print("chay tyar hai ")
    return wraaper

@tea_time
def tea():
    print("chay me pati chani or milk dal do ")


tea()