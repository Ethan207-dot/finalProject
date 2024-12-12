from colors import *
from diceRoller import *
from characterStuff import *
from testingFile import *
def main():
    world = readMem()
    win = ""
    characterStuff(world)
    print(world)
    while True:
        if world["loc"] == "library":
            library(world)
            continue
        if world["loc"] == "graveyard":
            graveyard(world)
            continue
        if world["loc"] == "closet":
            closet(world)
            continue
        if win == "win":
            print(f"Congratulations you have stopped the zombie apocalypse. {color("green", "You Win")}")
            break


main()