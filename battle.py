from random import *
from diceRoller import *
from characterStuff import *
from memory import *

def turn(attacker, defender, who):
    if who == "player":
        print("Pick an option : ")
        print("1: Attack")
        print("2: Do Nothing")
        decision = input() # Validate their input
    else:
        if (randint(1,2) == 1):
            decision = "1"
        else:
            decision = "2"
    if decision == "1":
        defender["hp"] -= attacker["strength"]
        print(f"{attacker["name"]} hits {defender["name"]} for {attacker["strength"]}")
    
    if decision == "2":
        heal = sum(dndRoll("1d4"))
        attacker["hp"] += heal
        print(f"{attacker["name"]} rests and recovers {heal}")



def battle(player, enemy):
    world = readMem
    world["name"]
    world["hp"]
    world["strength"] = dndRoll("3d6")

    enemy = {
        "name" : "diggle",
        "hp" : 20,
        "strength" : dndRoll("3d6")
    }
    print(f"A {enemy["name"]} approaches {world["name"]}. Get ready!!!!!")

    while True:
        turn(player, enemy, "player")
        turn(enemy, player, "enemy")
        print(f"{player["name"]} has {player["hp"]} hp left")
        print(f"{enemy["name"]} has {enemy["hp"]} hp left")
        if (player["hp"] <= 0):
            return "player dead"
        if (enemy["hp"] <= 0):
            return "enemy dead"
