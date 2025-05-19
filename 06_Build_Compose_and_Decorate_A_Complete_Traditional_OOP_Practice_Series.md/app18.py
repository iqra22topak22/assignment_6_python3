# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it

class Product:
    def __init__(self, price):
        self._price = price  # Yeh private variable hai

    @property
    def price(self):
        """Product ki price ko get karna."""
        return self._price

    @price.setter
    def price(self, value):
        """Price ko update karna."""
        if value < 0:
            raise ValueError("Price negative nahi ho sakti.")
        self._price = value

    @price.deleter
    def price(self):
        """Price ko delete karna."""
        print("Price delete ki ja rahi hai...")
        del self._price

# Example use:
p = Product(100)  # Product ka price 100 hai
print(p.price)  # Output: 100

p.price = 150  # Ab price ko change kar rahe hain
print(p.price)  # Output: 150

del p.price  # Price ko delete kar rahe hain
# Ab agar aap p.price ko access karenge, to error aaega kyunki price delete ho chuki hai
