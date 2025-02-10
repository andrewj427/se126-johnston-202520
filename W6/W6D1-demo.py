#W6D1 - Searching algorithms: binary vs sequential

import csv

librarynum = [] #the only ORDERED field
titles = []
authors = []
genres = []
pages = []

with open("text_files/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        librarynum.append(i[0])
        titles.append(i[1])
        authors.append(i[2])
        genres.append(i[3])
        pages.append(i[4])
print(f"{'lib':5}   {'title':25}  {'author':15}    {'genre':20}   {'pages':5}")
print("----------------------------------------------------------------------------------------")
for i in range(0, len(librarynum)):
    print(f"{librarynum[i]:5}   {titles[i]:25}  {authors[i]:15}    {genres[i]:20}   {pages[i]:5}") 
print("----------------------------------------------------------------------------------------")

#sequential search: search for a title
#titles[] is not ordered

found = []
searchnum = input("Which # are you looking for? ")
seq_count = 0

for i in range(0, len(librarynum)):
    seq_count += 1
    if searchnum in librarynum[i]:
        found.append(i)
print(f"Search iterations: {seq_count}")
if not found:
    #found list is still empty
    print(f"Your search for {searchnum} was not found")
else:
    print(f"Your search for {searchnum} was found:")

    print(f"{'lib':5}   {'title':25}  {'author':15}    {'genre':20}   {'pages':5}")

    print("----------------------------------------------------------------------------------------")

    for i in range(0, len(found)):
        print(f"{librarynum[found[i]]:5}   {titles[found[i]]:25}  {authors[found[i]]:15}    {genres[found[i]]:20}   {pages[found[i]]:5}") 
    print("----------------------------------------------------------------------------------------")

#binary search: must be performed on ordered lsits(library nums)

min = 0
max = len(librarynum) - 1
mid = int((min + max) / 2)

bin_count = 0

while min < max and searchnum != librarynum[mid]:
    #min < max ---> list has not been exhausted of potential values yet
    #Searchnum += lib nums[mid] --> what we are looking for is not in the mid position

    if searchnum < librarynum[mid]: 
        #everything after mid point is not possible
        max = mid - 1
    else:
        #everything before mid point is not possible
        min = mid + 1

    mid = int((min + max) / 2)
    bin_count += 1

print(f"Binary seach iterations: {bin_count}")

if searchnum == librarynum[mid]:
    print(f"Your search for {searchnum} was found:")
    print(f"{'lib':5}   {'title':25}  {'author':15}    {'genre':20}   {'pages':5}")

    print("----------------------------------------------------------------------------------------")

    for i in range(0, len(found)):
        print(f"{librarynum[mid]:5}   {titles[mid]:25}  {authors[mid]:15}    {genres[mid]:20}   {pages[mid]:5}") 
    print("----------------------------------------------------------------------------------------")
else:
    print(f"Your search for {searchnum} was not found")
