ciphertext = "oujp{xkurpjcxah_ljnbja_lryqna}"


def spin(c, key):
    return chr((ord(c) - ord('a') - key) % 26 + ord('a'))


plaintext = ''.join(
    spin(c, 43) if 'a' <= c <= 'z' else c
    for c in ciphertext
)

print(plaintext)


# flag{obligatory_caesar_cipher}
