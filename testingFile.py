from diceRoller import *
from memory import *

def library(world):
    print(world)
    try:
        writeMem(world)
    except:
        pass
    fD = input("You are in the Library that you work at\n\nEverything is dusty and there are only three bookshelves\nYou notice 2 doors 1 to your left and right\n\nWhich door would you like to go through\n")
    return fD