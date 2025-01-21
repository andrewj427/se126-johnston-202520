#Andrew Johnston
#1-21-25
#W3 lab

#prompt: Construct a program that will analyze potential voters. The program should generate the following
#totals:
#1. Number of individuals not eligible to register.
#2. Number of individuals who are old enough to vote but have not registered.
#3. Number of individuals who are eligible to vote but did not vote.
#4. Number of individuals who did vote.
#5. Number of records processe

#Variable dictionary:
#noteligible - users under 18
#eligiblenotreg - users >= 18, but not registered to vote
#eligiblenovote - >= 18, registered to vote, but havent
#didvote - voted
#^^^these are the variables for the totals at the end^^^

#Imports
from os import system, name
import csv
#functions
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def counter(var1):
    '''a function that is passed a value, adds one to the value, and then returns the value'''
    var1 += 1
    return var1




#---Main code-----------------------------
clear()

#initialize variables to use at the end of program
notEligible = 0
eligibleNotReg = 0
eligibleNoVote = 0
didvote = 0


#initialize list variables and a total count
totalrec = 0
idnum = []
age = []
registered = []
voted = []
#connect to file
with open("text_files/voters_202040.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        idnum.append(i[0])
        age.append(i[1])
        registered.append(i[2])
        voted.append(i[3])
        totalrec += 1
#after data is stored to lists, disconnect from file

for i in range(0 , totalrec):
    if int(age[i]) < 18 and registered[i] == "N" and voted[i] == "N":
        notEligible = counter(notEligible)

    elif int(age[i]) >= 18 and registered[i] == "N" and voted[i] == "N":
        eligibleNotReg = counter(eligibleNotReg)

    elif int(age[i]) >= 18 and registered[i] == "Y" and voted[i] == "N":
        eligibleNoVote = counter(eligibleNoVote)

    elif int(age[i]) >= 18 and registered[i] == "Y" and voted[i] == "Y":
        didvote = counter(didvote)
    else:
        print("\nAn error in the data has occured, please try again")



#print final totals
print("\n\t\t\t***TOTAL***\n")
print( "|--------------------------------------------------------------|")
print(f"|            Individuals unable to register:             {notEligible:5.0f} |")
print(f"|Individuals who are old enough but have not registered: {eligibleNotReg:5.0f} |")
print(f"|     Individuals who are eligible but didn't vote:      {eligibleNoVote:5.0f} |")
print(f"|              Individuals who did vote:                 {didvote:5.0f} |")
print(f"|                   Records processed:                   {totalrec:5.0f} |")
print( "|--------------------------------------------------------------|")


