days = ('Mo', 'Tu', 'We')
print(days) # ('Mo', 'Tu', 'We')

days = 'Mo', 'Tu', 'We', 'Th'
print(days) # ('Mo', 'Tu', 'We', 'Th')

print('Fr' in days) # False

week = days + ('Fr', 'Sa', 'Su')
print(week) # ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')

print(week[2]) # We
print(len(week)) # 7
print(2*week)
# ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')