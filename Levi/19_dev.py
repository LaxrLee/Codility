# guessing gme

secret_word = "dev"
guess = ""
guess_count = 0
guess_limt = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limt:
        guess = input("Guess a word: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses")
else:
    print("You guessed correctly")