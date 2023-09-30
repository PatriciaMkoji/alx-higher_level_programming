#!/usr/bin/python3
""" Error code for package req"""
if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
