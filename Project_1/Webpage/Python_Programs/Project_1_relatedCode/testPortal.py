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



# import optparse

# parser = optparse.OptionParser()

# parser.add_option("")

# import optparse
import sys   
import json
import os.path

# Storage
usersAndPasswords = {}
args = []
operation = []
domain = []
objectName = []
objectType = []
keyWords = ["AddUser", "Authenticate", "SetDomain", "DomainInfo", "SetType", "TypeInfo", "AddAccess", "CanAccess"]

def get_arguments(): 
    for arg in sys.argv[1:]:
        args.append(arg)
    
def AddUser(user, password):    
    # before submitting to file, CHECK
    checkIfTheUserExists = userExists(user)
    # print("Hello")
    if user == checkIfTheUserExists:
        print("Error: user exists")
    else:
        # create a dictionary 
        usersAndPasswords.update({user: password})
        # UAP = users and passwords
        UAP = json.dumps(usersAndPasswords)
        with open("userFile.json", "a+") as f:
            f.write(UAP)
            f.close()
        
    # usersInfo = json.load(open("userFile.json"))
    # print(usersInfo)

def checkIfFileExists():
    pass

def checkForKeyWord(key):
    keyExists = True
    for k in keyWords:
        if key == k:
            return keyExists
    return False

# Helper function
def userExists(username):
    # get the usernames from the file
    user = ""
    # print(usersAndPasswords)s
    if os.path.isfile("userFile.json") is False:
        with open("userFile.json", "w") as file:
            json.dump({}.file)
            file.close
        return False
    else:
        data = json.load(open("userFile.json"))
        for keys in usersAndPasswords.keys():
            # print("Hello2")
            if username == keys:
                user = username
    return user


def Authenticate():
    pass

def SetDomain():
    pass

def DomainInfo():
    pass

def SetType():
    pass

def TypeInfo():
    pass

def AddAccess():
    pass

def CanAccess():
    pass



if __name__ == "__main__":
    get_arguments()
    i = 1
    print("========================")
    print("Arguments input: {}".format(len(args)))
    for st in args:
        print("{}".format(st))
    print("========================")
    
    if len(args) == 0:
        print("Missing arguments!")
    else:
        # check if the key word AddUser exists for the purpose of this program
        if checkForKeyWord(args[0]):
            if args[0] == "AddUser" and len(args) == 3:
                # create the file even if the user doesnt input a username and password
                # open(userFile, 'w').close()
                # user = userExists(args[1])
                # if args[1] == user: # get the user name for checking 
                #     print("Error: user exists")
                AddUser(args[i], args[i+1])
                print("Success")
            else:
                if len(args) == 2:
                    # open(userFile, 'w').close()
                    # user = userExists(args[1])
                    # if args[1] == user: # get the user name for checking 
                    #     print("Error: user exists")
                    noPassGivenAtThisPoint = ""
                    AddUser(args[i], noPassGivenAtThisPoint)
                    print("Success without password")
                else:
                    print("Error: username missing")
                    


   
            
                
    # else:
    #     print("Error: username missing")
            
            
            
            
            
            
            
        #     print("Error: username missing")
        # else:
        #     print("{}, this key is not supported. ".format(args[0]))
        
            
            
            
            
            
            
    # else: 
    #     if checkForKeyWord(args[0]):
    #         if len(args) == 3:
    #             AddUser(args[i], args[i+1])
    #             print("Success")
    #         if len(args) <= 2:
    #             if args[0] == "AddUser":
    #                 user = userExists(args[1]) # get the user name for checking 
    #                 if args[1] == user:
    #                     print("Error: user exists")
    #                     exit(1)
    #                 if args[1] == "":
    #                     print("Error: username missing")
    #                     exit(1)
    #                 else:
    #                     if len(args) < 3:
    #                         pass
    #                     else: 
    #                         AddUser(args[i], args[i+1])
    #                         print("Success")
    #         else:
    #             print("Error: username missing")
    #     else:
    #         print("{}, this key is not supported. ".format(args[0]))
    # elif args[0] == "Authenticate":
    #     pass
    # elif args[0] == "SetDomain":
    #     pass
    # elif args[0] == "DomainInfo":
    #     pass
    # elif args[0] == "SetType":
    #     pass
    # elif args[0] == "TypeInfo":
    #     pass
    # elif args[0] == "AddAccess":
    #     pass
    # elif args[0] == "CanAccess":
    #     pass

    # for users, password in usersAndPasswords.items():
    #     print(users)
    #     print(password)
    
    # usersInfo = json.load(open("userFile.json"))
    # print(usersInfo)







# this did not work for my purpose 
# def get_arguments():
#     # keyword, user, password
#     parser = optparse.OptionParser()
#     parser.add_option("-a", "AddUser", dest="AddUser", help="Adding User if the user do not exist")
#     parser.add_option("-u", "user", dest="newUser", help="New User")
#     parser.add_option("-p", "password", dest="newPassword", help="Assign password")
#     (options, arguments) = parser.parse_args()
#     if options.addUser:
#         parser.error("[-] Please specify a keyWord, use -h, --help for more info")
#     elif options.newUser:
#         parser.error("[-] The username cannot be an empty string, use -h, --help for more info")
#     # elif options.password:
#     #     parser.error("[-] Please ")
#     return options 