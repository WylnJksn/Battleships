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
attack_index = 0
row_index = 0
column_index = 0

def ShipCheck():
    #This will be where the program will check to see if all segments of any ship have been hit. If so, then it will print out "You sank (opposite player)'s (specific ship)."
    #The program will then check if all of the enemy player's ships have been sunk, determining a game end or not.
    pass

def RowCheck():
    valid_row = False
    while valid_row != True:
        if row_input == "A" or "a":
            row_index = 0
            break
        elif row_input == "B" or "b":
            row_index = 10
            break
        elif row_input == "C" or "c":
            row_index = 20
            break
        elif row_input == "D" or "d":
            row_index = 30
            break
        elif row_input == "E" or "e":
            row_index = 40
            break
        elif row_input == "F" or "f":
            row_index = 50
            break
        elif row_input == "G" or "g":
            row_index = 60
            break
        elif row_input == "H" or "h":
            row_index = 70
            break
        elif row_input == "I" or "i":
            row_index = 80
            break
        elif row_input == "J" or "j":
            row_index = 90
            break
        else:
            print("Please input a valid row letter.")
            row_input = input("Please input a row letter.")

#I need to implement a check into both the valid_row and valid_column input checks that checks
#if they put a different type than they're supposed to (i.e. an integer for the row or a string for the column).
def ColumnCheck():
    valid_column = False
    while valid_column != True:
        if column_input == 1:
            attack_index = row_index
            break
        elif column_input < 1 or column_input > 10:
            print("Please enter a valid column number.")
            column_input = int(input("Please input a column number."))
        else:
            column_index = column_input
            attack_index = row_index + column_index - 1
            break
#if attack_coordinates:

#this will check to see if the coordinate that the player is attacking is occupied by an enemy or not, indicating a hit or miss
#it will also check if the player's already attacked there
valid_coords = False
while valid_coords != True:
    if """coordinate's on oppsite player's grid""" == "[ ]" or """enemy coords""" == "[*]":
        if """coords on current player's attack grid""" == "[X]" or """coords on current player's attack grid""" == "[O]":
            print("Please input coordinates that haven't been attacked yet.")
            row_input = input("Please input a row letter.")
            RowCheck()
            column_input = input("Please input a column number.")
            ColumnCheck()
        else:
            valid_coords = True
    else:
        print("Please input valid coordinates.")
        row_input = input("Please input a row letter.")
        RowCheck()
        column_input = input("Please input a column number.")
        ColumnCheck()
#p1 attack sequence
if p2_grid[attack_index] == "[ ]":
    print() #insert "miss" message
    p1_attack_grid[attack_index] = "[O]"
else:
    print() #insert hit message
    p1_attack_grid[attack_index] = "[X]"
    p2_grid[attack_index] = "[X]"
ShipCheck()
#p2 attack sequence
if p1_grid[attack_index] == "[ ]":
    print() #insert "miss" message
    p2_attack_grid[attack_index] = "[O]"
else:
    print() #insert hit message
    p2_attack_grid[attack_index] = "[X]"
    p1_grid[attack_index] = "[X]"
ShipCheck()
