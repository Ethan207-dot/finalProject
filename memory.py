#This file contains any functions that are related to the function of the memory

# This function reads from a file processes the information and turns the information into the world dictionary and returns the world 
#dictionairy for use
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
    try:
        worldmem["inv"].append(fline[8])
    except:
        pass
    f.close()
    return worldmem
# This function takes the current state of the world and writes it to the same file that is read to make the dictionary and returns nothing
def writeMem(world):
    f = open("worldMemory.txt", "r")
    fcon = f.read()
    fline = fcon.split("\n")
    f.close()
    f = open("worldMemory.txt", "w")
    while "" in fline:
        fline.remove("")
    l = [world["name"]+"\n", world["loc"]+"\n", str(world["max hp"])+"\n", \
    str(world["hp"])+"\n",str(world["accuracy"])+"\n", str(world["dexterity"])+"\n", \
    str(world["damage"])+ "\n"]
    for i in range(len(world["inv"])):
        if i == len(l)-1:
            l.append(world["inv"][i])
        else:
            l.append(world["inv"][i] + "\n")
    for line in range (len(l)):
        f.writelines(l[line])
    f.close()