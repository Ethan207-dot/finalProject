from colors import *
from diceRoller import *
from testingFile import *
from memory import *
def characterStuff():
    world = readMem()
    while True:
        world["hp"] -= world["damage"]
        if world["hp"] == 0:
            print(red + "Game Over" + reset)
            break
        if world["accuracy"] == 0:
            print(world) #test print statement
            world["name"] = input("What would you like your name to be? \n")
            if len(world["name"]) == 0:
                print("Your name must at least be a character\n")
                continue
            world["accuracy"] = accuracy("4d6")
            world["dexterity"] = dexterity("4d6")
            print(world)
        if world["loc"] == "library":
            fD = input("You are in the Library that you work at\n\nEverything is dusty and there are only three bookshelves\nYou notice 2 doors 1 to your left and right\n\nWhich door would you like to go through\n")
            fD = fD.lower().strip()
        if fD == "left":
            world["loc"] = "graveyard"
            print("You see a rumbling from the ground")
            if "B.F.G" in world["inv"]:
                print("You shoot the ground until it is no longer recognisbale as a Graveyard")
                print(f"Congratulations you have stopped the zombie apocalypse. {green} You Win {reset}")
                break
            if "B.F.G" not in world["inv"]:
                print("Zombies rise from the ground as you realise you forgot that the doors are always locked")
                print(red + "Game Over" + reset)
                break
        if fD == "right":
            world["loc"] = "Closet"
            if "B.F.G" not in world["inv"]:
                print("You enter the janitor's closet and find a gun labeled the B.F.G\nYou pick it up")
                world["inv"].insert(0,"B.F.G")
                world["loc"] = "library"
                print(world) #test print statement
                continue
            else:
                print("It's just a Janitor's Closet. However, there is an awfully strange dent in the floor.")
                world["loc"] = "library"
            continue
        else:
            print("\nYour only options are left or right pick one\n")
            continue
    writeMem(world)
    return world
