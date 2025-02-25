#W8D2 - dictionaries and text file data


#--imports-----------------------------
import csv
#--main  code--------------------------


library = {
    #indexes are strings set by developer
    #'key' : value
    "1230" : "red rising",
    "1231" : "The little prince" 
}

with open("text_files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        #add each record's data as a new key + value pair from the text file
        #key --> i[0]  ;  value --> i[1]
        library.update({i[0] : i[1]})
        #when using .update() -- > pass {'key' : value}
#disconnect from file
print(f"\n{'key':6}\t{'Title'}")
print("-" * 50)
for key in library:
    #for every key and value pair found within the library dictionary
    print(f"{key:6}\t{library[key]}")
print("-" * 50)

#dequential search for a title
search = input("\nEnter the title you are looking for: ")
found = 0

for key in library:
    if search.lower() == library[key].lower():
        #store the found title's location in the dictionary -->
        found = key

if found != 0:
    print(f"KEY: {found:6}\tTITLE: {library[found]}")
else:
    print(f"Your search for {search} was not found")

#type() returns the class type of the data passed to it
if type(library) is dict:
    print("library is a DICTIONARY")


#binary search for a lib number
#in order to binary searhc a set of keys you must first 
