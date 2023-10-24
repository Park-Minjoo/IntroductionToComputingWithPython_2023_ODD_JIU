import sys

try:
    inf = open('myfile.txt', 'r')
    s = inf.readline()
except IOError as err:
    print("I/O error: {0}".format(err))