# 🤖 Reeborg's World — Maze Challenge Solution

A Python solution that guides a robot named Reeborg through any randomly generated maze using the **Right-Hand Wall Following Rule**.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Try It Yourself](#try-it-yourself)
- [The Strategy](#the-strategy)
- [The Code](#the-code)
- [How It Works](#how-it-works)
- [Key Concepts](#key-concepts)
- [Skills Demonstrated](#skills-demonstrated)

---

## Overview

Reeborg's World is a free, browser-based Python learning environment where you write code to control a robot. In the Maze Challenge, Reeborg is lost inside a randomly generated maze and needs to find the exit.

The maze layout **changes every time** the world reloads, so the solution must be smart enough to work for **any maze configuration** — not just one specific layout.

---

## 🔗 Try It Yourself

Click the link below to open the Maze Challenge directly in Reeborg's World, paste the code into the Python editor, and hit **Play**!

👉 **[Open Maze Challenge in Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json)**

### Steps to Run
1. Click the link above
2. Copy the code from [The Code](#the-code) section below
3. Paste it into the **Python editor** on the left panel
4. Click ▶️ **Play** to watch Reeborg solve the maze
5. Click 🔄 **Reload** (top right of the maze) to get a new maze and run it again!

---

## The Strategy

The robot uses the **Right-Hand Wall Following Rule** — a classic maze-solving technique. Imagine walking through a maze while keeping your right hand touching the wall at all times. Follow that rule consistently and you will always find the exit.

Every step, the robot checks three conditions in priority order:

| Priority | Condition | Action |
|---|---|---|
| 1st | Right side is clear | Turn right and move forward |
| 2nd | Front is clear | Move straight ahead |
| 3rd | Both right and front are blocked | Turn left (last resort) |

---

## The Code

```python
# Reeborg's World — Maze Challenge
# Strategy: Right-Hand Wall Following Rule

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

---

## How It Works

### `turn_right()`
Reeborg's World only provides a built-in `turn_left()` function. To turn right, we call `turn_left()` three times — rotating 270° left is the same as turning 90° right.

```python
def turn_right():
    turn_left()   # 90° left
    turn_left()   # 180° left
    turn_left()   # 270° left = 90° RIGHT ✅
```

### `while not at_goal()`
The main loop keeps running until Reeborg reaches the finish flag. The `not` keyword means *"keep going while the goal has NOT been reached yet."*

```python
while not at_goal():
    # keep making decisions until we reach the exit
```

### `if / elif / else` — 3 Decisions Per Step

```python
if right_is_clear():       # Always try right first
    turn_right()
    move()

elif front_is_clear():     # If right is blocked, go straight
    move()

else:                      # Dead end — turn left as last resort
    turn_left()
```

> 💡 **Why `else` and not another `elif`?**
> If the right AND front are both blocked, turning left is the only option remaining. No need to check — `else` covers all remaining cases automatically.

---

## 🔑 Key Concepts

| Concept | How It's Used |
|---|---|
| `def turn_right()` | Custom function built from 3x `turn_left()` |
| `while not at_goal()` | Loops until Reeborg reaches the finish flag |
| `right_is_clear()` | Checks if the path to the right is open |
| `front_is_clear()` | Checks if the path ahead is open |
| `if / elif / else` | Three prioritized decisions made every step |
| `not` keyword | Negates `at_goal()` to keep the loop running |

---

## 🎓 Skills Demonstrated

| Python Concept | Example |
|---|---|
| Defining functions | `def turn_right():` |
| `while` loops | `while not at_goal():` |
| Boolean negation | `not at_goal()` |
| `if / elif / else` | Three-way decision branching |
| Built-in conditions | `right_is_clear()`, `front_is_clear()` |
| Code reusability | One solution works for every maze layout |

---

*Built as part of a Python learning curriculum — Day 6: Functions, Loops & Reeborg's World*

🔗 [Reeborg's World — Main Site](https://reeborg.ca/reeborg.html)
