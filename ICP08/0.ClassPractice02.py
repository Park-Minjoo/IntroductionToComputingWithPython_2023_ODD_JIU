class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"The {self.name} makes a '{sound}' sound.")

# Create Animal objects
lion = Animal("Lion", "Mammal")
parrot = Animal("Parrot", "Bird")

# Specify the sounds the animals make
lion.make_sound("roars")
parrot.make_sound("squawks")
