from pwn import *

start_addr = 0x00400000
flag_addr_hex = []
flag_addr_int_encode = []
flag_addr_hex_encode = []

with open('badchars', 'rb') as f:
  s = f.read()
for i in b'flag.txt':
	flag_addr_hex.append(hex(s.find(i) + start_addr))
	flag_addr_int_encode.append(p32(s.find(i) + start_addr))
	flag_addr_hex_encode.append(hex(s.find(i) + start_addr).encode())
print(flag_addr_hex)
print(flag_addr_int_encode)
print(flag_addr_hex_encode)


print(int.from_bytes(flag_addr_hex_encode[0], byteorder='little'))
print(int.from_bytes(flag_addr_int_encode[0], byteorder='little'))
