#!/usr/bin/python3
""" POST an Email """
if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.parse

    email = {"email": sys.argv[2]}
    encd = urllib.parse.urlencode(email)
    encd = encd.encode("ascii")
    resp = urllib.request.Request(sys.argv[1], encd)

    with urllib.request.urlopen(resp) as response:
        print(response.read().decode('utf-8'))
