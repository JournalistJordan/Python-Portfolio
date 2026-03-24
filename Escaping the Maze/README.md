# 🤖 Reeborg's World — Maze Challenge Solution

A Python solution for the Maze Challenge in Reeborg's World, using the **Right-Hand Wall Following Rule** to navigate any randomly generated maze layout.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Try It Yourself](#try-it-yourself)
- [The Strategy](#the-strategy--right-hand-rule)
- [The Code](#the-code)
- [How It Works](#how-it-works)
- [Key Concepts](#key-concepts)
- [Comparing Maze vs Hurdle 4](#maze-vs-hurdle-4)
- [Skills Demonstrated](#skills-demonstrated)

---

## Overview

Reeborg was exploring a dark maze and the battery in his flashlight ran out. Your job is to write a program that guides Reeborg to the exit — no matter where in the maze he starts or which direction he's facing.

The challenge: the maze layout **changes every time** the world reloads, so you cannot hardcode a fixed path. Your solution must be smart enough to work for **any maze configuration**.

---

## 🔗 Try It Yourself

Click the link below to open the Maze Challenge directly in Reeborg's World, then paste the code from this README into the Python editor and hit **Play**!

👉 **[Open Maze Challenge in Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json)**

### How to Run It
1. Click the link above
2. Copy the code from [The Code](#the-code) section below
3. Paste it into the **Python code editor** on the left panel
4. Click the ▶️ **Play button** to watch Reeborg solve the maze
5. Click the 🔄 **Reload button** (top right of maze) to generate a new maze layout and run it again!

---

## The Strategy — Right Hand Rule 🖐️

The robot uses a technique borrowed from real-world navigation — the **Right-Hand Wall Following Rule**. Imagine walking through a maze with your right hand always touching the wall. If you keep following that rule consistently, you will always find the exit.

The robot checks three conditions in priority order every single step:

| Priority | Condition | Action |
|---|---|---|
| 1st | Right side is clear | Turn right and move forward |
| 2nd | Front is clear | Move straight ahead |
| 3rd | Right and front both blocked | Turn left (last resort) |

```
Decision flow every step:

    [Right is clear?] ──YES──▶ turn_right() + move()
           │
           NO
           │
    [Front is clear?] ──YES──▶ move()
           │
           NO
           │
    [Both blocked]    ──YES──▶ turn_left()
           │
    🔁 Repeat until at_goal() ✅
```

---

## The Code

```python
# Reeborg's World — Maze Challenge
# Strategy: Right-Hand Wall Following Rule
# Works for any randomly generated maze layout

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

> ✅ Works on every maze reload — no changes needed!

---

## How It Works

### Step 1 — Define `turn_right()`
Reeborg's World only provides a built-in `turn_left()` function. To turn right, we call `turn_left()` three times, which rotates the robot 270° to the left — the same as a 90° right turn.

```python
def turn_right():
    turn_left()   # 90° left
    turn_left()   # 180° left
    turn_left()   # 270° left = effectively 90° RIGHT ✅
```

### Step 2 — The `while not at_goal()` Loop
The main loop keeps running every single step until Reeborg reaches the finish flag. The `not` keyword flips the condition:

```python
# Means: "keep looping while we have NOT reached the goal yet"
while not at_goal():
```

### Step 3 — The `if/elif/else` Decision
Every step inside the loop, Reeborg checks three things in order:

```python
if right_is_clear():       # Always try right first (follow the wall)
    turn_right()
    move()

elif front_is_clear():     # If can't go right, go straight
    move()

else:                      # Dead end — only option is to turn left
    turn_left()
```

> 💡 **Why `else` instead of checking `left_is_clear()`?**
> If right is blocked AND front is blocked, turning left is the only remaining option — no need to check! `else` handles all remaining cases perfectly.

---

## 🔑 Key Concepts

| Concept | How It's Used |
|---|---|
| `def turn_right()` | Custom function built from 3x `turn_left()` |
| `while not at_goal()` | Loop runs until Reeborg reaches the finish flag |
| `right_is_clear()` | Checks if the path to the right is open |
| `front_is_clear()` | Checks if the path ahead is open |
| `if / elif / else` | Three prioritized decisions per step |
| `not` keyword | Negates `at_goal()` to keep the loop running |

---

## Maze vs Hurdle 4

Both challenges use the same core loop structure but solve very different problems:

| Feature | Maze | Hurdle 4 |
|---|---|---|
| **Strategy** | Follow right wall | Jump over obstacles |
| **Main loop** | `while not at_goal()` | `while not at_goal()` |
| **Key condition** | `right_is_clear()` | `wall_in_front()` |
| **Helper function** | `turn_right()` | `jump()` + `turn_right()` |
| **Movement type** | Turns in 4 directions | Climbs up and over |
| **Complexity** | Simple 3-branch logic | Multi-step jump sequence |

---

## 🎓 Skills Demonstrated

| Python Concept | Example in Code |
|---|---|
| Defining functions | `def turn_right():` |
| Calling functions | `turn_right()`, `move()` |
| `while` loop | `while not at_goal():` |
| `not` keyword | Negates boolean condition |
| `if / elif / else` | Three-way decision branching |
| Built-in conditions | `right_is_clear()`, `front_is_clear()`, `at_goal()` |
| Code reusability | One solution works for every maze layout |

---

## 🔒 Why This Works on Every Maze

The Right-Hand Rule is a proven maze-solving algorithm. As long as the maze:
- Has a connected path from start to finish
- Has no completely isolated islands of walls

...the robot will always find the exit. The `while not at_goal()` loop combined with the three-priority decision tree guarantees the robot keeps making progress.

---

*Built as part of a Python learning curriculum — Day 6: Functions, Loops & Reeborg's World*

🔗 **[Reeborg's World — Main Site](https://reeborg.ca/reeborg.html)**
