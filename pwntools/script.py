#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    r.sendlineafter(b".. Invia un qualsiasi carattere per iniziare ...",b"a")

    
    while(1):
        bytes_list = build_num_list(r)
        print("Bytes_list = ", bytes_list)
        # We initialize res 
        res:int = 0

        # Cycle each element in bytes_list 
        for byte in bytes_list:
            num = int(byte.decode('utf8'))
            res = res + num

        res_byte = str(res).encode('utf8')
        r.sendlineafter(b"Somma?",res_byte)

        data2 = r.recvuntil(b"Somma?")
        print("DATA2 = ", data2, "END")
        r.interactive()

    r.close()

def build_num_list(r:remote)-> list[bytes]:
    '''
    function to return a list of bytes
    '''
    #Catch the line ending with ]
    # nums = r.recvline_endswith(b"]")
    nums = r.recvuntil(b"Somma?")
    print("NUMS = ", nums, "END")
    #Find index of both [ and ] (extremities of array) 
    index_start= nums.find(b"[",0,4000)
    print("INDEX START = ", index_start)
    index_end = nums.find(b"]",0,4000)
    print("INDEX END = ", index_end)

    # Split the list eachtime we've a comma and space
    cutnum = nums[index_start + 1:index_end]
    bytes_list = cutnum.split(b", ")

    # Return bytes_list
    return bytes_list

if __name__ == "__main__":
    main()
