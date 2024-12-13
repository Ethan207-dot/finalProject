from colors import *
from diceRoller import *
from testingFile import *
from memory import *
#The file containes functions that set up character defining traits like stats and the name

# A function that takes a string roll creates a list of numbers sums them into one number to be assigned to a character and returns 
# the number asigned to the world
def accuracy(stringRoll):
    accRoll = dndRoll(stringRoll)
    accRoll.sort()
    accRoll.pop(0)
    accRoll = sum(accRoll)
    return accRoll
#A function that takes a string roll creates a list of numbers sums them into one number to be assigned to a character stat and returns 
# the number asigned to the world
def dexterity(stringRoll):
    dexRoll = dndRoll(stringRoll)
    dexRoll.sort()
    dexRoll.pop(0)
    dexRoll = sum(dexRoll)
    return dexRoll
# takes the world and checks if the player should be dead, and assigns stats and the name by asking the player what they want the name
#of the character to be and returns the world
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