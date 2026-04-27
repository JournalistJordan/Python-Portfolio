# 🔨 Silent Auction — Highest Bidder Finder

*A terminal-based silent auction program built in Python*

---

## 🎯 What It Does

This program simulates a **silent auction** where multiple bidders can enter their name and bid amount privately. Once all bidders have entered their offers, the program automatically identifies and announces the winner — the person who submitted the highest bid.

The screen is cleared between bidders using repeated newlines so that each participant cannot see what others have typed.

---

## 💡 Why I Built It

This project was built to practice **dictionaries**, **functions**, and **while loops** in Python. It also demonstrates how to iterate over a dictionary to find a maximum value — a pattern that appears frequently in data analysis when searching for peaks, maximums, or top performers across a dataset.

---

## 🧠 Concepts Demonstrated

| Concept | Where It Appears |
|---|---|
| Dictionaries | `bids = {}` stores each bidder's name and amount as key-value pairs |
| Adding to a dictionary | `bids[name] = price` dynamically adds each new bid |
| Iterating over a dictionary | `for bidder in bidding_dictionary` loops through all entries |
| Functions | `find_highest_bidder()` encapsulates the winner logic separately from input collection |
| While loops | Keeps accepting bids until no more bidders remain |
| Boolean flags | `continue_bidding = True` controls the bidding loop |
| f-strings | Formatted winner announcement output |
| Input handling | `.lower()` normalizes yes/no responses |
| Screen clearing | `print("\n" * 50)` simulates a cleared screen between bidders |
| ASCII art | Custom gavel logo rendered with a raw string literal (`r'''...'''`) |

---

## 🗂️ How It Works

1. The program displays a gavel logo and prompts the first bidder to enter their name and bid
2. Each bid is stored in a dictionary as `{"Name": amount}`
3. After each bid, the program asks if there are more bidders
   - If **yes**, the screen is cleared so the next bidder cannot see previous entries
   - If **no**, the `find_highest_bidder()` function runs and announces the winner
4. The winner is determined by iterating through all bids and tracking the highest value found

---

## ▶️ How to Run

**Requirements:** Python 3 (no external libraries needed)

```bash
python silent_auction.py
```

Follow the prompts:
```
Please enter your name: Jordan
Please enter your bid: $250
Are there any other bidders? Type 'yes' or 'no'
yes

Please enter your name: Alex
Please enter your bid: $310
Are there any other bidders? Type 'yes' or 'no'
no

The winner is Alex with a bid of $310.
```

---

## 📅 Project Info

- **Author:** Jordan Foltz
- **Date:** 2026
- **Language:** Python 3
- **Status:** Complete
