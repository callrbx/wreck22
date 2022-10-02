#!/usr/local/bin/python

import random
import math
import gen_prime


with open("flag.txt", "r") as f:
    flag = f.read()


#n = int(input(">> "))
n = gen_prime.gen_prime()

n_len = n.bit_length()

if n_len < 1020 or n_len > 1028:
    print("no. 1")
    quit()
for i in range(2, 1000):
    if n % i == 0:
        print("no. 2")
        quit()
if all([pow(random.randrange(1, n), n-1, n) == 1 for i in range(256)]):
    a = []
    for _ in range(70):
        #a.append(int(input(">> ")))
        a.append(1)
    print([n % i == 0 for i in a])
    if all([n % i == 0 for i in a]):
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if math.gcd(a[i], a[j]) != 1:
                    print(a[i], a[j])
                    print("no. 3")
                    quit()
        print(flag)
    else:
        print("no. 4")
        quit()
