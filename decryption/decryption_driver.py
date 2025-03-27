import decryption.decryption as de
import encryption.key_generation as kg
import utilities.file_operations as fo
import utilities.util as ut


def decryptDriver(eMessage: list):
    n = kg.p * kg.q
    fPath = "utilities\\p_q.txt"

    if (ut.checkForPrivateKey(fPath)):
        private_key = fo.readPrivateKey(fPath)
    else:
        private_key = kg.generatePrivateKey()

    dMessage = de.decryp(eMessage, private_key, n)
    print(dMessage)