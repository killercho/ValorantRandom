import random
import argparse

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

guns = {"None": 0, "Stinger": 1100, "Spectre": 1600, "Bucky": 850, "Judge": 1800, "Buldog": 2050,
        "Guardian": 2100, "Phantom": 2900, "Vandal": 2900, "Marshal": 950, "Operator": 4700, "Ares": 0, "Odin": 3200}

pistols = {"None": 0, "Shorty": 300, "Frenzy": 450, "Ghost": 500, "Sheriff": 800}

armor = {"None": 0, "Small": 400, "Big": 1000}

agents = ["Astra", "Breach", "Brimstone", "Deadlock", "Chamber", "Cypher", "Fade", "Gekko", "Jett", "Kay/O", "Killjoy",
          "Neon", "Omen", "Harbor", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

if not args.agent and not args.rules:
    result = "Armor: " + random.choice(armor) + "\nSecondary: " + \
        random.choice(pistols) + "\nMain: " + random.choice(guns)
elif args.rules:
    result = "Choose a random agent to play.\nAfter that choose random weapons.\n"
    result += "If the main weapon you have to buy is too expensive you can skip buying the main gun.\n"
    result += "Buying the pistol is mandatory. If the shield is too expensive you skip buying it too.\n"
    result += "Abilities are bought afterwards with the leftover money.\nSwitching to weapons you find is forbiden (exception is if the gun is the same as the one the randomiser has chosen for you).\n"
    result += "Ults can be used whenever.\n\nThats it have fun. :)\nPS: You can see all avaliable commands with '-h'."
else:
    result = "Agent: " + random.choice(agents)

# print(result)
