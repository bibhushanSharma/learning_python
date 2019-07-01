game_display = [["TL", "TM", "TR"],
                ["ML", "MM", "MR"],
                ["BL", "BM", "BR"]]
def display(game_display):
    print(game_display[0] [0] + "|" + game_display[0] [1] + "|" + game_display[0][2])
    print("__ __ __")
    print(game_display[1] [0] + "|" + game_display[1] [1] + "|" + game_display[1][2])
    print("__ __ __")
    print(game_display[2] [0] + "|" + game_display[2] [1] + "|" + game_display[2][2])
def player_input(game_display, current_player_symbol):
    print('Hi player ', current_player_symbol, ':')
    position_choice = input("Where do you want to play? ")
    if position_choice == "TL":
        game_display [0] [0] = current_player_symbol
        display(game_display)
    elif position_choice == "TM":
        game_display [0] [1] = current_player_symbol
        display(game_display)
    elif position_choice == "TR":
        game_display [0] [2] = current_player_symbol
        display(game_display)
    elif position_choice == "ML":
        game_display [1] [0] = current_player_symbol
        display(game_display)
    elif position_choice == "MM":
        game_display [1] [1] = current_player_symbol
        display(game_display)
    elif position_choice == "MR":
        game_display [1] [2] = current_player_symbol
        display(game_display)
    elif position_choice == "BL":
        game_display [2] [0] = current_player_symbol
        display(game_display)
    elif position_choice == "BM":
        game_display [2] [1] = current_player_symbol
        display(game_display)
    elif position_choice == "BR":
        game_display [2] [2] = current_player_symbol
        display(game_display)
    else:
        print("Not a valid input")

display(game_display)
current_player_symbol = " X"
win = False
while win is False:
    player_input(game_display, current_player_symbol)
    if current_player_symbol == " X":
        current_player_symbol = " O"
    else:
        current_player_symbol = " X"
    print('current_player_symbol', current_player_symbol)
    if game_display [0][0] == game_display [0][1] == game_display [0][2]:
        win == True
        print(game_display [0][0] + " Won the game")
        break
    if game_display [1][0] == game_display [1][1] == game_display [1][2]:
        win == True 
        print(game_display [1][0] + " Won the game")
        break
    if game_display [2][0] == game_display [2][1] == game_display [2][2]:
        win == True 
        print(game_display [2][0] + " Won the game")
        break
    if game_display [0][0] == game_display [1][0] == game_display [2][0]:
        win == True 
        print(game_display [2][0] + " Won the game")
        break
    if game_display [0][1] == game_display [1][1] == game_display [2][1]:
        win == True 
        print(game_display [2][1] + " Won the game")
        break
    if game_display [0][2] == game_display [1][2] == game_display [2][2]:
        win == True 
        print(game_display [2][2] + " Won the game")
        break
    if game_display [0][0] == game_display [1][1] == game_display [2][2]:
        win == True 
        print(game_display [2][2] + " Won the game")
        break
    if game_display [0][2] == game_display [1][1] == game_display [2][0]:
        win == True 
        print(game_display [2][2] + " Won the game")
        break

    tie = True
    for i in range(3):
        for j in range(3):
            if not (game_display[i][j] == ' X' or game_display[i][j]  == ' O'):
                tie = False
    if tie == True:
        print("You tied")
        break
