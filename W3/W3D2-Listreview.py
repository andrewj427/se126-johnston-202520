#W3D2 - List review - 1D lists & parallel lists
#this file uses : class_grades.csv

#--IMPORTS-------------------------------------
import csv
#-FUNCTIONS------------------------------------

#--MAIN CODE-----------------------------------

total_records = 0

#create an empty list for every potential field
first = []
last = []
test1 = []
test2 = []
test3 = []

with open("text_files/class_grades.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for i in file:
        #for every record (i) in the file, do the following
        #print(f"{i[0]:10} \t {i[1]:10}")

        #fname = i[0]
        #lname = i[1]
        #test1 = i[2]

        #add the record data to its corresponding list (1 list per field)
        #append --> to add to the end
        first.append(i[0])
        last.append(i[1])

        test1.append(int(i[2])) # cast as int for easier math later
        test2.append(int(i[3]))
        test3.append(int(i[4]))
#disconnect from the file -- all file deata is retained bc we are using lists
#create a new list to hold each student's test score avg
avg = []

#process the current student data to find and store each student's test score avg to the avg list
for i in range(0, len(test1)):

    a = (test1[i] + test2[i] +test3[i]) / 3
    avg.append(a)
    #could also put equation in avg.append
#basic processing - use the 1D parallel lists to print al data to the console
print(f"INDEX: {' #':2} : {'first':10}  {'last':10}  {' t1':3}  {' t2':3}  {' t3':3} {'avg':3}")
print("_______________________________________________________________")
for index in range(0, len(first)): #len() --> length of collection, returns # of items
    #index ---> key of the list, allows access to one specific value
    print(f"INDEX: {index:2} : {first[index]:10}  {last[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3}    {avg[index]:3.2f}")
print("_______________________________________________________________")

#find current avg of class by processing the avg list data
totalavg = []

for i in range(0, len(avg)):
    totalavg += avg[i] #adds each avg value to the total avg

#calculate the avg
classavg = totalavg / len(avg)
print(f"the class averege of these {len(avg)} students is: {classavg:.2f}")