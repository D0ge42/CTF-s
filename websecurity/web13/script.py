#!/usr/bin/env python3

# This ctf is also based on finding the flag with the find_all method. This time tho
# we''ll have to deal with highlighted text (found between <span> tags .)
# So we'll have to first filter all the span tags and then filter the response.
# By using the get_text method on every span tag, we'll get the text.
# I've then used the append method to append everything onto the flag list.
# Then i've joined every element onto a string.

import requests
from requests.sessions import Session
from bs4 import BeautifulSoup

def main():
    url = "http://web-13.challs.olicyber.it/"
    r = requests.get(url)
    B4 = BeautifulSoup(r.text,features='html.parser')
    resp = B4.find_all('span')
    flag = []
    for piece in resp:
        flag.append(piece.get_text())
    form_flag =''.join(flag)
    print(form_flag)

if __name__ == "__main__":
    main()
