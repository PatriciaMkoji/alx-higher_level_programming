#!/usr/bin/python3
""" Interview solving taking 2 args """
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    reposit = sys.argv[1]
    user = sys.argv[2]

    resp = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(user, reposit)
    )

    try:
        data = resp.json()
        # find the sha and enter to the commit dic
        for dic in data[:10]:
            sha = dic.get('sha')
            sha_key = dic.get('commit')

            if sha_key:
                author = sha_key.get('author')
            if author:
                name = author.get('name')

            print("{}: {}".format(sha, name))
    except ValueError:
        print("Not a valid JSON")
