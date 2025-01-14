#Andrew Johnston
#W2 Lab
#1-14-25

#prompt: produce a report that lists all the computers in the csv file

#Dictionary:
#total - total amount of records processed
#comp, brand, cpu, ram, disk1, num, disk2, os, yr - variables that hold field data from the csv file 
#csvfile / file - the csv file

#imports------------
import csv
from os import system, name
#functions----------
def clear():
    if name =='nt':
        _ = system('cls')
    else:
        _ = system('clear')


#main code----------------------
#initialize counting var
clear()
total = 0
with open("text_files/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    print(f"{'Type':9}    {'Brand':9}    {'CPU':4}    {'RAM':4}    {'1st Disk':8}    {'HDDs':4}    {'2nd Disk':6}    {'OS':5}    {'YR':4}")
    for i in file:
        #vars per field
        comp = i[0] #couldn't use type so i used comp instead
        if comp == "D":
            comp = "Desktop"
        else:
            comp = "Laptop"
        brand = i[1]
        if brand == "DL":
            brand = "Dell"
        elif brand == "GW": #using elif because we dont need to change HP from its original
            brand = "Gateway"
        cpu = i[2]
        ram = i[3]
        disk1 = i[4]
        num = int(i[5])

        if num == 2: #IF pc has another disk, if not entry will be blank
            disk2 = i[6]
            os = i[7]
            yr = i[8]
        else:
            disk2 = "-"
            os = i[6]
            yr = i[7]
        total += 1
        print(f"{comp:9}    {brand:9}    {cpu:4}    {ram:4}    {disk1:5}    {num:4}       {disk2:5}       {os:5}    {yr:4}")
    print(f"\n\t\tTotal records: {total}\n")