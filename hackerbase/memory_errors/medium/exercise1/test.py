from pwn import *

string = b"ciao\x00vai"

p = process("./test")
p.sendline(string)
p.interactive()
