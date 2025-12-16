import random

# List of words for the game
words = ["python", "hangman", "programming", "agent", "algorithm"]

# Function to choose a random word
def choose_word():
    return random.choice(words)

# Simple Reflex Agent: guesses letters based on frequency
letter_frequency = "etaoinshrdlcumwfgypbvkjxqz"

def hangman_game():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6
    display = ["_"] * len(word)
    
    print("Welcome to Hangman! Try to guess the word.")
    
    while attempts > 0 and set(display) != word_letters:
        # Simple reflex agent picks the next unguessed frequent letter
        for letter in letter_frequency:
            if letter not in guessed_letters:
                guess = letter
                break
        
        guessed_letters.add(guess)
        
        if guess in word_letters:
            print(f"Correct guess: '{guess}'")
            for idx, char in enumerate(word):
                if char == guess:
                    display[idx] = guess
        else:
            attempts -= 1
            print(f"Wrong guess: '{guess}'. Attempts left: {attempts}")
        
        print("Current word: ", " ".join(display))
        print("Guessed letters: ", " ".join(sorted(guessed_letters)))
        print("-"*30)
    
    if set(display) == word_letters:
        print(f"Congratulations! The word was '{word}'. You won!")
    else:
        print(f"Game over! The word was '{word}'.")

# Run the game
hangman_game()

