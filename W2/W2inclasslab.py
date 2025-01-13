#Andrew Johnston
#W2 in class lab
#1-13-25

#prompt: Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list
#imports
import csv
from os import system, name

#functions
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def difference(people, max_cap):
    '''a function that is passed both the number of people attending the meeting, as well as the maximum room capacity. This function should determine the number of people over/under the capacity based on these two values, and return the difference value.'''

    difference = max_cap - people
    
    return difference

#---main code----------------------------
clear()
total_records = 0
rooms_over = 0
with open("text_files\classLab2.csv") as csvfile:
    file = csv.reader(csvfile)

    print(f"{'Room':20} \t {'Max':3} \t {'Min':3} \t {'Over'}")
    #loop thru every record in the file
    for i in file:
        room = i[0]
        max = int(i[1])
        min = int(i[2])

        over = difference(min, max)
        if over < 0:
            over = over * -1 #make value positive
            print(f"{room:20} \t {max:3} \t {min:3} \t {over}")
            rooms_over += 1 #add 1 to count of rooms over the max limit

        #add +1 to total_records
        total_records += 1

        #print(record) #the list view of each record
    print(f"\nProcessed {total_records} records")
    print(f"There are {rooms_over} rooms over the limit")
    input("\nPress enter to continue...")

       

        