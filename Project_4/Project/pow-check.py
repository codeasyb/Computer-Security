#!/usr/bin/python3  
import sys 
import hashlib
import re
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

def sha256Hash(hashable):
    return hashlib.sha256(hashable.encode('utf-8')).hexdigest()

def sha256FileHash(fileName):
    fileHash = hashlib.sha256()
    with open(fileName, 'rb') as file:
        data = file.read(65536)
        while len(data) > 0:
            fileHash.update(data)
            data = file.read(65536)
    return fileHash.hexdigest()

def values(fileName):
    results = [None] * 4
    with open (fileName, 'r+') as file:
        data = file.readlines()
        for items in data:
            line = items.replace(' ', '')
            if re.compile('Initial-hash').search(line) != None:
                new_data = items.split(':')
                results[0] = new_data[1].strip()
            if re.compile('Hash').search(line) != None:
                new_data = items.split(':')
                results[1] = new_data[1].strip()
            if re.compile('Leading-bits').search(line) != None:
                new_data = items.split(':')
                results[2] = new_data[1].strip()
            if re.compile('Proof-of-work').search(line) != None:
                new_data = items.split(':')
                results[3] = new_data[1].strip()
    return results

if __name__ == "__main__":
    arguments()
    result = values(args[0])
    messageHash = sha256FileHash(args[1])
    computeHash = sha256Hash(str(result[3]) + messageHash)
    numZeros = countZeroBytes(computeHash)
    
    if (result[0] == messageHash) and result[1] == computeHash and result[2] == str(numZeros):
        print("PASSED")
    else:
        if result[0] != messageHash:
            print("Initial-hash didn't match.")
        if result[1] != computeHash:
            print("Final Hash didn't match.")
        if result[2] != str(numZeros):
            print("Number of Leading-bits didn't match.")