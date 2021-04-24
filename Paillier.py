import random


# encrypts message 'm'
#   m = message
#   n = p * q (generated prime numbers)
#   g = random int from 1 to n^2
def encrypt(m, n, g):
    # generate random number 'r' from 1 to n-1, that satisfies gcd(r, n) = 1
    r = random.randint(1, n-1)
    while gcd(r, n) != 1:
        r = random.randint(1, n-1)
    c = (pow(g, m) * pow(r, n)) % pow(n, 2)
    return c


# decrypts messsage 'c'
#   c = encrypted message
#   n = p * q (generated prime numbers)
#   mu = modular multiplicative inverse
#   sig = lcm(p-1, q-1)
def decrypt(c, n, mu, sig):
    m = L_Func(pow(c, sig, pow(n, 2)), n) * mu % n
    return m


# x = g^sig % n2
# n = p * q (generated prime numbers)
def L_Func(x, n):
    output = (x - 1)/n
    return output


# if n is prime, return true
def is_prime(n):
    count = 0
    for i in range(int(n/2)):
        if n % (i+1) == 0:
            count = count+1
    return count == 1


# calculate least common multiple between x and y
def compute_lcm(x, y):

    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


# calculate gcd between a and b
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
