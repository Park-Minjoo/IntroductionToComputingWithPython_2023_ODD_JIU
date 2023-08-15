sports ={1:"soccer", 2:"baseball", 4:"swimming", 5:"basketball"}
l = len(sports)
index = l//2
print(sports[index]) # Q1.

print(3 in sports) # False
print(sports.pop(5)) # basketball
sports[3] = "judo"
print(sports) # {1: 'soccer', 2: 'baseball', 4: 'swimming', 3: 'judo'}

