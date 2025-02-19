#w7d2 - review of binary seach and bubble sort + 2d lists

def menu():
    print("simple searching menu")
    print("1. search by NAME")
    print("2. search by NUM")
    print("3. search by COLOR")

    choice = input("enter your search type: [1-4]: ")
    return choice

def swap(index, listname):
    temp = listname[index]
    listname[index] = listname[index + 1]
    listname[index + 1] = temp

import csv

#create empty 1d parallel lists
names = []
nums = []
colors =[]
choiceans = ['1','2','3','4']

with open("text_files/simple.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        names.append(i[0])
        nums.append(i[1])
        colors.append(i[2].title())

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in choiceans:
        print("\nINVALID ENTRY\n")
    
    elif choice == "1":
        print("\n~Search by NAME~")
        #bubble sort before binary search
        for i in range(len(names) -1):
            for j in range(len(names) -1):
                #see if 'heavier' value is in front of 'smaller' value
                if names[j] > names[j + 1]:
                    #swap places
                    swap(j, colors)
                    #swap other lists
                    swap(j, names)
                    swap(j, nums)

        min = 0
        max = len(names) - 1
        mid = int((min + max) / 2)

        search = input("Enter the NAME you are looking for: ")
        
        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max) / 2)

        if search.lower() == names[mid].lower():
            #found
            print(f"Your search for {search} was found:")
            print(f"{'NAME':8}  {'NUM':3}   {'COLOR'}")
            print("---------------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
        else:
            print(f"Your search for {search} could not be completed")
            

    elif choice == "2":
        print("\n~Search by NUM~")

    elif choice == "3":
        print("\n~Search by COLOR~")

        for i in range(len(colors) -1):
            for j in range(len(colors) -1):
                #see if 'heavier' value is in front of 'smaller' value
                if nums[j] >nums[j + 1]:
                    #swap places
                    swap(j, colors)
                    #swap other lists
                    swap(j, names)
                    swap(j, nums)

        min = 0
        max = len(names) - 1
        mid = int((min + max) / 2)

        search = input("Enter the number you are looking for: ")
        
        while min < max and search.lower() != nums[mid].lower():
            if search < nums[mid]:
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max) / 2)

        if search == nums[mid]:
            #found
            print(f"Your search for {search} was found:")
            print(f"{'NAME':8}  {'NUM':3}   {'COLOR'}")
            print("---------------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
        else:
            print(f"Your search for {search} could not be completed")

        #bubble sort before binary search
        for i in range(len(colors) -1):
            for j in range(len(colors) -1):
                #see if 'heavier' value is in front of 'smaller' value
                if colors[j] > colors[j + 1]:
                    #swap places
                    swap(j, colors)
                    #swap other lists
                    swap(j, names)
                    swap(j, nums)

        min = 0
        max = len(names) - 1
        mid = int((min + max) / 2)

        search = input("Enter the color you are looking for: ")
        
        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max) / 2)

        if search.lower() == colors[mid].lower():
            #found
            print(f"Your search for {search} was found:")
            print(f"{'NAME':8}  {'NUM':3}   {'COLOR'}")
            print("---------------------------------------------------------")
            print(f"{names[mid]:8}  {nums[mid]:3}   {colors[mid]}")
        else:
            print(f"Your search for {search} could not be completed")
    else:
        print("\nEXIT")
        ans = 0

#---2D lists---------------------------------------

datafile = [
    #this will be a 2D list to hold all of the file data
    names, #a list of names
    nums,  #a list of nums
    colors,#a list of colors
]

print("\n\nDATA FILE (2D list[][]):")
for i in range(0, len(datafile)):
    print(f"INDEX {i} of 'datafile': {datafile[i]}")
    for j in range(0, len(datafile[i])):
        #accessing each value within the list currently lookede at from outer for loop
        print(f"INDEX {i} and value dtafile[{j}]: {datafile[i][j]}")
