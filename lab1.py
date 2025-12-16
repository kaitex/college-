# TITLE: Implementation of Hangman Game using Simple Reflex Agent
# Theory:
# A simple reflex agent selects actions based only on the current percept.

import random

def hangman():
    words = ["Computer", "Python", "hangman", "reflex", "university"]
    word = random.choice(words).lower()

    guessed = ['_'] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman Game!")

    while tries > 0 and '_' in guessed:
        print("Current word: ", " ".join(guessed))
        print(f"Tries left: {tries}")

        guess = input("Guess a letter: ").lower()

        # Reflex agent behavior: reacts only to the current input

        # Already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            tries -= 1
            print("Wrong guess!")

    # Game result
    if '_' not in guessed:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The correct word was: {word}")

# Run the game
hangman()
