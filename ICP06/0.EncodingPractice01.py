def encoding(text):
    print('Char   Decimal    Hex     Binary')

    for c in text:
        code = ord(c)
        print('   {}   {:7}   {:4x}    {:7b}'.format(c, code, code, code))

encoding('dad')
encoding('안녕')