#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = len(sys.argv) - 1
    print("{:d} argument{}{}".format(number ,"s" if number != 1 else "", ":" if number > 0 else "."))
    if number > 0:
        for i in range(1, number + 1):
            print("{}: {}".format(i, sys.argv[i]))
