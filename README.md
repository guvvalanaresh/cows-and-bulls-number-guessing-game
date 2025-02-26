# cows-and-bulls-number-guessing-game

# Cows and Bulls Game 🐮🐂

This is a **Cows and Bulls** number-guessing game built using **Flask** (Python) for the backend and **HTML, CSS, and JavaScript (jQuery)** for the frontend. The game challenges players to guess a unique 3-digit number based on clues.

## 🎮 How to Play

1. The computer randomly generates a **3-digit number** where **all digits are unique**.
2. The player enters a **3-digit guess** and clicks **Submit**.
3. The game provides feedback:
   - **Bulls** 🐂: Correct digits in the correct position.
   - **Cows** 🐮: Correct digits but in the wrong position.
4. The player has **8 chances** to guess the correct number.
5. If the guess is correct, the player wins! 🎉
6. If the player runs out of chances, the correct number is revealed.
7. A **Restart** button allows the player to start a new game.

---

## 📸 Screenshots
![Screenshot 2025-02-26 191644](https://github.com/user-attachments/assets/700eb6fb-dafd-4216-b38c-caafcd52fbed)

---

## 📂 Project Structure


### 📌 **Explanation of Files & Folders**
✔ **`app.py`** → Flask backend, handles game logic & API.  
✔ **`README.md`** → Documentation explaining the project.  
✔ **`/templates/index.html`** → UI for user input & display.   
✔ **`/screenshots/`** → Stores game screenshots for README. 
---



---
## 🛠 Features

✔ **Interactive Gameplay:** Play without refreshing the page, thanks to AJAX.  
✔ **Cows & Bulls Logic:** Get hints with bulls (correct digit & position) and cows (correct digit, wrong position).  
✔ **Guess History Tracking:** See all your previous guesses along with bulls & cows count.  
✔ **Chances Counter:** Displays remaining attempts to make your best guess.  
✔ **Restart Game Anytime:** Reset the game with a single click without refreshing the page.  
✔ **Session-Based State:** Each session stores a new random number and track of guesses.  
✔ **Input Validation:** Ensures only 3-digit numbers with unique digits are allowed.  
✔ **Clean & Simple UI:** User-friendly design with easy-to-read game information.  


