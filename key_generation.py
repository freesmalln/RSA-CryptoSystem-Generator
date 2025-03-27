# Choose 2 prime numbers, done
# Compute n = p * q, done
# Select O/(n) = (p -1) * (q-1), done
# Select the public exponent e {1,2, ... O/ (n) - 1} such that
# gcd(e, O/ (n)) = 1
# Compute the private key d such that d * e = 1 mod O/(n)
# return kpub = (n, e), kp = d

import util as ut
import file_operations as fo

vlist = ut.generateNumbers()
p = vlist[0]
q = vlist[1]

def generatePrivateKey():
    global p, q
    phiN = (p - 1) * (q - 1)

    if (ut.isCoPrime(phiN, 65537)):
        e = 65537
    else:
        # regenerate values
        while not (ut.isCoPrime(phiN, 65537)):
            vlist = ut.reGenerateNumbers()
            p = vlist[0]
            q = vlist[1]

            phiN = (p - 1) * (q - 1)
            e = 65537

    private_key = ut.mod_inverse(e, phiN)
    fo.write("p_q.txt", "\n")
    fo.write("p_q.txt", str(private_key))

    return private_key