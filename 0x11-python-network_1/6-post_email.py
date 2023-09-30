#!/usr/bin/python3
""" Posts an email """
if __name__ == "__main__":
    import sys
    import requests

    dict = {'email': sys.argv[2]}
    resp = requests.post(sys.argv[1], data=dict)
    print(resp.text)
