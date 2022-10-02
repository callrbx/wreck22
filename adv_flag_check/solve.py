import binascii

nums = [
    (0x558c4dc, 0x6239a8ba),
    (0x71100c9b, 0x17f64e0),
    (0xce3d1dde, 0xa14442bb),
    (0x322958fc, 0x415c0789),
    (0x8cbe8f4e, 0xf6e1eb2b),
    (0xb14a374b, 0xde2c6878),
    (0xee9707a, 0x669d2f08),
    (0xf98ddd38, 0xc8d2ae51),
    (0x5d715f4d, 0x6c12677f),
    (0x410b9f90, 0x3c3cfba3)
]

hex_flag = b""

for a, b in nums:
    hex_flag += binascii.unhexlify(hex(a ^ b)[2:])[::-1]

print(hex_flag)

# flag{hope_you_used_z3_for_this_128c13d7}
