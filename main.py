from colors import *
from diceRoller import *
from characterStuff import *
from testingFile import *
# This file has the main in it and in the main function every location function along with functions that end the game by telling the 
# player if they win or lose and break

# Runs the game is given nothing and does not return anything
def main():
    world = readMem()
    while True:
        try:
            writeMem(world)
        except:
            pass
        characterStuff(world)
        print(f"\n{world}\n")
        if world["loc"] == "library":
            library(world)
            continue
        if world["loc"] == "graveyard":
            graveyard(world)
            continue
        if world["loc"] == "closet":
            closet(world)
            continue
        if world["loc"] == "entrance":
            entrance(world)
            continue
        if world["loc"] == "win":
            if world["hp"] == 100 or "B.F.G" in world["inv"]:
                print(f"\nCongratulations you have stopped the zombie apocalypse. {color("green", "You Win")}\n")
            if world["hp"] < 100 and "B.F.G" not in world["inv"]:
                print(f"You have survived the starting and the ending of a zombie apocalypse {color("green", "You Win")}")
            break
        if world["loc"] == "lose":
            print(color("red", "Game Over"))
            break
main()