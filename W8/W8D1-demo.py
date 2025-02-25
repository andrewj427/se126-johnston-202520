#W8D1 - intro to dictionaries



#--imports-------------------

#--main code-----------------

#start by creating a populated dictionary
mycar = {
    #'key' : value,
    "make": "Chevy",
    "model": "Malibu",
    "year": 2020,
    "name": "andrew",
    "color": "blue",
    #keys cannot be repated/no duplicates allowed
    #repeats will replace first value
    "color": "red"
} 

#display entire dictionary -> 'mycar'
print(mycar)
#display just the make and model values of the dictionary


#dictionaryname["keyName"] --> accesses stored value
#'keyName' will always be a string index, created by developer
print(f"My car is a {mycar["make"]} {mycar["model"]}")

#keys cannot be repeated within a dictionary, but they can be reused acoss unique dictionary names: mycar vs yourcar
yourcar = {
    #'key' : value,
    "make": "GMC",
    "model": "Canyon",
    "year": 2019,
    "name": "Jolly",
    "color": "Black",
    "friends": ["ray", "matt", "duncan"]
}

print(f"Rob's car is a {yourcar["make"]} {yourcar["model"]}")

#since friends gives access to a list, secondary [] are used to point to which value in said list
print(f"{yourcar["friends"][2]}")

#processing through a dictionary and its keys
for key in yourcar:
    print(f"{key.upper()} : {yourcar[key]}")

#add a key and value to a preexisting list
yourcar['plate'] = '12345'