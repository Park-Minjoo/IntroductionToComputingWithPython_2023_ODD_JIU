# Define the Animal class
class Animal:
    def __init__(self, species):
        self.species = species

# Define the Dog class (Inherits from Animal)
class Dog(Animal):
    def make_sound(self, sound):
        print(f"This {self.species} barks: '{sound}'")

# Create instances of Dog
dog = Dog("Bull dog")

# Print the sounds
dog.make_sound("woof")

