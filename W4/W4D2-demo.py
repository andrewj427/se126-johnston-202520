#w4D2 - sequential search review + creating & writing to text files



#--imports------------------------
import csv
#--functions----------------------

#--main code----------------------

#creating empty lists - one for each field 
dragons = []
riders = []
count = []
color1 = []
color2 = []

with open("text_files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        dragons.append(i[0])
        riders.append(i[1])
        count.append(i[2])
        if i[2] == "2":
            color2.append(i[4])
        else:
            color2.append('-')
        color1.append(i[3])
#disconnected from file

#process the lists to display data to the console
print(f"{'dragons':15}   {'riders':30}    {'#':3}    {'color1':8}    {'color2'}")
print("----------------------------------------------------------------------------")
for i in range(0, len(dragons)):
    print(f"{dragons[i]:15}   {riders[i]:30}    {count[i]:3}    {color1[i]:8}    {color2[i]}")

#search for a specific dragon
#setup and gain of search
found = "x"
search = input("Which dragon are you looking for: ")

#perform search --> for loop/if statement
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():
        #hold onto the found location of our searched-for value
        found = i
#step 3: filter and display results
if found != "x": #search was found
    print(f"Your search for {search} was found:")
    print(f"{dragons[found]:15}   {riders[found]:30}    {count[found]:3}    {color1[found]:8}    {color2[found]}")
else:
    print(f"Your search for {search} was not found")

#search for a color set
found = []
search = input("Enter the dragon color you are looking for: ")
for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

if not found: #if the found list is empty
     print(f"Your search for {search} was not found")
else:
    print(f"Your search for {search} was found:")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15}   {riders[found[i]]:30}    {count[found[i]]:3}    {color1[found[i]]:8}    {color2[found[i]]}")

#write some data to a new file
file = open('text_files/test1.csv', 'w')
for i in range(0, len(dragons)):
    file.write(f"{dragons[i]},{riders[i]}\n")
file.close()