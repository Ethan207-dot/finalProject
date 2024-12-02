from colors import *
from diceRoller import *
from characterStuff import *
def main():
    uI = input("How many dice and sides to those dice do you want to roll? ")
    uI = uI.lower().strip()
    x = dndRoll(uI)
    print(x)

main()