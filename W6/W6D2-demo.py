#W6D2 - Binary search + bubble sort

#this file uses party.csv

#Prompt: build a repeatable menu driven program to access and search for data within the file

#mports---
import csv

#functions---
def display(x, foundlist, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single recod or multiple
                when x != "x" we have multiple values, otherwise we have one value

            records - the length of a list we are going to process through (# of loops / prints)
    '''
    print(f"{'CLASS':8}   {'NAME':10}    {'MEANING':25} {'CULTURE'}")
    print("-------------------------------------------------------------------------")
    if x != "x":
        #printing 1 record
        print(f"{class_type[x]:8}   {name[x]:10}    {meaning[x]:25} {culture[x]}")
    
    elif foundlist:
        #printing multiples, based on length stored in foundlist
        for i in range(0, records):
            print(f"{class_type[foundlist[i]]:8}   {name[foundlist[i]]:10}    {meaning[foundlist[i]]:25} {culture[foundlist[i]]}")

    else:
        #printing multiples, based on length stored in records
        for i in range(0, records):
            print(f"{class_type[i]:8}   {name[i]:10}    {meaning[i]:25} {culture[i]}") 
    print("-------------------------------------------------------------------------\n")

def swap(i, listname):
    temp = listname[i]
    listname[i] = listname[i + 1]
    listname[i + 1] = temp

#main code---

class_type = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

with open("text_files/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        class_type.append(i[0])
        name.append(i[1])
        meaning.append(i[2])
        culture.append(i[3])
#Disconnected from file--------------

#display whole list data to user
display("x",0,len(class_type)) #Practice with function

ans = input("Would you like to enter the search program? [y/n]: ").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***\n")
    ans = input("Would you like to enter the search program? [y/n]: ").lower()

#main searching loop
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by TYPE") #shows all of either elf or dragon
    print("2. Search by NAME")
    print("3. Search by MEANNING")
    print("4. EXIT")

    searchtype = input("\nHow would you like to search? [1-4]: ")

    #using 'not in' for user validity checks
    if searchtype not in ["1", "2", "3", "4"]:
        print("***INVALID ENTRY!***\n")
        searchtype = input("\nHow would you like to search? [1-4]: ")
    elif searchtype == "1":
        print(f"You have chosen to search by TYPE")

        search = input("Which type: 'dragon' or 'elf': ").lower()

        if search not in ['dragon', 'elf']: #could also be: if search.title() not in class_type
            print("***INVALID ENTRY!***\n")
            search = input("Which type: 'dragon' or 'elf': ").lower()
        
        else:
            found = []
            for i in range(0, len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)

            if not found:
                print(f"Sorry, your search for {search} could not be completed")
            else:
                print(f"Your search for {search} Is complete! details below: ")
                display("x", found, len(found))
    elif searchtype == "2":
        print("\nYou have chosen to search by NAME")

        #BINARY SEARCH
    #BUBBLE SORT----------------------------------------
        for i in range(0, len(name) - 1):#outter loop
           # print("OUTER LOOP! i = ", i)
            for index in range(0, len(name) - 1):#inner loop

               # print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(name[index] > name[index + 1]):

                   # print("\t\t SWAP! ", name[index], "<-->", name[index + 1])

                    #if above is true, swap places!

                    swap(index, name)
                    swap(index, class_type)
                    swap(index, culture)
                    swap(index, meaning)
        #Check your sorting!
        display("x", 0, len(name))

        #binary search
        search = input("Enter the NAME you are looking for: ")

        min = 0
        max = len(name) - 1
        mid = int((min + max) / 2)

        while min < max and search != name[mid]:
            if search < name[mid]:
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) / 2)
            
        if search == name[mid]: 
            display(mid, 0, len(name))
        else:
            print(f"Your search for {search} came up empty")
    
    elif searchtype == "3":
        print(f"\nYou have chosen to search by MEANING")
        found = []
        search = input("Which name meaning are you looking for? ")
        for i in range(0, len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)
        if not found:
            print(f"Your search for {search} came up empty")
        else:
            display("x", found, len(found))
    
    elif searchtype == "4":
        ans = 0