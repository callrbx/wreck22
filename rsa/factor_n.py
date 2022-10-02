
#!/usr/bin/python3

from Crypto.Util.number import getRandomNBitInteger, isPrime


def FindNthRoot(x, n):

    high = 1
    while high ** n <= x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


def FindNextPrime(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while not isPrime(n):
            n += 2
        return n


n = 13554551333873705442726458106864886220477941999050426902520575554059267727259251592874465994053017687921942864696229386078583498221949098836785061295094204174068472655445008165955102937086757725371308014797658690720415848483440076914441674029990157316666858672848004343680000056425931705594995559042797123927439707571231425094693478661842990163100428585116374483194249826509703206464637820242820679500322267552176505717212328042101372964849654719681727252186759073080566198208809696161708117764617307824300463783825161430873266966103124629553452988773424424848565007453371192910907749205412105638794126336989274629075

# Find the cube root of n, search prime numbers greater than this until the factor of n is found
p = FindNthRoot(n, 3)

while n % p != 0:
    p = FindNextPrime(p)
print(p)

# Compute m, set q equal to p and search prime numbers greater than this until the factor of m is found
m = n // p
q = p

while m % q != 0:
    q = FindNextPrime(q)
print(q)

# The final factor is m divided by q
r = m // q
print(r)
