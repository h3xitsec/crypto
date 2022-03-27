import random
from .rsa_utils import *
from gmpy2 import *
from binascii import hexlify
from Crypto.Util.number import *
# really simple rsa theory example
# primes
def basic_rsa():
    p = 11
    q = 13
    print("Choose primes (p, q) for public key (n = p*q)")
    print("p = "+str(p)+"\nq = "+str(q))
    # phi, usually represented with the Greek symbol φ
    phi = (p - 1) * (q - 1)
    print("phi = (p - 1) * (q - 1) = "+str(phi))
    # common modulus (n)
    n = p * q
    print("n = p * q = "+str(n)+"\n")
    # public exponent / public encryption key (e)
    # choose one from list of possible values
    print("Possible values for public exponent, e")
    print(generate_exponents(n,phi))
    e = 7
    print("e = " + str(e))
    # private encryption key (d)
    # choose one from list of possible values
    print("Possible values for encryption key, d")
    print(generate_enckey(e,phi))
    d = 223
    print("d = " + str(d)+"\n")
    # carmichael functions (m) (λ(n))
    m = math.lcm(n - 1, q - 1)
    # public key (e, n), private key (d, n)
    print(f"Public Key: ({e}, {n})\nPrivate Key: ({d}, {n})\n")
    # text (t)
    print("Encryption\n----------")
    t = 4
    print("Encrypt character "+str(t))
    print("t = "+str(t)+"\n")
    # cipher text (ct)
    ct1 = pow(t,e,n)
    ct2 = (t ** e) % n
    assert ct1 == ct2
    print("Ciphered text\nct1 = pow(t, e, n)\nct2 = (t ** e) % n = "+str(ct1))
    print("Ciphered: "+str(ct1)+"\n")
    # plain unciphered text (pt)
    print("Decryption\n-----------")
    pt1 = pow(ct1,d,n)
    pt2 = (ct1 ** d) % n
    assert pt1 == pt2 == t
    print("Plain text: \npt1 = pow(ct1, d, n)\npt2 = (ct1 ** d) % n = "+str(pt1))
    print("Unciphered : " + str(pt1))

# generates a list of possible values for public exponent, e

def random_rsa():
    p = prime_finder(100,1000)
    q = prime_finder(100,1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_pubkey(n,phi)
    d = get_privkey(e,phi)
    print("RSA Params\n-----------")
    print("p = "+str(p))
    print("q = "+str(q))
    print("n = "+str(n))
    print("phi = "+str(phi))
    print("e = "+str(e))
    print("d = "+str(d))
    print(f"Public Key: ({e}, {n})\nPrivate Key: ({d}, {n})\n")
    string = 'hello'
    print("Encryption\n----------")
    print("Plain text : "+string)
    ciphered_string = [pow(ord(char), e, n) for char in string]
    print("Ciphered string: "+str(''.join(map(lambda x: str(x), ciphered_string)))+"\n")
    print("Decryption\n-----------")
    dec = [str(pow(char, d, n)) for char in ciphered_string]
    # Return the array of bytes as a string
    unciphered_string = ''.join([chr(int(char2)) for char2 in dec])
    assert unciphered_string == string
    print("Unciphered: " + unciphered_string)

