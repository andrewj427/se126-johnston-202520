#W4D1 - sequential search

#This file uses class_Grades.csv

#--imports--------------------------------
import csv

#--Functions------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let #let value replaces the funtion call in the main executing code
#--Main code------------------------------

#create empty lists to hold file data
fname = []
lname = []
test1 = []
test2 = []
test3 = []

with open("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append file data into appropriate lists
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from file -- can still access stored data via the lsits

#process the list data to calc an avg scroe for each student, and find a letter grade equivalent

numavg = [] #will hold each student's numeric average of test scores
letavg = [] #will hold each student's letter average of test scores

for i in range(0, len(fname)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    numavg.append(a)

    l = letter(a)
    letavg.append(l)
#process the lists to display all of the info back to user
print(f"{'fname':10}   {'lname':10}   {'t1'}  {'t2'}  {'t3'}  {'numavg'} {'letavg'}\n")
for i in range(0, len(fname)):
    print(f"{fname[i]:10}   {lname[i]:10}   {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {numavg[i]:.2f} {letavg[i]}")

print("---------------------------------------------------------------------")
print(f"There are {len(fname)} students in the file.")

#Write a program that allows a user to repeatedly search for a studen by their lname or letter grade

print("\n\nWelcome to the student search program!\n\n")

ans = input("Would you like to begin searching? [y/n] ").lower()

while ans == "y":
    
    #get search type from user
    print("\tSearch menu options:")
    print("1. search by LAST name")
    print("2. search by LETTER grade")
    print("3. exit")

    searchtype = input("Enter your search type [1-3]: ")

    if searchtype == "1":

        print("\tSEARCH BY LAST NAME")
        #get search item from user
        found = -1 #invalid index num, will use to check later to see if a student has been found
        
        searchname = input("Enter the LAST NAME of the stund you are searching for: ")
        #search
        for i in range(0, len(lname)):
            #the FOR LOOP alows for the "sequence" part -> from beginning to end
            if searchname.lower() == lname[i].lower():
                #if statement allows for the search part
                found = i
        #display results
        if found != -1:
            #if true last name has been found and we can display data
            print(f"Your search for {searchname} was found!")
            print(f"{fname[found]:10}   {lname[found]:10}   {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {numavg[found]:.2f} {letavg[found]}")
        
    elif searchtype == "2":
        print('\tSEARCH BY LETTER GRADE')
        found = [] #creates empty list to gather and store found index values
        
        searchgrade = input("Enter the LAST NAME of the stund you are searching for: ")
        #search
        for i in range(0, len(letavg)):
            #the FOR LOOP alows for the "sequence" part -> from beginning to end
            if searchgrade.upper() == letavg[i]:
                #if statement allows for the search part
                found.append(i)
        #display results
        if not found: #the list is empty
            print(f"Your search for {searchgrade} was not found")
        else:
            
            #if true last name has been found and we can display data
            print(f"Your search for {searchgrade} was found!")
            for i in range(0, len(found)):
                print(f"{fname[found[i]]:10}   {lname[found[i]]:10}   {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {numavg[found[i]]:.2f} {letavg[found[i]]}")

    elif searchtype == "3":
        print("\tEXITING")
        ans = "n"
    else:
        print("INVALID ENTRY")
    if searchtype == "1" or searchtype == "2":
        ans = input("Would you like to search again? [y/n]: ").lower()

    