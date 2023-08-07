import fileinput
import collections
ligNames = dict()

def readLigandName(path: str):
    
    name = ""
    
    firstNameEntry = True
    for line in fileinput.input(path, inplace=True):
        lineOut = ""
        if not line:
            break
        if("Name = " in line):
            name = line.split("Name = ")[-1].replace("\n","")
            
            if name in ligNames.keys() and firstNameEntry:
                ligNames[str(name)] += 1
            elif(firstNameEntry):
                ligNames[str(name)] = 1
            firstNameEntry = False
            if(int(ligNames[str(name)]) > 1):
                lineOut = str(line).replace(str(name),str(name)+"-"+str(ligNames[str(name)]))
                print('{}'.format(lineOut), end='')
        if(lineOut == ""):
            print('{}'.format(line), end='')
            
file1 = open('results_list.txt', 'r')
count = 0
while True:
    count += 1

    line = file1.readline().replace("\n","")
    if not line:
        break

    if(readLigandName(line)):
        print("Line{}: {}".format(count, line.strip()))

od = collections.OrderedDict(sorted(ligNames.items()))
for key,value in od.items():
    if False:
        if value != 1:
            print(str(key)+" "+str(value))
        if("_" in key):
            print(str(key)+" "+str(value))
    print(str(key)+" "+str(value))
print(str(len(ligNames)))
noDuplicates = count-len(ligNames)-1
print("handled duplicates:", str(noDuplicates))


file1.close()