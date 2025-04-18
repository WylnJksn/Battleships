import string
Ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2,
}

#Makes sure the index is 2-3 characters long
def coord_to_index(coord):
    if len(coord) <2 or len(coord) >3:
        return "Invalid entry"
#Takes first letter and checks if its a valid row
    row_letter = coord[0].upper()
    if row_letter not in string.ascii_uppercase[:10]:
        return "Invalid row"
#Checks if the other characters are numbers (the "2" in "A2")
    if not coord[1:].isdigit():
        return None
#Converts the string number to and integer and subtracts 1    
    col = int(coord[1:]) - 1
    if not (0 <= col <=9):
        return None
#Converts the index letters into row numbers 0-9   
    row = string.ascii_uppercase.index(row_letter)
    return row * 10 + col











































#ACSII art for "Hit"

print("""                   ....         .....         ...    ..+*-.     .....                      
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
.+*==:::....::..................................................................................:**.""")


#Miss ascii art

print("""                                                                                                 
                                                                                                              
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
                                                                .  .                            """)
