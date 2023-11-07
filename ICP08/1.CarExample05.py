class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
class AutoDriving:
    def check(self):
        print('Auto driving is enabled.')
class Convertible:
    def open(self):
        print('The sunroof is opening...')
class Hyundai(Car, AutoDriving, Convertible):
    def __init__(self, model, price, color):
        super().__init__(model, price)
        self.color = color
    def show_battery(self, per):
        print(f'Battery {per}% left.')


c1 = Hyundai('Kota Electric', 100000, 'Silver')
c1.check()
c1.open()
