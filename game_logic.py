import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):

    # Display game over message
    if mistakes >= 3:
        print(STAGES[mistakes])
        return
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    while True:
        # Display game state.
        display_game_state(mistakes, secret_word, guessed_letters)
        # Display Game over message
        if mistakes >= 3:
            print(f"Game Over! The word was: {secret_word}")
            break

        # Check if the player has won
        if set(secret_word).issubset(guessed_letters):
            print("Congratulations, you saved the snowman!")
            break

        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
