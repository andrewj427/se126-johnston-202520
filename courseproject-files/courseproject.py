'''
GOALS FOR NEW ADDITIONS

save files:
use CSV files for save data as well as inventory, so you can pick up where you left off

item durability:
parallel lists used to store item uses and/or durability



SAVE FILE STRUCTURE

{savename}-info.csv
class,currenthp,maxhp,flasks,level,xp

{savename}-inventory.csv
itemname, itemclass, equip, durability, dmg, defense

item classes:
weapon, armor, potion
'''
#imports--------------------------------------------------------------------------------------
import csv
from os import system, name
import time
import random

#Functions------------------------------------------------------------------------------------
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
#classes---------------------------------------------------------------------------------------
class newweapon:
    def __init__(self,name,durability,dmg):
        self.name = name
        self.durability = durability
        self.dmg = dmg

class newarmor:
    def __init__(self,name,durability,defense):
        self.name = name
        self.durability = durability
        self.defense = defense

#Main code-------------------------------------------------------------------------------------
character = {
    "class" : "",
    "hp" : 0,
    "max hp" : 100,
    "level" : 1,
    "xp" : 10
    }
weaponnames = []

armors = []

potions = []
consumables = []
#using a dict for character info and a list for inventory so that you can have repeat inventory items
clear()
print("\tWelcome to the DND program!\n")
prevsave = input("do you have a save you would like to import? [y/n]: ").lower()
while prevsave != 'y' and prevsave != 'n':
    print("Invalid entry, please try again\n")
    prevsave = input("do you have a save you would like to import? [y/n]: ").lower()

if prevsave == 'n':
    classes = ["barbarian", "rogue", "mage"]
    username = input("Please input a username: ").lower()
    dndclass = input("Please enter what class you would like to play: [barbarian/rogue/mage] ").lower()
    while dndclass not in classes:
        print("Invalid entry, please try again")
        dndclass = input("Please enter what class you would like to play: [barbarian/rogue/mage] ").lower()

    file = open(f"courseproject-files/{username}-info.csv", 'w')
    if dndclass == "barbarian":
        file.write("barbarian,200,200,5,1,0")
        file.close()
    elif dndclass == "rogue":
        file.write("rogue,100,100,5,1,0")
        file.close()
    elif dndclass == "mage":
        file.write("mage,150,150,5,1,0")
    
    file = open(f"courseproject-files/{username}-inventory.csv", 'w')
    if dndclass == "barbarian":
        file.write("beserker's armor,armor,equip,100,100\n")
        file.write("warrior's sword,weapon,equip,100,20\n")
        file.write("Strength potion,potion")
        file.close()
    elif dndclass == "rogue":
        file.write("assassin's armor,armor,equip,100,75\n")
        file.write("theif's knife,weapon,equip,100,75\n")
        file.write("stealth potion,potion\n")
        file.close()
    elif dndclass == "mage":
        file.write("wizard's robe,armor,equip,100,50\n")
        file.write("arcane scepter,weapon,equip,100,150\n")
        file.write("mana potion,potion")

elif prevsave == 'y':
    username = input("Please input your username here: ").lower()
#try: #in case the user's file cannot be found, otherwise the code will break
with open(f"courseproject-files/{username}-info.csv") as csvfile:
    file = csv.reader(csvfile)
    for i in file:
        character["class"] = i[0]
        character["hp"] = i[1]
        character['max hp'] = i[2]
        character["level"] = i[3]
        character["xp"] = i[4]
with open(f"courseproject-files/{username}-inventory.csv") as csvfile:
    file = csv.reader(csvfile)
    for i in file:
        if i[1] == "weapon" and i[2] == "equip":
            weapon = newweapon(i[0], i[3], i[4])
        elif i[1] == "weapon" and i[2] != "equip":
            weaponnames.append(i)
        elif i[1] == "armor" and i[2] == "equip":
            armor = newarmor(i[0], i[3], i[4])
        elif i[1] == "armor" and i[2] != "equip":
            armors.append(i)
        elif i[1] == "potion":
            potions.append(i[0])



print("-" * 28)
print("|CHARACTER SHEET:          |")
for key in character:
    print(f"|{key:7} : {character[key]:16}|")
print("|" + ("-" * 26) + "|")
print("|CHARACTER'S EQUIPPED ITEMS|")
print(f"|weapon: {weapon.name:18}|")
print(f"|armor : {armor.name:18}|")
print("-" * 28)