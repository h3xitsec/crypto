import random

# generate a list of possible values for public exponent, e
def generate_exponents(n,phi):
    pub_keys = []
    for i in range(2, phi):
        if gcd(i, phi) == 1 and gcd(i, n) == 1:
            pub_keys.append(i)
        if len(pub_keys) >= 100:
            break
    return pub_keys

# generate a list of possible values for encryption key, d
def generate_enckey(e,phi):
    priv_keys = []
    i = 2
    while len(priv_keys) < 5:
        if i * e % phi == 1:
            priv_keys.append(i)
        i += 1
    return priv_keys

# check if 2 numbers are co-prime
def coprime(a, b):
    if ( gcd(a, b) == 1):
        return True
    else:
        return False

# calculate gcd
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# generate random prime numer
def prime_finder(low,high):
    test_number = random.randrange(low, high)
    for i in range(2, test_number):
        if test_number % i == 0:
            return prime_finder(low,high)
    return test_number

# return random e from possible values
def get_pubkey(n,phi):
    return random.choice(generate_exponents(n,phi))

# return random d from possible values
def get_privkey(e,phi):
    return random.choice(generate_enckey(e,phi))
