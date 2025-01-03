#Theresa Thompson
import random

# Prompt user to enter a valid max range
max_range= input("Enter a number: ")
if max_range.isdigit():
    max_range= int(max_range)

    if max_range <= 0:
        print("Please enter a number larer than 0 next time. ")
        quit()
else:
    print("Please enter a number next time. ")
    quit()

# Generate a random number within the max range
random_number= random.randint(0, max_range)
guesses = 0

# Start the guessing game loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    
    else:
        print("Please enter a number next time. ")
        continue

    if user_guess == random_number:
        print("Well done, you got it right!")
        break

    elif user_guess > random_number:
        print("Your guess is too high. Try again")
    else:    
        print("Your guess is too low. Try again")
    

print(f"You got it in {guesses} guesses")