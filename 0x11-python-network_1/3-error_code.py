#!/usr/bin/python3
""" Error Code """
if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            disp = str(response.read().decode('utf-8'))
            print(disp)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
