#!/usr/bin/env python
# coding: utf-8

row_num = 26
col_num = 26
list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
cnt1 = 0
cnt2 = 0
for row in range(row_num):
    cnt1 = cnt2
    for col in range(col_num):
        multi_list[row][col]= list1[cnt1%len(list1)]
        cnt1 = cnt1 + 1
    cnt2 = cnt2+1

print(multi_list)

file = open('keys.txt')
keyfile = file.readlines()
print(keyfile[0].rstrip('\n'))
key1 = keyfile[0].rstrip('\n')


string = "GEEKSFORGEEKS"
cnt = 0
while len(key1) < len(string):
    key1 = key1+key1[cnt]
    cnt = cnt +1
print(string)
print(key1)

mlist = []
klist = []
for i in string:
    count = 0
    for j in list1:
        if i == j:
            mlist.append(count)
        count = count +1
for i in key1:
    count = 0
    for k in list1:
        if i == k:
            klist.append(count)
        count = count +1
print(mlist)
print(klist)

encryptedtext = []
cnt3 = 0
for i in range(len(mlist)):
    encryptedtext.append(multi_list[mlist[cnt3]][klist[cnt3]])
    cnt3 = cnt3+1
print(encryptedtext)
separator = ''
etext = separator.join(encryptedtext)
print(etext)


decryptedindex = []
decryptedtext = []
cnt3 = 0
i = 0
for i in range(len(klist)):
    #print(multi_list[klist[cnt3]])
    if encryptedtext[cnt3] in multi_list[klist[cnt3]]:
        index = multi_list[klist[cnt3]].index(encryptedtext[cnt3])
        decryptedindex.append(index)
    cnt3 = cnt3 +1
print(decryptedindex)

for a in decryptedindex:
    if a == 0:
        decryptedtext.append('A')
    elif a == 1:
        decryptedtext.append('B')
    elif a == 2:
        decryptedtext.append('C')
    elif a == 3:
        decryptedtext.append('D')
    elif a == 4:
        decryptedtext.append('E')
    elif a == 5:
        decryptedtext.append('F')
    elif a == 6:
        decryptedtext.append('G')
    elif a == 7:
        decryptedtext.append('H')
    elif a == 8:
        decryptedtext.append('I')
    elif a == 9:
        decryptedtext.append('J')
    elif a == 10:
        decryptedtext.append('K')
    elif a == 11:
        decryptedtext.append('L')
    elif a == 12:
        decryptedtext.append('M')
    elif a == 13:
        decryptedtext.append('N')
    elif a == 14:
        decryptedtext.append('O')
    elif a == 15:
        decryptedtext.append('P')
    elif a == 16:
        decryptedtext.append('Q')
    elif a == 17:
        decryptedtext.append('R')
    elif a == 18:
        decryptedtext.append('S')
    elif a == 19:
        decryptedtext.append('T')
    elif a == 20:
        decryptedtext.append('U')
    elif a == 21:
        decryptedtext.append('V')
    elif a == 22:
        decryptedtext.append('W')
    elif a == 23:
        decryptedtext.append('X')
    elif a == 24:
        decryptedtext.append('Y')
    elif a == 25:
        decryptedtext.append('Z')
print(decryptedtext)
separator = ''
dtext = separator.join(decryptedtext)
print(dtext)


# encryptedtext

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


# decryptedtext

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


import sys

args = []

def arguments():
    for arg in sys.argv[1:]:
        args.append(arg)

def linearCongruentialMethod(Xo, randomNums, noOfRandomNums):
  
    # Initialize the seed state
    randomNums[0] = Xo
    m = 256
    a = 1103515245
    c = 12345
  
    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
          
        # Follow the linear congruential method
        randomNums[i] = ((randomNums[i - 1] * a) +c) % m



def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


if __name__ == "__main__":

    arguments()
    linear_congruential(hash_djb2(args[0]))
