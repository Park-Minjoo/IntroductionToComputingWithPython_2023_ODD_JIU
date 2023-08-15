country_code = {1:"US", 20:"Egypt", 30:"Greece", 39:"Italy", 81:"Japan", 82:"Korea", 62:"Indonesia"}
print(len(country_code)) # 7
print(country_code[62]) # Indonesia
print(country_code[82]) # Korea

print(82 in country_code) # True
print(60 in country_code) # False
country_code[60] = "Malaysia"
print(60 in country_code) # True
country_code.pop(81)
print(81 in country_code) # False

