#!/usr/bin/env python3

# This CTF is about POST verb.
# A POST request can use every format, but usually when we've to sent the content of a form
# the MIMEtype application/x-www-form-urlencoded will be used.
# For that reason, many servers that receives data from user trough POST requests, accept this format.

# In this CTF we'll be sending a post request to the server, and send a payload with key:values.
# Essentially the application/x-www-form-urlencoded is a sequence of key:value pair.
# This can be done by using a python dictionary like the one in "payload"
# Once we've it in the post request we'll specify data parameter to be payload


import requests

def main():
    payload = {'username':'admin','password':'admin'}
    url = "http://web-08.challs.olicyber.it/login"
    r = requests.post(url,data=payload)
    print(r.text)

if __name__ == "__main__":
    main()
