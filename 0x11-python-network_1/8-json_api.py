#!/usr/bin/python3
""" Searching for API """
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        dict = {'q': ""}
    else:
        dict = {'q': sys.argv[1]}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=dict)
        data = r.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
