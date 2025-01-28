#W4D1
#Andrew Johnston, 1-27-25

#prompt: take data from a csv file of students grades, create a sequential search program

#imports------------
import csv

#Main code----------

fname = []
lname = []
test1 = []
test2 = []
test3 = []
num_avg = []
let_avg = []

with open("text_files/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)
    for i in file:
        fname.append(i[0])
        lname.append(i[1])
        test1.append(int(i[2]))
        test2.append(int(i[3]))
        test3.append(int(i[4]))
#disconnect from file

#calculate averages
for i in range(0,len(fname)):
    avg = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(avg)

    if avg >= 90:
        let_avg.append("A")
    elif avg >= 80:
        let_avg.append("B")
    elif avg >=70:
        let_avg.append("C")
    elif avg >=60:
        let_avg.append("D")
    elif avg < 60:
        let_avg.append("F")
#Print each students data
print(f"{'fname':10}   {'lname':10}   {'t1':3}  {'t2':3}  {'t3':3}  {'numavg':6} {'letavg':6}\n")
print("------------------------------------------------------------------------------------------")
for i in range(0, len(fname)):
    print(f"{fname[i]:10}   {lname[i]:10}   {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:6.2f} {let_avg[i]}")

print("\n--------SEARCH MENU--------")
print("1. Search by LAST name")
print("2. Search by FIRST name")
print("3. Search by LETTER GRADE")
print("4.        EXIT")
print("---------------------------\n")

ans = int(input("Which option would you like to search by? [1-4]: "))

while ans != 1 and ans != 2 and ans != 3 and ans != 4:
    print("INVALID INPUT\n")
    ans = int(input("Which option would you like to search by? [1-4]: "))

if ans == 1:
    found = 'x'
    search = input("Please input the last name you would like to search for: ")
    for i in range(0, len(fname)):
        if search.lower() == lname[i].lower():
            found = i
    if found != 'x':
        print(f"Your search for {search} was found: ")
        print(f"{fname[found]:10}   {lname[found]:10}   {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.2f} {let_avg[found]}")
    else:
        print(f"Your search for {search} was not found :(")

if ans == 2:
    found = 'x'
    search = input("Please input the last name you would like to search for: ")
    for i in range(0, len(fname)):
        if search.lower() == fname[i].lower():
            found = i
    if found != 'x':
        print(f"Your search for {search} was found: ")
        print(f"{fname[found]:10}   {lname[found]:10}   {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.2f} {let_avg[found]}")
    else:
        print(f"Your search for {search} was not found :(")

if ans == 3:
    found = [] #create a list to store all letter grades found
    search = input("Please input the average letter grade you would like to search for: ")
    for i in range(0, len(let_avg)):
        if search.upper() == let_avg[i]:
            found.append(i)
    
    if not found:
        print(f"Your search for the letter grade {search} was not found :(")
    else:
        print(f"Your search for the letter grade {search} was found: ")
        for i in range(0, len(found)):
            print(f"{fname[found[i]]:10}   {lname[found[i]]:10}   {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.2f} {let_avg[found[i]]}")
