country = {"Indonesia":1, "USA":2, "Germany":3, "France":4, "Mexico":8}
print(country["Indonesia"]) # 1
print(country["France"]) # 4
print(country["Mexico"]) # 8
print(country)
# {'Indonesia': 1, 'USA': 2, 'Germany': 3, 'France': 4, 'Mexico': 8}

print(country.pop("Germany")) # 3
print(country.pop("France")) # 4
print(country)
# {'Indonesia': 1, 'USA': 2, 'Mexico': 8}

