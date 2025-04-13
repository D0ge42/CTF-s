#!/usr/bin/env python3

# This is just a different way of doing the same challenge.
# This time we use try and except statement so that the script won't raise an error when ['href'] attribute is not found on script.
# We'll iterate trough given links with a for loop. We'll check if current link name is either link or script.
# Then we'll do a get request by joining the href/script link to the web url.
# We'll search fla{ inside given response. If so we print it and break out of the loop.

import re
from typing import Iterable
import requests
from requests.sessions import Session
from bs4 import BeautifulSoup, Comment, ResultSet

def main():
    url = "http://web-15.challs.olicyber.it/"
    r = requests.get(url)
    B4 = BeautifulSoup(r.text,features='html.parser')
    links = B4.find_all(['link','href','script'])
    link_url = ''
    for link in links:
        print(link)
        try:
            if link.name == "link":
                link_url = link.get("href")
            elif link.name == "script":
                link_url = link.get("src")
            response = requests.get(url+link_url)
            if "flag{" in response.text:
                print(response.text)
                break
        except:
            pass

if __name__ == "__main__":
    main()
