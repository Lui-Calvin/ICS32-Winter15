from pathlib import Path
from pathlib import PurePath
def __main__():
    while True:
        Pname = Path(input())
        #print(Pname)
        if Pname.exists():
            interestingList = secondLine(Pname)
            print(interestingList)
            #action = input("what would you like to do with file?")
            #if action == "F":
                #read(interestingList)
            
        else:
            print("ERROR")
def searchNames(P:Path,key:str)->'list of Path':
    pathList =[]
    for file in P.iterdir():
        #print(file.name.split(".")[0])
        if file.is_dir():
            pathList.extend(searchNames(file,key))
        elif key == file.name.split(".")[0]:
            pathList.append(file)
        
    return pathList
            
def searchExtensions(P:Path,key:str)->'list of Path':
    pathList = []
    for file in P.iterdir():
        if file.is_dir():
            pathList.extend(searchExtensions(file,key))
        elif file.name[-len(key):] == key:
            pathList.append(file)
    return pathList

def searchSize(P:Path, size:int)->'list of Path':
    pathList = []
    for file in P.iterdir():
        if file.is_dir():
            pathList.extend(searchSize(file,size))
        elif file.stat().st_size > size:
            pathList.append(file)
            print(file.name +":  " + str(file.stat().st_size) + " bytes")
    return pathList

def read(L:"list of Path"):
    for path in L:
        print(path.read_text())

def secondLine(P:Path)->'list of Path':
    
    while True:
        print("Hi")
        search = input("Write an action letter followed by file name")
        if search[0] == "N":
            return searchNames(P,search[2:])
            
        elif search[0] == "E":
            return searchExtensions(P,search[2:])
        elif search[0] == "S":
            try:
                return searchSize(P, int(search[2:]))
            except ValueError:
                print("Sorry that is not an integer")         
        else:
            print("ERROR")         

__main__()
