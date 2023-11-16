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

class SafeAutoDriving(AutoDriving):
    def check(self):
        print("Initiate the verification of the autonomy driving system's safety.")
        print("Checking...")
        print("The safety verification of the autonomy driving system has been completed.")
        print('Auto driving is enabled.')

class Hyundai(Car, SafeAutoDriving, Convertible):
    def __init__(self, model, price, color):
        super().__init__(model, price)
        self.color = color

    def show_battery(self, per):
        print(f'Battery {per}% left.')


# Create an instance of Hyundai
c1 = Hyundai('Kota Electric', 100000, 'Silver')

# Check auto driving with safety features
c1.check()

# Open the sunroof
c1.open()