#!/usr/bin/python3
"""  Respose Header """
if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
