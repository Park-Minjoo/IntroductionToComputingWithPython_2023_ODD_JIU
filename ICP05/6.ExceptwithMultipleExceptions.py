import sys

try:
    f = open('myfile.txt', 'r')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an Integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])

