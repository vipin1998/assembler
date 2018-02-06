# assemble project Started

opcode = {}
pseudo = []

symbol = {}
icf = []


with open("opcode.txt") as f:
    for line in f:
        line = line.split()
        opcode[line[0]] = (line[1],line[2])

with open("pseudo.txt") as f:
    for line in f:
        line = line.split()
        pseudo.append(line[0])

locationCounter = 1000

def error(msg):
    print (msg)
    exit()

def opcodeLine(list):
    total_operand = len(list) - 1;
    if(int(opcode[list[0]][1]) != total_operand ):
        error("Invalid No of arguments")
    else:
        icf.append(opcode[list[0]][0])
        for i in range (1,total_operand+1):
            icf.append(list[i])
            if not list[i].startswith('R'):
                if list[i] not in symbol.keys():
                    symbol[list[i]] = -1
        return len(list)
        
def pseudoLine(list,locationCounter):
    if(list[0] == "BYTE"):
        if(len(list) == 3):
            symbol[list[1]] = locationCounter;
            icf.append(list[2])
        else:
            error("Invalid oprand in BYTE")
    elif(list[0] == "RESB"):
        if(len(list) == 2):
            symbol[list[1]] = locationCounter;
            icf.append(0)
        else:
            error("Invalid oprand in RESB")
    return 1


def labelLine(list,locationCounter):
    if list[0] in symbol.keys():
        error("lebel allready exist")
    else:
        symbol[list[0]] = locationCounter;
        list.pop(0)
        return processLine(list,locationCounter)

def processLine(list,locationCounter):
    if(list[0] in pseudo):
        return pseudoLine(list,locationCounter)
    elif (list[0] in opcode.keys()):
        return opcodeLine(list)
    else:
        if(list[0].endswith(':')):
            return labelLine(list,locationCounter)
        else:
            error("Syntax error near " + list[0])
            
with open("input.txt") as f:
    firstLine = False
    end = False
    for line in f:
        line = line.split()
        if(firstLine == False):
            if(line[0] == "START"):
                if(len(line) == 2):
                    locationCounter = int(line[1])
                firstLine = True
            else:
                error("First Line Should be start")
        elif(end == True):
            error("Nothing Come after the end");
        elif(firstLine == True and end == False):
            if(line[0] == "END"):
                end = True
            else: 
                locationCounter = locationCounter + processLine(line,locationCounter)
    if (firstLine == False):
        error("First Line Should be START")
    if (end == False):
        error("Last Line Should be END")

        
for key in symbol.keys():
    if(int(symbol[key]) == -1):
        error(key + " Not Found")

print (symbol)
