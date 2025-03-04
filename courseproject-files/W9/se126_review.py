#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------
def swap(j, name):
    temp = name[j]
    name[j] = name[j + 1]
    name[j + 1] = temp

#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)                            #entire list
print(names_list[0])                         #first value  
print(names_list[len(names_list) - 1])       #last value

#create an empty list for each potential field - these must remain the same length in order to be parallel
names = []
riders = []
nums = []
color1 = []
color2 = []


#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    'fname' : 'george',
    'mname' : 'bulleit',
    'lname' : 'wayne',
    'age' : 12,

}

print(people_dictionary)            #entire dictionary
print(people_dictionary['fname'])   #replaces with value assigned to 'fname' key


dragon_dict = {} #empty dictionary to be populated by the file


#gaining data from a text file 
with open("text_files/dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0])
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == '2':
            color2.append(rec[4])
            colorvar = rec[4]
        else:
            color2.append('-')
            colorvar = '-'

        #adding data to a dictionary
        dragon_dict.update({rec[0] : [rec[1], rec[2], rec[3], colorvar]})



#processing data from collections
print(f"{'name':12} {'rider':30} {'num':3} {'color1':8} {'color2'}")
print('-'*75)
for i in range(0, len(names)):
    
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print('-'*75)


print('-'*75)

for key in dragon_dict:
    print(f"{key.upper():15} : {dragon_dict[key]}")

    for value in dragon_dict[key]:
        print(f"{key} - {value}", end = "")
    print()
    for i in range(0, len(dragon_dict[key])):
        print(f"{key} / {dragon_dict[key][i]}", end = "")
    print("\n")
print('-'*75)


#searching & sorting
#sequential search
search = input("\nEnter the rider you wish to find: ").lower()
found = []

for key in dragon_dict:
    if search.lower() in dragon_dict[key][0].lower():
        found.append(key) # adds key of found locations to the list

if not found:
    #found list is empty
    print(f"Sorry, your search for {search} did not find anything")

else:
    print(f"\nHere are the results for your search of {search}:")
    for i in range(0, len(found)):
         print(f"{found[i].upper()} {dragon_dict[found[i]][0]} {dragon_dict[found[i]][1]} {dragon_dict[found[i]][2]} {dragon_dict[found[i]][3]}")


#BINARY SEARCH *requires* the sorting of data before searching
#we must also ensure the collection we search through is populated with UNIQUE values

#bubble sort algorithm - loop inside a loop
for i in range(len(names) - 1):
    for j in range(len(names) - 1):
        if names[j] > names[j + 1]:
            swap(j,names)
            swap(j,riders)
            swap(j,nums)
            swap(j,color1)
            swap(j,color2)

min = 0
max = len(names) - 1
mid = int((min + max) / 2)

search = input("what would you like to search for? ")

while min < max and search.lower() != names[mid].lower():
    if search.lower() < names[mid].lower():
        max = mid - 1
        
    else:
        min = mid + 1

    mid = int((min + max) / 2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record # {mid}, see info below")
    print(f"{names[mid]} {riders[mid]} {nums[mid]} {color1[mid]} {color2[mid]}")
else:
    print(f"sorry, your search for {search} could not be found")


#2D lists - lists of lists! 
letters = [
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I']
]

print(letters)
print(letters[0])
print(letters[0][0])
print(letters[0][len(letters[0]) - 1])