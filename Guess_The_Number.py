'''Program Guess the Number
Author: Jeremy Belisle
Last Date Modified: 1/10/17
This program will let the user guess the number between 1-100'''

print("Guess a number between 1-100")

import random
randomNumber = random.randrange(1,100) # settig the random number to be between 1-100
userGuess = int(input("Guess here: ")) # getting the user input

while(userGuess != randomNumber): # while loop to keep going until the right number is guessed

    if userGuess > randomNumber: # letting the user know the number is too high
        print(userGuess, " is too high, guess again")

        userGuess = int(input("Guess here: "))

    elif userGuess < randomNumber: # letting the user know the number is too low
        print(userGuess, " is too low, guess again")
        userGuess = int(input("Guess here: "))
    
print("You guessed the right number! The number was", randomNumber) # will print when the user get the number right
