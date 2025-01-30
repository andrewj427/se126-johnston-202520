#Andrew Johnston
#W4 Lab
#1-29-25


#prompt: Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension\

#imports-----------
import csv
from os import system, name
#functions---------
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
#main code---------

clear()
#create empty lists to store data from the file
fname = []
lname = []
age = []
screen = []
allegiance = []

#Create data pieces from above lists and store them to parallel lists
email = []
department = []
extension = []
#vars for department totals later
rnd = 0
marketing = 0
hr = 0
account = 0
sales = 0
audit = 0


with open('text_files/got_emails.csv') as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        fname.append(i[0])
        lname.append(i[1])
        age.append(i[2])
        screen.append(i[3])
        allegiance.append(i[4])

        email.append(i[3] + "@westeros.net")
        if i[4] == "House Stark":
            department.append("Research & Development") #Add each houses department
            rnd += 1
            num = 100
            while num in extension and num < 199:
                num += 1
            if num not in extension and num < 199: #check to make sure the extension doesn't already exist so no one has the same ext as another person
                extension.append(num)
            
                
        elif i[4] == "House Targaryen":
            department.append("Marketing")
            marketing += 1
            num = 200
            while num in extension and num < 299:
                num += 1
            if num not in extension and num < 299:
                extension.append(num)
            
                
        elif i[4] == "House Tully":
            department.append("Human Resources")
            hr += 1
            num = 300
            while num in extension and num < 399:
                num += 1
            if num not in extension and num < 399:
                extension.append(num)
            
                
        elif i[4] == "House Lannister":
            department.append("Accounting")
            account += 1
            num = 400
            while num in extension and num < 499:
                num += 1
            if num not in extension and num < 499:
                extension.append(num)
            
                
        elif i[4] == "House Baratheon":
            department.append("Sales")
            sales += 1
            num = 500
            while num in extension and num < 599:
                            num += 1
            if num not in extension and num < 599:
                extension.append(num)
            
                
        elif i[4] == "The Night's Watch":
            department.append("Auditing")
            audit += 1
            num = 600
            while num in extension and num < 699:
                num += 1
            if num not in extension and num < 699:
                extension.append(num)
            
                
        else:
            print("ERROR")
#disconnect from file, print values
print("--------------------------------------------------------------------------------")
print(f"|{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}|")
print("--------------------------------------------------------------------------------")
for i in range(0, len(fname)):
    print(f"|{fname[i]:8} {lname[i]:10} {email[i]:30} {department[i]:23} {extension[i]:3}|")
print("--------------------------------------------------------------------------------")

file = open('text_files/westeros.csv', 'w')
for i in range(0, len(fname)):
    file.write(f"{fname[i]},{lname[i]},{email[i]},{department[i]},{extension[i]}\n")
file.close()
print(f"The program successfully wrote {len(fname)} records to 'westeros.csv'.\n ")
print("\tEmployees in each department:")
print(f"\tResearch & Development: {rnd}")
print(f"\tMarketing:              {marketing}")
print(f"\tHuman resources:        {hr}")
print(f"\tAccounting:             {account}")
print(f"\tSales:                  {sales}")
print(f"\tAuditing:               {audit}")