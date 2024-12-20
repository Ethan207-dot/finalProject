from diceRoller import *
from memory import *
# This file has all the location functions used in the main function

# Holds every action the player can make in the library and all the content in the library like descriptions of the library 
# that take place in the library it takes the world dictionary and returns nothing
def library(world):
    if world["hp"] == 100:
        fD = input("You are in the Library that you work at\n\nEverything is dusty and there are only three bookshelves\nYou notice 2 doors 1 to your left and right\n\nWhich door would you like to go through\n")
        fD = fD.lower().strip()
    elif world["hp"] < 100:
        print("\nYou see the front door cracked a bit\n")
        fD = input("\nYou are in the Library that you work at\n\nEverything is dusty and there are only three bookshelves\nYou notice 3 doors 1 to your left, right, and the entrance\n\nWhich door would you like to go through\n")
        fD = fD.lower().strip()
    if fD == "right":
        world["loc"] = "closet"
    elif fD == "left":
        world["loc"] = "graveyard"
    elif fD == "entrance":
        world["loc"] = "entrance"
    elif fD != "right" and fD != "left" and world["hp"] == 100:
        print("\nYour only options are left or right pick one\n")
    else:
        print("\nYour only options are left, right, and the entrance pick one\n")
    return
# Holds every action the player can make in the graveyard and all the content related to the location of the graveyard 
# that occurs in the graveyardit takes the world and returns nothing
def graveyard(world):
    print("\nYou see a rumbling from the ground\n")
    if "B.F.G" in world["inv"]:
        fD = input("\nWould you like to shoot?\n")
        fD = fD.lower().strip()
        if fD != "yes" and fD != "no":
            print("\nIt's either yes or no\n")
            return
        if fD == "yes":
            print("\nYou shoot the ground until it is no longer recognizable as a Graveyard\n")
            world["loc"] = "win"
            return
        if fD == "no":
            pass
    if "B.F.G" not in world["inv"] or fD == "no":
        fD = input("\nWould you like to run?\n")
        fD = fD.lower().strip()
        if fD != "yes" and fD != "no":
            print("\nIt's either yes or no\n")
            return        
        if fD == "yes":
            dexRoll = sum(dndRoll("1d20"))
            if world["dexterity"] < 10:
                dexRoll -= 3
            if dexRoll < 10:
                print("\nZombies rise from the ground as you slip and fall\n")
                world["loc"] = "lose"
                world["hp"] = 0
                return
            if dexRoll < 15:
                print("\nThe Zombie Scratches you as you make your way into the library\n")
                world["damage"] += sum(dndRoll("2d6"))+1
                world["loc"] = "library"
                return
            else: 
                print("\nYou escaped to the library\n")
                world["loc"] = "library"
        if fD == "no":
            print("\nYou wait as you see the zombies rise from the ground and eat you\n")
            world["loc"] = "lose"
            return
#Holds every the player can make in the closet along with all the content related to the location of the closet that 
# happens in the closet. it takes the world and returns nothing
def closet(world):
    while True:
        if "B.F.G" not in world["inv"]:
            fD = input("\nYou enter the janitor's closet and find a gun labeled the B.F.G.\nWould you like to pick it up?\n")
            fD = fD.lower().strip()
            if fD != "yes" and fD != "no":
                print("\nIt's either yes or no\n")
                return
            if fD == "yes":
                print("\nYou pick it up\n")
                world["inv"].insert(0,"B.F.G")
                world["loc"] = "library"
                return
            if fD == "no":
                fD = input("\nWould you like to leave the closet?\n")
                fD = fD.lower().strip()
                if fD != "yes" and fD != "no":
                    print("\nIt's either yes or no\n")
                    return
                if fD == "yes":
                    print("\nYou Leave\n")
                    world["loc"] = "library"
                    print(world["loc"])
                    return
                if fD == "no":
                    continue
        else:
            print("\nIt's just a Janitor's Closet. However, there is an awfully strange dent in the floor.\n")
            world["loc"] = "library"
            return
#Holds every the player can make in the entrance along with all the content related to the location of the entrance that takes place in 
# the entrance it takes the world and returns nothing
def entrance(world):
    fD = input("You see the army has arrrived as you go out the entrance\nA person who introduces himself as Major Lieutenant tells you to get behind cover\nWould you like to go behind cover?\n")
    fD = fD.lower().strip()
    if fD != "yes" and fD != "no":
        print("\nIt's either yes or no\n")
        return
    if fD == "yes":
        world["loc"] = "win"
        return
    if fD == "no":
        fD = input("\nWould you like to reason with the army to save the building?\n")
        fD = fD.lower().strip()
        if fD != "yes" and fD != "no":
            print("\nIt's either yes or no\n")
            return
        if fD == "yes":
            print("\nThe army instead rushes the building and shoots the zombies\n")
            world["loc"] = "win"
        if fD == "no":
            print("\nThe army blows the library sky high with you in front of it\n")
            world["loc"] = "lose"
        return