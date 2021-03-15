#!/usr/bin/env python
# coding: utf-8


def linearCongruentialMethod(Xo, m, a, c, randomNums, noOfRandomNums): 
  
    # Initialize the seed state 
    randomNums[0] = Xo 
  
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


string = "monkey01"
plaintext = "ABCDE"


#Modulus = 256 (1 byte)
#Multiplier = 1103515245
#Increment = 12345

# Seed value 
Xo = len(string) 
# Modulus parameter 
m = 256     
# Multiplier term 
a = 1103515245    
# Increment term 
c = 12345 
# Number of Random numbers 
# to be generated 
noOfRandomNums = len(string) 
# To store random numbers 
randomNums = [0] * (noOfRandomNums)

print(randomNums)

linearCongruentialMethod(Xo, m, a, c, randomNums, noOfRandomNums)

print(randomNums)

for i in randomNums:
    print(i, end = " ")
    
hash1 = hex(hash_djb2(string))

cletter = []
cnt1 = 0
for i in randomNums:
    cletter.append(chr(ord(string[cnt1])^i))
    cnt1 = cnt1 + 1
print(cletter)
s3 = "".join(cletter)
print(s3)

dletter = []
cnt1 = 0
for i in randomNums:
    dletter.append(chr(ord(s3[cnt1])^i))
    cnt1 = cnt1 + 1
print(dletter)
dtext = "".join(dletter)
print(dtext)


