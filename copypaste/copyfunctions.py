from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def swap(x, y):
    '''
    Swap 2 items in a list
    X = index, y = listname
    '''
    temp = y[x]
    y[x] = y[x + 1]
    y[x + 1] = temp