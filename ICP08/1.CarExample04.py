class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class Hyundai(Car):
    def show_battery(self, per):
        print(f'Battery {per}% left.')
    def auto_driving(self, vel):
        print(f'Auto-driving mode with a speed of {vel} km/h.')

c1 = Car('Black', 200000)
c2 = Hyundai('Kona Electric', 100000)

c2.show_battery(10)