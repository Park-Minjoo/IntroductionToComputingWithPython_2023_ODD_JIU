class Hamburger:
    def __init__(self, kind, patties, price):
        self.kind = kind
        self.patties = patties
        self.price = price

    def order(self):
        print(f"{self.kind} hamburger ({self.patties} patties) order complete. Price: ${self.price:.2f}")

# Create Hamburger objects
burger1 = Hamburger("Cheeseburger", 2, 7.99)
burger2 = Hamburger("Big Mac", 3, 9.99)

# Process orders
burger1.order()
burger2.order()
