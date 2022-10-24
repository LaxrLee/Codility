# guessing game

# secret_word = "giraffe"
# guess = ""

# # while loop in order to continually ask the person to guess the word

# while guess != secret_word:
#     guess = input("Enter guess: ")

# print("You win!")

# setting a limit after three tries

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:
    guess = input("Enter secret word: ")
    guess_count += 1

print("You guessed correctly!")