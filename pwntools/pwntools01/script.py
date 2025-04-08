#!/usr/bin/env python3

# This ctf is mainly focussed on discovering how pwntools library works.
# List of integers will be given troughout the software execution.
# Your goal is to sum them and send back the result.
# 10 Sums of numbers in 10 seconds.

from pwn import *
context.log_level = "debug"

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)
    # Send some data to start the challenge
    r.sendlineafter(b".. Invia un qualsiasi carattere per iniziare ...",b"a")
    # While loops that cycle different list of numbers
    while(1):
        solve_first(r)
    r.close()

def solve_first(r:remote)-> int:
    '''
    function to solve first set of nums
    '''

    #Recv to parse the received data 
    nums = r.recvuntil(b"somma questi numeri\n")
    nums = r.recvuntil(b"[")
    nums = r.recvuntil(b"]")[:-1]
    # print(f"nums = {nums}")
    # Split the list eachtime we've a comma and space
    bytes_list = nums.split(b", ")
    res:int = 0

    # Cycle each element in bytes_list and translate each byte into an int. 
    for byte in bytes_list:
        num = int(byte.decode('utf8'))
        res = res + num

    # Cast to string from int
    res_byte = str(res).encode('utf8')
    # print("RES = ",res_byte, "END\n")
    # Send result to SHELL
    r.sendline(res_byte)
    # Return bytes_list
    return 1

if __name__ == "__main__":
    main()
