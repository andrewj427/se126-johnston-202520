#w2d2 text file handling review

#functions-----------
def difference(people, max_cap):
    '''this function is passed 2 values and returns the difference'''
    diff = max_cap - people
    return diff

#imports
import csv

#main code

#initialize neede counting variables
total_records = 0
rooms_over = 0

with open("text_files/classLab2.csv") as csvfile:
    #indent 1 level while connected to file

    file = csv.reader(csvfile)
    print(f"{'Name':20} \t {'  Max':5} \t {'  Ppl':5} \t {'Over'}")
    print("---------------------------------------------------------")
    for rec in file:
        #below code occurs for every record (row) in the file

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1])
        ppl = int(rec[2])

        #call the difference() functino to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display room sthat are over capacity (remaining is negative)
        if remaining < 0:
            rooms_over += 1
            remaining = remaining * -1
            print(f"{name:20} \t {max:5} \t {ppl:5} \t {remaining}")

        total_records += 1

#display final data(counting vars)
print(f"\nRooms currently OVER CAPACITY: {rooms_over}")
print(f"Total rooms in file: {total_records}\n\n")