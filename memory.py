from characterStuff import world
def readMem():
    f = open("worldMemory.txt", "r")
    fcon = f.read()
    fline = fcon.split("\n")
    worldmem = {
        "name" : "string",
        "loc" : "string",
        "max hp" : 0,
        "hp" : 0,
        "accuracy" : 0,
        "dexterity" : 0,
        "damage" : 0,
        "inv" : []
        }
    worldmem["name"] = fline[0]
    worldmem["loc"] = fline[1]
    worldmem["max hp"] = int(fline[2])
    worldmem["hp"] = int(fline[3])
    worldmem["accuracy"] = int(fline[4])
    worldmem["dexterity"] = int(fline[5])
    worldmem["damage"] = int(fline[6])
    worldmem["inv"].append(fline[7])
    f.close()
    return worldmem

def writeMem():
    f = open("worldMemory.txt", "r")
    fcon = f.read()
    fline = fcon.split("\n")
    f.close
    f = open("worldMemory.txt", "w")
    l = [world["name"]+"\n", world["loc"]+"\n", world["max hp"]+"\n", \
    world["hp"]+"\n", world["accuracy"]+"\n", world["dexterity"]+"\n", \
    world["damage"]+"\n", world["inv"]+"\n"]
    for line in range (len(l)):
        f.writelines(l[line])
    f.close

def createWorld(worldmem):
    world = {}
    world["name"] = worldmem["name"]

print(readMem())
print("---------------------------------")
print(writeMem())