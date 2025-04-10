p1_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer",]
p2_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer",]

player_1 = input("Place your Ships")
print(p1_grid)

player_2 = input("Place your Ships")
print(p2_grid)






if p1_ships == 0:
    print("Player 2 has won the Game!!", 'Art goes here')
elif p2_ships == 0:
    print("Player 1 has won the Game!!", 'Art goes here')
else:
    print("Something has gone wrong")



































