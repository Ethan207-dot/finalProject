from colors import *
from diceRoller import *
from characterStuff import *
from testingFile import *
def main():
    world = readMem()
    while True:
        characterStuff(world)
        if world["loc"] == library:
            library(world)
            continue


main()