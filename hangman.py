
import random

# List of words
words = ["python", "apple", "tiger", "school", "computer"]
stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,

    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,

    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,

    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,

    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,

    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,

    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

# Randomly select a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of chances
attempts = 6

print("WELCOME TO HANGMAN GAME!")

# Game loop
while attempts > 0:
    print(stages[attempts])

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Remaining attempts:", attempts)

    # Check whether the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You Won!")
        break

    # Get input from player
    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

else:
    print("\nGAME OVER!")
    # print("The correct word was:", secret_word)