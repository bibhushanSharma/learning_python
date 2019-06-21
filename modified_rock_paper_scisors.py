from random import randint as random_int
def rock_paper_scissors ():
    quit = False
    hand = {1:"rock", 2:"paper", 3:"scissers"}
    while (quit is False):
        user_input = int(input("Enter 1 for rock, 2 for paper, and 3 for scissors: "))
        cpu = random_int (1,3)
        tie = False
        win = False
        if(user_input is 1 and cpu is 3):
            # if user inputs rock and cpu enters scissors, then player wins
            win = True
        elif(user_input is 2 and cpu is 1):
            #if user inputs paper, and cpu enters rock, then player wins
            win = True
        elif(user_input is 3 and cpu is 2):
            #if player enters scissers, and cpu enters paper, then player wins
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
        print('user_input %s'%(hand[user_input] ))
        print('cpu %s'%(hand[cpu]))
        go_on = int(input("Do you want to quit? 1 is Yes, 2 is No "))
        if go_on is 1:
            quit = True
        else:
            quit = False
            
rock_paper_scissors()