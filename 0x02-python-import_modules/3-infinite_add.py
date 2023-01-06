#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = 0
    for a in range(len(sys.argv) - 1):
        count += int(sys.argv[a + 1])
    print("{}".format(count))
