import sys

try:
    f = open('file.txt', 'r')
    s = f.readlines()
except IOError as err:
    print("I/O error: {0}".format(err))