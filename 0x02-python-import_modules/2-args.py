#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count1 = len(argv) - 1
    if count1 == 0:
        print("0 arguments.")
    elif count1 == 1:
        print("1 argument:")
        print('1: {}'.format(argv[1]))
    else:
        print("{} arguments:".format(count1))
        for a in range(1, len(argv)):
            print("{}: {}".format(a, argv[a]))
