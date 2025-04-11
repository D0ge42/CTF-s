#!/usr/bin/env python3

# This CTF is about the OPTION http request.
# Not all the OPERATIONS are supported by the HTTP server.
# By doing a requestion.Options and printing the HEADERS we can retrieve the Allow HEADERS.
# Inside the Allow headers we can find the "Allowed" HTTP verbs.
# Using non-allowed verbs can sometimes reveal some hidden infos.
# IN this case allowed verbs were HEAD OPTIONS and GET

import requests

def main():
    url = "http://web-10.challs.olicyber.it"
    r = requests.patch(url)
    print(r.headers)

if __name__ == "__main__":
    main()
