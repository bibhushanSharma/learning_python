from random import randint as random_int

class rock_paper_scissors:
    def game (self):
        quit = False
        choise = {1: "rock", 2:"paper", 3: "scissors"}
        while(quit is False):
            user_input = int(input("Enter 1 for rock, 2 for paper, and 3 for scissors: ")) 
            win = False
            tie = False
            cpu = random_int(1,3)
            if user_input is 1 and cpu is 3:
                win = True
            elif user_input is 2 and cpu is 1:
                win = True 
            elif user_input is 3 and cpu is 2:
                win = True
            elif user_input is cpu:
                tie = True
            else:
                win = False
            if win is True:
                print("You won!")
            elif tie is True:
                print ("You tied!")
            else:
                print("You Lost!")
            print('Your Choise %s'%(choise[user_input] ))
            print('Computer\'s Choise %s'%(choise[cpu]))

            keep_playing = int(input("Enter 1 to keep playing, enter 2 to stop playing "))
            if keep_playing is 1:
                quit = False
            else:
                quit = True

class hangman:
    def game_2(self):
        number_of_guesses = 7
        secret_word = ["c", "o", "a", "g", "u", "l", "a", "t", "e"]
        blank_word = [ "_ ", "_ ", "_ ", "_ ", "_ ","_ ", "_ ", "_ ", "_ " ]
        while(number_of_guesses > 0):
            match = True
            for i in range (len(secret_word)):
                if secret_word[i] != blank_word[i]:
                    match = False
                    break
            if match is True:
                print("You Win!")
                print(blank_word)
                break
            print(blank_word)
            print(str(number_of_guesses) + " guesses left")
            guess = input("Guess a letter: ")
            if len(guess) != 1:
                print("You must guess 1 letter")
                number_of_guesses -=1
            elif guess == "c":
                blank_word[0]= "c"
            elif guess == "o":
                blank_word [1] = "o"
            elif guess == "a":
                blank_word [2] = "a"
                blank_word [6] = "a"
            elif guess == "g":
                blank_word [3] = "g"
            elif guess == "u":
                blank_word [4] = "u"
            elif guess == "l":
                blank_word [5] = "l"
            elif guess == "t":
                blank_word [7] = "t"
            elif guess == "e":
                blank_word [8] = "e"
            else:
                print("Your guess was wrong")
                number_of_guesses -=1
        if number_of_guesses == 0:
            print("You lost :)")

playing = True
while playing is True:
    desision = input("Enter 1 to play 'rock paper scissors' or Enter 2 to play 'hangman' or Enter 3 to exit: ")

    if desision == "1":
        play_game=rock_paper_scissors()
        play_game.game()
    elif desision == "2":
        play_game_2=hangman()
        play_game_2.game_2()
    elif desision == "3":
        print("Goodbye")
        break
    else:
        print("Not a valid input")