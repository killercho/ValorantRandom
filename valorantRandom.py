import random
import argparse

parser = argparse.ArgumentParser(
    description="Valorant Random Weapons and Agents App")

parser.add_argument("-r", "--rules", action="store_true",  dest="rules",
                    default=0, help="shows the rules involving the game")

parser.add_argument("-a", "--agent", action="store_true",  dest="agent",
                    default=0, help="shows a random agent pick instead of the normal weapons")

args = parser.parse_args()

guns = ["None", "Stinger", "Spectre", "Bucky", "Judge", "Buldog",
        "Guardian", "Phantom", "Vandal", "Marshal", "Operator", "Ares", "Odin"]
pistols = ["None", "Classic", "Shorty", "Frenzy", "Ghost", "Sheriff"]
armor = ["None", "Small", "Big"]
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

print(result)
