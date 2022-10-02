from Crypto.Util.number import *
from pwn import *
from math import gcd
import codecs

sh = remote("challs.wreckctf.com", 31745)

pandaman = b"PANDAMAN! I LOVE PANDAMAN! PANDAMAN MY BELOVED! PANDAMAN IS MY FAVORITE PERSON IN THE WHOLE WORLD! PANDAMAN!!!!"


def enc(msg):
    sh.recvuntil(b">>")
    sh.sendline(b"1")
    sh.recvuntil(b":")
    sh.sendline(msg)
    enc = sh.recvline().strip()
    try:
        return int(enc)
    except:
        sh.interactive()


def check(msg):
    sh.recvuntil(b">>")
    sh.sendline(b"2")
    sh.recvuntil(b":")
    sh.sendline(str(msg).encode('utf-8'))


# maybe needed?
def recover_n():
    e2 = enc(b"\x02")
    e3 = enc(b"\x03")
    e4 = enc(b"\x04")
    e9 = enc(b"\x09")
    n = gcd(e2**2 - e4, e3**2 - e9)
    return n


z = bytes_to_long(pandaman)
zp = z*(2**65536)
c1 = enc(long_to_bytes(zp))
c2 = enc(long_to_bytes(2))

p = (c1*c2)//2
check(p)

sh.interactive()
