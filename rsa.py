# M - message, c = ciphertext, d = private key
# Encryption: c(m) = m^e mod n
# Decryption: m(c) = c^d mod n

import key_generation as kg
import util as ut
import file_operations as fo
import encryption as en
import decryption_driver as dd

e = 65537

if __name__ == '__main__':
    m = input("Enter a message: ")
    ldict = ut.letterDict()

    if (ut.checkForPrivateKey("p_q.txt")):
        private_key = fo.readPrivateKey("p_q.txt")
    else:
        private_key = kg.generatePrivateKey()

    n = kg.p * kg.q
    eMessage = en.encryp(m, e, n)
    dd.decryptDriver(eMessage)