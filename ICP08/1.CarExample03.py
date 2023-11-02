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
    def show_color(self):
        print(f'The color of {self.name} is {self.color}.')
c1 = Hyundai('Kona Electric', 100000, 'Gray')
c1.show_color()