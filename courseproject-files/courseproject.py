'''
GOALS FOR NEW ADDITIONS

save files:
use CSV files for save data as well as inventory, so you can pick up where you left off

item durability:
parallel lists used to store item uses and/or durability



SAVE FILE STRUCTURE

{savename}-info.csv
class,currenthp,maxhp,flasks,level,xp,damage,defense

{savename}-inventory.csv
itemname, itemclass, equip, durability, dmg, defense

item classes:
weapon, armor,
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
    print(f"Level up! you are now level {character['level']}!")
    character["xp"] = 0
    point = input("What stat would you like to increase? [hp/dmg/defense]: ").lower()
    valid = 0
    while valid == 0:
        if point == "hp":
            character["max hp"] += 25
            character["hp"] = character["max hp"]
            valid += 1
        elif point == "dmg":
            character['damage'] += 5
            alid += 1

        elif point == "defense":
            character['defense'] += 5
            valid += 1
        else:
            print("Invalid entry, please try again")
            point = input("What stat would you like to increase? [hp/dmg/defense]: ").lower()


    
#classes---------------------------------------------------------------------------------------
class newweapon:
    def __init__(self,name,durability,dmg):
        self.name = name
        self.durability = int(durability)
        self.dmg = int(dmg)

class newarmor:
    def __init__(self,name,durability,defense):
        self.name = name
        self.durability = int(durability)
        self.defense = int(defense)

class enemy:
    def __init__(self,name,hp,dmg):
        self.name = name
        self.hp = int(hp)
        self.dmg = int(dmg)

#Main code-------------------------------------------------------------------------------------

#CHARACTER IMPORTING/CREATION--------------
character = {
    "class" : "",
    "hp" : 0,
    "max hp" : 100,
    "flasks" : 5,
    "level" : 1,
    "xp" : 10,
    "damage" : 5,
    "defense" : 5
    }
weaponnames = []

armors = []

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
        
    elif dndclass == "rogue":
        file.write("rogue,100,100,5,1,0")
        
    elif dndclass == "mage":
        file.write("mage,150,150,5,1,0")
    file.close()
    
    file = open(f"courseproject-files/{username}-inventory.csv", 'w')
    if dndclass == "barbarian":
        file.write("beserkers armor,armor,equip,100,100\n")
        file.write("warriors sword,weapon,equip,100,20\n")
        
        
    elif dndclass == "rogue":
        file.write("assassins armor,armor,equip,100,75\n")
        file.write("thieves knife,weapon,equip,100,75\n")
        
        
    elif dndclass == "mage":
        file.write("wizards robe,armor,equip,100,50\n")
        file.write("arcane scepter,weapon,equip,100,150\n")
    file.write("fists,weapon,999,20")
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
                    weaponnames.append([i[0], int(i[2]), int(i[3])]) 
                    
                elif i[1] == "armor" and i[2] == "equip":
                    armor = newarmor(i[0], i[3], i[4])
                elif i[1] == "armor" and i[2] != "equip":
                    armors.append([i[0],int(i[2]),int(i[3])])
                
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
 
#create enemies using the enemy class
redo = 'y'
while redo == 'y':
    goblin = enemy("goblin", 75, armor.defense + 5)
    skeleton = enemy("skeleton", 50, armor.defense + 10)
    orc = enemy("orc", 100, armor.defense + 20)
    enemychoice = roll(3)#randomly select an enemy
    if enemychoice == 1:
        activeenemy = goblin
        print("A goblin has appeared!")
    elif enemychoice == 2:
        activeenemy = skeleton
        print("A skeleton has appeared!")
    elif enemychoice == 3:
        activeenemy = orc
        print("An orc has appeared!")
    quit = 0

    while int(character["hp"]) > 0 and activeenemy.hp > 0 and redo == 'y':
        turns = 1
        action = input("What would you like to do? [attack/inventory/heal/save/quit]: ").lower()
        while action != "attack" and action != "inventory" and action != "heal" and action != "save" and action != "quit":
            print("Invalid entry, please try again")
            action = input("What would you like to do? [attack/inventory/heal/save]: ").lower()

        if action == "attack":
            dmg = roll(int(weapon.dmg))
            activeenemy.hp -= dmg
            weapon.durability -= 1
            if weapon.durability == 0:
                print("Your weapon has broken!")
                del weapon
            print(f"You dealt {dmg} damage to the {activeenemy.name}! it has {activeenemy.hp} hp left!\n")
            turns -= 1

        elif action == "heal":
            if character["flasks"] > 0 and character["hp"] <= int((character["max hp"]) - 20):
                character["flasks"] -= 1
                character["hp"] += 20
                print(f"You healed 20 hp! you have {character['hp']} hp left!")
            elif character['flasks'] > 0 and character['hp'] != character['max hp'] and character['hp'] > character['max hp'] - 20:
                character['flasks'] -=1
                character['hp'] = character['max hp']
                print(f"You healed 20 hp! you have {character['hp']} hp!")

            elif character['flasks'] < 1 or character['hp'] == character['max hp']:
                print("Sorry, you can't heal right now!")

        elif action == "inventory":
            inv = input("What would you like to view? [weapons/armors]: ").lower()
            while inv != "weapons" and inv != "armors":
                print("Invalid entry, please try again")
                inv = input("What would you like to view? [weapons/armors]: ").lower()

            if inv == "weapons":
                #sequential search to pick weapon to equip
                print("Name:                Durability:          Damage:")
                
                for i in range(0, len(weaponnames)):
                    print(f"{weaponnames[i][0]:20} {weaponnames[i][1]:11} {weaponnames[i][2]:16}")
                equip = input("Would you like to equip a weapon? [y/n]: ").lower()
                while equip != 'y' and equip != 'n':
                    print("invalid entry, please try again")
                    equip = input("Would you like to equip a weapon? [y/n]: ").lower()
                if equip == 'y':
                    choice = input("Which weapon would you like to equip?: ").lower()
                    found = 0
                    for i in range(0, len(weaponnames)):
                        if choice == weaponnames[i][0].lower():
                            weaponnames.append([weapon.name,weapon.durability,weapon.dmg])
                            weapon = newweapon(weaponnames[i][0],weaponnames[i][1],weaponnames[i][2])
                            weaponnames.remove([weaponnames[i][0],weaponnames[i][1],weaponnames[i][2]])
                            print(f"Equipped {weapon.name}!")
                            found += 1
                    if found == 0:
                        print(f"Sorry, {choice} was not found")
                        
            elif inv == "armors":
                #sequential search to pick armor to equip
                print("Name:                Durability:          defense:")
                for i in range(0, len(armors)):
                    print(f"{armors[i][0]:20} {armors[i][1]:11} {armors[i][2]:17}")
                equip = input("Would you like to equip new armor? [y/n]: ").lower()
                while equip != 'y' and equip != 'n':
                    print("invalid entry, please try again")
                    equip = input("Would you like to equip new armor? [y/n]: ").lower()
                if equip == 'y':
                    choice = input("Which armor would you like to equip?: ").lower()
                    found = 0
                    for i in range(0, len(armors)):
                        if choice == armors[i][0].lower():
                            armors.append([armor.name,armor.durability,armor.defense])
                            armor = newweapon(armors[i][0],armors[i][1],armors[i][2])
                            armors.remove([armors[i][0],armors[i][1],armors[i][2]])
                            print(f"Equipped {armor.name}!")
                            found += 1
                    if found == 0:
                        print(f"Sorry, {choice} was not found")
        
        elif action == 'save':
            print("Saving...")
            file = open(f"courseproject-files/{username}-info.csv", 'w')
            file.write(f"{character['class']},{character['hp']},{character['max hp']},{character['flasks']},{character['level']},{character['damage']},{character['defense']}")
            file.close()
            #save inventory
            file = open(f"courseproject-files/{username}-inventory.csv", 'w')
            file.write(f"{weapon.name},weapon,equip,{weapon.durability},{weapon.dmg}\n")
            file.write(f"{armor.name},armor,equip,{armor.durability},{armor.defense}")
            for i in range(0,len(weaponnames)):
                file.write(f"\n{weaponnames[i][0]},weapon,{weaponnames[i][1]},{weaponnames[i][2]}")
            for i in range(0,len(armors)):
                
                file.write(f"\n{armors[i][0]},armor,{armors[i][1]},{armors[i][2]}")
            file.close()
        elif action == 'quit':
            print("goodbye!")
            redo = 'n'
        if turns == 0 and activeenemy.hp > 0:
            #Enemies turn
            enemydmg = roll(activeenemy.dmg)
            taken = (enemydmg - (character['defense'] + armor.defense))
            if taken < 0:
                print(f"You blocked the hit from {activeenemy.name}!\n")
            else:
                print(f"Armor defense: {armor.defense} character defense: {character['defense']} enemy roll: {enemydmg}")
                character['hp'] -= taken
                print(f"You took {taken} damage from the {activeenemy.name}! Your HP is now {character['hp']}!\n")

        if activeenemy.hp < 0:
            print(f"The {activeenemy.name} has been defeated!")
            xp = roll(25)
            character["xp"] += xp
            print(f"You gained {xp} xp!\nYou have {character['xp']} / 100 xp!")
            if character["xp"] >= 100:
                levelup()
            redo = input("would you like to try again? [y/n] ").lower()
            while redo != 'y' and redo != 'n':
                print("Invalid entry, please try again")
                redo = input("would you like to try again? [y/n] ").lower()

if character['hp'] < 0:
    print("You have died! you can restart from your last save.")
    