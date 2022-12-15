from random import choice

user = 0
computer = 0

def game():
    print("Rock... Paper... Scissors... Shoot!")
    inp = input("Make your move r (rock), p (paper), s (scissors) or q (to quit): ")
    inp = inp.lower()
    pro = choice("rps")  # chooses a random letter between r, p and s
    play(inp, pro)  # calling the play function

def play(inp, pro):
    # declaring variables (user and computer) in global scope
    global user
    global computer
    
    # conditions and their outputs if computer wins
    if (inp=='r' and pro=='p'):  # paper beats rock
        computer+=1
        print("\nI said paper.")
        print("Ha! You are zapped.---{}:{}\n".format(user, computer))
        game()
        
    elif (inp=='p' and pro=='s'):  # scissors beats paper
        computer+=1
        print("\nI said scissors.")
        print("Ha! You are zapped.---{}:{}\n".format(user, computer))
        game()
        
    elif (inp=='s' and pro=='r'):  # rock beats scissors
        computer+=1
        print("\nI said rock.")
        print("Ha! You are zapped.---{}:{}\n".format(user, computer))
        game()
        
        
    # conditions and their outputs if user wins
    elif (inp=='r' and pro=='s'):
        user+=1
        print("\nI said scissors.")
        print("You won.---{}:{}\n".format(user, computer))
        game()
        
    elif (inp=='p' and pro=='r'):
        user+=1
        print("\nI said rock.")
        print("You won.---{}:{}\n".format(user, computer))
        game()
        
    elif (inp=='s' and pro=='p'):
        user+=1
        print("\nI said paper.")
        print("You won.---{}:{}\n".format(user, computer))
        game()
        
        
    # if user chooses quit then the code below will be executed.
    # if score of user is more than the computer.
    elif (inp == 'q'):
        if user>computer:
            print("\nCongratulations! You won.---{}:{}".format(user, computer))
            print("Thanks for playing.")
        
        # if score of computer is more than the user.
        elif computer>user:
            print("\nSorry, you lost!---{}:{}".format(user, computer))
            print("Thanks for playing.")
        
        # if the scores of both user and computer are same.
        else:
            print("\nIt's a tie---{}:{}".format(user, computer))
            print("Thanks for playing.")
            

    # conditioins and their outputs if user input and computer choices are same.
    elif (inp == 'r' and pro == 'r'):
        print("\nI said rock.")
        print("rock-rock! Tie.---{}:{}\n".format(user, computer))
        game()
        
    elif (inp == 'p' and pro == 'p'):
        print("\nI said paper.")
        print("paper-paper! Tie.---{}:{}\n".format(user, computer))
        game()
        
    elif (inp == 's' and pro == 's'):
        print("\nI said scissors.")
        print("scissors-scissors! Tie.---{}:{}\n".format(user, computer))
        game()
        
    # if the inputs entered by the user are except r,p,s and q.    
    else:
        print("\nPlease enter a valid input.\n")
        game()

game()