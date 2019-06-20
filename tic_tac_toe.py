from random import randint as random_int
def tic_tac_toe ():
    quit = False
    while (quit is False):
        user_input = int(input("Enter 1 for rock, 2 for paper, and 3 for scissors: "))
        cpu = random_int
        tie = False
        win = False
        if(user_input is 1 and cpu is 3):
            win = True
        elif(user_input is 2 and cpu is 1):
            win = True
        elif(user_input is 3 and cpu is 2):
            win = True
        elif(user_input is cpu):
            tie = True
        else:
            win is False
        
        if win is True:
            print("You win")
        elif tie is True:
            print("Tie")
        else:
            print("You loose")
        
        go_on = int(input("Do you want to quit? 1 is Yes, 2 is No "))
        if go_on is 1:
            quit = True
        else:
            quit = False
            
tic_tac_toe()