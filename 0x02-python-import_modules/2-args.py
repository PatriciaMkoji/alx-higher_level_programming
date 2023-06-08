#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    idxcount = len(sys.argv) - 1
    if idxcount == 0:
        print("0 arguments.")
    elif idxcount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(idxcount))
    for x in range(idxcount):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
