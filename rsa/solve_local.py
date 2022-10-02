from Crypto.Util.number import *
from pwn import *
from math import gcd


e = 65537

pandaman = b"PANDAMAN! I LOVE PANDAMAN! PANDAMAN MY BELOVED! PANDAMAN IS MY FAVORITE PERSON IN THE WHOLE WORLD! PANDAMAN!!!!"


# def enc(msg):
#     sh.recvuntil(b">>")
#     sh.sendline(b"1")
#     sh.recvuntil(b":")
#     sh.sendline(msg)
#     enc = sh.recvline().strip()
#     return int(enc)


# def check(msg):
#     sh.recvuntil(b">>")
#     sh.sendline(b"2")
#     sh.recvuntil(b":")
#     sh.sendline(str(msg).encode('utf-8'))

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537
flag = open('flag.txt', 'rb').read()
d = inverse(e, (p-1)*(q-1))

pandaman = b"PANDAMAN! I LOVE PANDAMAN! PANDAMAN MY BELOVED! PANDAMAN IS MY FAVORITE PERSON IN THE WHOLE WORLD! PANDAMAN!!!!"


def enc(m):
    if pandaman == m:
        return "No :("
    else:
        return pow(bytes_to_long(m), d, n)


def check(m):
    t = long_to_bytes(pow(m, e, n))
    print(t)
    if t == pandaman:
        print(flag)
    else:
        print("darn :(")


def recover_n():
    e2 = enc(b"\x02")
    e3 = enc(b"\x03")
    e4 = enc(b"\x04")
    e9 = enc(b"\x09")
    n = gcd(e2**2 - e4, e3**2 - e9)
    return n


def normalize(x):
    t = long_to_bytes(x).decode('latin-1')
    return t


n = recover_n()
z = bytes_to_long(pandaman)
f1 = 5
f2 = 7
f3 = 127
f4 = 193
f5 = 21211
f6 = 254447
f7 = 72050257
f8 = 1939303315420219046960018154685373915387234571881073610300392793536129074899070311578399989850647897594894191349572540907622153300914865620787414911914481665252463115484878819316899244103608295017235223309381353356534696286848452920032763470993

c1 = enc(long_to_bytes(f1))
c2 = enc(long_to_bytes(f2))
c3 = enc(long_to_bytes(f3))
c4 = enc(long_to_bytes(f4))
c5 = enc(long_to_bytes(f5))
c6 = enc(long_to_bytes(f6))
c7 = enc(long_to_bytes(f7))
c8 = enc(long_to_bytes(f8))


cz = (c1 * c2 * c3 * c4 * c5 * c6 * c7 * c8) % recover_n()

print(cz)
check(cz)
