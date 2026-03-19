# 🔍 Operation: Shadow Files

*A text-based spy adventure game built in Python*

---

## 🕵️ What It Does

Operation: Shadow Files is an interactive, terminal-based spy thriller where the player must infiltrate an enemy headquarters and recover classified documents. Every choice you make determines whether you complete the mission — or get caught.

The game features multiple branching paths, dozens of decision points, and several ways to win (and lose). No two playthroughs are exactly alike depending on the route you take.

---

## 🎯 Why I Built It

This project was built to practice and demonstrate **conditional logic and control flow** in Python — one of the most fundamental skills in programming and data analysis scripting. Rather than building a dry exercise, I designed a game with real narrative stakes so that the logic structure had a purpose.

It also gave me practice thinking in **decision trees**, which directly maps to concepts used in business analysis, process mapping, and even machine learning classification.

---

## 🧠 Concepts Demonstrated

| Concept | Where It Appears |
|---|---|
| `if / elif / else` branching | Every player decision in the game |
| Nested conditionals | Multi-level branching (up to 5 levels deep) |
| User input capture | `input()` at every decision point |
| Input normalization | `.lower()` applied to all inputs to prevent case errors |
| String comparison | Matching typed responses to expected values |
| Program flow control | Logical sequencing of narrative and outcomes |
| ASCII art & formatting | Opening title card built with raw string literals |

---

## 🗺️ Game Structure Overview

The player begins outside enemy headquarters and chooses one of three approaches:

```
Mission Start
├── Stealth
│   ├── Ventilation Shaft
│   │   ├── Night Vision → Junction → Terminal → Vault (WIN path exists)
│   │   └── Grappling Hook → ...
│   ├── Sewer Access → ...
│   ├── Roof Access → ...
│   └── Underground Tunnel → ...
├── Disguise
│   ├── IT Technician → Social Engineering → Server Room (WIN path exists)
│   ├── Janitor → Cleaning Skills → Vault (WIN path exists)
│   └── Executive Consultant → Name Drop → Vault (WIN path exists)
└── Brute Force
    ├── Explosives → Fight Back (WIN path exists)
    ├── Hostage Situation → ...
    └── Full Assault → ...
```

---

## ▶️ How to Run

**Requirements:** Python 3 (no external libraries needed)

```bash
python shadow_files.py
```

Then follow the prompts. Type your choices exactly as shown and press Enter to continue.

**Example:**
```
Type "stealth", "disguise", or "brute force": stealth
Do you take the "ventilation", "sewer", "roof", or "tunnel"? ventilation
```

> 💡 Tip: Inputs are case-insensitive — "Stealth", "STEALTH", and "stealth" all work the same.

---

## 📅 Project Info

- **Author:** Jordan Foltz
- **Date:** March 2026
- **Language:** Python 3
- **Status:** Complete
