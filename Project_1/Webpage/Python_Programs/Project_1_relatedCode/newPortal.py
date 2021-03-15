import sys
import json
import os.path


args = []
users_Data = {}


def arguments():
    for arg in sys.argv[1:]:
        args.append(arg)


# addUser 
def AddUser(user, password):
    
    users_Data.update({user: password})
   
    
    with open("userInfo.json", "r+") as f:
        if os.path.getsize("userInfo.json") <= 2 :
             json.dump(users_Data, f)
        else: 
            temp_dict = json.load(f)
            temp_dict.update(users_Data)
            f.seek(0)
            json.dump(temp_dict, f)
           
        
    



# helper function for checking if the user exists 

def checkUser_exists(userName):
    #if file doesn't exixts create one
    if not os.path.isfile('userInfo.json'):
        with open ('userInfo.json', 'w') as json_file:
            json.dump({},json_file)
            json_file.close
        return False
    else:
        with open ('userInfo.json', 'r') as json_file:
            data = json.load(json_file)
            for user_id in data.keys():
                if userName == user_id:
                    return True
                else:
                    return False
        
    

    
def Authenticate(userName, password):
 
    if checkUser_exists(userName):
        with open ('userInfo.json', 'r') as json_file:
            data = json.load(json_file)
            for user_id, user_password in data.items():
                if userName == user_id and password == user_password:
                   print("Success")
                elif userName == user_id and not (password == user_password):
                    print("Error: Bad Password")
    else:
        print("No such User")

def SetDomain(userName, domain):
    if domain == None:
        print("Error: Missing Domain")
    elif not checkUser_exists(userName):
        print("Error: No Such User")
    else:
        domain_name = domain + ".txt"
        if not os.path.isfile(domain_name):
            with open (domain_name, 'w') as txt_file:
                txt_file.write(userName + "\n")
        else: 
            with open (domain_name, 'r+') as txt_file:
                data = txt_file.readlines()
                new_data = [items.strip() for items in data]
                if not userName in new_data:
                    txt_file.write(userName + "\n")


def DomainInfo(domain_name):
    if domain_name == None :
        print("Error: Missing domain")
    else:
        domain = domain_name + ".txt"
        if os.path.isfile(domain):
            with open (domain, 'r') as txt_file:
                data = txt_file.readlines()
                new_data = [items.strip() for items in data]
                if len(new_data) > 0:
                    for items in new_data:
                        print(items)


def SetType(obj, type_name):
    if obj == None or type_name == None:
        print("Failed:")
        print("syntax: SetType object type_name")
    else:
        obj_type = type_name + '.txt'
        if not os.path.isfile(obj_type):
            with open (obj_type, 'w') as txt_file:
                txt_file.write(obj + "\n")
                print("Success")
        else:
            with open (obj_type, 'r+') as txt_file:
                data = txt_file.readlines()
                new_data = [items.strip() for items in data]
                if not obj in new_data:
                    txt_file.write(obj + "\n")




def TypeInfo(type_name):
    if type_name == None :
        print("Error: Missing type")
    else:
        obj_type = type_name + ".txt"
        if os.path.isfile(obj_type):
            with open (obj_type, 'r') as txt_file:
                data = txt_file.readlines()
                new_data = [items.strip() for items in data]
                if len(new_data) > 0:
                    for items in new_data:
                        print(items)


def AddAccess(operation, domain_name, type_name):
    if operation == None:
        print("Error: Missing operation")
    elif domain_name == None:
        print("Error: Missing domain")
    elif type_name == None:
        print("Error: Missing type")
    else:
        if not os.path.isfile(domain_name + ".txt"):
            with open (domain_name + ".txt", 'w') as txt_file:
                txt_file.write()
        if not os.path.isfile(type_name + ".txt"):
            with open (type_name + ".txt", 'w') as txt_file:
                txt_file.write()
        if not os.path.isfile("operationList.txt"):
            with open ("operationList.txt", 'w') as txt_file:
                txt_file.write(operation + ',' + domain_name + ',' + type_name + '\n')
        else:
             with open ("operationList.txt", 'a+') as txt_file:
                txt_file.write(operation + ',' + domain_name + ',' + type_name + '\n')
    

def CanAccess(operation, user, obj):
    if operation == None:
        print("Error: Missing operation")
    if user == None:
        print("Error: Missing User")
    elif not checkUser_exists(user):
            print("Error: User doesn't exists.")
    elif obj == None:
        print("Error: Missing type")
    else:
        with open('operationList.txt', 'r') as txt_file:
            data = txt_file.readlines()
            new_data = [items.strip().split(',') for items in data]
            for item in new_data:
                if item[0] == operation:
                    if (check_user(user, item[1]) and check_obj(obj, item[2])):
                        print("Success")
                    else:
                        print("Error: Access Denied")



#check if the user in domain
def check_user(user, domain):
    domain_name = domain + ".txt"
    with open (domain_name, 'r') as txt_file:
        data = txt_file.readlines()
        new_data = [items.strip() for items in data]
        if user in new_data:
            return True
        else:
            return False


#check if object exists in object Type
def check_obj(obj, obj_type):
    obj_name = obj_type + ".txt"
    with open (obj_name, 'r') as txt_file:
        data = txt_file.readlines()
        new_data = [items.strip() for items in data]
        if obj in new_data:
            return True
        else:
            return False



def helper_function(key_arg):
    keywords = ["AddUser", 'Authenticate', 'SetDomain', 'DomainInfo', 'SetType', 'TypeInfo']
    keywords1 = ['AddAccess', 'CanAccess']
    if key_arg in keywords:
        print("Syntax:  " + "{} argument1 argument2".format(key_arg))
    if key_arg in keywords1:
        print("Syntax:  " + "{} argument1 argument2 argument3".format(key_arg))
    
    



# hold all your keywords in a list and compare during the CLI input



      

        
if __name__ == "__main__":

    arguments()
 
    '''Make sure no more than 2 arguments are given 
    if no argument for password field is provided defult is set to password'''
    
    
    # Success
    # Error: User exists
    # Error: username missing 
    
    if len(args) == 0:
        print("Missing arguments")
    elif args[0] == "CanAccess" and len(args) in range (1,5):
        if len(args) <= 1:
            CanAccess(None, None, None)
        if len(args) == 2:
            CanAccess(args[1], None, None)
        if len(args) == 3:
            CanAccess(args[1], args[2], None)
        if len(args) == 4:
            CanAccess(args[1], args[2], args[3])

    elif args[0] == "AddAccess" and len(args) in range(1,5):
        if len(args) <= 1:
            AddAccess(None, None, None)
        if len(args) == 2:
            AddAccess(args[1], None, None)
        if len(args) == 3:
            AddAccess(args[1], args[2], None)
        if len(args) == 4:
            AddAccess(args[1], args[2], args[3])
    elif args[0] == "TypeInfo" and len(args) <= 2:
        if len(args) <= 1:
            TypeInfo(None)
        else:
             TypeInfo(args[1])
    elif args[0] == "SetType" and len(args) in range(2,4):
        if  len(args) < 3:
            SetType(args[1], None)
        else:
            SetType(args[1], args[2])
    elif args[0] == "DomainInfo" and len(args) <= 2:
        if len(args) <= 1:
            DomainInfo(None)
        else:
             DomainInfo(args[1])
    elif args[0] == "Authenticate" and len(args) in range(2,4):
        Authenticate(args[1], args[2])
    elif args[0] == "SetDomain" and len(args) in range(2,4):
        if len(args) < 3:
            SetDomain(args[1], None)
        else:
            SetDomain(args[1], args[2])
    else:
        if args[0] == "AddUser" and len(args) in range(2,4):
            if (checkUser_exists(args[1]) is False):
                if len(args) < 3:
                    AddUser(args[1], "password")
                    print("Success, defult password has been set")
                else:
                    AddUser(args[1], args[2])
                    print("Success")
            else:
                print("Error: User Already Exists")
        else:
            print("Error:")
            #print("Syntax: AddUser UserName Password")
            helper_function(args[0])
   