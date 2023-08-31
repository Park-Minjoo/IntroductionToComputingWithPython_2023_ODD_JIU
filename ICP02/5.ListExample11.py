marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes)) # Groucho, Chico, Harpo

friends = ['Ray', 'Najib', 'Grace', 'Diaz', 'Julior']
separator = ' * '
joined = separator.join(friends)
print(joined) # Ray * Najib * Grace * Diaz * Julior

sorted_friends = sorted(friends)
print(sorted_friends) # ['Diaz', 'Grace', 'Julior', 'Najib', 'Ray']
print(friends) # ['Ray', 'Najib', 'Grace', 'Diaz', 'Julior']
friends.sort()
print(friends) # ['Diaz', 'Grace', 'Julior', 'Najib', 'Ray']

