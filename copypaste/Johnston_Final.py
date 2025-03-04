#Andrew Johnston
#SE116 Final project

#Prompt: A DND style boss fight using a diceroll function to determine damage, with class bonuses and an invenntory system

#Variable dictionary:

#player / boss stats:
    #playerhealth - the players current health
    #playermaxhealth- the maximum amount of health the player can have, upgradeable with items
    #healthpotions - # of health potions the player has
    #dndclass - the players class - barbarian, rogue, or paladin
    #bosshealth - the bosses current health
    #evasion - rng 1-100, if > x the player dodges the bosses attack
    #attack - attack damage the player does to the boss, upgradeable with items and class bonuses
    #bossattackdmg - attack damage the boss does to the player, nullifiable with items and class bonuses
    
#INVENTORY SYSTEM VARIABLES:
    #inventory[] - a list of the players items in their inventory
    #activeitems[] - a list of items that the player has activated to use in the next turn
    #groundlootitems[] - a list of possible items for the player to use
    #groundloot - flip a coin to determine if the player finds an item on the ground


#imports
from os import system, name 
import time
import random
# import sleep to show output for some time period 
from time import sleep

#functions
def clear(): 

  # for windows 
  if name == 'nt': 
    _ = system('cls') 

  # for mac and linux(here, os.name is 'posix') 
  else: 
    _ = system('clear')

def diceroll(num):
    roll = random.randint(1, num)
    return roll

def ground(grounditem):
    '''takes the ground loot roll and adds that item to the inventory'''
    founditem = groundlootitems[grounditem - 1]
    inventory.append(founditem)
    print(f"\n\tYou found '{founditem}' on the ground and put it in your inventory!")

def useitem(item):
    '''Use the selected item and remove it from the inventory'''
    #use global to alter the value of these variables from within the function
    global healthpotions
    global bosshealth
    global playermaxhealth
    global activeitems
    itemname = inventory[item]
    
    if inventory[item] in activeitems:
        print("\n\tYou cant stack the same item!")
        
        return 0
    else:
        if inventory[item] == "Healing potion":
            healthpotions += 1
            print(f"You added another Healing potion to your toolbelt! you now have {healthpotions}.")
            inventory.remove("Healing potion")
            return 0
        elif inventory[item] == "Potion of strength":
            print("You feel your body surge with power as you drink the potion. the next attack you do will deal +5 damage!")
            
        elif inventory[item] == "Amulet of health":
            playermaxhealth += 25
            print(f"As you put on the amulet, your body starts to glow! Your maximum health has been raised to {playermaxhealth}!")
            inventory.remove(itemname)
            return 0
        elif inventory[item] == "Potion of invisibility":
            print("As you drink the potion, your body becomes invisible! The next attack that King Malathor uses will miss!")

        elif inventory[item] == "Rusty shield":
            print("You raise the rickety shield against King Malathor, negating 5 damage from his next attack!")

        elif inventory[item] == "Fireball in a bottle":
            print("You pick up the flaming hot fireball and open the lid towards king malathor! Your next attack will deal an additional 10 damage and set him on fire for 3 turns!")

        elif inventory[item] == "Ring of protection":
            print("As you slide the ring on your finger, you feel your skin grow tougher. You will negate 3 damage from King Malathor's next attack!")

        elif inventory[item] == "Rusty key":
            print("You notice a chest in the corner of the room, and while King Malathor is distracted, you run over and use the key to open it!")

        elif inventory[item] == "Bag of gold":
            print("You throw the heavy bag of gold at king malathor, dealing 1 damage!")
            bosshealth -= 1
            inventory.remove(itemname)
            return 0

        else:
            print("***UNEXPECTED ERROR USING ITEM***")
            return 0
        print(f"Removed {inventory[item]} from inventory!\n")
        
        inventory.remove(itemname)
        return itemname

def classpicker():
    valid = "choosing"
    while valid == "choosing":       
        dndclass = input("\n\tChoose your Class: Barbarian, Rogue, or Paladin. type ? for a description: ").lower()
        if dndclass == "barbarian":
            input("\nYour Class: Barbarian! Press enter to continue...")
            valid = "chosen"
            #+5 to attack roll

        elif dndclass == "rogue":
            input("\nYour Class: Rogue! Press enter to continue...")
            valid = "chosen"
            #+10 % chance to evade attack

        elif dndclass == "paladin":
            input("\nYour Class: Paladin! Press enter to continue...")
            valid = "chosen"
            # +5 damage resistance

        elif dndclass == "?":
            print("\n\tThe Barbarian is a fierce warrior who gains +5 to attack, the Rogue is a stealthy trickster with an additional +10 percent chance to evade attacks, and the Paladin is a holy knight who can negate 5 damage from incoming hits.")
        else:
            print("\n\t\t\t***INVALID ENTRY!***")
    return dndclass


#Put the ASCII drawings in functions so i dont have to scroll all the way thru them every time, makes the code look cleaner
def malathor():
    input("""@@@@@@@@@@@@@@@@@@@@@@@@@@*%@@@@@@@@#+@@@@@@@@@@++#@@@@@@@@@@-#@@@@@@@@%+@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@#+@@@#%@@@%=%@@@@@@@@%-++%@@@@@@@@#:%@@@#@@@@-#@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@%=#@@##@@@%=+@@%#=:::-:+=-:::-*%@@-=%@@@*@@@++@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@*-%@#%%@@@+-=-==+===-:+*-===++=--:*%@@%*@@#++@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@**=@@#%@@++-+#++==--=:+#---==+*#+:#+@@#%@@++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@%++*@#@+-+*=-#*++==+--+#+===+*##=-%+-+@%@#=+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@+#+%*=+%%*+==#%#+=-:--##+=*#%%+=+##%*+#%-**@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@#+%-=@@#+*+--=+===--=*+*+++=+==-=###@%+-%+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@%-%%#####*+==-=----***%%+--=-==+*##%#%%%%=#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@%-*@@%##**+==-------=*%*=---===+*####%@@#-#@@%%%@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@%%%==@###%%@@@@@%%%@@=-+#*@@@%%@@@@@@%###@+-%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@%%%@%%%%%=#@@%#*+#@%%%@#%#%%=+#@#*###@%%@%*##@@@%=#%%%%%%@%@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@%%%%%%%%%%%+=%%+***%**=-=*=:-+**#*-::-#=+##@#**#%%*+%%%%%%%%%%@%@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@%%%%%%%%%%%%%%+=##+#@@#+-::::.:-:**%--:..---==#@#**#@+=%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@%%%%%%%%%%%%%%=+#*#%@#-...:-:....+%+:..:-::.::-*%@**%=-#%%%%%%%%%%%%%%@@@@@@@@@@@@@@@
    @@@@@@@@@@@@@%%@%%%%%%%%%%%%%:*#+#@#==*##%@%#+--=%=-==#%%%##*==#@%*#*-*%%%%%%%%%%%%%@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@%%%%%%%%%%%%%%%%#-*###@#@@@@@@@@@@@#=-=#%@@@@@@@@@%%@%***=*%%%%%%%%%%%%%%%@@%@@@@@@@@@@@
    @@@@@@@%@@%%%%%%%%%%%%%%%%%%+-*#%@@+*@@@@@@@@@#=:.:+#@@@@@@@@@#+@@#*%=+###%%%%%%%%%%%%%%%%%@@@@@@@@@
    @@@@@@@%@%%%%%%%%%%%%%%#%%%#==**@@@+-#%@@@@@@#=::-:-=#@@@@@@@%=*@@%*#++###%%%%%%%%%%%%%%%%@@@@@@@@@@
    @@@@@@@@@%%%%%%%%%%%###%####:+#*@@*+-:=++++=:.:+@@@+:::=++*+=:-=#@%*#*=#######%%%%%%%%%@%%%%@@@@@@@@
    @@@@@@@@%@%%%%%%%%#########*.*#*@#*+=---::===--%@@@%=--=----:-=+##%*#*-#######%%%%%%%%%%%%%@@@@@@@@@
    @@@@@@%%%@%%%%%%%##########=:#*%%@%*+**###***+*@@%@@*+***###*++#%@@###-+###########%%%%%%%%%@@@@@@@@
    @@@@@@@@%%%%%%%%%%########*--##@%@@@%@@@@%***+*%#-%%*=***%%@@@@@@@@%*#=:###########%%%%%%%%%@@@@@@@@
    @@@@@@@%%%%%%%%%##########+-=#*@@@@@@@@@@@%+==--=#----++#@@@@@@@@@@#***:+########%%%%%%%%%%%%%%%@@@@
    @@@@@@@%%%%%%%%##########*--+#*@@@@@@@@@@@#+-:::.:.:::-+#@@@@@@@@@@*+*#::##########%%%%%%%%%%@@@@@@@
    @@@@@@%%%%%%%%%##########+:=***@@@@@@#%#@@%*+====-====+*%@@%#%@@@@@#**#::+#########%%%%%%%%%%%%@@@@@
    @@@@@%%#%%%%%%%#########*.:+#+#@@@@@@#**%%**++-=.+.=-=+*#@%*+#@@@@@#@**#::+#######%%%%%%%%%%%%%%@@@@
    %@@@@@@@%%##%%#########*:-+***%@%@@@@#*+*%%%%#*#+*+*###%@%*+##@@@@@@#**%=+:+##########%%%%%%%%@@@@@@
    *+=+=+*#%%%%*+%######*-.***%+*@@@@@@@#*++**##*#**#**###*##+++#@@@@@@#**#***.=#########%%%%%%%%@@@@@@
    @@@@@#*%@%#+-:.:+##**.=+#%#@**@@@@@@@@%#++==+*+*++****++=++*%@@@@@@@@##%##@=:-*#######%%%%%%%@@@@@@@
    @@@@@@%#+*%%%@@=.:..:.+##@#%%%#@@@@@@@@@%***+==-::--==+*++%@@@@@@@@@%+%#%%@+-:::-*####%%%%%%%@@@@@@@
    @@@@@@@@#=---=--+=*=+**##@%%%%#@@@@@@@@@@@@#+-:----::-+#%@@@@@@@@@@@##@%%%##*+++-=*=+##%%%%%@@@@@@@@
    @@@@@@@##%%*+=--+*#***####@@%%#*@@%@@@@@@@@@@%#%@@@@%%@@@@@@@@@@@@@@%#%@@#*++*%#%%=...:-==+*%@@@@@@@
    @@%%#*-.-+*#%#++++*##+*###%@@%%*#@@%@@@@@@@@@@@@@%@@@@@@@@@@@@@@%@@%##@@#+++%%*##*+*=-=+****#@@@@@@@
    @*--::=*+***#%%*+++*#%*+*%##@@%**%@@@@@@@@@@@@+:..:-*@@@@@@@@@@%@@#*#@%#++*@%###**#=**##==-:.:--=*@@
    +-.:=++*++***+%%##++###%*+####@@%*%@@@%@@@@@@+*-::-*#*@@%@@@@%#@@#*%@%#+*#@%***++++*#***+--+*=+#@@+%
    @@%#*++++**+*###%%%*++*##%#**#%%@%##@@@%%@@@@*%%%%@@%+@@@@@@#%@@*#%%##*##@#***+*+**++*+#%%%%@@@@@#%%
    %%%@##++*++*#***#%%%%*+**#%#%***%%%%%%@@%%#@@%#%##%%#@@%%@%#%@%#%%#*####@#**#*+***=+==*++@@%%%%@@@#-
    %%#*###*+**++##*#+*#@@%****%##@##*#%%%#@%@@@%@@+**%*@@@@%*#@%%%%**+*@#%%**#*####+++====*@#-:-=*##%@@
    ##*+*#@%#***+**%%#####@%%##**###%@%%##%%%@%%@@@+++%*@@%%%@@%##****#%%%#*##*####*++===+%#-....:=*#%%@
    *+**++*#@#*##***#@##*%%##%%#%%%#*#%@%##%##%@@@@=++%#%@@@%**+*+++*%@%*###****###*+++#@@#=--:-*+-==+*#
    #**###+*#%%**##*#*%@%%**%%##%####%###@@%%%@@##++=+@#+**#%*#*+*%@@%**@*++**##%#+++**#@#*+=+#=..::-*##
    #********#%%#**#####%@%###*#%%####*##***###%@@=+=+@#*%#***#%@@@#*#@%*****#%%#****#@@%%#*#*---::-**+#
    %%#*******##@%+**####*%@@%#%%#%##****#########:*=+%#+#*#%@@@%**%@@#*#**#%%##**##@@@%%###++====---=++
    @@@@@###**##%%##**#%#%###@@@#*#%%##*****++****:+=+%%+@@@%%##%%@@**%***#@%##%#*#@@@@%%@%%##+++++==+#@
    %%%%#****#%%#%%@@@%%%%%#*##@@@@@@%%%%%%%%###%#=+=+%@+@@%%%%@@%##%%***%%%#%%**%@@%%@@@@%%%#**++*%@@@@
    @%%%@@@#***#%@%%%@@%%%%%%###*%@@%%@@@@@@@@@@@#+*+*%%+@@@@@%##%@%#*#*%@%%@#*#%@%@@%@@@@@@%%**%@@%*+*#
    #%@@%%####**##%@%%%@@%%##%%%%#*#@@@%##%@@@@@@*=*=+%@+%@%#%%@@%#*%#%@%%%@###%@%@@@%@*%@@%*#@@@**++++*
    #*#+=%@@@@##%%%%%@@@@@@%%%%%%@@@###@@@@%%%%%%=##=-*%**@@@@@%#%@%%@@@@@@##%@@@@@@@#*%#**%@@@%##***+**
    ##*++#%@@@%%%%%%%@%++*@@@%%%%@%@@@@%%%###*=----:::--=---=+*##%@@@@@@@%%%%@@@@#++%@%#%@@@@%%%%@###***
    @@@@@%%%%@@@@%@@@+=:.:-::::....::::::::-=+*#%@@@@@@@@@%#*+=-:::..:.::.:::-::::.:=*@@@@@@@%@@%%#%####
    @@@@@@@@@@@@@@@@@+######%%%%%%#%##%%%%%%%%%%%%#@@#@@%%%%%%%%%%%%%#%%%%%%%@@#%%###*@@%@@@@@@@@@%%####
    %%%%%%%%%%@@@@@@@@###*%@@@@@@@@%%@%%%@@@@@*-:::%@#@#=---%@@@@@@@%@%@@@@@@@@@%####@@@@@@@@@@@%#%%@@@@
    @@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@+::::#%#@#----%@@%@@@@%@@@@@@@@@%@@@@@@@@@@@@@%%#@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*::::#%*@#----%@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@%%%@\n\n\t\tKING MALATHOR THE UNDYING!!!\n\n\t\tPress ENTER to continue""")
def victory():
    print("""    .....:................................................................:##-@@#+*@@#-.................
    .....................................:................................+-=%*#@@%#+==*................
    ........................................:........................:....#:......:..+#.................
    .......................................................:..........:..%*++=---=*#**..................
    :...................................................................-+-%###@@@@@@=..................
    ..........................:................:........................*+....-=-:.:*...................
    .................................................................#%++..........:+...................
    .................................................................***-*#%%+:....*:...........-.......
    ................................:...............................-#.:%%@@@@@%%%#-....................
    .............................................................:.-#:...+@@@@@#=*......................
    ..........................................:..................*@-............*-......................
    ..:.....:...............................+*.:%%-....:.:.......##............:#.......................
    .......................................-*.:#@@#=:...........:@=@+++%%@@%***+:..............:........
    ..................................:....:**#@%+-.....-+##*++++@=..:%%@%+*:...........................
    ...............................:........#@@@@%#@#@@**:......:#@+.....::#............................
    ......................:..................**%@@*...-%#@#+#:.....-+%@*..#*............................
    ............................................:.......::*@@#-:....=@@@@@%*:..:........................
    ........................................................*%#:...:....:::..-**:.......................
    ....................................:...................=*%@%:-#*-:..=@=.....-#*....................
    .......................................................:%:...=%*%%#%%%##%%**-:...+*-..:-==-.........
    .....:.................................................#-....:.:*=*@:...:=*%#%#*#-::%%***-*@:.......
    ......................................:...............:%:.........#-...........:+%@@#=.....@*.:.:...
    ...:................................:.................#:.........=#:...............#@@#+..-@=.......
    .....................................................-+.........:#.................:#+%@%%@%........
    .....................................................%:....-....++....:...............-*%%-.........
    ...........................:........................-*....*=....%:..................................
    ....................................................#:...:*:=..+*..............:....................
    ......:.........................:..................-*....#-.*..#-...................................
    .:.............................:...................*-...:%..+.-*....................................
    ......................................-...........:*...:*==.-:#-....................................
    ...:......................:.......................%-....%:--..%.....................................
    ...........:.................:...................-#....#=..+.==.....................................
    ..................:..............................@:...:@:=:=-%:..........:..........................
    ................................................-#....*-.#..=%++==-.................................
    ..........::....................................#.:..-#-.*:.#:......:=-....................:........
    .............................:...............:*##.::.#--=-:-#...........=-................:.........
    ..........................................=*=:.#-...=#.:*..#:.............:=:.......................
    .......................................=%-....+*....*=--#:=*:.....:.....:...:=:.....................
    ...............................:....-#-:....=*%:....#..=..#:===-:............::=....................
    .................................:*+:..:.-*@@%#--:.-+..%.+#*++==++-===-:........+...................
    ..........................=....-%-:.......:.........::-+*%%@%-::==+*#*+=:........+..........:.......
    :............................=*:........................:-++#@@#++**###**:.......:+.................
    ..........................::#............................:-++=++*+==+-:-=%#*-.....:+................
    ..........................++...............:....:.........................:===*....-:...............
    .........................-+.+%@@@@%=:...-*#*:.=%*#*@#=.........=*+=*+=+++=**+-::....#...............
    :.......................=*#@@@@@@@@@#..*%#-=+%#%#%#*--@@*...................:-%%+:..:=..............
    ........................+%@@@@@@@@@@@-.%==#@%%%**%+#+@@@@@-........===*##+==--::.....+:.............
    .............::....::...:@@@@@@@@@@@@##:+*@@%@+#:%#%#@@@@@@....::..-:.........:-=+*:..+.............
    .........................-@@@@@@@@@@@#:*##@%@##:.=*=@@@@@@@=..=:..::.....**==+#*-::...+-...:........
    ...:......................@@@@@@@@@@@-:*==@%#++-...#@@@@@@%=.+::::==...........::--=...+............
    ......:...................@@@@@@@@@@*:#---@#%%-*..-@@@@@@@@--=..:-:...............=*#..+...........:
    .........................+%@@@@@@@@*.=:#**+%-*-#..%@@@@@@@%-#:-:=--=.............:=++..+:...........
    ......................:.*-=%%@@@@%-%@@-#*#+==:*#%+@@@@@@@@+#:+:+=-:..............-+++:.+-...........
    ..:....................*:#%+.+:*+*%@@@*%**=.#-:@+@@@@@@@+-+=:+==.-.............:*#:::..=-....-......
    ......................*=.--*==#**@@@@@-=*+=*-:#*%@@@%%-..:+.:-+-=:.............:=++:...*:..........:
    .....................++.....:*+@@@@@@@:.#+*-:=:+...-:.:+-*-::.:=+..............::=#*-:-*.:..........
    .....................#.......#@@@@@@@*-....#=::=..::-:=+..:--..*:.:..........:+***-...%:*#.:..=@@*.:
    ....................*-......%@@@@@@@%=%:..:#:.:.:+:-+===.---:..*=-:.......=*#+**+%#:.%%#%=#@%#%@%:..
    .:.................:%:......*@@@@@@@@%-:......::--:*-...=+:#.:*-=:..........==::-+**#:%@#@%*:.::....
    ...................:#..........:...-+*..:.....:=-#-=::==:-*--:-=:.....:=*+#%###*=-=%#%-=+*#@@@%*:...
    ...................+-..........................-*:::-*:.=++::*:......++#*%##%%=-=%@%%%*#%%%%%+......
    ........:..........%**-:.....................=*-..-*-:-=...:+#%#*+:..==-##=:-+=#-=#=%@@@@@@@@@%#--:.
    ...................#:%:..%===:...............=....==.:=:*@@@@@%%*#%%=::=+**=+%=-%%*@@@@@%+#*++:=*##:
    ............:......:***=-@..#-:+*:................:*##=%@@@@##%+%%@%%@%:....*-%@@%#@@@@@@@@@@@@:....
    .....................:==-:=*#+--%@@@*:::........:#@=:%@@@%+-%*%++%@@%#:-+=:.-%%#=++==+#%#*+:.:......
    ...................#%-.#:-=#@@@@@@#%+:.#=--*#=-%@%@%%@@#::==#%-.*@@@%####*+###@@%@@%#%#*+*#%%#:.....
    .................:%*..*@@@@@@@@@@#-#@@@@%%#%%@@@@%=-@+..:+-**.%@@@@@@@@@#:==:..=*%@%%%*+--=+:.......
    .................-*.:#*.:%@@@%+#%@#%%@@@@%@@@@@#:%@=.-:-*=#:-*@@@@@@%#+#%@@@@@@@%*#*++*#%%#+:.......
    ..................*.-:..:--=++**##++*:-*==*@%@%@#-.=*=*-%*%%@%*+%%@@@*++-:==*%%@@@%#%@%:............
    ..................-=-%-:-..........:..........:::++*=-%#@@%@%%@#=:=#@%@%*-:..:+%%#=:.............:..
    ...................#%+++**#*+#:.......+--*=:=:.+==*:#@@@%%%%%@%%#=::=--+#%%%%%#:..............::===.
    ..............:....#:=:#**-#:#+#=:*=:+:=*:+-*:*==#%+#@+-#%%+++%%@@@@@%#*-::......-+*#**++-:::..:....
    ..................:%..:.....++*.=*-+-+..=--==-:=#:%%%#@@%%%*@@@%=:...::-*%**=-::=+*+*+*=.........:..
    ..................:#............:.........:*=#%++=+#=@@#+=:.:=+#%@@%%#*++++++:--+**##*=-............
    .:.................+:.................+.:*#-.#@@@@@%.-#@@@@@@%##%#%@@%##*+-:........................
    .....................*=-:..........:=#*=..:@@%@@@%%%@%##%*##*+=..............................:......
    ..................::......:----==-:........:-:..-*+=-:........=-...:.............:..................
    .........:...................................................::.....................................
    ....................................................................................................
    ....................................................................................:...............""")


#--Main code----------------------------------------------------

dndclass = 0
clear()
print("\t\t\tWelcome to the DND BOSS FIGHT!")

#initialize variables to use in while loops
bossretry = "y"



while bossretry == "y":
    
    dndclass = classpicker()

    clear() 
    print("You step into a dark underground chamber, the air heavy with decay. From a shattered sarcophagus rises...")
    
    malathor()
    
    print("\tHis glowing eye sockets fixed on you as he raises his rusted sword.")
    input(" \n\tPress ENTER to fight!")

    #START OF FIGHT

    bosshealth = 150
    playerhealth = 100
    playermaxhealth = 100
    healthpotions = 5
    inventory = ["Potion of strength", "Amulet of health", "Rusty shield", "Ring of protection", "Fireball in a bottle"]
    activeitems = []
    bossfire = 0
    groundloot = 0
    #possible ground loot drops
    groundlootitems = ["Healing potion", "Potion of strength", "Amulet of health", "Potion of invisibility", "Rusty shield", "Fireball in a bottle", "Ring of protection", "Healing potion", "Rusty key", "Bag of gold"]
    while bosshealth > 0 and playerhealth > 0:
        clear()
        #groundloot = 2
        groundloot = diceroll(2) # 50% chance to find something on the ground to add to your inventory
        print(f"\tGROUNDLOOT ROLL: {groundloot}\n")
        
        
        if groundloot == 2:
            grounditem = diceroll(10) #randomly choose between 10 different items
            
            ground(grounditem)

        
        choiceloop = 0
        while choiceloop == 0:
            
            if len(activeitems) > 0:
                print(f"\tActive items: {len(activeitems)}")
                print("|----------------------------|")
                for i in range(0,len(activeitems)):
                    print(f"| {i + 1:3}. {activeitems[i]:22}|")
                print("|----------------------------|")
            playerchoice = input(f"\n\tChoose your action: Attack [1], Heal [2], or Inventory [3]?\n\n\tYou currently have {playerhealth} health: \n\n\t").lower()
            if playerchoice == "attack" or playerchoice == "1":
                clear()
                attack = diceroll(20)  # Attack roll between 1 and 20

                #handle item effects
                if "Potion of strength" in activeitems:
                    print(f"\tInitial attack roll is {attack}, with a +5 bonus from the strength potion!")
                    attack += 5
                    activeitems.remove("Potion of strength")
                if "Fireball in a bottle" in activeitems:
                    attack += 10
                    print(f"\tThe fireball flies out of the jar and hits King Malathor directly, dealing 10 damage! he is now on fire for 3 turns")
                    bossfire += 3
                    activeitems.remove("Fireball in a bottle")
                #handle class bonuses
                if dndclass == "barbarian":
                    attack += 5  # Barbarian bonus
                    bosshealth -= attack
                    input(f"\n\tYou attacked for {attack} damage, +5 from class bonus! king Malathor's health is now {bosshealth}. Press ENTER to continue\n")

                elif dndclass != "barbarian":
                    bosshealth -= attack  # No bonus for Rogue or Paladin
                    input(f"\n\tYou attack for {attack} points! King Malathor's health is now {bosshealth}. Press ENTER to continue\n")

                # Exit the loop after a successful action
                choiceloop = 1

            elif playerchoice == "heal" or playerchoice == "2":
                if healthpotions > 0:
                    if playerhealth == playermaxhealth:
                        input("\n\tYou are already at full health! Press ENTER to continue\n")
                        choiceloop = 0

                    elif playerhealth + 20 > playermaxhealth:
                        playerhealth = playermaxhealth  # Heal to max health
                        healthpotions -= 1
                        print(f"\n\tYou are at full health! You have {healthpotions} health potions left.\n")
                        
                        choiceloop = 0
                    else:
                        playerhealth += 20  # Heal for 20 points
                        healthpotions -= 1
                        print(f"\n\tYou healed for 20 points! Your new health is {playerhealth}, and you have {healthpotions} health potions left.\n")
                        
                else:
                    input("\n\tYou have no health potions left! Press ENTER to continue.")

            elif  playerchoice == "inventory" or playerchoice == "3" and len(inventory) == 0:
                input("Your inventory is empty! press enter to continue")

            elif playerchoice == "inventory" or playerchoice == "3" and len(inventory) > 0:
                print("\tInventory:\n|------------------------------|")
                for i in range(0,len(inventory)):
                    print(f"|{i + 1:3}. {inventory[i]:25}|")
                print("|------------------------------|")
                invchoice = input("Which item would you like to use? type 'back' to select a different option: ").lower()
                if invchoice == "back":
                    choiceloop = 0
                else:
                    try:
                        invchoice = int(invchoice) - 1
                        if invchoice > len(inventory) - 1:
                            print("\t\t***INVALID ENTRY***")
                        else:
                            print(f"\nYou chose to use {inventory[invchoice]}!\n")
                            chosenitem = useitem(invchoice)
                            if chosenitem == 0:
                                input("Press enter to continue")
                            else:
                                activeitems.append(chosenitem)
                                input("press enter to continue")
                            
                    except ValueError:  #<-- only activates if the user enters a non int
                        print("***INVALID ENTRY!***")

            elif playerchoice == "uuddlrlrba":  #instakill cheat code to speed up runs
                print("***CHEAT CODE ACTIVATED!***")
                time.sleep(1)
                bosshealth = -1
                choiceloop = 1

            if "Rusty key" in activeitems:
                            grounditem = diceroll(10) - 1
                            input(f"\nYou opened the chest and found {groundlootitems[grounditem]} and added it into your inventory!")
                            inventory.append(groundlootitems[grounditem])
                            activeitems.remove("Rusty key")
            elif playerchoice != "uuddlrlrba" and playerchoice != "attack" and playerchoice != "heal" and playerchoice != "inventory" and playerchoice != "1" and playerchoice != "2" and playerchoice != "3":  # Handle invalid entries
                input("\n\t\t***INVALID ENTRY***\nPress Enter to retry: ")
            if bossfire > 0:
                firedmg = diceroll(10)
                bosshealth -= firedmg
                print(f"King Malathor was burned by the fireball for an additional {firedmg} damage! His health is now {bosshealth}")
                bossfire -= 1

        #Bosses turn:
        if bosshealth > 0 and choiceloop != 0:   #make sure boss cant attack after he dies  
            time.sleep(.5)
            if "Potion of invisibility" in activeitems:
                input("\tKing Malathor swings his sword wildly, confused as to where you went! He completely misses!\n\tPress Enter to continue")
                activeitems.remove("Potion of invisibility")
            else:
                bossattack = random.randint(1,3)
                
                #shuffle between bosses 3 attacks at random
                if bossattack == 1:
                    print("\n\tKing malathor raises his enchanted sword and attacks you!")
                    time.sleep(.5)
                    
                    evasion = diceroll(100)   #random roll to dodge attacks
                    
                    if dndclass == "rogue":
                        print(f"\n\tevasion roll: {evasion}, + 10 from class bonus!\n")
                        evasion = evasion + 10   #bonus from class

                    if evasion >= 75:
                        print(f"\n\tevasion roll: {evasion}\n\tEvasion needed to dodge: 75")
                        input("\n\tYou dodged the attack! press ENTER to continue.")
                        
                    else:
                        print(f"\n\tevasion roll: {evasion}\n\tEvasion needed to dodge: 75")
                        bossattackdmg = diceroll(15)
                        if "Ring of protection" in activeitems and "Rusty shield" not in activeitems:
                            activeitems.remove("Ring of protection")
                            if dndclass != "paladin":
                                if bossattackdmg > 3:
                                    bossattackdmg -= 3
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou Block 3 damage from the ring of protection, but feel it snap in half! You took {bossattackdmg} damage and your health is not {playerhealth}.")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 3:
                                    print("\tYou raised your shield and fully blocked the hit, breaking the shield in half!")
                                    input("\tPress Enter to continue")
                            else:
                                bossattackdmg -= 10
                                if bossattackdmg > 10:
                                    bossattackdmg -= 10
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou took {bossattackdmg + 10} damage from King Malathor's attack, but negated 5 from your class and blocked another 5 with the shield, breaking it in half! your health is now {playerhealth}")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 10:
                                    input("\tYou blocked the attack due to your class bonus and the ring!\n\tPress enter to continue")

                        elif "Rusty shield" in activeitems and "Ring of protection" not in activeitems:
                            activeitems.remove("Rusty shield")
                            if dndclass != "paladin":
                                if bossattackdmg > 5:
                                    bossattackdmg -= 5
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou Block 5 damage with the rusty shield, breaking it in the process! You took {bossattackdmg} damage and your health is now {playerhealth}.")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 5:
                                    print("\tYou raised your shield and fully blocked the hit, breaking the shield in half!")
                                    input("\tPress Enter to continue")
                                else:
                                    print("\tYou raised the shield and blocked the attack!")
                                    input("\tPress Enter to continue")
                            else:
                                
                                if bossattackdmg > 10:
                                    bossattackdmg -= 10
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou took {bossattackdmg + 10} damage from King Malathor's attack, but negated 5 from your class and blocked another 5 with the shield, breaking it in half! your health is now {playerhealth}")
                                    input("\tPress Enter to continue")
                                else:
                                    input(f"King Malathor attacked for {bossattackdmg} damage, but you blocked 5 from your class ability and another 5 from the shield, breaking it in half!\nPress Enter to continue")
                        
                        elif "Rusty shield" in activeitems and "Ring of protection" in activeitems:
                            activeitems.remove("Ring of protection")
                            activeitems.remove("Rusty shield")
                            if dndclass != "paladin":
                                if bossattackdmg > 8:
                                    bossattackdmg -= 8
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou Block 3 damage from the ring of protection and 5 from the shield, but break both! You took {bossattackdmg} damage and your health is now {playerhealth}.")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 8:
                                    print("\tYou raised your shield and fully blocked the hit, breaking the shield in half and destroying the ring!")
                                    input("\tPress Enter to continue")
                            else:
                                bossattackdmg -= 13
                                if bossattackdmg > 13:
                                    bossattackdmg -= 13
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou took {bossattackdmg + 13} damage from King Malathor's attack, but negated 5 from your class bonus and blocked another 8 with the shield and ring, breaking both! your health is now {playerhealth}")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 13:
                                    input("\tYou raised the shield and blocked King Malathor's attack, breaking the shield and the ring!\n\tPress enter to continue")
                        elif dndclass == "paladin" and "Rusty shield" not in activeitems and "Ring of protection" not in activeitems:
                            if bossattackdmg > 5:
                                damage_taken = bossattackdmg - 5
                                playerhealth -= damage_taken
                                input(f"\tYou took {bossattackdmg} damage from King Malathor's attack, but resisted 5 from your class bonus! Your health is now {playerhealth}. Press ENTER to continue")
                            else:
                                input(f"\tKing Malathor attacked for {bossattackdmg}, but you resisted it from your class bonus! Press ENTER to continue")

                                        
                        else:
                            playerhealth -= bossattackdmg
                            input(f"\tYou took {bossattackdmg} points from King Malathor's attack! Your health is now {playerhealth}. press ENTER to continue")
                            
                elif bossattack == 2:
                    print("\n\tKing malathor summons a skeleton to fight you!")
                    time.sleep(.5)
                    
                    evasion = diceroll(100)
                    
                    if dndclass == "rogue":
                        print(f"\n\tevasion roll: {evasion}, + 10  from class bonus!")
                        evasion = evasion + 10   #bonus from class

                    if evasion >= 85:
                        print(f"\n\tevasion roll: {evasion}\n\tEvasion needed to dodge: 85")
                        input("\tYou dodged the attack! press ENTER to continue.")
                        
                    else:
                        print(f"\n\tevasion roll: {evasion}\n\tEvasion needed to dodge: 85")
                        bossattackdmg = diceroll(10)

                        if "Ring of protection" in activeitems and "Rusty shield" not in activeitems:
                            activeitems.remove("Ring of protection")
                            if dndclass != "paladin":
                                if bossattackdmg > 3:
                                    bossattackdmg -= 3
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou Block 3 damage from the ring of protection, but feel it snap in half! You took {bossattackdmg} damage and your health is not {playerhealth}.")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 3:
                                    print("\tYou raised your shield and fully blocked the hit, breaking the shield in half!")
                                    input("\tPress Enter to continue")
                            else:
                                bossattackdmg -= 10
                                if bossattackdmg > 10:
                                    bossattackdmg -= 10
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou took {bossattackdmg + 10} damage from King Malathor's attack, but negated 5 from your class and blocked another 5 with the shield, breaking it in half! your health is now {playerhealth}")
                                    input("\tPress Enter to continue")
                                else:
                                    print("\tYou blocked the attack, breaking the ring in the process!")
                                    input("\tPress Enter to continue")

                        elif "Rusty shield" in activeitems and "Ring of protection" not in activeitems:
                            activeitems.remove("Rusty shield")
                            if dndclass != "paladin":
                                if bossattackdmg > 5:
                                    bossattackdmg -= 5
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou Block 5 damage with the rusty shield, breaking it in the process! You took {bossattackdmg} damage< and your health is not {playerhealth}.")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 5:
                                    print("\tYou raised your shield and fully blocked the hit, breaking the shield in half!")
                                    input("\tPress Enter to continue")
                                else:
                                    print("\tYou raised the shield and blocked the attack!")
                                    input("\tPress Enter to continue")
                            else:
                                bossattackdmg -= 10
                                if bossattackdmg > 10:
                                    bossattackdmg -= 10
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou took {bossattackdmg + 10} damage from King Malathor's attack, but negated 5 from your class and blocked another 5 with the shield, breaking it in half! your health is now {playerhealth}")
                                    input("\tPress Enter to continue")
                                else:
                                    input(f"\tYou raised your shield and blocked King Malathor's atatck, but the shield broke in half!\n\tPress Enter to continue")
                        
                        elif "Rusty shield" in activeitems and "Ring of protection" in activeitems:
                            activeitems.remove("Ring of protection")
                            activeitems.remove("Rusty shield")
                            if dndclass != "paladin":
                                if bossattackdmg > 8:
                                    print(f"\tKing malathor attacked for {bossattackdmg} damage")
                                    bossattackdmg -= 8
                                    playerhealth -= bossattackdmg
                                    print(f"\tYou Block 3 damage from the ring of protection and 5 from the shield, but break both! You took {bossattackdmg} damage and your health is now {playerhealth}.")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 8:
                                    print("\tYou raised your shield and fully blocked the hit, breaking the shield in half and destroying the ring!")
                                    input("\tPress Enter to continue")
                            else:
                                bossattackdmg -= 13
                                if bossattackdmg > 13:
                                    bossattackdmg -= 13
                                    playerhealth -= bossattackdmg
                                    print(f"t\You took {bossattackdmg + 13} damage from King Malathor's attack, but negated 5 from your class bonus and blocked another 8 with the shield and ring, breaking both! your health is now {playerhealth}")
                                    input("\tPress Enter to continue")
                                elif bossattackdmg <= 13:
                                    input("\tYou raised the shield and blocked King Malathor's attack, breaking the shield and the ring!\n\tPress enter to continue")

                        elif dndclass == "paladin" and "Rusty shield" not in activeitems and "Ring of protection" not in activeitems:
                            if bossattackdmg > 5:
                                damage_taken = bossattackdmg - 5
                                playerhealth -= damage_taken
                                input(f"\tYou took {bossattackdmg} damage from King Malathor's attack, but resisted 5 from your class bonus! Your health is now {playerhealth}. Press ENTER to continue")
                            else:
                                input(f"\tKing Malathor attacked for {bossattackdmg}, but you resisted it from your class bonus! Press ENTER to continue")

                                        
                        else:
                            playerhealth -= bossattackdmg
                            input(f"\tYou took {bossattackdmg} points from King Malathor's attack! Your health is now {playerhealth}. press ENTER to continue")

                elif bossattack == 3:
                    print("\n\tKing malathor hurls a boulder towards you!")
                    time.sleep(.5)
                    
                    evasion = diceroll(100)
                    
                    if dndclass == "rogue":
                        print(f"\n\tevasion roll: {evasion}, + 10 from class bonus!\n")
                        evasion = evasion + 10   #bonus from class

                    if evasion >= 65:
                        print(f"\n\tevasion roll: {evasion}\n\tEvasion needed to dodge: 65")
                        input("\tYou dodged the attack! press ENTER to continue.")
                        
                    else:
                        print(f"\n\tevasion roll: {evasion}\n\tEvasion needed to dodge: 65")
                        bossattackdmg = diceroll(20)

                        if "Ring of protection" in activeitems and "Rusty shield" not in activeitems:
                            activeitems.remove("Ring of protection")
                            if dndclass != "paladin":
                                if bossattackdmg > 3:
                                    bossattackdmg -= 3
                                    playerhealth -= bossattackdmg
                                    print(f"You Block 3 damage from the ring of protection, but feel it snap in half! You took {bossattackdmg} damage and your health is not {playerhealth}.")
                                    input("Press Enter to continue")
                                elif bossattackdmg <= 3:
                                    print("You raised your shield and fully blocked the hit, breaking the shield in half!")
                                    input("Press Enter to continue")
                            else:
                                bossattackdmg -= 10
                                if bossattackdmg > 10:
                                    bossattackdmg -= 10
                                    playerhealth -= bossattackdmg
                                    print(f"You took {bossattackdmg + 10} damage from King Malathor's attack, but negated 5 from your class and blocked another 5 with the shield, breaking it in half! your health is now {playerhealth}")
                                    input("Press Enter to continue")
                                else:
                                    print("\tYou blocked the attack but broke the ring in the process!")
                                    input("\tPress Enter to continue")

                        elif "Rusty shield" in activeitems and "Ring of protection" not in activeitems:
                            activeitems.remove("Rusty shield")
                            if dndclass != "paladin":
                                if bossattackdmg > 5:
                                    bossattackdmg -= 5
                                    playerhealth -= bossattackdmg
                                    print(f"You Block 5 damage with the rusty shield, breaking it in the process! You took {bossattackdmg} damage< and your health is not {playerhealth}.")
                                    input("Press Enter to continue")
                                elif bossattackdmg <= 5:
                                    print("You raised your shield and fully blocked the hit, breaking the shield in half!")
                                    input("Press Enter to continue")
                                else:
                                    print("\tYou raised the shield and blocked the attack!")
                                    input("\tPress Enter to continue")
                            else:
                                bossattackdmg -= 10
                                if bossattackdmg > 10:
                                    bossattackdmg -= 10
                                    playerhealth -= bossattackdmg
                                    print(f"You took {bossattackdmg + 10} damage from King Malathor's attack, but negated 5 from your class and blocked another 5 with the shield, breaking it in half! your health is now {playerhealth}")
                                    input("Press Enter to continue")
                                else:
                                    input(f"King Malathor attacked for {bossattackdmg} damage, but you blocked 5 from your class ability and another 5 from the shield, breaking it in half!\nPress Enter to continue")
                        
                        elif "Rusty shield" in activeitems and "Ring of protection" in activeitems:
                            activeitems.remove("Ring of protection")
                            activeitems.remove("Rusty shield")
                            if dndclass != "paladin":
                                if bossattackdmg > 8:
                                    bossattackdmg -= 8
                                    playerhealth -= bossattackdmg
                                    print(f"You Block 3 damage from the ring of protection and 5 from the shield, but break both! You took {bossattackdmg} damage and your health is now {playerhealth}.")
                                    input("Press Enter to continue")
                                elif bossattackdmg <= 8:
                                    print("You raised your shield and fully blocked the hit, breaking the shield in half and destroying the ring!")
                                    input("Press Enter to continue")
                            else:
                                bossattackdmg -= 13
                                if bossattackdmg > 13:
                                    bossattackdmg -= 13
                                    playerhealth -= bossattackdmg
                                    print(f"You took {bossattackdmg + 13} damage from King Malathor's attack, but negated 5 from your class bonus and blocked another 8 with the shield and ring, breaking both! your health is now {playerhealth}")
                                    input("Press Enter to continue")
                                elif bossattackdmg <= 13:
                                    input("You raised the shield and blocked King Malathor's attack, breaking the shield and the ring!\nPress enter to continue")

                        elif dndclass == "paladin" and "Rusty shield" not in activeitems and "Ring of protection" not in activeitems:
                            if bossattackdmg > 5:
                                damage_taken = bossattackdmg - 5
                                playerhealth -= damage_taken
                                input(f"\tYou took {bossattackdmg} damage from King Malathor's attack, but resisted 5 from your class bonus! Your health is now {playerhealth}. Press ENTER to continue")
                            else:
                                input(f"\tKing Malathor attacked for {bossattackdmg}, but you resisted it from your class bonus! Press ENTER to continue")
                   
                        else:
                            playerhealth -= bossattackdmg
                            input(f"\tYou took {bossattackdmg} points from King Malathor's attack! Your health is now {playerhealth}. press ENTER to continue")

        if bosshealth <= 0:
            print("\n\tYou have defeated KING MALATHOR THE UNDYING!\n")
            victory()
            time.sleep(1)
            
            input("Press ENTER to claim his sword and return to the surface.")
            bossretry = input("\n\t\tWould you like to fight the boss again? [y/n]: ").lower()
        elif playerhealth <= 0:
            print("\n\tYou have been defeated!")
            time.sleep(1)
            bossretry = input("Would you like to retry? [y/n]: ").lower()