#!/usr/bin/env python3

# This ctf is mainly focussed on the packing/unpacking functions.
# It is requested to send back hexadecimals received either as 32 or 64 packets
# Goal is to complete 100 steps in 10 seconds.

from pwn import *
context.log_level = "debug"

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)
    # Send some data to start the challenge
    r.sendlineafter(b".. Invia un qualsiasi carattere per iniziare ...",b"a")
    pack = 0
    while(1):
        bytes_seq = extract_byte_sequence(r)        # We first extract the byte sequence
        bytes_type = extract_type(r)                # Then extract the package type (32/64)
        decoded_string = bytes_seq.decode('utf-8')  # The byte sequence is decoded into a utf-8 string.
        packed_int = int(decoded_string, 16)        # After that we specify the base to convert from (16).
        if bytes_type == b"32-bit":
            pack = p32(packed_int)                  # Pack the integer as a 32 bit packet.
        if bytes_type == b"64-bit":
            pack = p64(packed_int)                  # Pack the integer as a 64 bit packet.
        r.send(pack)                                # Send package.
    r.interactive()
    r.close()

def extract_type(r:remote) -> bytes:
    '''
    Function made to extract the type of pack.
    In our case is either gonna be 64 or 32.
    Returns the byte sequence.
    '''
    r.recvuntil(b"packed ")
    r.recvuntil(b"a ")
    data = r.recvuntil(b"\n")[:-1]
    return data

def extract_byte_sequence(r:remote) -> bytes:
    '''
    Extract the integer given as byte sequence and returns it.
    '''
    r.recvuntil(b"restituiscimi ")
    data = r.recvuntil(b" ")[:-1]
    return data

if __name__ == "__main__":
    main()
