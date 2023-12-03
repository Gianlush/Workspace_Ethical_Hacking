from pwn import *

p = process("./vuln")

pid = gdb.attach(p, gdbscript = '''

break main

''')
addr = gdb.find_module_addresses("./vuln")
print(hex(addr[0].symbols[b'sym.win_authed']))
p.interactive()
