# Q3
def crypto(filename):
    file = open(filename)
    content = file.read()
    file.close()
    print(content.replace('secret','xxxxxx'))

crypto('crypto.txt')