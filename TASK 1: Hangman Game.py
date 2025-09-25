import random

# Predefined list of 5 words
words = ["python", "hangman", "computer", "programming", "algorithm"]

# Select a random word
secret_word = random.choice(words).lower()
word_length = len(secret_word)

# Initialize game state
display = ['_'] * word_length  # Display as underscores
guessed_letters = set()  # Track guessed letters
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print(f"The word has {word_length} letters.")

# Main game loop
while incorrect_guesses < max_incorrect and '_' in display:
    # Display current state
    print("\nCurrent word:", ' '.join(display))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    
    # Get user input
    guess = input("Guess a letter: ").lower().strip()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    # Add to guessed letters
    guessed_letters.add(guess)
    
    # Check if guess is correct
    if guess in secret_word:
        # Reveal all occurrences
        for i in range(word_length):
            if secret_word[i] == guess:
                display[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game over
print("\nGame Over!")
if '_' not in display:
    print(f"Congratulations! You guessed the word: {secret_word}")
else:
    print(f"You lost! The word was: {secret_word}")
