#!/usr/bin/env python3

# Accept headers let us specify a list of formats that clients
# consider acceptable. This is done using a system classification called MIME
# Sometimes different format can provide more infos.
# Mime stands for Multipurpose Inteernet Mail Extensions

import requests

def main():
    url = "http://web-04.challs.olicyber.it/users"
    header = {'Accept':'application/xml'}
    r = requests.get(url,headers=header)
    print(r.text)

if __name__ == "__main__":
    main()
