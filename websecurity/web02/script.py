#!/usr/bin/env python3

# Same as web01 but this time we provide payload infos

import requests

def main():
    payload = {'id':'flag'}
    r = requests.get("http://web-02.challs.olicyber.it/server-records",payload)
    print(r.text)

if __name__ == "__main__":
    main()
