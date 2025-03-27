# M - message, c = ciphertext, d = private key
# Decryption: m(c) = c^d mod n

def decryp(c, d, n):
    dMessage = []
    dMessageS = ""

    for i in c:
        i = pow(i, d, n)
        dMessage.append(chr(i))

    for i in dMessage:
        dMessageS += i

    return dMessageS