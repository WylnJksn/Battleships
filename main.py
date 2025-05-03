import os
import string

# ASCII art
asciihit = """                  ....          .....         ...    ..+*-.     .....                      
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
asciimiss = """                                                       
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
                                                                .  ."""

# Utility functions
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def transition_to_next_turn():
    input("\nPress Enter to end your turn and pass to the next player...")
    clear_terminal()

def get_valid_row():
    while True:
        row_input = input("Enter row (A-J): ").upper()
        if row_input in string.ascii_uppercase[:10]:
            return string.ascii_uppercase.index(row_input)
        print("Invalid row")

def get_valid_column():
    while True:
        col_input = input("Enter column (1-10): ")
        if col_input.isdigit():
            col = int(col_input)
            if 1 <= col <= 10:
                return col - 1
        print("Invalid column.")

def place_ship(grid, ship_length, name, ship_segments):
    while True:
        print(f"\nPlacing {name} (length {ship_length})")
        row = get_valid_row()
        col = get_valid_column()
        direction = input("Direction (H or V): ").upper()
        positions = set()

        if direction == "H":
            if col + ship_length > 10:
                print("Ship doesn't fit horizontally.")
                continue
            if any(grid[row * 10 + col + i] != "[ ]" for i in range(ship_length)):
                print("Overlap detected.")
                continue
            for i in range(ship_length):
                grid[row * 10 + col + i] = "[#]"
                positions.add(row * 10 + col + i)
            ship_segments[name] = positions
            break
        elif direction == "V":
            if row + ship_length > 10:
                print("Ship doesn't fit vertically.")
                continue
            if any(grid[(row + i) * 10 + col] != "[ ]" for i in range(ship_length)):
                print("Overlap detected.")
                continue
            for i in range(ship_length):
                grid[(row + i) * 10 + col] = "[#]"
                positions.add((row + i) * 10 + col)
            ship_segments[name] = positions
            break
        else:
            print("Invalid direction.")

def check_if_ship_sunk(ship_segments, defender_grid, defender_name):
    for ship, positions in ship_segments.items():
        if not positions:
            continue  # Already reported sunk
        if all(defender_grid[pos] == "[X]" for pos in positions):
            print(f"\n*** {defender_name}'s {ship} has been sunk! ***")
            ship_segments[ship] = set()  # Prevent repeated messages

def ShipCheck():
    global p1_total_segments, p2_total_segments
    p1_remaining = p1_grid.count("[#]")
    p2_remaining = p2_grid.count("[#]")

    if p2_remaining < p2_total_segments:
        print("You hit Player 2's ship!")
        p2_total_segments = p2_remaining

    if p1_remaining < p1_total_segments:
        print("You hit Player 1's ship!")
        p1_total_segments = p1_remaining

    if p1_remaining == 0:
        print(f"\nCongratulations {player1_name}, you win! All of {player2_name}'s ships are sunk.")
        exit()

    if p2_remaining == 0:
        print(f"\nCongratulations {player2_name}, you win! All of {player1_name}'s ships are sunk.")
        exit()

def attack(attacker_grid, defender_grid, attacker_name, defender_name, defender_ship_segments):
    print(f"\n{attacker_name}'s turn to attack.")
    while True:
        row = get_valid_row()
        col = get_valid_column()
        index = row * 10 + col

        if attacker_grid[index] in ["[X]", "[O]"]:
            print("You've already attacked here.")
            return False

        if defender_grid[index] == "[#]":
            print(f"Hit! {attacker_name} struck the enemy ship! {asciihit}")
            attacker_grid[index] = "[X]"
            defender_grid[index] = "[X]"
            check_if_ship_sunk(defender_ship_segments, defender_grid, defender_name)
        else:
            print(f"Miss! {attacker_name} missed. {asciimiss}")
            attacker_grid[index] = "[O]"
            defender_grid[index] = "[O]"

        break

# Initial setup
basic_grid = ["[ ]"] * 100

def print_grid(player_grid):
    print(player_grid[:10])
    print(player_grid[10:20])
    print(player_grid[20:30])
    print(player_grid[30:40])
    print(player_grid[40:50])
    print(player_grid[50:60])
    print(player_grid[60:70])
    print(player_grid[70:80])
    print(player_grid[80:90])
    print(player_grid[90:])

p1_grid = basic_grid[:]
p1_attack_grid = basic_grid[:]
p2_grid = basic_grid[:]
p2_attack_grid = basic_grid[:]

p1_ship_segments = {}
p2_ship_segments = {}

Ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2,
}

p1_total_segments = sum(Ships.values())
p2_total_segments = sum(Ships.values())

print("Welcome to Battleship!")

# Get player names
player1_name = input("Player 1, please enter your name: ")
player2_name = input("Player 2, please enter your name: ")

# Player 1 places ships
print(f"\n{player1_name}, place your ships.")
for ship_name, ship_length in Ships.items():
    place_ship(p1_grid, ship_length, ship_name, p1_ship_segments)
    print_grid(p1_grid)
transition_to_next_turn()

# Player 2 places ships
print(f"\n{player2_name}, place your ships.")
for ship_name, ship_length in Ships.items():
    place_ship(p2_grid, ship_length, ship_name, p2_ship_segments)
    print_grid(p2_grid)
transition_to_next_turn()

# Main game loop
while True:
    attack(p1_attack_grid, p2_grid, player1_name, player2_name, p2_ship_segments)
    ShipCheck()
    print(f"\n{player1_name}'s attack grid:")
    print_grid(p1_attack_grid)
    transition_to_next_turn()

    attack(p2_attack_grid, p1_grid, player2_name, player1_name, p1_ship_segments)
    ShipCheck()
    print(f"\n{player2_name}'s attack grid:")
    print_grid(p2_attack_grid)
    transition_to_next_turn()

















