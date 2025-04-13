#!/usr/bin/env python3

#IN this ctf we're asked to make a simple get request to retrieve the flag.
# Once we've done the get request, we can just print it by accessing the response with .text property.

import requests

def main():
    flag = requests.get("http://web-01.challs.olicyber.it/")
    print(flag.text)

if __name__ == "__main__":
    main()
