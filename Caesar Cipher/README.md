# 🔐 Caesar Cipher — Custom Encoder & Decoder

*A terminal-based encryption tool built in Python*

---

## 🕵️ What It Does

This program encrypts and decrypts secret messages using the **Caesar Cipher** — one of the oldest and most well-known encryption techniques in history. The user types a message, chooses a shift number, and the program shifts each letter by that amount through the alphabet to produce an encoded or decoded result.

The program runs in a loop, allowing the user to encode and decode as many messages as they want in a single session.

---

## 🎯 Why I Built It

This project was built to practice **functions**, **list indexing**, **modular arithmetic**, and **while loops** in Python. It also introduces a real concept from the field of cryptography — demonstrating how even a simple algorithm can transform readable text into unreadable cipher text and back again.

The logic behind this cipher maps directly to concepts used in data security, access control, and information systems — all areas relevant to analytics and cybersecurity work.

---

## 🧠 Concepts Demonstrated

| Concept | Where It Appears |
|---|---|
| Functions with parameters | `caesar(original_text, shift_amount, encode_or_decode)` |
| Lists | Alphabet stored as a list for index-based shifting |
| List indexing | `alphabet.index(letter)` finds the position of each character |
| Modular arithmetic (`%`) | Wraps the shift around the alphabet (e.g. z → b) |
| While loops | Keeps the program running until the user types "no" |
| Boolean flags | `should_continue = True` controls the loop |
| f-strings | Formatted output using `f"Here is the {encode_or_decode}d result:"` |
| Input handling | `.lower()` normalizes user input for consistent matching |
| Non-alpha character preservation | Spaces, numbers, and symbols pass through unchanged |
| ASCII art | Custom title card rendered with multi-line string literals |

---

## 🔑 How the Cipher Works

Each letter in the message is shifted forward (encode) or backward (decode) through the alphabet by the chosen number:

```
Original:  h  e  l  l  o
Shift:    +3 +3 +3 +3 +3
Encoded:   k  h  o  o  r
```

When the shift goes past `z`, it wraps back around to the beginning using **modular arithmetic** (`% 26`), so no letter ever goes out of bounds.

To decode, the shift is simply reversed by multiplying it by `-1`.

---

## ▶️ How to Run

**Requirements:** Python 3 (no external libraries needed)

```bash
python caesar_cipher.py
```

Follow the prompts in the terminal:

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
Here is the encoded result: khoor zruog
Type 'yes' if you want to go again. Otherwise, type 'no'.
no
Goodbye!
```

> 💡 Note: The cipher is case-insensitive — all input is automatically converted to lowercase before processing. Spaces and special characters are preserved as-is.

---

## 📅 Project Info

- **Author:** Jordan Foltz
- **Date:** 2026
- **Language:** Python 3
- **Status:** Complete
