from random import *
#This file has the dice rolling function that is used to set character stats and to check if the character is succesful depending on 
# how high they role in both character stuff and testing file

# a function that takes the stringroll and generates random amount of numbers and random numbers set within a range to simulate 
# rolling a x sided die x number of times and returns a list of numbers
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