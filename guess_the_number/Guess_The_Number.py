
import random

print("Guess a number between 1-100")


def check_guess(userGuess, randomNumber):

    if userGuess > randomNumber: # letting the user know the number is too high
        print(userGuess, " is too high, guess again")
        userGuess = int(input("Guess here: "))

        return userGuess

    elif userGuess < randomNumber: # letting the user know the number is too low
        print(userGuess, " is too low, guess again")
        userGuess = int(input("Guess here: "))

        return userGuess


def main():
    randomNumber = random.randrange(1, 100)  # settig the random number to be between 1-100
    userGuess = int(input("Guess here: "))  # getting the user input
    count = 1
    while (userGuess != randomNumber):  # while loop to keep going until the right number is guessed

        userGuess = check_guess(userGuess, randomNumber)
        count += 1


    print("You guessed the right number! It took you", count, "guesses. The number was",
              randomNumber)  # will print when the user get the number right


main()