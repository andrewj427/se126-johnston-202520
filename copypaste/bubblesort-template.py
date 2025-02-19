#use this function to swap lists
def swap(x, y):
    '''
    X is the list name and Y is the index
    '''
    t = x[y]
    x[y]= x[y + 1]
    x[y + 1] = t


#---MAIN BUBBLE SORT CODE---

for i in range(0, number_of_elements - 1):#outter loop
    for j in range(0, number_of_elements - 1):#inner loop
        if(name[j] > name[j + 1]):
            #place swap function here
            swap(name, j)
            