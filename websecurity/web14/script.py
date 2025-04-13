#!/usr/bin/env python3

# In this CTF we'll use a custom function to filter from a list, all the commments.
# We can achieve that by using the isistance function.
# It will return True or False. True if a certain element is part of a specified Class, else false.
# The string parameters also accept regular expressions,functions,list and True.
# That means that by filtering the content of find_all method we'll be able to get a list of comments inside the HTML.

import requests
from requests.sessions import Session
from bs4 import BeautifulSoup, Comment, ResultSet

def main():
    url = "http://web-14.challs.olicyber.it/"
    r = requests.get(url)
    B4 = BeautifulSoup(r.text,features='html.parser')
    comments = B4.find_all(string=is_comment)
    print(comments)

def is_comment(elem):
    return isinstance(elem,Comment)

if __name__ == "__main__":
    main()
