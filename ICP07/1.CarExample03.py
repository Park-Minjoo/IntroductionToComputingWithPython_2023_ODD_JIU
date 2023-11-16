class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class Hyundai(Car):
    def __init__(self, model, price, color):
        super().__init__(model, price)
        self.color = color
    def show_battery(self, per):
        print(f'Battery {per}% left.')
c1 = Hyundai('Kona Electric', 100000, 'Silver')

