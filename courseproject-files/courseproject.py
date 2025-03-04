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

def roll(num):
    rand = random.randint(1, num)
    return rand

def levelup():
    character["level"] += 1
    print(f"Level up! you are now level {level}!")
    character["xp"] = 0
    point = input("What stat would you like to increase? [hp/dmg/defense]: ").lower()
    valid = 0
    while valid == 0:
        if point == "hp":
            character["max hp"] += 25
            character["hp"] = character["max hp"]
        elif point == "dmg":
            weapon.dmg += 5
        elif point == "defense":
            armor.defense += 5
        else:
            print("Invalid entry, please try again")
            point = input("What stat would you like to increase? [hp/dmg/defense]: ").lower()
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

class consumable:
    def __init__(self,name,length,effect):
        self.name = name
        self.length = length
        self.effect = effect

class enemy:
    def __init__(self,name,hp,dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

#Main code-------------------------------------------------------------------------------------

#CHARACTER IMPORTING/CREATION--------------
character = {
    "class" : "",
    "hp" : 0,
    "max hp" : 100,
    "flasks" : 5,
    "level" : 1,
    "xp" : 10
    }
weaponnames = []

armors = []

potions = []
inventory = []
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
        file.write("stealth potion,potion")
        file.close()
    elif dndclass == "mage":
        file.write("wizard's robe,armor,equip,100,50\n")
        file.write("arcane scepter,weapon,equip,100,150\n")
        file.write("mana potion,potion")
        file.close()

elif prevsave == 'y':
    username = input("Please input your username here: ").lower()
    valid = 0
while valid == 0:
    try: #in case the user's file cannot be found, otherwise the code will break
        with open(f"courseproject-files/{username}-info.csv") as csvfile:
            file = csv.reader(csvfile)
            for i in file:
                character["class"] = i[0]
                character["hp"] = int(i[1])
                character['max hp'] = int(i[2])
                character["flasks"] = int(i[3])
                character["level"] = int(i[4])
                character["xp"] = int(i[5])
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
        valid = 1 #if both files are found, code can continue properly, so set value != 0
    except FileNotFoundError:
        print(f"Sorry, username {username} was not found")
        username = input("Please input your username here: ").lower()


print("-" * 28)
print("|CHARACTER SHEET:          |")
for key in character:
    print(f"|{key:7} : {character[key]:16}|")
print("|" + ("-" * 26) + "|")
print("|CHARACTER'S EQUIPPED ITEMS|")
print(f"|weapon: {weapon.name:18}|")
print(f"|armor : {armor.name:18}|")
print("-" * 28)

#BATTLE-----------------------------------
print("WARNING: if you forcefully quit the program without saving, your progress will NOT be saved!\n")
enemychoice = roll(3) #randomly select an enemy
#create enemies using the enemy class
goblin = enemy("goblin", 75, 10)
skeleton = enemy("skeleton", 50, 15)
orc = enemy("orc", 100, 20)
if enemychoice == 1:
    activeenemy = goblin
    print("A goblin has appeared!")
elif enemychoice == 2:
    activeenemy = skeleton
    print("A skeleton has appeared!")
elif enemychoice == 3:
    activeenemy = orc
    print("An orc has appeared!")
    
while int(character["hp"]) > 0 and activeenemy.hp > 0:
    action = input("What would you like to do? [attack/inventory/heal/save]: ").lower()
    while action != "attack" and action != "inventory" and action != "heal" and action != "save":
        print("Invalid entry, please try again")
        action = input("What would you like to do? [attack/inventory/heal/save]: ").lower()

    if action == "attack":
        dmg = roll(int(weapon.dmg))
        activeenemy.hp -= dmg
        weapon.durability -= 1
        if weapon.durability == 0:
            print("Your weapon has broken!")
            del weapon
        print(f"You dealt {dmg} damage to the {activeenemy.name}! it has {activeenemy.hp} hp left!")

    elif action == "heal":
        if int(character["flasks"]) > 0 and character["hp"] < int((character["max hp"]) - 20):
            character["flasks"] -= 1
            character["hp"] += 20
            print(f"You healed 20 hp! you have {character['hp']} hp left!")
    elif action == "inventory":
        inv = input("What would you like to view? [weapons/armor/potions]: ").lower()
        while inv != "weapons" and inv != "armor" and inv != "potions":
            print("Invalid entry, please try again")
            inv = input("What would you like to view? [weapons/armor/potions]: ").lower()
        if inv == "weapons":
            print("Weapons:")
            print("Name:                Durability:          Damage:")
            for i in range(0, len(weaponnames)):
                print(f"{weaponnames[i][0]:20} {weaponnames[i][2]:20} {weaponnames[i][3]:20}")
            equip = input("Would you like to equip a weapon? [y/n]: ").lower()
            if equip == 'y':
                choice = input("Which weapon would you like to equip?: ").lower()
                for i in range(0, len(weaponnames)):
                    if choice == weaponnames[i][0]:
                        weaponnames.append(f"{weapon.name},{weapon.durability},{weapon.dmg}")
                        weapon = newweapon(weaponnames[i][0],weaponnames[i][2],weaponnames[i][3])
                        weaponnames.pop(i)
print(f"The {activeenemy.name} has been defeated!")
xp = roll(25)
character["xp"] += xp
print(f"You gained {xp} xp!")
if character["xp"] == 100:
    levelup()