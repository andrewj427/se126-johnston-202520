#W2D1 - Text file handling - introduction

#STEP 1: IMPORT THE CSV (comma separated value) library
import csv

total_records = 0 #total number of recors (rows) in the file

#connecting to the files path - swtich \ to /
#-----connected to file----------------------------------------------
print(f"{'name':10} \t {'number':3} \t {'color'}") #header print
print("-----------------------------------------")
with open("text_files/simple.csv") as csvfile:
    #indent 1 level (new block)

    #allow the processor to read the file data
    file = csv.reader(csvfile)

    #loop thry every record in the file
    for record in file:

        #add +1 to total_records
        total_records += 1

        #print(record) #the list view of each record

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name:10} \t {number:3} \t {color.title()}")
        
#------disconnected from file-----------------------------------------
print("-----------------------------------------")
print(f"TOTAL RECORDS: {total_records}\n")