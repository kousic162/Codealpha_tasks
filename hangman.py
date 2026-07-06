"""
Hangman Game
A simple text-based Hangman game where the player guesses a word one letter at a time.
"""

import random

# Predefined list of words to choose from
WORD_LIST = ["python", "hangman", "keyboard", "elephant", "gaming"]

MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word(word_list):
    """Randomly select a word from the given list."""
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_guess(guessed_letters):
    """Prompt the player for a single valid letter guess."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
        elif not guess.isalpha():
            print("Please enter a valid letter (a-z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_game():
    """Main game loop."""
    word = choose_word(WORD_LIST)
    guessed_letters = []
    incorrect_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("=" * 40)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        if guessed_letters:
            print("Guessed letters: " + ", ".join(sorted(guessed_letters)))
        print()

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[incorrect_guesses])
            print(f"Congratulations! You guessed the word: {word}")
            print("You won! 🎉")
            return

    # Player lost
    print(HANGMAN_STAGES[incorrect_guesses])
    print(f"Game over! You've run out of guesses.")
    print(f"The word was: {word}")


def main():
    """Run the game, allowing the player to play again."""
    while True:
        play_game()
        again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing Hangman! Goodbye.")
            break
        print()


if __name__ == "__main__":
    main()
