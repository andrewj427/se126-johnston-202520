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
print(f"{'fname':10}   {'lname':10}   {'t1'}  {'t2'}  {'t3'}  {'numavg'} {'letavg'}\n")
for i in range(0, len(fname)):
    print(f"{fname[i]:10}   {lname[i]:10}   {test1[i]:3}  {test2[i]:3}  {test3[i]:3}  {num_avg[i]:.2f} {let_avg[i]}")