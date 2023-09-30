#!/usr/bin/python3
"""the package request"""
if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    print(resp.headers.get('X-Request-Id'))
