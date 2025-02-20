'''
GOALS FOR NEW ADDITIONS

save files:
use CSV files for save data as well as inventory, so you can pick up where you left off

item durability:
parallel lists used to store item uses and/or durability



SAVE FILE STRUCTURE

{savename}-info.csv
class,maxhp,currenthp

{savename}-inventory.csv
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
clear()
print("\tWelcome to the DND program!\n")
prevsave = input("do you have a save you would like to import? [y/n]: ").lower()
if prevsave == 'y':
    filepath = input("Please input the relative path of your save file here: ")
    with open(filepath) as csvfile:
        file = csv.reader(csvfile)
        for i in file:
