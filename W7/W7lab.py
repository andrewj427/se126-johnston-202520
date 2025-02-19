#Andrew Johnston
#W7 lab
#prompt: write a program to assign passengers plane seats using 1D/ 2D lists

#imports---------------------------------
import csv
from os import system, name

#functions-------------------------------
def swap(x, y):
    '''
    Swap 2 items in a list
    X = index, y = listname
    '''
    temp = y[x]
    y[x] = y[x + 1]
    y[x + 1] = temp

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def showseats():
    print("\nCURRENT SEATING:\n")
    print("---------------------")
    for i in range(0, len(seating)):
        print(f"| {seating[i][0]}     {seating[i][1]} {seating[i][2]}     {seating[i][3]} {seating[i][4]} |")
    print("---------------------")
def again():
    '''
    Asks the user if they would like to book another seat, handles validity checking and returns y or n
    '''
    ans = input("Would you like to book another seat? [Y/N]: ").lower()
    while ans != 'y' and ans != 'n':
        print("INVALID ENTRY\n")
        ans = input("Would you like to book another seat? [Y/N]: ").lower()
    return ans




#Main code-------------------------------
clear()
#create 2D list with full seating map
seating = [
    ['1','A','B','C','D'],
    ['2','A','B','C','D'],
    ['3','A','B','C','D'],
    ['4','A','B','C','D'],
    ['5','A','B','C','D'],
    ['6','A','B','C','D'],
    ['7','A','B','C','D'],
]
ans = "y"
sections = ['A','B','C','D'] # create a separate section and rows list for easy calculations later
rows = ['1','2','3','4','5','6','7']
while ans == "y":
    showseats()
    row = input("Please select what row you would like to sit in [1-7]: ")
    section = input("Please select which seat you would like [A-D]: ").upper()
    if section in sections and row in rows:
        for i in range(0, len(sections)):
            if section == sections[i]:
                section = int(i + 1)
                #A=1, B=2, C=3, D=4: easier to search to see if the seat is taken

        #check if seat is taken, update if not, tell the user if it is
        for i in range(0, len(seating)):
            if row in seating[i]:
                if seating[i][section] == "X":
                    print("Sorry, this seat is already taken. please try again")
                else:
                    seating[i][section] = "X"
        
        ans = again()
    else:
        print("\nInvalid entry, please try again")
        
