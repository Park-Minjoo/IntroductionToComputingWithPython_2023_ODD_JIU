marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes)) # Groucho, Chico, Harpo

friends = ['Ray', 'Najib', 'Grace', 'Dia', 'Julio']
separator = ' * '
joined = separator.join(friends)
print(joined) # Ray * Najib * Grace

sorted_friends = sorted(friends)
print(sorted_friends) # ['Dia', 'Grace', 'Julio', 'Najib', 'Ray']
print(friends) # ['Ray', 'Najib', 'Grace', 'Dia', 'Julio']
friends.sort()
print(friends) # ['Dia', 'Grace', 'Julio', 'Najib', 'Ray']

