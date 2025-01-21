#Andrew Johnston
#W3 in class lab
#1-21-25

#prompt: determine how much it would cost the company to replace all machines that are from 2016 and earlier

#var dictionary
#LIST VARS - these vars store data from the file into lists per field
#pctype
#brand
#cpu
#ram
#ssd1
#num
#ssd2
#windowsver
#year
#----------------------------
#totalrecords - counts total # of records, used for display and further calculations
#laptops, desktops, lapcost, deskcost - # of laptops/desktops from 2016 or earlier AND how much it costs to replace them

#--imports----------------------
import csv
from os import system, name
#--functions--------------------
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#--main code--------------------
clear()
#initialize list vars and open file
pctype = []
brand = []
cpu = []
ram = []
ssd1 = []
num = []
ssd2 = []
windowsver = []
year = []
totalrecords = 0

with open("text_files/filehandling-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        if i[0] == "D":
            pctype.append("Desktop")
        else:
            pctype.append("Laptop")
        if i[1] == "DL":
            brand.append("Dell")
        elif i[1] == "HP":
            brand.append(i[1])
        elif i[1] == "GW":
            brand.append("GateWay")
        cpu.append(i[2])
        ram.append(i[3])
        ssd1.append(i[4])

        if i[5] == "1":
            num.append(i[5])
            ssd2.append("-")
            windowsver.append(i[6])
            year.append(i[7])
        else:
            num.append(i[5])
            ssd2.append(i[6])
            windowsver.append(i[7])
            year.append(i[8])

        totalrecords += 1
#disconnect from file, use lists for calculations
print(f"{'Type':9} {'Brand':9}  {'CPU':3}  {'RAM':3}  {'SSD1':5}  {'#SSD':3}  {'SSD2':5}   {'VER':5}  {'YR':5}")
print("-------------------------------------------------------------")
for i in range(0, totalrecords):
    print(f"{pctype[i]:9} {brand[i]:9}  {cpu[i]:3}  {ram[i]:3}  {ssd1[i]:6}  {num[i]:3}  {ssd2[i]:6}  {windowsver[i]:5}  {year[i]:5}")
print("-------------------------------------------------------------")
print(f"\n\t\tTotal records: {totalrecords}")

#calculate if pc is from before 2016
laptops = 0
desktops = 0
for i in range(0, totalrecords):
    if int(year[i]) <= 16:
        if pctype[i] == "Desktop":
            desktops += 1
        else:
            laptops += 1
lapcost = laptops * 1500
deskcost = desktops * 2000
print(f"\nTo replace {desktops} destktops it will cost ${deskcost}. To replace {laptops} laptops it will cost ${lapcost}\n")
