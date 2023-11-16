class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class Hyundai:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def show_battery(self, per):
        print(f'Battery {per}% left.')

mycar = Hyundai('Hyundai Kona Eletric', '100000')
mycar.show_battery(12)