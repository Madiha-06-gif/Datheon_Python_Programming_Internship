

import random

with open("words.txt", "r", encoding="utf-8") as file:
    WORDS = [
        word.strip().lower()
        for word in file
        if word.strip().isalpha()
    ]
if not WORDS:
    raise ValueError("words.txt does not contain any valid words.")
HANGMAN_ART = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


secret_word = random.choice(WORDS)
guessed_letters = set()
wrong_guesses = set()
max_attempts = 6

print("Welcome to Hangman!")
print("Guess the hidden word.")

while len(wrong_guesses) < max_attempts:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "
    print(HANGMAN_ART[len(wrong_guesses)])
    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - len(wrong_guesses))

    guess = input("Enter a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print("You already guessed that letter!")
        continue

    if guess in secret_word:
        guessed_letters.add(guess)
        print("Correct guess!")
    else:
        wrong_guesses.add(guess)
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nWord:", secret_word.upper())
        print("Congratulations! You won!")
        break

else:
    print(HANGMAN_ART[max_attempts])
    print("\nGame over!")
    print("The correct word was:", secret_word.upper())