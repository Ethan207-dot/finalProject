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
    world["hp"] = world["max hp"] - world["damage"]
    if world["hp"] <= 0:
        world["loc"] = "lose"
    if world["accuracy"] == 0:
        world["name"] = input("What would you like your name to be? \n")
        if len(world["name"]) == 0:
            print("Your name must at least be a character\n")
        world["accuracy"] = accuracy("4d6")
        world["dexterity"] = dexterity("4d6")
    return world