from diceRoller import *
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

print(accuracy("4d6"))
print(dexterity("4d6"))