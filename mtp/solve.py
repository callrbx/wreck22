from pwn import *
import string

flag = b"flag{oops_key_reuse_bwcjpqdweoclkwlbkoc}"

sh = remote("challs.wreckctf.com", 31239)


def get_flag():
    sh.recvuntil(b">")
    sh.sendline(b"2")
    sh.recvuntil(b"Result: ")
    flag = sh.recvline().strip()
    return flag


def encrypt_message(msg):
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b"message? ")
    sh.sendline(msg)
    sh.recvuntil(b"Result: ")
    enc = sh.recvline().strip()
    return enc


encrypted_flag = get_flag()

while len(flag) != len(encrypted_flag):
    for c in string.ascii_lowercase + "_}":
        test = encrypt_message(flag + c.encode("utf-8"))
        if test in encrypted_flag:
            flag += c.encode("utf-8")
            print(flag)
            break


print(flag)
