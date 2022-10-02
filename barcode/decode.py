from PIL import (
    Image,
    ImageDraw,
)
import sys

INPUT_PATH = sys.argv[1]

STRIPE_WIDTH = 16
STRIPE_HEIGHT = 128

im = Image.open(INPUT_PATH)

num_chars = int(im.width / (8 * STRIPE_WIDTH))

print(f"{num_chars} char read from image")

flag = ""

cur_bit = 0
for x in range(num_chars):
    n = '0b'
    for b in range(8):
        # should get middle of stripe
        if im.getpixel((cur_bit + 8, STRIPE_HEIGHT/2)) == (0, 0, 0):
            n += '1'
        else:
            n += '0'
        cur_bit += STRIPE_WIDTH
    flag += (chr(int(n, 2)))

print(flag)

# flag{not_really_a_barcode_i_guess}
