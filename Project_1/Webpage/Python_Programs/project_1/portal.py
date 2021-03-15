# Amir Ayoub
# Computer Security
""" 
    ------- The format of what is going on during compile time -------------------------
    ------- for the functions related to [AddUser] [Authenticate] [SetDomain] [SetType]- 
    [AddUser] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - user = sys.argv[2]       # 1st argument index
        - password = sys.argv[3]   # 2nd argument index
    [Authenticate] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - user = sys.argv[2]       # 1st argument index
        - password = sys.argv[3]   # 2nd argument index
    [SetDomain] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - user = sys.argv[2]       # 1st argument index
        - domain = sys.argv[3]     # 2nd argument index
    [SetType] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - objectName = sys.argv[2] # 1st argument index
        - type = sys.argv[3]       # 2nd argument index
    
    ------- The format is for the following functions [DomainInfo] [TypeInfo] -----------
    [DomainInfo] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - domain = sys.argv[2]     # 1st argument index
    [TypeInfo] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - type = sys.argv[2]       # 1st argument index
        
    ------- The format is for the following functions [AddAccess] [CanAccess] -----------
    [AddAccess] = keyWord
        - fileName = sys.argv[0]   # <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - operation = sysargv[2]   # 1st argument index
        - domain_name = sysargv[3] # 2nd argument index
        - type_name = sys.argv[4]  # 3rd argument index
    [CanAccess] = keyWord
        - fileName = sys.argv[0] <<<<<<<file name index, [ THIS WE DONT USE  ]>>>>>>
        - keyWord = sys.argv[1]    # keyWord index, keyWord = the function we running 
        - operation = sysargv[2]   # 1st argument index
        - user = sys.argv[3]       # 2nd argument index
        - object = sys.argv[4]     # 3rd argument index
    
"""
"""
                      LOGIC
----------------------------------------------------
AddUser("user", "password")

----------------------------------------------------
----------------------------------------------------
Authenticate("user", password)

----------------------------------------------------
----------------------------------------------------
SetDomain("user", "domain")

----------------------------------------------------
----------------------------------------------------
DomainInfo("domain")

----------------------------------------------------
----------------------------------------------------
SetType("objectname", "type")

----------------------------------------------------
----------------------------------------------------
TypeInfo("type")

----------------------------------------------------
----------------------------------------------------
AddAccess("operation", "domain_name", "type_name")

----------------------------------------------------
----------------------------------------------------
CanAccess("operation", "user", "object")
    The logic to this function 
        for d in domains(user)
            if access[d][t] contains operation
                return
        return false
        
Test Program: portal CanAcess operation user object
----------------------------------------------------
"""

import sys
import json
import os.path


args = []
usersAndPasswords = {}
defaultFile = "userFile.json"
tempDictForAppend = {}
keyWords = ["AddUser", "Authenticate", "SetDomain", "DomainInfo", "SetType", "TypeInfo", "AddAccess", "CanAccess"]

def arguments():
    for arg in sys.argv[1:]:
        args.append(arg)

def AddUser(user, password):
    if user and password == None:
        usersAndPasswords.update({user: ""})
        # print("Show Update: {}".format(usersAndPasswords))
        with open(defaultFile, "r+") as file:
            if os.path.getsize(defaultFile) <= 2:
                json.dump(usersAndPasswords, file)
            else:
                data = json.load(file)
                data.update(tempDictForAppend)
                file.seek(0)
                json.dump(data, file)
    else:
        usersAndPasswords.update({user: password})
        # print("Show second update: {}".format(usersAndPasswords))
        with open(defaultFile, "r+") as file:
            if os.path.getsize(defaultFile) <= 2:
                json.dump(usersAndPasswords, file)
            else:
                data = json.load(file)
                data.update(tempDictForAppend)
                file.seek(0)
                json.dump(data, file)
           
def checkForKeyWord(key):
    keyExists = True
    for k in keyWords:
        if key == k:
            return keyExists
    return False    
    
def userExists(user):
    #if file doesn't exixts create one
    if not os.path.isfile(defaultFile):
        with open(defaultFile, 'w') as file:
            json.dump({},file)
            # print("File created")
            file.close
    else:
        with open(defaultFile, "r") as file:
            readData = json.load(file)
            tempDictForAppend.update(readData)
            for userName in tempDictForAppend.keys():
                if userName == user:
                    return True
                else:
                    pass
            return False
       
def Authenticate(user, password):
    if userExists(user) is False:
        print("Error: no such user")
    else:
        with open('userFile.json', 'r') as file:
            data = json.load(file)
            for userName, passToMatch in data.items():
                if user == userName and password == passToMatch:
                   print("Success")
                else:
                    if user == userName and not password == passToMatch:
                        print("Error: password not match") 

def SetDomain(userName, domain):  
    if domain == None:
        print("Error: missing domain")
    elif userExists(userName) is False:
        print("Error: no such user")
    else:
        domainFile = domain + ".txt"
        if not os.path.isfile(domainFile):
            with open(domainFile, 'w') as file:
                file.write(userName + "\n")
                print("Success")
        else: 
            with open(domainFile, 'r+') as file:
                data = file.readlines()
                readData = [items.strip() for items in data]
                if not userName in readData:
                    file.write(userName + "\n")
                    print("success")

def DomainInfo(domainName):
    if domainName == None :
        print("Error: missing domain")
    else:
        domain = domainName + ".txt"
        if os.path.isfile(domain):
            with open (domain, 'r') as file:
                data = file.readlines()
                readData = [items.strip() for items in data]
                if len(readData) > 0:
                    for items in readData:
                        print(items)

def SetType(obj, typeName):
    if typeName == None:
        print("Failed: type not given")
    else:
        objectType = typeName + '.txt'
        if not os.path.isfile(objectType):
            with open (objectType, 'w') as file:
                file.write(obj + "\n")
                print("Success")
        else:
            with open (objectType, 'r+') as file:
                data = file.readlines()
                new_data = [items.strip() for items in data]
                if not obj in new_data:
                    file.write(obj + "\n")
                    print("Success")

def TypeInfo(typeName):
    if typeName == None :
        print("Error: type can not be an empty string")
    else:
        objType = typeName + ".txt"
        with open(objType, 'r') as file:
            data = file.readlines()
            readData = [types.strip() for types in data]
            if len(readData) > 0:
                for items in readData:
                    print(items)

def AddAccess(operation, domainName, typeName):
    if operation == None and domainName == None and typeName == None:
        print("Error: missing operation")
        print("Error: missing domain")
        print("Error: missing type")
        print("Format: [operation] [domain] [type]")
    elif domainName == None and typeName == None:
        print("Error: missing domain")
        print("Error: missing type")
    elif typeName == None:
        print("Error: missing type")
    else:
        domainFile = domainName + ".txt"
        typeFile = typeName + ".txt"
        if not os.path.isfile(domainFile):
            with open(domainFile, 'w') as file:
                file.write(domainName)
        if not os.path.isfile(typeFile):
            with open(typeFile, 'w') as file:
                file.write(typeName)
        if not os.path.isfile("operations.txt"):
            with open("operations.txt", 'w') as file:
                file.write(operation + ',' + domainName + ',' + typeName + '\n')
                print("Success")
        else:
             with open("operations.txt", 'a+') as file:
                file.write(operation + ',' + domainName + ',' + typeName + '\n')
                print("Success")
    

def CanAccess(operation, user, obj):
    if operation == None and user == None and obj == None:
        print("Error: access denied") 
    elif userExists(user) is False:
        print("Error: access denied")
    elif obj == None:
        print("Error: access denied")
    else:
        if userExists(user):
            with open('operations.txt', 'r') as file:
                data = file.readlines()
                readData = [items.strip().split(',') for items in data]
                for item in readData:
                    if item[0] == operation:
                        if (checkUser(user, item[1]) and checkObject(obj, item[2])):
                            print("Success")
                        else:
                            print("Error: access denied")
        else:
            print("Error: access denied")

"""
    Checking for user exists in domain
"""
def checkUser(user, domain):
    domainName = domain + ".txt"
    with open (domainName, 'r') as file:
        data = file.readlines()
        readData = [items.strip() for items in data]
        if user in readData:
            return True
        else:
            return False

"""
    Checking for objectType with object
"""
def checkObject(obj, objectType):
    objectName = objectType + ".txt"
    with open (objectName, 'r') as file:
        data = file.readlines()
        readData = [items.strip() for items in data]
        if obj in readData:
            return True
        else:
            return False
    
if __name__ == "__main__":
    arguments()   # get the arguments 

    if len(args) == 0:
        print("no arguments given")
    else:
        if checkForKeyWord(args[0]):
            if args[0] == "Authenticate" and (len(args) > 1 and len(args) <= 3):      
                Authenticate(args[1], args[2])   
            elif args[0] == "SetDomain" and (len(args) >= 1 and len(args) <= 3):
                if len(args) < 3:
                    SetDomain(args[1], None)
                else:
                    SetDomain(args[1], args[2])
            elif args[0] == "DomainInfo" and len(args) <= 2:
                if len(args) <= 1:
                    DomainInfo(None)
                else:
                    DomainInfo(args[1])
            elif args[0] == "SetType" and (len(args) >= 1 and len(args) <= 3):
                if len(args) > 1 and len(args) <= 2:
                    SetType(args[1], None)
                elif len(args) >= 2 and len(args) <= 3:
                    SetType(args[1], args[2])
                else:
                    print("Failed: Object and Type not given")
            elif args[0] == "TypeInfo" and len(args) <= 2:
                if len(args) <= 1:
                    TypeInfo(None)
                else:
                    TypeInfo(args[1])
            elif args[0] == "AddAccess" and (len(args) >= 1 and len(args) <= 4):
                if len(args) == 1:
                    AddAccess(None, None, None)
                elif len(args) <= 2:
                    AddAccess(args[1], None, None)
                elif len(args) <= 3:
                    AddAccess(args[1], args[2], None)
                else:
                    AddAccess(args[1], args[2], args[3])
            elif args[0] == "CanAccess" and (len(args) >= 1 and len(args) <= 4):
                if len(args) == 1:
                    CanAccess(None, None, None)
                elif len(args) <= 2:
                    CanAccess(args[1], None, None)
                elif len(args) <= 3:
                    CanAccess(args[1], args[2], None)
                else:
                    CanAccess(args[1], args[2], args[3])
            else:
                if args[0] == "AddUser" and (len(args) >= 1 and len(args) <= 3):
                    if len(args) == 1:
                        print("Error: username missing")
                    elif userExists(args[1]):
                        print("Error: user exists")
                    else:
                        if len(args) <= 2:
                            if args[1]:
                                # print("One given")
                                tempDictForAppend.update({args[1]: ""})
                                AddUser(args[1], None)
                                print("Success")
                        elif len(args) <= 3:
                            if args[1] and args[2]:
                                # print("Both given")
                                tempDictForAppend.update({args[1]: args[2]})
                                AddUser(args[1], args[2])
                                print("Success")
        else:
            print("Invalid Arguments")
  