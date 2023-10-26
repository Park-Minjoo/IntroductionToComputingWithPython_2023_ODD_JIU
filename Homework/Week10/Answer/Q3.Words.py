inf = open('youandme.txt', 'r')
sm = inf.readlines()
for i in range(len(sm)) :
    s=sm[i].strip(" ")
    slist = s.split()
    print(slist)
inf.close()