#!/usr/bin/env python3

# This CTF is mainly focussed on using the find_all method from BeatifulSoup library.
# Basically given an html page, we'll make a simple get request to it, using html.parser.
# Once we've the response, we can build our B4 instance, and use the built-in method find_all.
# Inside find all we'll specify what we're looking for, like paragraphs, href etc.


import requests
from requests.sessions import Session
from bs4 import BeautifulSoup

def main():
    url = "http://web-12.challs.olicyber.it/"
    r = requests.get(url)
    B4 = BeautifulSoup(r.text,features='html.parser')
    resp = B4.find_all('p')
    print(resp)

if __name__ == "__main__":
    main()
