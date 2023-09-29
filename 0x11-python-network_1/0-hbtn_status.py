#!/usr/bin/python3
""" header """
if __name__ == "__main__":
    import urllib.request

    
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:

        print("Body response:")

        resp = response.read()
        print("\t- type: {}".format(type(response.read())))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode('utf8')))
