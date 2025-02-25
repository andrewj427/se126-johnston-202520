'''
GOALS FOR NEW ADDITIONS

save files:
use CSV files for save data as well as inventory, so you can pick up where you left off

item durability:
parallel lists used to store item uses and/or durability



SAVE FILE STRUCTURE

{savename}-info.csv
class,currenthp,maxhp

{savename}-inventory.csv
itemname, itemclass, durability, maxdurability, dmg, defense
'''

import csv
from os import system, name
import time
import random


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Main code-------------------------------------------------------------------------------------
dndclass = ""
maxhp = 0
currenthp = 0
inventory = []
clear()
print("\tWelcome to the DND program!\n")
prevsave = input("do you have a save you would like to import? [y/n]: ").lower()
while prevsave != 'y' and prevsave != 'n':
    print("Invalid entry, please try again\n")
    prevsave = input("do you have a save you would like to import? [y/n]: ").lower()

if prevsave == 'y':
    username = input("Please input your username here: ").lower()
    try: #in case the user's file cannot be found, otherwise the code will break
        with open(f"courseproject-files/{username}-info.csv") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                dndclass = i[0]
                currenthp = int(i[1])
                maxhp = int(i[2])
        print(f"     Class: {dndclass}")
        print(f"Current HP: {currenthp}")
        print(f"Maximum HP: {maxhp}")
        with open(f"courseproject-files/{username}-inventory.csv") as csvfile:
            file = csv.reader(csvfile)
    except:
        print(f"Couldn't find a file under {username}")