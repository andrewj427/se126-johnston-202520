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
    for index in range(0, number_of_elements - 1):#inner loop
        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing
        if(name[index] > name[index + 1]):
            swap(name, index)
            #swap all other values
            #temp = age[index]
            #age[index] = age[index + 1]
            #age[index + 1] = temp
            swap(age, index)