#!/usr/bin/env python3

# This ctf let us use both a binary file and a binary file hosted on a server.
# It checks if REMOTE is given as argument.
# If so it connects to the remote server, else it uses the binary file.
# We'll have to provide the function addresses that are situated inside the ELF file.
# Goal is to complete 20 steps in 10 seconds.

from pwn import *
context.log_level = "debug"

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    
    HOST = "software-17.challs.olicyber.it"
    PORT = 13002
    exe = ELF("./sw-19") # ELF will provide info about an ELF file. 
    if args.REMOTE: # This checks if REMOTE is the first arg. Default is arg[0]
        p = remote(HOST,PORT) # If so it means we wanna connect to the remote server
    else:
        p = process(["./sw-19"]) # Else we use the provided binary file
    p.sendlineafter(b".. Invia un qualsiasi carattere per iniziare ...",b"a")
    while(1):
        func_name = extract_func_name(p).decode('utf8') #Loops that will extract the function name and make it a string.
        # print(func_name)
        data = str(exe.sym[func_name])                  # Thanks to exe which we assigned before we can retrieve a function address by using exe.sym[func_name]
        address = int(data)                             # We first convert the address to an integer and then to hex, and encode it back to get a byte sequence.
        hexa_address = hex(address).encode('utf8')
        print(f"Address = {hexa_address}")
        p.sendline(hexa_address)                        # We send the output back with sendline (which adds a new line in this case) and then repeat.
    p.close()

def extract_func_name(p):
    '''
    This function is responsible for extracting the function name provided by the binary.
    It uses recvuntil that receives output until a certain delim is met.
    Returns an unknown variable type that is the function name.
    '''
    p.recvuntil(b"-> ")
    func_name = p.recvuntil(b": ")[:-2]
    return func_name

if __name__ == "__main__":
    main()
