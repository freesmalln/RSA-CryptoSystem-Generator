# M - message, c = ciphertext, d = private key
# Encryption: c(m) = m^e mod n

def encryp(m, e, n):
    eMessage = []

    for i in m:
        i = ord(i)
        eMessage.append(pow(i, e, n))

    return eMessage