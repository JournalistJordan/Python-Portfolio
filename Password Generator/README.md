# 🔐 Python Password Generator

A beginner-friendly Python program that generates a secure, randomized password based on user-specified quantities of letters, symbols, and numbers.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [Code Breakdown](#code-breakdown)
- [Skills Demonstrated](#skills-demonstrated)

---

## Overview

This program prompts the user to choose how many **letters**, **symbols**, and **numbers** they want in their password. It then generates a randomized password by shuffling all the characters together, making it more secure and harder to guess.

---

## ✨ Features

- User-controlled password length and composition
- Randomized character selection from letters, symbols, and numbers
- Shuffled output so characters are never in a predictable pattern
- Simple command-line interface

---

## ⚙️ Requirements

- Python 3.x
- No external libraries needed — only the built-in `random` module

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your machine.
2. Save the script as `password_generator.py`.
3. Open a terminal and navigate to the file location.
4. Run the program:

```bash
python password_generator.py
```

5. Follow the prompts to enter your desired number of letters, symbols, and numbers.

---

## 💡 How It Works

1. The user is asked three questions:
   - How many **letters**?
   - How many **symbols**?
   - How many **numbers**?
2. The program uses `random.choice()` to pick random characters from each category.
3. All selected characters are added to a list.
4. `random.shuffle()` randomizes the order of the list.
5. The list is joined into a single string and displayed as the final password.

---

## 🖥️ Example Output

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
>> 5
How many symbols would you like?
>> 2
How many numbers would you like?
>> 3

Your new password is: x$d24g*f9k
```

---

## 🧩 Code Breakdown

```python
import random

# Character pools
letters = ['a', 'b', ..., 'Z']   # 52 upper and lowercase letters
symbols = ['!', '#', '$', ...]    # 9 special characters
numbers = ['0', '1', ..., '9']    # 10 digits

# Get user input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Build password list
password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle and join
random.shuffle(password_list)

revised_password = ""
for char in password_list:
    revised_password += char

print(f"Your new password is: {revised_password}")
```

---

## 🎓 Skills Demonstrated

| Concept | Usage |
|---|---|
| `import random` | Importing a built-in Python module |
| `random.choice()` | Picking a random item from a list |
| `random.shuffle()` | Randomly reordering a list in place |
| `for` loops | Iterating a set number of times with `range()` |
| `.append()` | Adding items to a list |
| String concatenation | Building the final password character by character |
| `f-strings` | Formatting the output message |
| `int(input())` | Collecting and converting user input |

---

## 🔒 Security Note

This generator is designed for **learning purposes**. For production-level password security, consider using Python's `secrets` module instead of `random`, as it is specifically designed for cryptographic use.

```python
import secrets
# secrets.choice() is safer than random.choice() for real passwords
```

---

*Built as part of a Python learning curriculum — Day 5: Loops & Randomization*
