# HANGMAN PROGRAM

import random
words = [
    "python",
    "computer",
    "developer",
    "hangman",
    "artificial",
    "intelligence",
    "algorithm",
    "programming",
    "database",
    "network"
]

stages = [
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# SELECT RANDOM WORD
secret_word = random.choice(words)

# CREATE BLANKS
display = ["_"] * len(secret_word)

# STORE GUSSED LETTERS
guessed_letters = []

# NUMBER OF LIVES
lives = 6

print("-" * 25)
print("WELCOME TO HANGMAN")
print("-" * 25)

# MAIN GAME
while True:

    print("\nWord: ", " ".join(display))
    print("\nGuessed Letters:", guessed_letters)
    print(f"Lives Left: {lives}")
    print(stages[lives])

    guess = input("Guess a letter: ").lower()

    # INPUT VALIDATION
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE alphabet.")
        continue

    # ALREADY GUSSED
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # CORRECT GUESS
    if guess in secret_word:

        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display[index] = guess

        print("Correct!")

    else:
        lives -= 1
        print("Wrong Guess!")

    # WIN CONDITION
    if "_" not in display:
        print("\n" + "-" * 25)
        print("Congratulations! You Won!")
        print("The word was:", secret_word)
        print("-" * 25)
        break

    # LOSE CONDITION
    if lives == 0:
        print(stages[0])
        print("\n Game Over!")
        print("The word was:", secret_word)
        break
