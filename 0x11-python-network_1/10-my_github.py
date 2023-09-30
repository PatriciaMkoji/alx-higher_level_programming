#!/usr/bin/python3
""" Connect to github api"""
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    user = sys.argv[1]
    paswd = sys.argv[2]

    resp = requests.get("https://api.github.com/user",
                        auth=(HTTPBasicAuth(user, paswd)))

    try:
        data = resp.json()
        print(data.get('id'))
    except json.JSONDecodeError:
        print("Not a valid JSON")
