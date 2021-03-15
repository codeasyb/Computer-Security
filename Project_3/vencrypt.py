import sys
from itertools import starmap, cycle

args = []

def arguments():
    for arg in sys.argv[1:]:
        args.append(arg)

def cipherKey(keyFile):
    with open(keyFile + ".txt", 'r+') as file:
        keyFile = file.readlines()
        keyText = keyFile[0].rstrip('\n')
        return keyText

def encrypt(key, plain_textFile, cipher_textFile):
    encList = []
    def enc(c, k):
        return chr(((ord(k) + ord(c) -2 * ord('A')) %26) + ord('A'))

    with open(plain_textFile + '.txt', 'r+') as file:
        for lines in file.readlines():
            lines.replace('"', '')
            message = filter(str.isalpha, lines.upper())
            solution  = ''.join(starmap(enc, zip(message, cycle(key))))
            encList.append(solution)

    with open(cipher_textFile + '.txt', 'w') as file:
        file.writelines(encList)

if __name__ == "__main__":
    arguments()
    key = cipherKey(args[0])
    encrypt(key, args[1], args[2])