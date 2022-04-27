#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.'''


import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        var = argv[1]
    else:
        var = ""
    try:
        url = 'http://0.0.0.0:5000/search_user'
        letter = {"q": var}
        r = requests.post(url, data=letter)
        user = r.json()
        if len(user) > 0:
            print("[{}] {}".format(user.get('id'), user.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
