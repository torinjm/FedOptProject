# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 14:58:37 2021

@author: Travis
"""

def encrypt(m, n, g):
    r = 13
    c = (pow(g,m) * pow(r,n)) % pow(n,2)
    return c

def decrypt(c, n, mu, sig):
    m = L_Func(pow(c,sig,pow(n,2)),n) * mu % n
    return m

def L_Func(x, n):
    output = (x - 1)/n
    return output


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


p = 19
q = 23

n = p * q
n2 = pow(n,2)

sig = compute_lcm(p-1, q-1)

g = n+1

Lg = L_Func(pow(g, sig, n2), n)
Lg = int(Lg)

mu = pow(Lg, -1, n)
m1 = 123
m2 = 124
m3=125


c1 = encrypt(m1, n, g)
print(str(c1))

c2 = encrypt(m2, n, g)
print(str(c2))

c3 = encrypt(m3, n, g)
print(str(c3))


c1add2 = encrypt(m1+m2, n, g)
print(c1add2)

print(str(m1+m2))
addmessage = decrypt(c1add2, n, mu, sig)
print(addmessage)


indivenc = c1 * c2
indidec = decrypt(indivenc, n, mu, sig)
print(str(indidec))
print(str(m1 + m2))

