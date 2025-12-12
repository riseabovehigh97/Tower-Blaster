# Tower Blaster Game

A Python implementation of the classic **Tower Blaster** game. Players (user vs computer) take turns picking bricks from a main pile or discard pile to build a tower in ascending order. The first player to arrange their tower from lowest to highest wins!

---

## **Features**

* Console-based, turn-based gameplay.
* Single-player vs computer AI.
* Handles brick shuffling, drawing, and replacement.
* Tracks the main pile and discard pile dynamically.
* Checks for a winning tower automatically.

---

## **Requirements**

* Python 3.x

No additional libraries are required since the game uses only Python’s standard library (`random` and `time`).

---

## **How to Play**

1. Run the script:

```bash
python tower_blaster.py
```

2. The game will shuffle the bricks and deal 10 bricks to both the player and the computer.
3. The top brick from the main pile will be revealed.
4. On each turn, the player can choose to:

   * Pick the top brick from the **main pile**
   * Pick the top brick from the **discard pile**
5. Replace a brick in your tower with the chosen brick.
6. The computer takes its turn automatically with a simple strategy.
7. The game ends when either the player or computer has a fully **sorted tower**.

---

## **Gameplay Flow**

* The main pile starts with bricks numbered **1–60**.
* Players take turns picking bricks from either pile.
* Replaced bricks are moved to the discard pile.
* The winner is the first to have a tower arranged in ascending order.

---

## **Code Structure**

* **shuffle(b)** – Shuffles a given pile of bricks.
* **check_b(main_pile, discard)** – Replenishes main pile from discard if empty.
* **check_tower_blaster(tower)** – Checks if a tower is sorted.
* **get_top_brick(brick_pile)** – Draws the top brick from a pile.
* **deal_initial_b(main_pile)** – Deals 10 bricks each to player and computer.
* **find_and_replace(new_brick, old_brick, tower, discard)** – Replaces a brick in the tower and moves the replaced brick to discard.
* **computer_play(tower, main_pile, discard)** – Simple AI logic for computer moves.
* **check_user_choice(choice, tower, main_pile, discard)** – Handles player decisions each turn.

---

## **How to Run**

```bash
python tower_blaster.py
```

Follow the on-screen instructions to replace bricks and build your tower.

## **License**

This project is for **educational and recreational purposes** only.

