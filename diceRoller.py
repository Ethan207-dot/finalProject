from random import *
def dndRoll(stringRoll):
    finalRolls = []
    rollList = stringRoll.split("d")
    if len(rollList) != 2:
        print("Input needs to be in the format number of die, d, number of sides on the die")
        return finalRolls
    
    try:
        numOfDice = int(rollList[0])
        numOfSides = int(rollList[1])
    except:
        return finalRolls
    
    for i in range(numOfDice):
        randnum = randint(1, numOfSides)
        finalRolls.append(randnum)
    
    return finalRolls