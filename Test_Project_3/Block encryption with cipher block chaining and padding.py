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
keystreamblock = []
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
for i in range(16):
    rgen = linearCongruentialMethod(Xo, m, a, c, randomNums, noOfRandomNums)
    keystreamblock.append(rgen)

i=0
while i < keystreamblock:
    first = keystreamblock[i] & 0xf
    second = (keystreamblock[i] >> 4) & 0xf
    swap(block[first], block[second])


