# ✂️ Rock Paper Scissors — Random Number Generator

*A terminal-based Rock Paper Scissors game built in Python*

---

## 🎮 What It Does

This is a classic Rock Paper Scissors game played in the terminal against a computer opponent. The computer's choice is generated randomly each round, making every game unpredictable. ASCII art visuals display both the player's and computer's choices before the winner is announced.

---

## 🎯 Why I Built It

This project was built to practice **random number generation**, **list indexing**, and **conditional logic** in Python. It also demonstrates how to use Python's built-in `random` module to simulate an opponent — a concept that scales into more advanced applications like simulations, data sampling, and probabilistic modeling used in analytics.

---

## 🧠 Concepts Demonstrated

| Concept | Where It Appears |
|---|---|
| `import random` | Importing Python's built-in random module |
| `random.randint()` | Generating the computer's random choice (0, 1, or 2) |
| Lists | Storing ASCII art images in a list indexed by choice number |
| List indexing | Retrieving the correct image using `game_images[user_choice]` |
| User input handling | Capturing and converting input with `int(input())` |
| Input validation | Checking for out-of-range numbers before proceeding |
| `if / elif / else` logic | Determining win, lose, or draw outcomes |
| ASCII art | Multi-line string literals used as visual game elements |

---

## ▶️ How to Run

**Requirements:** Python 3 (no external libraries needed)

```bash
python rock_paper_scissors.py
```

When prompted, type a number and press Enter:

```
What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:
0
```

The game will display both choices as ASCII art and announce the result:

```
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You lose!
```

---

## 📅 Project Info

- **Author:** Jordan Foltz
- **Date:** March 2026
- **Language:** Python 3
- **Module Used:** `random`
- **Status:** Complete
