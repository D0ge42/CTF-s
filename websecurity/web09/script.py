#!/usr/bin/env python3
# In this case we're sending a POST request to the web server.
# This time we're gonna use a JSON format

import requests

def main():
    payload = {'username':'admin','password':'admin'}
    url = "http://web-09.challs.olicyber.it/login"
    r = requests.post(url,json=payload)
    print(r.text)

if __name__ == "__main__":
    main()
