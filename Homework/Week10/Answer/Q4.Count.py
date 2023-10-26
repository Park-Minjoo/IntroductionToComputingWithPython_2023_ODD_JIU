inf = open('youandme.txt', 'r')
NumWord = []
for i in range(8):
    fline = inf.readline()
    flist = fline.split()

    NumWord.append(len(flist))
print(NumWord)
inf.close()