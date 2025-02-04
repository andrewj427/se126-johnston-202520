#Andrew Johnston
#2-4-25
#Midterm practical exam

#Choice #3
#imports-------------
import csv
#functions-----------

#main code-----------
#create lists to store data to
fname = []
lname = []
department = []
gpa = []
studentID = []
idnum = 10001
with open("text_files/students.csv") as csvfile:
    file = csv.reader(csvfile)
    for i in file:
        fname.append(i[0])
        lname.append(i[1])
        department.append(i[2])
        gpa.append(i[3])
        if idnum not in studentID:
            studentID.append(idnum)
        elif idnum in studentID:
            idnum += 1
            studentID.append(idnum)
        elif idnum > 10021:
            studentID.append("ERROR")
#print data from lists
print("-------------------------------------------")
print(f"|{'FIRST':11}  {'LAST':11}  {'DEP':3}  {'GPA':4} {'ID':5}|")
print("-------------------------------------------")
for i in range(0, len(fname)):
    print(f"|{fname[i]:11}  {lname[i]:11}  {department[i]:3}  {gpa[i]:4} {studentID[i]:5}|")
print("-------------------------------------------")
print(f"\n\tTOTAL RECORDS: {len(fname)}")


#write data to new csv file
file = open('text_files/midterm_choice3.csv', 'w')
for i in range(0, len(fname)):
    file.write(f"{fname[i]},{lname[i]},{department[i]},{gpa[i]},{studentID[i]}\n")
file.close()

#sequential search
ans = "y"
while ans == "y":
    found = [] #store data that matches search query into this list
    lnamefound = -1
    print("\n\tSequential search menu:")
    print("-------------------------")
    print("|1. Search by LAST NAME |")
    print("|2. Search by DEPARTMENT|")
    print("|3.        Exit         |")
    print("-------------------------")

    menuans = input("Which option would you like to choose? ")
    while menuans != "1" and menuans != "2" and menuans != "3":
        print("\n\tINVALID ENTRY\n")
        menuans = input("Which option would you like to choose? ")

    if menuans == "1":
        print("Search by LAST NAME")
        search = input("Please enter the last name: ")
        for i in range(0, len(lname)):
            if search.lower() == lname[i].lower():
                lnamefound = i
        if lnamefound == -1:
            print(f"Your search for {search} did not find any results")
        else:
            print(f"Your search for {search} found a result:\n")
            print("-------------------------------------------")
            print(f"|{fname[lnamefound]:11}  {lname[lnamefound]:11}  {department[lnamefound]:3}  {gpa[lnamefound]:4} {studentID[lnamefound]:5}|")
            print("-------------------------------------------")
    elif menuans == "2":
        print("Search by DEPARTMENT")
        search = input("Please enter the department: ")
        for i in range(0, len(department)):
            if search.lower() == department[i].lower():
                found.append(i)
        if not found:
            print(f"Your search for {search} did not find any results")
        else:
            print(f"Your search for {search} found {len(found)} results:\n")
            print("-------------------------------------------")
            for i in range(0, len(found)):
                print(f"|{fname[found[i]]:11}  {lname[found[i]]:11}  {department[found[i]]:3}  {gpa[found[i]]:4} {studentID[found[i]]:5}|")
            print("-------------------------------------------")
    elif menuans == "3":
        ans = "n"