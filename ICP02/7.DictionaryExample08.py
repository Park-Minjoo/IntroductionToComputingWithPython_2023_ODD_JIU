h = {1:['Jak','Let'], 2:['arta','us'], 3:['Interna','transform'], 4:['tional','the'], 5:['University','world'],}
print(h.keys()) # dict_keys([1, 2, 3, 4, 5])
print(h.values())
# dict_values([['Jak', 'Let'], ['arta', 'us'], ['Interna', 'transform'], ['tional', 'the'], ['University', 'world']])
print(h[5]) # ['University', 'world']
print(h[1].pop()) # Let
print(h)
# {1: ['Jak'], 2: ['arta', 'us'], 3: ['Interna', 'transform'], 4: ['tional', 'the'], 5: ['University', 'world']}

