#!/usr/bin/env python3

# In this CTF we focus on Headers. 
# Headers are http headers that can be used inside a request context, so that the server can tailer the response.
# Headers can be used to supply authentication credentilas(Authorization), to ccontrol caching, or to get information about the user agent.

import requests
from requests.models import HTTPBasicAuth

def main():
    url = "http://web-03.challs.olicyber.it/flag"
    header = {'X-Password':'admin'}
    r = requests.get(url,headers=header)
    print(r.text)

if __name__ == "__main__":
    main()
