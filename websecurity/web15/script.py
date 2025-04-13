#!/usr/bin/env python3

# In this CTF we've to extract external links/scripts from an html page.
# These are usually identified by the link or script tag.
# links will have the href attribute, while script the src one.
# Since script cannot have a src attribute and this could raise an error, i've made 2 different extract functions.
# This could've been done with a try/except statement aswell.
# By using findall on the we'll find --> "dynamic.js","serif.css","style.css"
# We'll have to attach those to the main url and do a get request.
# We then search for the flag in each response.

import re
from typing import Iterable
import requests
from requests.sessions import Session
from bs4 import BeautifulSoup, Comment, ResultSet

def main():
    url = "http://web-15.challs.olicyber.it/"
    r = requests.get(url)
    B4 = BeautifulSoup(r.text,features='html.parser')
    link = B4.find_all(['link','href'])
    script = B4.find_all(['script'])
    to_append = extract_url(link)
    to_append.append(extract_src(script))
    for to_check in to_append:
        combined_url = url + to_check
        req = requests.get(combined_url)
        print(req.content)

def extract_url(content:ResultSet)->list:
    url_list = []
    for elem in content:
        url = elem['href'][1:]
        url_list.append(url)
    return url_list

def extract_src(content:ResultSet)->str:
    src = ''
    for elem in content:
        src = (elem['src'][1:])
    return src

if __name__ == "__main__":
    main()
