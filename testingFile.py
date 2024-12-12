from diceRoller import *
from memory import *
def library(world):
    print(world)
    try:
        writeMem(world)
    except:
        pass
    fD = input("You are in the Library that you work at\n\nEverything is dusty and there are only three bookshelves\nYou notice 2 doors 1 to your left and right\n\nWhich door would you like to go through\n")
    if fD == "right":
        world["loc"] = "Closet"
    if fD == "left":
        world["loc"] = "graveyard"
    else:
        print("\nYour only options are left or right pick one\n")
    return

def graveyard(world):
    print("You see a rumbling from the ground")
    if "B.F.G" in world["inv"]:
        print("You shoot the ground until it is no longer recognizable as a Graveyard")
        win = "win"
        return
    if "B.F.G" not in world["inv"]:
        dexRoll = sum(dndRoll("1d20"))
        if world["dexterity"] < 10:
            dexRoll -= 3
        if dexRoll < 10:
            print("Zombies rise from the ground as you slip and fall")
            world["hp"] = 0
            return
        if dexRoll < 15:
            print("The Zombie Scratches you as you make your way into the library")
            world["damage"] += sum(dndRoll("2d6"))+1
            world["loc"] = "library"
            return

def closet(world):
    if "B.F.G" not in world["inv"]:
        print("You enter the janitor's closet and find a gun labeled the B.F.G\nYou pick it up")
        world["inv"].insert(0,"B.F.G")
        world["loc"] = "library"
        return
    else:
        print("It's just a Janitor's Closet. However, there is an awfully strange dent in the floor.")
        world["loc"] = "library"
        return