class City:
    def __init__(self, name, population, is_capital):
        self.name = name
        self.population = population
        self.is_capital = is_capital

    def get_info(self):
        capital_status = "Yes" if self.is_capital else "No"
        print(f"{self.name}, Population: {self.population} million, Capital: {capital_status}.")

class CapitalCity(City):
    def __init__(self, name, population):
        super().__init__(name, population, is_capital=True)

    def get_info(self):
        super().get_info()
        print(" - The Capital City.")

# Create instances
jakarta = City("Jakarta", 10, True)
bandung = City("Bandung", 2, False)
capital_jakarta = CapitalCity("Jakarta", 10)

# Call the get_info method for each object
jakarta.get_info()          # Output: Jakarta, Population: 10 million, Capital: Yes.
bandung.get_info()          # Output: Bandung, Population: 2 million, Capital: No.
capital_jakarta.get_info()  # Output: Jakarta, Population: 10 million, Capital: Yes. - The Capital City.
