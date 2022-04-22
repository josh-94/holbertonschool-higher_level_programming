#!/usr/bin/python3
import urllib.request
'''Python script that fetches https://intranet.hbtn.io/status'''

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

    print("Body response:")
    print("\t- type: ", type(html))
    print("\t- content: " + str(html))
    print("\t- utf8 content: " + response.msg)
