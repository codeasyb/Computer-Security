#!/usr/bin/python3  
import sys
import hashlib
import random
import string
import time
args = []

def arguments():
    for arg in sys.argv[1:]:
        args.append(arg)

def countZeroBytes(data):
    binaryString =  bin(int(data, 16))[2:].zfill(4 * len(data))
    keys = str(binaryString)
    count = 0
    for i in keys:
        if i == '0':
            count += 1
        else:
            break
    return count

def prefix(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

def sha256Hash(hashable):
    return hashlib.sha256(hashable.encode('utf-8')).hexdigest()

def sha256FileHash(fileName):
    fileHash = hashlib.sha256()
    with open(fileName, 'rb') as file:
        data = file.read(2**16)
        while len(data) > 0:
            fileHash.update(data)
            data = file.read(2**16)
    return fileHash.hexdigest()

def writeFile(fileName, initialHash, proofWork, finalHash, numZeros, iter, timeTaken):
    with open('Results.txt', 'w') as file:
        file.write("File: " + fileName)
        file.write("\nInitial Hash: " + initialHash)
        file.write("\nProof of Work: " + proofWork)
        file.write("\nHash: " + finalHash)
        file.write("\nLeading Bits: " + numZeros)
        file.write("\nIterations: " + iter)
        file.write("\nCompute Time: " + timeTaken)

if __name__ == "__main__":
    arguments()

    difficulty = args[0]
    specialText = ''
    number = specialText.zfill(int(difficulty) // 4)
    initialHash = sha256FileHash(args[1])
    found = False
    iterations = 0
    start = time.time()
    while found == False:
        prefixes = prefix(int(difficulty) // 4)
        solution = sha256Hash(prefixes + initialHash)
        if solution.startswith(number):
            timeRun = time.time() - start
            leading_zeros = countZeroBytes(solution)
            writeFile(args[1], initialHash, prefixes, solution, str(leading_zeros), str(iterations), str(timeRun))
            found = True
        iterations+= 1

   

     
    
    
    

    