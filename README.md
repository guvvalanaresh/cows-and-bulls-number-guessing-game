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

📸 Screenshots
![Screenshot 2025-02-26 191644](https://github.com/user-attachments/assets/700eb6fb-dafd-4216-b38c-caafcd52fbed)


## 📂 Project Structure

/cows and bulls game/--app.y
                    /templates/--index.html

## Run the Flask
python app.py
After running the command, open your browser and go to:
http://127.0.0.1:5000/

🛠 Features
✅ Real-time gameplay using AJAX (no page refresh needed).
✅ Bulls and Cows logic implemented for accurate hints.
✅ Guess history displayed dynamically to help players track progress.
✅ Restart button to start a fresh game.
✅ Session-based state management for each player.
✅ Input validation to ensure only valid 3-digit numbers are entered.

