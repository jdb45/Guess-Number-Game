import random

print("Guess a number between 1-10")

# assigning variables to names to be able to test the program
too_high = 'guess is too high!'
too_low = 'guess is too low!'
correct = 'Correct!'


def check_guess(user_guess, random_number):

    if user_guess > random_number: # letting the user know the number is too high
        print(too_high)

        return too_high

    elif user_guess < random_number: # letting the user know the number is too low
        print(too_low)

        return too_low

    elif user_guess == random_number: # returning the correct variable

        return correct


def get_user_input():
    # getting user input and checking to make sure the user enters a number
    while True:
        try:
            user_input = int(input("Guess here: "))
            break

        except ValueError:
            print('Please enter a number')

    return user_input


def get_random_Number():
    
    random_numb = random.randrange(1, 11) # setting the random number to be between 1-10
    return random_numb


def main():
    randomNumber = get_random_Number()
    count = 0
    while (True):  # while loop to keep going until the right number is guessed
        userGuess = get_user_input()
        userGuess = check_guess(userGuess, randomNumber)
        count += 1

        if userGuess == correct:
            break

    print("You guessed the right number! It took you", count, "guesses. The number was",
              randomNumber)  # will print when the user gets the number right

if __name__ == '__main__':
    main()
