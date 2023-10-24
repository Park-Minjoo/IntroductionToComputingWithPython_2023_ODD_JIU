try:
    fh = open("t.txt", "w")
    try:
        fh.write("This is me test file for exception handling!!\n")
        fh.write("="*35)
    finally:
        print("Going to close the file")
        fh.close()
        fh.open("t.txt", "r")
        print(fh.readlines())
        fh.close()

except IOError:
    print("Error: Can\'t find file or read data")
