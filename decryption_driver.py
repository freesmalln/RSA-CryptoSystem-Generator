import decryption as de
import key_generation as kg
import file_operations as fo
import util as ut


def decryptDriver(eMessage: list):
    n = kg.p * kg.q

    if (ut.checkForPrivateKey("p_q.txt")):
        private_key = fo.readPrivateKey("p_q.txt")
    else:
        private_key = kg.generatePrivateKey()

    dMessage = de.decryp(eMessage, private_key, n)
    print(dMessage)