#!/usr/bin/env python3
# This CTF is also about cookies but this time we'll use a class istance called Session.
# This is to make it so we can save cookies and re-use them later.
# In this CTF we'll use a get request using the class Instance Session.
# Once we saved cookies, we can make a get request and specify cookies as parameters.

# TO recap:
# Cookies are created by web servers while a user is browsing a website and placed 
# on the user's computer or other device by the user's web browser.


import requests

def main():
    s = requests.Session()
    url = "http://web-06.challs.olicyber.it/token"
    RESPONSE = s.get(url)
    r = requests.get("http://web-06.challs.olicyber.it/flag",cookies=RESPONSE.cookies)
    print(r.text)

if __name__ == "__main__":
    main()
