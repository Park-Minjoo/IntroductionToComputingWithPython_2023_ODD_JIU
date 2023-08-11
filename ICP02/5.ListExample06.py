marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo']

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
print(marxes) # ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']

