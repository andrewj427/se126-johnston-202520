#Andrew Johnston
#W6 lab 2-10-25
#Prompt: Build a personal library search system using the file book_list.csv. It is set up as follows

#imports
import csv
from os import system, name

#functions
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():
    print("-----Library search menu-----")  
    print("|1. Show all titles         |")
    print("|2. Search by title         |")
    print("|3. Search by author        |")
    print("|4. Search by genre         |")
    print("|5. Search by Library number|")
    print("|6. Show all available books|")
    print("|7. Show all books on loan  |")
    print("|8.          Exit           |")
    print("-----------------------------")

    ans = input("Please choose your answer: ")
    return ans

def swap(x, y):
    '''
    X is the list name and Y is the index
    '''
    t = x[y]
    x[y]= x[y + 1]
    x[y + 1] = t
    
#Main code
#create blank lists to store data to from the file
clear()
libnum = []
title = []
author = []
genre = []
page = []
status = []

with open("text_files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        libnum.append(i[0])
        title.append(i[1])
        author.append(i[2])
        genre.append(i[3])
        page.append(i[4])
        status.append(i[5])

#search menu

ans = menu()

acceptable_ans = ['1', '2', '3', '4', '5', '6', '7', '8'] #put answers in a list to keep while statement small
while ans not in acceptable_ans:
    print("\n\tInvalid entry\n")
    ans = input("Please choose your answer: ")
while ans != '8':
    if ans == '1': 
        for i in range(0, len(title) - 1):#outter loop
            for index in range(0, len(title) - 1):#inner loop
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
                if(title[index] > title[index + 1]):
                    swap(title, index)
                    #swap all other values
                    #temp = age[index]
                    #age[index] = age[index + 1]
                    #age[index + 1] = temp
                    swap(libnum, index)
                    swap(author, index)
                    swap(genre, index)
                    swap(page, index)
                    swap(status, index)


        print("------------------------------------------------------------------------------------------------------")
        print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
        print("|----------------------------------------------------------------------------------------------------|")
        for i in range(0, len(libnum)):
            print(f"|{libnum[i]:5}   {title[i]:35}   {author[i]:15}  {genre[i]:15}   {page[i]:5}    {status[i]:10}|")
        print("------------------------------------------------------------------------------------------------------")
        ans = menu()

    elif ans == '2': 
        found = []
        search = input("Please input the title you would like to search for: ")
        for i in range(0, len(title)):
            if search.lower() in title[i].lower():
                found.append(i)
        if not found:
            print(f"Your search for {search} did not find any results")
        else:
            print(f"Your search for {search} found {len(found)} result(s): ")
            print("------------------------------------------------------------------------------------------------------")
            print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
            print("|----------------------------------------------------------------------------------------------------|")
            for i in range(0, len(found)):
                print(f"|{libnum[found[i]]:5}   {title[found[i]]:35}   {author[found[i]]:15}  {genre[found[i]]:15}   {page[found[i]]:5}    {status[found[i]]:10}|")
            print("------------------------------------------------------------------------------------------------------")
        ans = menu()
    
    elif ans == '3':
        found = []
        search = input("Please input the author you would like to search for: ")
        for i in range(0, len(author)): 
            if search.lower() in author[i].lower():
                found.append(i)
        if not found:
            print(f"Your search for {search} did not find any results")
        else:
            print(f"Your search for {search} found {len(found)} result(s): ")
            print("------------------------------------------------------------------------------------------------------")
            print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
            print("|----------------------------------------------------------------------------------------------------|")
            for i in range(0, len(found)):
                print(f"|{libnum[found[i]]:5}   {title[found[i]]:35}   {author[found[i]]:15}  {genre[found[i]]:15}   {page[found[i]]:5}    {status[found[i]]:10}|")
            print("------------------------------------------------------------------------------------------------------")
        ans = menu()
    
    elif ans == '4':
        found = []
        search = input("Please input the genre you would like to search for: ")
        for i in range(0, len(genre)): 
            if search.lower() in genre[i].lower():
                found.append(i)
        if not found:
            print(f"Your search for {search} did not find any results")
        else:
            print(f"Your search for {search} found {len(found)} result(s): ")
            print("------------------------------------------------------------------------------------------------------")
            print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
            print("|----------------------------------------------------------------------------------------------------|")
            for i in range(0, len(found)):
                print(f"|{libnum[found[i]]:5}   {title[found[i]]:35}   {author[found[i]]:15}  {genre[found[i]]:15}   {page[found[i]]:5}    {status[found[i]]:10}|")
            print("------------------------------------------------------------------------------------------------------")
        ans = menu()
    
    elif ans == '5':
        #bubble sort again because if user shows all titles first the lib# will be out of order, so binary search won't work
        for i in range(0, len(title) - 1):#outter loop
            for index in range(0, len(title) - 1):#inner loop
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
                if(libnum[index] > libnum[index + 1]):
                    swap(libnum, index)
                    swap(title, index)
                    swap(author, index)
                    swap(genre, index)
                    swap(page, index)
                    swap(status, index)


        search = input("Please input the library # you would like to search for: ")

        #binary search
        min = 0
        max = len(libnum) - 1
        mid = int((min + max) / 2)


        while min < max and search != libnum[mid]:
            if search < libnum[mid]:
                max = mid - 1 
            else:
                min = mid + 1
            mid = int((min + max) / 2)
        
        if search == libnum[mid]:
            print(f"Your search for {search} was found:")
            print("------------------------------------------------------------------------------------------------------")
            print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
            print("|----------------------------------------------------------------------------------------------------|")
            print(f"|{libnum[mid]:5}   {title[mid]:35}   {author[mid]:15}  {genre[mid]:15}   {page[mid]:5}    {status[mid]:10}|")
            print("------------------------------------------------------------------------------------------------------")
           
        else:
            print(f"Your search for {search} was not found")
        ans = menu()
        
                
    elif ans == '6':
        found = []
        for i in range(0, len(status)):
            if status[i] == "available":
                found.append(i)
        
        print("------------------------------------------------------------------------------------------------------")
        print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
        print("|----------------------------------------------------------------------------------------------------|")
        for i in range(0, len(found)):
            print(f"|{libnum[found[i]]:5}   {title[found[i]]:35}   {author[found[i]]:15}  {genre[found[i]]:15}   {page[found[i]]:5}    {status[found[i]]:10}|")
        print("------------------------------------------------------------------------------------------------------")
        ans = menu()
    
    elif ans == '7':
        found = []
        for i in range(0, len(status)):
            if status[i] == "on loan":
                found.append(i)
        
        print("------------------------------------------------------------------------------------------------------")
        print(f"|{'lib#':5}   {'title':35}   {'author':15}  {'genre':15}   {'page':5}    {'status':10}|")
        print("|----------------------------------------------------------------------------------------------------|")
        for i in range(0, len(found)):
            print(f"|{libnum[found[i]]:5}   {title[found[i]]:35}   {author[found[i]]:15}  {genre[found[i]]:15}   {page[found[i]]:5}    {status[found[i]]:10}|")
        print("------------------------------------------------------------------------------------------------------")
        ans = menu()
