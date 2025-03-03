#Andrew Johnston
#Week 8 Lab
#2/26/25
#prompt: build a mini programming dictionary a user can search througha nd add to using the words.csv file

#imports-----------
import csv
from os import system, name
#functions---------
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    print("\n-----------------------------")
    print("|Programming dictionary menu|")
    print("|---------------------------|")
    print("|1. Show all words          |")
    print("|2. Search for a word       |")
    print("|3. Add a word              |")
    print("|3.5 show all words in order|")
    print("|4. Exit                    |")
    print("-----------------------------")

    choice = input("Please select an option [1-4]: ")
    choices = ['1', '2', '3', '3.5', '4']
    while choice not in choices:
        print("Invalid entry, please try again")
        choice = input("Please select an option [1-4]: ")
    return choice
def swap(x, y):
    '''
    Swap 2 items in a list
    X = index, y = listname
    '''
    temp = y[x]
    y[x] = y[x + 1]
    y[x + 1] = temp
#main code---------
clear()

#create blank dictionary to store file data to
words = {}
#create 2 blank lists for bubble sort later for option 3.5
word = []
definition = []
with open("text_files/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for i in file:
        words[i[0]] = i[1]
        word.append(i[0])
        definition.append(i[1])

choice = menu() #put menu in function so it can be called multiple times

while choice != '4': #if choice == 4, program will end automatically
    if choice == '1':
        print("1. Show all words")
        for key in words:
            print(f"{key} : {words[key]}")
        input("\n\n\tPress enter to continue")
        choice = menu()
    
    elif choice == '2':
        print("2. Search for a word")
        found = 0
        search = input("Please enter a word to search for: ")
        for key in words:
            if search.lower() == key.lower():
                found = key
        if found == 0:
            print(f"Sorry, your search for {search} was not found")
        else:
            print(f"{found} : {words[found]}")
            input("\n\n\tPress enter to continue")
        choice = menu()
    
    elif choice == '3':
        print("3. Add a word")
        new = input("Please enter a new word: ")
        if new in words:
            print(f"{new} already exists in the dictionary")
        else:
            definition = input(f"Please enter the definition for {new}: ")
            words[new] = definition
            print(f"{new} has been added to the dictionary")
        choice = menu()

    elif choice == '3.5':
        print("3.5 Show all words in order")
        #bubble sort the 2 lists
        for i in range(0, len(word) - 1):#outter loop
            for j in range(0, len(word) - 1):#inner loop
                if(word[j] > word[j + 1]):
                    swap(j, word)
                    swap(j, definition)
        #print sorted list
        for i in range(0, len(word)):
            print(f"{word[i]} : {definition[i]}")
        input("\n\n\tPress enter to continue")
        choice = menu()


#when the user exits, write updated dictinoary to new file
file = open('text_files/updated_words.csv', 'w')
for key in words:
    file.write(f"{key},{words[key]}\n")
file.close()
print("Successfully wrote new entries to updated_words.csv")