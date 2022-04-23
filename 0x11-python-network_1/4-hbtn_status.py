#!/usr/bin/python3
'''Script that fetches https://intranet.hbtn.io/status'''
from urllib import response

if __name__ == "__main__":
    import requests

    x = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type:", type(x.text))
    print("\t- content:", x.text)
