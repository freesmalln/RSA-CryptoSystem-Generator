import os


def write(fPath, x):
    file = open(fPath, "a")
    file.write(x)
    file.close()

def read(fPath):
    file = open(fPath, "r")
    x = file.readline().strip()
    y = file.readline().strip()

    file.close()

    x = int(x)
    y = int(y)

    return x, y

def isEmpty(fPath):
    return os.path.getsize(fPath) == 0

def readPrivateKey(fPath):
    file = open(fPath, "r")
    list = file.readlines()
    file.close()

    private_key = list[2].strip()

    return int(private_key)

def clearFileContents(fPath):
    open(fPath, "w").close()