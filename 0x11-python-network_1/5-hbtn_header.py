#!/usr/bin/python3
'''Script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id in the response header.'''
if __name__ == "__main__":
    import requests
    import sys

    x = requests.get(sys.argv[1])
    print(x.headers.get('X-Request-Id'))
