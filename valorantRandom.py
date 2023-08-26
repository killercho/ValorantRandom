import random
import argparse
from os import system, name

# Helper functions
def clear():
    # Clearing the screen

    # Clear for windows machines
    if name == 'nt':
        _ = system('cls')
    # Clear for linux machines
    else:
        _ = system('clear')

def getRandomPistol(current):
    # Returns 2 values for a pistol name and its price depending on the money entered.
    # 0 - 3000 : could be Sheriff and Ghost 
    # 3000 - 5000 : could be Frenzy, Shorty, Classic and None
    # 5000 - 9000 : could be Shorty, Classic or None

    def filterUnwanted(pair):
        _, value = pair
        if 0 <= current <= 3000:
            if value < 500:
                return False
            else:
                return True
        if 3000 <= current <= 5000:
            if value >= 500:
                return False
            else:
                return True
        else:
            if value >= 450:
                return False
            else:
                return True
    return random.choice(list(filter(filterUnwanted, pistols.items())))

def getRandomShield(current):
    # Returns 2 values for a shield name and its price depending on the money entered.
    # 0 - 3000 : could be Small or Big
    # 3000 - 5000 : could be Small, Big or None
    # 5000 - 9000 : could be Small, None

    if 0 <= current <= 3000:
        return (0, 3000)
    if 3000 <= current <= 5000:
        return (3000, 5000)
    else:
        return (5000, 9000)

# Main script
parser = argparse.ArgumentParser(
    description="Valorant Random Weapons and Agents App")

parser.add_argument("-r", "--rules", action="store_true",  dest="rules",
                    default=0, help="shows the rules involving the game")

parser.add_argument("-a", "--agent", action="store_true",  dest="agent",
                    default=0, help="shows a random agent pick instead of the normal weapons")

parser.add_argument("-c", "--continuous", action="store_true",  dest="continuous",
                    default=0, help="runs the program continuously and recieves input")

args = parser.parse_args()

# Idea: the random choice has the price of the item that is going to be used to calculate the max value and whether the player can buy it.
#       If the player does not have enough money for something from this dict remove all options that exceed the value given.

guns = {"None": 0, "Stinger": 1100, "Spectre": 1600, "Bucky": 850, "Judge": 1850, "Buldog": 2050,
        "Guardian": 2250, "Phantom": 2900, "Vandal": 2900, "Marshal": 950, "Operator": 4700, "Ares": 1600, "Odin": 3200}

pistols = {"None": 0, "Classic": 0, "Shorty": 300, "Frenzy": 450, "Ghost": 500, "Sheriff": 800}

armor = {"None": 0, "Small": 400, "Big": 1000}

agents = ["Astra", "Breach", "Brimstone", "Deadlock", "Chamber", "Cypher", "Fade", "Gekko", "Jett", "Kay/O", "Killjoy",
          "Neon", "Omen", "Harbor", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

if args.agent:
    result = "Agent: " + random.choice(agents)
elif args.rules:
    result = "Choose a random agent to play.\nAfter that choose random weapons.\n"
    result += "If the main weapon you have to buy is too expensive you can skip buying the main gun.\n"
    result += "Buying the pistol is mandatory. If the shield is too expensive you skip buying it too.\n"
    result += "Abilities are bought afterwards with the leftover money.\nSwitching to weapons you find is forbiden (exception is if the gun is the same as the one the randomiser has chosen for you).\n"
    result += "Ults can be used whenever.\n\nThats it have fun. :)\nPS: You can see all avaliable commands with '-h'."
    print(result);
elif args.continuous:
    print("You started the continuous process that lasts untill you enter 0 as a parameter.")
    targetPrice = -1
    while targetPrice != 0:
        targetPrice = int(input("Enter the first price for the round: "))
        if(targetPrice != -1):
            clear()
        currentPrice = 0
        pistol, pistolPrice = getRandomPistol(targetPrice)
        print(pistol, pistolPrice)
    result = "continuous"
else:
    result = "Armor: " + random.choice(list(armor.keys())) + "\nSecondary: " + \
        random.choice(list(pistols.keys())) + "\nMain: " + random.choice(list(guns.keys()))
    print(result)
