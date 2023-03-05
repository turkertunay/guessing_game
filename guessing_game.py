secret_letter = "h"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_letter and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("your guess?: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses. You lose")
else:
    print("You win")
