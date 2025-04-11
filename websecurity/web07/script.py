#!/usr/bin/env python3

# This CTF is about the verb HEAD.
# HEAD verb is a method that requests the metadata of a resource in the form of Headers
# that the server wouldve hae sent if the get method was used instead.
# This method can be used in cases where a URL might produce a large download.
# For example a HEAD request can read the content lenght to check the file size before downloading the file
# with GET.

import requests

def main():
    url = "http://web-07.challs.olicyber.it"
    r = requests.head(url)
    print(r.headers)

if __name__ == "__main__":
    main()

