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

#start of reading player attack coordinates and 
row_input = input("Please input a row letter.")
column_input = int(input("Please input a column number."))
#attack_coordinates = str(str(row_input) + str(column_input))
"""attack_index = 0"""
"""row_index = 0"""
"""column_index = 0"""

def ShipCheck():
    #This will be where the program will check to see if all segments of any ship have been hit. If so, then it will print out "You sank (opposite player)'s (specific ship)."
    #The program will then check if all of the enemy player's ships have been sunk, determining a game end or not.
    pass

def RowCheck(row_input):
    valid_row = False
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
def coordinates_check(enemy_grid, player_attack_grid):    
    valid_coords = False
    while valid_coords != True:
        if enemy_grid[attack_index] == "[ ]" or enemy_grid[attack_index] == "[#]":
            if player_attack_grid[attack_index] == "[X]" or player_attack_grid[attack_index] == "[O]":
                print("Please input coordinates that haven't been attacked yet.")
                row_input = input("Please input a row letter.")
                row_index = RowCheck(row_input)
                column_input = input("Please input a column number.")
                attack_index = ColumnCheck(column_input, row_index)
            else:
                valid_coords = True
        else:
            print("Please input valid coordinates.")
            row_input = input("Please input a row letter.")
            row_index = RowCheck(row_input)
            column_input = input("Please input a column number.")
            attack_index = ColumnCheck(column_input, row_index)
    return attack_index


#Still need to make it alternate between the two attacking until someone wins. I also need to make it print off each player's normal and attack grid each turn, then clear the terminal after their turn.
#p1 attack sequence
attack_index = coordinates_check(p2_grid, p1_attack_grid)
if p2_grid[attack_index] == "[ ]":
    print() #insert "miss" message
    p1_attack_grid[attack_index] = "[O]"
else:
    print() #insert hit message
    p1_attack_grid[attack_index] = "[X]"
    p2_grid[attack_index] = "[X]"
ShipCheck()
#p2 attack sequence
attack_index = coordinates_check(p1_grid, p2_attack_grid)
if p1_grid[attack_index] == "[ ]":
    print() #insert "miss" message
    p2_attack_grid[attack_index] = "[O]"
else:
    print() #insert hit message
    p2_attack_grid[attack_index] = "[X]"
    p1_grid[attack_index] = "[X]"
ShipCheck()
