import random

# Predefined words
words = ["apple", "tiger", "chair", "plant", "bread"]

# Random word selection
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game")

# Game loop
while wrong_guesses < max_wrong:
    display = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win condition
    if "_" not in display:
        print("You guessed the word correctly!")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("Game Over! The word was:", word)