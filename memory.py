def readMem():
    f = open("worldMemory.txt", "r")
    fcon = f.read()
    fline = fcon.split("\n")
    memWorld = {
        "name" : "string",
        "loc" : "string",
        "max hp" : 0,
        "hp" : 0,
        "accuracy" : 0,
        "dexterity" : 0,
        "damage" : 0,
        "inv" : []
        }
    memWorld["name"] = fline[0]
    memWorld["loc"] = fline[1]
    memWorld["max hp"] = int(fline[2])
    memWorld["hp"] = int(fline[3])
    memWorld["accuracy"] = int(fline[4])
    memWorld["dexterity"] = int(fline[5])
    memWorld["damage"] = int(fline[6])
    memWorld["inv"] = memWorld["inv"].append(fline[7])
    f.close()
    return memWorld
                
print(readMem())

def writeMem():
    f = open("worldMemory.txt", "w")
    f.write()