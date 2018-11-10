import random

play_again='y' # intialized to y for yes

while play_again != 'n':
    num = random.randint(1,10) #get random number
    guess = 0 #initialize guess

    #loops until the user guesses the correct number
    while guess != num:

        # this loop handles the exceptions of if the guess is out of the expected range,
        # or not a number
        while True:
            try:
                guess = int(input("Guess a number between 1 & 10: "))
                if 1 <= guess <= 10:
                    break
                else:
                    print("Number out of range.  Please Try Again. ")
            except ValueError:
                print("Input was not a number.  Please Try Again. ")

        if guess != num:
            if guess > num:
                print("Your number is high.  Try again. ")
            else:
                print("Your number is low.  Try again. ")
        else:
            print("You got it right!")

    #get input to see if they want to play again
    play_again = input("Play Again? (y/n) ")
