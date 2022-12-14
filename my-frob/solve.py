
crypt = [0xaf, 0xa5, 0xa8, 0xae, 0xb2, 0xa5, 0xa0, 0xa7, 0xbc, 0xb1, 0x96, 0xba, 0xa1, 0xa6, 0xbc, 0xa5,
         0xad, 0x96, 0xa8, 0xad, 0xad, 0x96, 0xa4, 0xb0, 0x96, 0xa4, 0xac, 0xa4, 0xaf, 0xbb, 0xa6, 0xab, 0xb4]


def defrob(data, mod):

    for i, d in enumerate(data):
        data[i] = data[i] ^ mod

    return data


count = 1
ocount = 1

while count != 0xe9:
    crypt = defrob(crypt, count)
    tcount = count
    count += ocount
    ocount = tcount


print(crypt)

print("".join([chr(c) for c in crypt]))
