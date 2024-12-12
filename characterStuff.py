from colors import *
from diceRoller import *
from testingFile import *
from memory import *
def accuracy(stringRoll):
    accRoll = dndRoll(stringRoll)
    accRoll.sort()
    accRoll.pop(0)
    accRoll = sum(accRoll)
    return accRoll
def dexterity(stringRoll):
    dexRoll = dndRoll(stringRoll)
    dexRoll.sort()
    dexRoll.pop(0)
    dexRoll = sum(dexRoll)
    return dexRoll
def characterStuff(world):
    while True:
        world["hp"] -= world["damage"]
        if world["hp"] == 0:
            print(color("red","Game Over"))
            break
        if world["accuracy"] == 0:
            world["name"] = input("What would you like your name to be? \n")
            if len(world["name"]) == 0:
                print("Your name must at least be a character\n")
                continue
            world["accuracy"] = accuracy("4d6")
            world["dexterity"] = dexterity("4d6")
    return world

def story(world):
    while True:
        if world["loc"] == "library" and world["hp"] == 100:
            print(world)
            try:
                writeMem(world)
            except:
                pass
            fD = input("You are in the Library that you work at\n\nEverything is dusty and there are only three bookshelves\nYou notice 2 doors 1 to your left and right\n\nWhich door would you like to go through\n")
            fD = fD.lower().strip()
        if fD == "left" or world["loc"] == "graveyard":
            print(world)
            world["loc"] = "graveyard"
            print("You see a rumbling from the ground")
            if "B.F.G" in world["inv"]:
                print("You shoot the ground until it is no longer recognizable as a Graveyard")
                print(f"Congratulations you have stopped the zombie apocalypse. {color("green", "You Win")}")
                break
            if "B.F.G" not in world["inv"]:
                dexRoll = sum(dndRoll("1d20"))
                if world["dexterity"] < 10:
                    dexRoll -= 3
                if dexRoll[0] < 10:
                    print("Zombies rise from the ground as you slip and fall")
                    print(color("red","Game Over"))
                    break
                if dexRoll[0] < 15:
                    print("The Zombie Scratches you as you make your way into the library")
                    world["damage"] += sum(dndRoll("2d6"))+1
                    world["loc"] = "library"
                    continue
        if fD == "right" or world["loc"] == "Closet":
            world["loc"] = "Closet"
            print(world)
            if "B.F.G" not in world["inv"]:
                print("You enter the janitor's closet and find a gun labeled the B.F.G\nYou pick it up")
                world["inv"].insert(0,"B.F.G")
                world["loc"] = "library"
                continue
            else:
                print("It's just a Janitor's Closet. However, there is an awfully strange dent in the floor.")
                world["loc"] = "library"
            continue
        else:
            print("\nYour only options are left or right pick one\n")
            continue
    if world["loc"] == "library" and world["hp"] < 100:
        print("You hear a banging on the door that leads to the graveyard")
        fD = input("The front door to the library is in front of you and the Doors to your left and right are still there\nWhat would you like to do? \n Wait\nRight\nLeft\nExit through the front door\n")
    writeMem(world)
    return world
