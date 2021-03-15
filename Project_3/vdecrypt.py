import sys
from itertools import starmap, cycle

args = []

def arguments():
    for arg in sys.argv[1:]:
        args.append(arg)

def cipherKey(keyFile):
    with open(keyFile + ".txt", 'r+') as f:
        keyFile = f.readlines()
        key_text = keyFile[0].rstrip('\n')
        return key_text

def decrypt(key, cipher_textFile, plain_textFile):
    decList = []
    def dec(c, k):
        return chr(((ord(c) - ord(k) - 2 * ord('A')) %26) + ord('A'))

    with open(cipher_textFile + '.txt', 'r+') as file:
        for lines in file.readlines():
            message = filter(str.isalpha, lines.upper())
            solution  = ''.join(starmap(dec, zip(message, cycle(key))))
            decList.append(solution)

    with open(plain_textFile + '.txt', 'w') as file:
        file.writelines(decList)

if __name__ == "__main__":
    arguments()
    key = cipherKey(args[0])
    decrypt(key, args[1], args[2])