
import random

print("Guess a number between 1-10")


def check_guess(userGuess, randomNumber):

    if userGuess > randomNumber: # letting the user know the number is too high
        print(userGuess, " is too high, guess again")
        userGuess = get_user_input()

        return userGuess

    elif userGuess < randomNumber: # letting the user know the number is too low
        print(userGuess, " is too low, guess again")
        userGuess = get_user_input()

        return userGuess

def get_user_input():
    guess = int(input("Guess here: "))
    return guess


def get_random_Number():
    randomNumb = random.randrange(1, 10) # settig the random number to be between 1-10
    return randomNumb


def main():
    randomNumber = get_random_Number()
    userGuess = get_user_input()
    count = 1
    while (userGuess != randomNumber):  # while loop to keep going until the right number is guessed
    
        userGuess = check_guess(userGuess, randomNumber)
        count += 1

    print("You guessed the right number! It took you", count, "guesses. The number was",
              randomNumber)  # will print when the user get the number right


main()
