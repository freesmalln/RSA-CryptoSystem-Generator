from random import random
import random as r
import file_operations
from Crypto.Util import number

def gcd(p, q):
    while q != 0:
        p, q = q, p % q

    return p

def isCoPrime(x, y):
    return gcd(x, y) == 1

def genPrimesList(count):
    primes = []

    for i in range(0, count):
        primes.append(number.getPrime(1024))

    return primes

fPath = "p_q.txt"
tempFile = open(fPath, "r")

if (len(tempFile.readlines()) == 0):
    primes = genPrimesList(100)

def generateNumbers():
    global primes

    if (file_operations.isEmpty(fPath)):
        p = r.choice(primes)
        q = r.choice(primes)

        file_operations.write(fPath, str(p))
        file_operations.write(fPath, "\n")
        file_operations.write(fPath, str(q))
    else:
        pAndQTuple = file_operations.read(fPath)

        p = int(pAndQTuple[0])
        q = int(pAndQTuple[1])

    vlist = [p, q]

    return vlist

def reGenerateNumbers():
    global primes
    p = r.choice(primes)
    q = r.choice(primes)

    file_operations.clearFileContents(fPath)
    file_operations.write(fPath, str(p))
    file_operations.write(fPath, "\n")
    file_operations.write(fPath, str(q))

    vlist = [p, q]

    return vlist

def mod_inverse(e, phiN):
    g, x, y = extended_gcd(e, phiN)
    if g != 1:
        raise ValueError("e and O(n) are not coprime, modular inverse doesn't exist.")
    return x % phiN

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return g, x, y

def letterList():
    ascii_list = [chr(i) for i in range(128)]
    return ascii_list

def letterDict():
    ascii_dict = {chr(i): i for i in range(128)}
    return ascii_dict

def checkForPrivateKey(fPath):
    file = open(fPath, "r")

    lineList = file.readlines()

    if (len(lineList) < 3):
        return False
    else:
        return True