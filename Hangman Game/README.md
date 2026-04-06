# 🪢 Hangman — Python Word Guessing Game

A classic Hangman game built in Python. Guess the hidden word one letter at a time before you run out of lives.

---

## 📋 Table of Contents

- [Overview](#overview)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [The Code](#the-code)
- [Features](#features)
- [How It Works](#how-it-works)
- [Skills Demonstrated](#skills-demonstrated)

---

## Overview

This is a terminal-based Hangman game written in Python. A word is randomly selected from a word list and the player guesses one letter at a time. Each wrong guess costs a life and draws the next stage of the hangman. The game ends when the player either uncovers the full word or runs out of lives.

---

## How to Play

1. Run the program in your terminal:
    ```bash
    python main.py
    ```
2. A hidden word is displayed as a row of blanks — one blank per letter.
3. Type a single letter and press **Enter** to guess.
4. Correct guesses reveal the letter in the word.
5. Wrong guesses cost a life and advance the hangman drawing.
6. You have **6 lives**. Guess the word before they run out!

### Example
```
Word to guess: _ _ _ _ _

 6/6 lives remaining | Wrong guesses: []
Pick a letter, any letter: a

Nice! 'a' is in there.
Word to guess: _ a _ _ _

 6/6 lives remaining | Wrong guesses: []
Pick a letter, any letter: z

Nope! 'z' isn't in the word. That's gonna cost you.
Word to guess: _ a _ _ _
```

---

## Project Structure

```
hangman/
│
├── main.py              # Main game logic
├── hangman_words.py     # Word list the game pulls from
└── hangman_art.py       # ASCII art — logo and hangman stages
```

### `hangman_words.py`
Contains a `word_list` — a list of strings the game randomly selects from each round.

### `hangman_art.py`
Contains two items:
- `logo` — printed at the start of the game
- `stages` — a list of 7 ASCII art frames showing the hangman at each life stage (6 lives down to 0)

---

## The Code

```python
import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Build the initial blanks
display = ["_"] * word_length
print("Word to guess: " + " ".join(display))

correct_letters = []
wrong_letters = []
game_over = False

while not game_over:

    print(f"\n {lives}/6 lives remaining | Wrong guesses: {wrong_letters}")
    guess = input("Pick a letter, any letter: ").lower()

    # Validate input — only single letters allowed
    if len(guess) != 1 or not guess.isalpha():
        print("One letter at a time! Try again.")
        continue

    # Already guessed check
    if guess in correct_letters or guess in wrong_letters:
        print(f"You already threw out '{guess}'. Pick something new!")
        continue

    # Check the guess
    if guess in chosen_word:
        print(f"Nice! '{guess}' is in there.")
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                display[position] = letter
                correct_letters.append(guess)
    else:
        lives -= 1
        wrong_letters.append(guess)
        print(f"Nope! '{guess}' isn't in the word. That's gonna cost you.")

    print("Word to guess: " + " ".join(display))
    print(stages[lives])

    # Win condition
    if "_" not in display:
        game_over = True
        print("\n YOU CRACKED IT! Not bad at all.")

    # Lose condition
    if lives == 0:
        game_over = True
        print(f"\n Game over. It was '{chosen_word}'. Better luck next time.")
```

---

## Features

- Random word selection every game
- Tracks and displays wrong guesses each round
- Input validation — blocks numbers, spaces, and multi-character entries
- Duplicate guess detection — flags letters already tried
- Progressive ASCII hangman art that updates with each wrong guess
- Clean win and loss messages at the end of each game

---

## How It Works

### Random Word Selection
```python
chosen_word = random.choice(word_list)
```
A new word is picked at random from `word_list` every time the game runs.

### Display as a List
```python
display = ["_"] * word_length
```
The hidden word is stored as a list of blanks. This allows individual positions to be updated precisely when a correct letter is guessed, rather than rebuilding the entire string from scratch.

### Input Validation
```python
if len(guess) != 1 or not guess.isalpha():
    print("One letter at a time! Try again.")
    continue
```
Only single alphabetical characters are accepted. Anything else skips the round with `continue` and prompts the player again.

### Revealing Letters with `enumerate()`
```python
for position, letter in enumerate(chosen_word):
    if letter == guess:
        display[position] = letter
```
`enumerate()` provides both the index and the character at each position, allowing the correct blank to be updated surgically — only the matching positions change.

### Win and Lose Conditions
```python
if "_" not in display:
    game_over = True   # all blanks filled — player wins

if lives == 0:
    game_over = True   # no lives left — player loses
```
Both conditions set `game_over = True`, which exits the `while` loop cleanly.

---

## 🎓 Skills Demonstrated

| Python Concept | How It's Used |
|---|---|
| `import` statements | Pulls in `random`, word list, and art from separate files |
| `random.choice()` | Selects a random word each game |
| Lists | `display` stored as a list for precise index updates |
| `while` loop | Keeps the game running until win or loss |
| `if / elif / else` | Handles correct guess, wrong guess, and duplicate guess logic |
| `enumerate()` | Updates only the exact positions of correct letters |
| `continue` | Skips invalid or duplicate guesses cleanly |
| `.isalpha()` | Validates that input is alphabetical only |
| f-strings | Formats live game messages dynamically |
| Boolean flag | `game_over` controls the main loop |

---

*Built as part of a Python learning curriculum — practicing functions, loops, lists, and modular code structure.*
