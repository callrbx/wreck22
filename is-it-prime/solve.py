from pwn import *
import gen_prime


sh = remote("challs.wreckctf.com", 31273)

prime = f"{gen_prime.gen_prime()}".encode('utf-8')

sh.recvuntil(b">>")
sh.sendline(prime)

while b">" in sh.recvline():
    sh.sendline(b"1")

sh.interactive()
