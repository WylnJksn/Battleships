import os
import string
import asciiart


#Need to add segment that reads player's inputs for placing down thier ships at the beginning of the game, and it needs to check if
#it is valid ship placement as well. 




asciihit ="""                    ....         .....         ...    ..+*-.     .....                      
                            :#########+.     -#####-      :####=  +######:   +#####.                     
                        .+###+=====+*#=.-++#########-..=##**######*+###*###*+#####:  ..                
                      .+#*===::-=====*####++===++*####*++=++*##*+====*###+===+###+:-##+.              
                 .==########+==...:=+++==*#*========+*###*=====+##+======*#*+====+####**####=.           
                :###*====+#*==-..:=######+#*====-====+##+=======*#+==:.-==*+==-===##*+==*####-.          
                :*##============:.-#*===+###*=-.....-==+#+=-...:==#+-....:===:..-=*#========##*:          
                :*#==-:...-*####*+=*======++=-.......-===-:.....:--:::::::-:....-=-:...:====##*:          
                .###==:...-##+==++##*==:=*####+.......-=+*-...=*=...=*######:.........--====*##*:          
                .###=-:...:-..:-==+*+=:-*#######-.....-*###=.-###*+##*===+*##-...+++###*+=**##-.           
            ::::-##==-:.........:-====.=#**==+##+:...+###*##*+#++####+=--=+##-..*###****#+=*###-.          
        .-##***===--....:........:--.-#+=--::=##=...+#+===*##+--=##+-...:-=+:.+#*+-:..-=#+==*###-         
        .*#=====::....:=-............:=:.....:==-...-==-:-===:..:=*+-........=#+==:....-=*+==*###:        
        .*#=====:...==+#-......:=-......:-.....:....:::....:......::.........-*+:.......-+*+==+###:       
        .*#==========+##-....:====-.....:===-......:==-.....................-==:.........::-====##*:      
        .=##+=======*##=-...:-====-:....:=+*=:.....-**+=-::....:-=-:........:-:..:::::......====###*:     
            ###*****##*===-:-=+*#====-..:=+###+=----+###+==-:.:=====:............-=+#*==-..:====*###*:     
            .+*#######========*##+====:-==+#####*+++*###*===========-:........::-===*##*+=====++###*:      
                    .#*======+####=======+###############+======+#+===-......-==###+=##############.       
                    .#########*###*=====*###=-#*+####++###+*#######+============#################*.        
                    =#####*-- :#####**####*:-#*--==+=-:+##*==##*-*#+=========+###+-----*#####=-.          
                                .:=#######*. -#*-:--==-:==:..-*#= .*###******####:         .:              
                                    :=====-   -#*-.:===-.:=:---*#=   -*########+=.                          
                                            -#*-:-=---.:=::--*#=     -*******-                            
                                            -#*--==---.:=:---*#=                                          
                                            -#*--====-.:=:---*#=                                          
                                            -#*--==--=-:==-.-*#=                                          
                                            -#*--==--=====-:-*#=                                          
                                            -#*--==--==-==-:=*#=                                          
                                            -#*--==--=-:==-:=*#=                                          
                                            -#*--=====-:==-:=*#=                                          
                                        ..   -#*=======-:=:..-*#=                                          
                                    .*##+..-#*-..:======:..-*#=    ..                    .               
                            .===   .+#####**#*-..:======:-++##=   -*#+.      -=.        =*+.             
                            .####*-:+#*+=+####+:.-*##+===*#####*--+*#####*: =+*##*:  .=######.            
                    .-#*:  .##*+#####=====+###++######+*###*######***####=*#######-.:*##+=*###=:  .:#-.  
                    :*#######*===+###*======+####*==*######*=*###+======*#####+=*#######=====####:*####-  
            .:**+::*##===+*#*=====+*=========+#+=====+##+====**========+###+=====*####+=====*#########*: 
            :*########+==================================================*##+==:-==###+=======+##+===##*: 
            .*##+===+#+===:.:====:..:===-:.:--=================================-..:-=======:::========+#*: 
            .*#==========-....:=-...:===-....:-=====-========-====-:...:======-:....:====-:....-=======##*.
        .-####*=====.:-===:....:-....:==:.....:===:..-===:...:===-.......:===-:......-==-......:========#*.
        .*#=========:...:=-:...:-.....:-......:=-.....-=-.....-==:.........--:........-=:......:--:..:==#*.
        .*#+====:.:===.........................:-...............--.....................-:..............==#*.
        .+*==:::....::..................................................................................:**."""




asciimiss ="""                                                                                                 
                                                                                                              
                                                 ::....                                                       
                                                :-:....:                                                      
                                                :-:...::                                                      
                                                 -=...:                                                       
                            .:...                                                                             
                             .:.                                         ::..                                 
                       ...     .:.:                                     .-...    ....                         
                      .:..:     -..       :..        :.                .-:.     :--....                       
                        ::::.   ....      ::.       :::        ::..    =:..     .=-=.:.                       
                          ..:.   .:::..   ::.       -::.       =:.    =::.  .                                 
                           ....  .:....   .-::    .::::.     .-:::. ==-:::=:::                                
                           ...:. ....:::.:::::::::-:::-:::-:-----..--=::=:=..                                 
                            .-::--::::::----:-::-::-::-------===-.:=+-==:--.                                  
                             .:::---::.::-----:-=..:=----=--==-=--==+:--:::.                                  
                         .....:------:..:..::-:---..::---+-=+::::-==-::::-:....                               
                ..........:::::-===---=-:-:-:-:-::::::=..-::=--:-:::::::::::....:..:.....                     
          .........::::::::--==-===+=====:--==----=---=--:::-::-:::---=-==*+--:::::......::..                 
      ........:::::::::--=------===+====-====-=---::-----=:-----------=====+--+*=::::::.......:...            
    .........:::::::::=------=--====+--==+====*--==--=--=+---:--=+-----==-:-++---*=::::::.......:....         
  ..:.........::::::::-----=-----=====--=------=-===:=---=--=::-:-===-=--=----::::-:::::::.............       
 .............:::::-::::::----===+=-:-=-------=------=---==-----=-::------::::::::::::::::........:....       
   ............:::::::::::::::::-------=-=-=-=--:-::::----------------::::::::::::::::-:..............        
    ..............::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::..............          
        ...............::::-.:-::::::::::::::::::::::::::::::::::::-::::::::::::..................            
             ...................::::::-::-:::-::::-::--:::::::::::-:::::::....................                
                    .....................................:......::....:........:....  .. ..                   
                              . ............................:........      .   .  ..                          
                                                                .  .                            """



#Need to add segment that reads player's inputs for placing down thier ships at the beginning of the game, and it needs to check if
#it is valid ship placement as well. 


basic_grid = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]",
        "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]





#at game start
p1_grid = basic_grid[:]
p1_attack_grid = basic_grid[:]
p2_grid = basic_grid[:]
p2_attack_grid = basic_grid[:]



Ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2,
}

#start of reading player attack coordinates and 
row_input = input("Please input a row letter.")
column_input = int(input("Please input a column number."))
#attack_coordinates = str(str(row_input) + str(column_input))
"""attack_index = 0"""
"""row_index = 0"""
"""column_index = 0"""

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ShipCheck():
    #This will be where the program will check to see if all segments of any ship have been hit. If so, then it will print out "You sank (opposite player)'s (specific ship)."
    #The program will then check if all of the enemy player's ships have been sunk, determining a game end or not.
    pass

def RowCheck(row_input):
    valid_row = False
    #I know for a fact this is inefficient. But if it works it works, I guess. I just gotta not make it a habit.
    while valid_row != True:
        if row_input == "A" or row_input == "a":
            row_index = 0
            valid_row = True
            return row_index
            break
        elif row_input == "B" or row_input == "b":
            row_index = 10
            valid_row = True
            return row_index
            break
        elif row_input == "C" or row_input == "c":
            row_index = 20
            valid_row = True
            return row_index
            break
        elif row_input == "D" or row_input == "d":
            row_index = 30
            valid_row = True
            return row_index
            break
        elif row_input == "E" or row_input == "e":
            row_index = 40
            valid_row = True
            return row_index
            break
        elif row_input == "F" or row_input == "f":
            row_index = 50
            valid_row = True
            return row_index
            break
        elif row_input == "G" or row_input == "g":
            row_index = 60
            valid_row = True
            return row_index
            break
        elif row_input == "H" or row_input == "h":
            row_index = 70
            valid_row = True
            return row_index
            break
        elif row_input == "I" or row_input == "i":
            row_index = 80
            valid_row = True
            return row_index
            break
        elif row_input == "J" or row_input == "j":
            row_index = 90
            valid_row = True
            return row_index
            break
        else:
            print("Please input a valid row letter.")
            row_input = input("Please input a row letter.")

#I need to implement a check into both the valid_row and valid_column input checks that checks
#if they put a different type than they're supposed to (i.e. an integer for the row or a string for the column).
def ColumnCheck(column_input, row_index):
    valid_column = False
    while valid_column != True:
        if column_input == 1:
            attack_index = row_index
            valid_column = True
            return attack_index
            break
        elif column_input < 1 or column_input > 10:
            print("Please enter a valid column number.")
            column_input = int(input("Please input a column number."))
        else:
            column_index = column_input
            attack_index = row_index + column_index - 1
            valid_column = True
            return attack_index
            break
#if attack_coordinates:

#this will check to see if the coordinate that the player is attacking is occupied by an enemy or not, indicating a hit or miss
#it will also check if the player's already attacked there
def coordinates_check(enemy_grid, player_attack_grid, row_input, column_input):    
    valid_coords = False
    while valid_coords != True:
        row_index = RowCheck(row_input)
        attack_index = ColumnCheck(column_input, row_index)
        if enemy_grid[attack_index] == "[ ]" or enemy_grid[attack_index] == "[#]":
            if player_attack_grid[attack_index] == "[X]" or player_attack_grid[attack_index] == "[O]":
                print("Please input coordinates that haven't been attacked yet.")
                row_input = input("Please input a row letter.")
                column_input = input("Please input a column number.")
            else:
                valid_coords = True
        else:
            print("Please input valid coordinates.")
            row_input = input("Please input a row letter.")
            column_input = int(input("Please input a column number."))
    return attack_index


def checkWinner(grid):
    functional_part = "[#]"
    ship_check = [i for i in grid if i == functional_part]
    return len(ship_check) > 0







p1_total_segments = 0
p2_total_segments = 0

print("Welcome to Battleship!")

# Get player names
player1_name = input("Player 1, please enter your name: ")
player2_name = input("Player 2, please enter your name: ")

def get_valid_row():
    while True:
        row_input = input("Enter row (A-J): ").upper()
        if row_input in string.ascii_uppercase[:10]:
            return string.ascii_uppercase.index(row_input)
        print("Invlaid row")
def get_valid_column():
    while True:
        col_input = input("Enter row (1-10): ")
        if col_input.isdigit():
            col = int(col_input)
            if 1 <= col <= 10:
                return col - 1
        print("Invalid column.")

def place_ship(grid, ship_length, name):
    while True:
        print(f"\nPlacing {name} (length {ship_length})")
        row = get_valid_row()
        col = get_valid_column()
        direction = input("Direction (H or V): ").upper()

        if direction == "H":
            if col + ship_length >10:
                print("Ship doesn't fit horizontally.")
                continue
            if any(grid[row * 10 + col + i] != "[]" for i in range(ship_length)):
                print("Overlap detected.")
                continue
            for i in range(ship_length):
                grid[row * 10 + col + i] = "[#]"
                break
        elif direction == "V":
            if row + ship_length >10:
                print("Ship doesn't fit vertically.")
                continue
            if any(grid[(row + i) * 10 + col] != "[]" for i in range(ship_length)):
                print("Overlap detected.")
                continue
            for i in range(ship_length):
                grid[(row + i) * 10 + col] = "[#]"
            break
        else:
            print("Invalid direction")
            



print(f"{player1_name}, it's your turn to attack!")



def ShipCheck():
    global p1_total_segments, p2_total_segments
    p1_remaining = p1_grid.count("[#]")
    p2_remaining = p2_grid.count("[#]")

    if p2_remaining < p2_total_segments:
        print("You hit Player 2's ship!")
        p2_total_segments = p2_remaining
    
    if p1_remaining < p1_total_segments:
        print("You hit Player 1's Ship!")
        p1_total_segments = p1_remaining

    if p1_remaining == 0:
        print(f"\nCongratulations {player1_name}, you win! All of {player2_name}'s ships are sunk.")
        exit()

    if p2_remaining == 0:
        print(f"\nCongratulations {player2_name}, you win! All of {player1_name}'s ships are sunk.")
        exit()
    

def attack(attacker_grid, defender_grid, attacker_name):
    print(f"\n{attacker_name}'s turn to attack.")
    while True:
        row = get_valid_row()
        col = get_valid_column()
        index = row * 10 + col

        if attacker_grid[index] in ["[X]", "[O]"]:
            print("You've already attacked here.")
            return False
        
        if defender_grid[index] == "[#]":
            print(f"Hit! {attacker_name} struck the enemy ship!")
            attacker_grid[index] = "[X]"
            defender_grid[index] = "[X]"
        else:
            print(f"Miss! {attacker_name} missed this time.")
            attacker_grid[index] = "[O]"
        return True

    ShipCheck()



print(f"\nWelcome, {player1_name} and {player2_name}!")

print(f"\n{player1_name}, place your ships:")
for name, length in Ships.items():
    place_ship(p1_grid, length, name)
p1_total_segments = p1_grid.count("[#]")



print(f"\n{player2_name}, place your ships:")
for name, length in Ships.items():
    place_ship(p2_grid, length, name)
p2_total_segments = p2_grid.count("[#]")

#Need to input the variable's that store each player's names into the code below.
while True:
    #p1 attack sequence
    print("""player1 name variable""" + "'s turn.")
    print("Your grid:")
    print(p1_grid)
    print("Attack grid:")
    print(p1_attack_grid)
    row_input = input("Please input a row letter.")
    column_input = int(input("Please input a column number."))
    attack_index = coordinates_check(p2_grid, p1_attack_grid, row_input, column_input)
    if p2_grid[attack_index] == "[ ]":
        print() #insert "miss" message  and ascii art
        p1_attack_grid[attack_index] = "[O]"
    else:
        print() #insert hit message  and ascii art
        p1_attack_grid[attack_index] = "[X]"
        p2_grid[attack_index] = "[X]"
    ShipCheck()
    if not checkWinner(p2_grid):  # Check if Player 2 has lost
        print("""player1 name variable""" + " wins!")
        break
    clear_terminal()
    
    #p2 attack sequence
    print("""player2 name variable""" + "'s turn.")
    print("Your grid:")
    print(p2_grid)
    print("Attack grid:")
    print(p2_attack_grid)
    row_input = input("Please input a row letter.")
    column_input = int(input("Please input a column number."))
    attack_index = coordinates_check(p1_grid, p2_attack_grid, row_input, column_input)
    if p1_grid[attack_index] == "[ ]":
        print() #insert "miss" message and ascii art
        p2_attack_grid[attack_index] = "[O]"
    else:
        print() #insert hit message and ascii art
        p2_attack_grid[attack_index] = "[X]"
        p1_grid[attack_index] = "[X]"
    ShipCheck()
    if not checkWinner(p1_grid):  # Check if Player 1 has lost
        print("""Player2 name variable""" + " wins!")
        break
    clear_terminal()


















