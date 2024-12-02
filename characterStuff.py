from colors import *
from diceRoller import *
world = {
    "name" : "Player",
    "loc" : "library",
    "max hp" : 100,
    "hp" : 100,
    "accuracy" : 0,
    "dexterity" : 0,
    "damage" : 0,
    "inv" : []
}

while True:
    world["hp"] -= world["damage"]
    if world["hp"] == 0:
        print(red + "Game Over" + reset)
        break
    if world["accuracy"] == 0:
        world["name"] = input("What would you like your name to be? \n")
        world["accuracy"] = dndRoll("3d6")
        world["dexterity"] = dndRoll("3d6")
    if world["loc"] == "library":
        fD = input("You wake up from your boring library job\n\nEverything is dusty and there are only three bookshelves\nYou notice 2 doors 1 to your left and right\n\nWhich door would you like to go through\n")
        fD = fD.lower().strip()
        if fD == "left":
            world["loc"] = "graveyard"
            print("You see a rumbling from the ground")
            if "B.F.G" in world["inv"]:
                pass
            continue
        if fD == "right":
            world["loc"] = "Closet"
            if "B.F.G" not in world["inv"]:
                print("You enter the janitor's closet and find a gun labeled the B.F.G\nYou pick it up")
                world["inv"].append("B.F.G")
            else:
                print("It's just a Janitor's Closet")
            continue
    break
print(world["inv"])

