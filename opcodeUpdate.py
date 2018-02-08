# assemble project Started
import os
opcode = {}
with open("opcode.txt") as f:
    for line in f:
        line = line.split()
        opcode[line[0]] = (line[1],line[2])

os.remove("opcode.txt")

def error(msg):
    print (msg)
    exit()

print ("MENU")
print ("1. ADD")
print ("2. UPDATE")
print ("3. SEARCH")
print ("4. DELETE")

n = int(input())

if(n == 1):
    str = input("Enter the string\n")
    if(str in opcode.keys()):
        error("String already exist")
    else:
        add = input("Enter address\n")
        for key in opcode.keys():
            if(add == opcode[key][0]):
                error("address already in use")
        p = input("Enter number of oprand\n")
        # add into file
        opcode[str] = (add,p)

elif( n == 2):
    str = input("Enter the string\n")
    if(str in opcode.keys()):
        add = input("Enter address\n")
        for key in opcode.keys():
            if(add == opcode[key][0] and str != opcode[key]):
                error("address already in use by other string")
        p = input("Enter number of oprand\n")
        opcode[str] = (add,p)
    else:
        error("No string Found")

elif( n == 3):
    str = input("Enter the string\n")
    if(str in opcode.keys()):
        print ("String exist")
    else:
        print ("String does not exist")

elif (n == 4):
    str = input("Enter the string\n")
    if(str in opcode.keys()):
        del opcode[str]
    else:
        print ("String does not exist")

with open("opcode.txt" , 'a') as f:
    for key in opcode.keys():
        f.write(key+' ' + opcode[key][0] + ' ' + opcode[key][1]+'\n')
