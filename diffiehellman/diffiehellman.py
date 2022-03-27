from Crypto.Util.number import *
# Alice generates parameters
p = 113 # prime modulus
g = 5 # generator
a = 14 # secret
A = pow(g,a,p) # A = 18

# Bob receive p, g, A
b = 127 # secret
B = pow(g,b,p) # B = 54

# Alice calculate shared secret
sA = pow(B,a,p) # sA = 44
sB = pow(A,b,p) # sB = 44

# Public values: p, g, A and B
# Private values: a, b, s

# Alice can find Bob's B :
sAB = (g ** b) % p
assert sAB == B

# Bob can find Alice's A:
sBA = (g ** a) % p
assert sBA == A

# One can try to guess Alice's a :
guess = 14
assert A == pow(g,guess,p)

## Find generator
def order(g, p): 
    for i in range(2, p): 
        if pow(g, i, p) == g:
            return i
    return p

for g in range(2,p):
    o = order(g, p)
    if o == p:
        print(str(g) + " is a generator")
        break

## Bruteforce Alice's secret (a)
secret = ''
for a1 in range(p):
	A1 = pow(g, a1, p)
	if A1 == A:
		secret = a1
		break

print(secret)


## Automated and more random
g = 2
p = getStrongPrime(512)
while True:
    a = getRandomRange(2, p-2)
    # Check that a shares no factor with p
    if GCD(a, p-1) == 1:
        break

A = pow(g, a, p)

#### dump
def order(g, p): 
    for i in range(2, p): 
        if pow(g, i, p) == g:
            return i
    return p

tmp = p
for g in range(2,tmp):
    o = order(g, tmp)
    if o == tmp:
        print(str(g) + " is a generator")
        break

