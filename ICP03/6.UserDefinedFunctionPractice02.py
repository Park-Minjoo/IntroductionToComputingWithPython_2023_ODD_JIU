def noVowel(s):
    vowels = set('aeiouAEIOU')
    # print(vowels)
    if set(s).intersection(vowels):
        return False
    else:
        return True


print(noVowel('crypt'))
print(noVowel('cwm'))
print(noVowel('car'))