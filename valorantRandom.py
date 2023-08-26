import random
import argparse
from os import name, system

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
    # 0 - 800 : could be Classic, Frenzy, Shorty, Sheriff, Ghost (All of them)
    # 800 - 3000 : could be Sheriff and Ghost 
    # 3000 - 5000 : could be Frenzy, Shorty, Classic and None
    # 5000 - 9000 : could be Shorty, Classic or None

    def filterUnwanted(pair):
        key, value = pair
        if 0 <= current <= 800:
            if value == 0 and key == "None":
                return False
            if current < value:
                return False
            return True
        if 800 < current <= 3000:
            if value < 500:
                return False
            return True
        if 3000 < current <= 5000:
            if value >= 500:
                return False
            return True
        else:
            if value >= 450:
                return False
            return True
    return random.choice(list(filter(filterUnwanted, pistols.items())))

def getRandomShield(current):
    # Returns 2 values for a shield name and its price depending on the money entered.
    # 0 - 400 : could be None
    # 400 - 1000 : could be None, Small
    # 1000 - 3000 : could be Small or Big 
    # 3000 - 5000 : could be Small, Big or None
    # 5000 - 9000 : could be Small, None

    def filterUnwanted(pair):
        _, value = pair
        if 0 <= current < 400:
            if value < 400:
                return True
            return False
        if 400 <= current <= 1000:
            if value < 1000:
                return True
            return False
        if 1000 < current <= 3000:
            if value < 400:
                return False
            return True
        if 3000 < current <= 5000:
            return True
        else:
            if value > 400:
                return False
            return True
    return random.choice(list(filter(filterUnwanted, armor.items())))

def getRandomGun(current):
    # Returns 2 values for a main gun name and its price depending on the money entered.
    # 0 - 800 : could be None
    # 800 - 1800: could be None, Stinger, Spectre, Bucky, Marshal, Ares (850 - 1600$)
    # 1800 - 2600 : could be Stinger, Spectre, Judge, Buldog, Guardian, Marshal, Ares (950 - 2250$)
    # 2600 - 3500 : could be Judge, Buldog, Guardian, Phantom, Vandal, Marshal, Odin (950 - 3200$ , but without 1100, 1600)
    # 3500 - 9000 : could be Phantom, Vandal, Operator, Odin, Guardian (2250 - 4700$)

    def filterUnwanted(pair):
        _, value = pair
        if 0 <= current <= 800:
            if value > 0:
                return False
            return True
        if 800 < current <= 1800:
            if 0 <= value <= 1600:
                return True
            return False
        if 1800 < current <= 2600:
            if 950 <= value <= 2250:
                return True
            return False
        if 2600 < current <= 3500:
            if 950 <= value <= 3200 and value != 1100 and value != 1600:
                return True
            return False
        else:
            if value >= 2250:
                return True
            return False
    return random.choice(list(filter(filterUnwanted, guns.items())))

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
    print(result)
elif args.rules:
    result = "Choose a random agent to play.\nAfter that choose random weapons.\n"
    result += "If you play the continuous mode you need to only input the correct amount of money for the current round.\nEverything else will be done by the script.\n"
    result += "In the event that you play the normal weapons mode use the following rules:\nIf the main weapon you have to buy is too expensive you can skip buying the main gun.\n"
    result += "Buying the pistol is mandatory. If the shield is too expensive you skip buying it too.\n"
    result += "Abilities are bought afterwards with the leftover money.\nSwitching to weapons you find is forbiden (exception is if the gun is the same as the one you have now).\n"
    result += "For both modes:\nif you survive the round you have to stay with the same weapons as the previous one and "
    result += "ults can be used whenever.\n\nThats it have fun. :)\nPS: You can see all avaliable commands with '-h'."
    print(result);
elif args.continuous:
    print("You started the continuous process that lasts untill you enter 0 as a parameter.")
    targetPrice = -1
    while True:
        targetPrice = abs(int(input("Enter the first price for the round: ")))
        if(targetPrice != -1):
            clear()
        if(targetPrice == 0):
            break
        currentPrice = 0
        pistol, pistolPrice = getRandomPistol(targetPrice)
        currentPrice += pistolPrice
        shield, shieldPrice = getRandomShield(abs(targetPrice - currentPrice))
        currentPrice += shieldPrice
        gun, gunPrice = getRandomGun(abs(targetPrice - currentPrice))
        result = "Armor: " + shield + "\nSecondary: " + pistol + "\nMain: " + gun
        print(result)
else:
    result = "Armor: " + random.choice(list(armor.keys())) + "\nSecondary: " + \
        random.choice(list(pistols.keys())) + "\nMain: " + random.choice(list(guns.keys()))
    print(result)
