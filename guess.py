import random

print('=========================')
print('     GUESS MY NUMBER     ')
print('     By Rhi Jenkins      ')
print('=========================')
print('')

name = input('What is your name? ')
the_number = random.randint(0, 100)

guess = -1

while guess != the_number:
    print("")
    print("I'm thinking of a number between 0 and 100. Can you guess it?")

    guess_text = input("What is your guess? ")
    guess = int(guess_text)
    if guess < the_number:
        print(f"Sorry, {name}, but your guess is too LOW. Try again.")
    elif guess > the_number:
        print(f"Sorry, {name}, but your guess is too HIGH. Try again.")
    else:
        print(f"You guessed it! Congratulations, {name}!")
print('Thanks for playing!')