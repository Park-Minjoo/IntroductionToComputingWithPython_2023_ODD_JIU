marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo', 'Karl']
del marxes[-1]
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']

print(marxes[2]) # Harpo
del marxes[2]
print(marxes) # ['Groucho', 'Chico', 'Gummo', 'Zeppo']

marxes.remove('Gummo')
print(marxes) # ['Groucho', 'Chico', 'Zeppo']

