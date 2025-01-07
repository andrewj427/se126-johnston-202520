#Andrew Johnston
#SE126.02
#W1 Lab
#1-7-25

#Prompt: it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity

#imports--------------------
from os import system, name
#Functions------------------
def difference(people, max_cap):
    '''a function that is passed both the number of people attending the meeting, as well as the maximum room capacity. This function should determine the number of people over/under the capacity based on these two values, and return the difference value.'''

    difference = max_cap - people
    
    return difference
        
def decision(response):
    ''' a function that is passed a value that represents response: the users response to whether or not they would like to continue in the program and enter another meetings attendance information'''

    
    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input("Would you like to try again? [y/n]: ").lower()

    return response

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Main code-------------------
clear()
print("\tWelcome to w1 lab!\n")

ans = "y"
while ans == "y":
    #initial variable collection
    meetingname = input("\nPlease enter the name of the meeting: ")
    max_cap = int(input("\nEnter the max amount of people allowed in the room: "))
    people = int(input("\nEnter the amount of people signed up for the meeting: "))
    
    #use differente() to calculate the amount of people over or under the cap
    diff = difference(people, max_cap) 

    if diff >=0:
        print(f"\n{meetingname} meets fire safety, and you can add {diff} more participant(s).")
    else: # people > max cap, diff is negative
        diff = diff * -1   #turn it into a positive #
        print(f"\n{meetingname} does not meet fire safety standards, you need to remove {diff} participant(s)")
        
    ans = input("Would you like to try again? [y/n]: ").lower()
    ans = decision(ans)

print("Thank you for using my progam, goodbye")