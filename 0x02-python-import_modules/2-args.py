#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count1 = len(sys.argv) - 1
    if count1 == 0:
        print("0 arguments.")
    elif count1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count1))
        for a in range(count1):
             print("{}: {}".format(a + 1, sys.argv[a + 1]))
