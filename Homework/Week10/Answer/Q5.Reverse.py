inf = open('youandme.txt', 'r')
fline = inf.readlines()

for line in fline:
    re=''
    for i in range(len(line)-1, -1, -1):
        re += line[i]
    print(re)
inf.close()