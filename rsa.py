# M - message, c = ciphertext, d = private key
# Encryption: c(m) = m^e mod n
# Decryption: m(c) = c^d mod n

import encryption.key_generation as kg
import utilities.util as ut
import utilities.file_operations as fo
import encryption.encryption as en
import decryption.decryption_driver as dd

e = 65537

if __name__ == '__main__':
    m = input("Enter a message: ")
    fPath = "utilities\\p_q.txt"
    ldict = ut.letterDict()

    if (ut.checkForPrivateKey(fPath)):
        private_key = fo.readPrivateKey(fPath)
    else:
        private_key = kg.generatePrivateKey()

    n = kg.p * kg.q
    eMessage = en.encryp(m, e, n)
    dd.decryptDriver(eMessage)