from flask import Flask, render_template, request, jsonify, session
from random import randint

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Function to generate a random number with unique digits
def generate_random_number():
    while True:
        n = str(randint(100, 999))
        if len(set(n)) == 3:  # Ensures all digits are unique
            return n

@app.route('/')
def home():
    # Initialize game session
    session['random_number'] = generate_random_number()
    session['chances'] = 8
    session['guess_history'] = []  # Store guess history
    return render_template('index.html', chances=session['chances'])

@app.route('/guess', methods=['POST'])
def guess():
    if 'random_number' not in session or 'chances' not in session:
        return jsonify({"message": "Session expired. Please refresh the page.", "gameOver": True})

    guess_number = request.json.get("guess")

    # Input validation
    if not guess_number or not guess_number.isdigit() or len(guess_number) != 3:
        return jsonify({"message": "Invalid input. Enter a 3-digit number.", "error": True})

    bulls, cows = 0, 0
    random_number = session['random_number']

    if guess_number == random_number:
        session.pop('random_number', None)  # Reset game on win
        session.pop('chances', None)
        return jsonify({"message": "Congratulations! You won!", "win": True, "chances": 0, "history": session['guess_history']})

    # Bulls and Cows logic
    for i in range(3):
        if guess_number[i] == random_number[i]:
            bulls += 1
        elif guess_number[i] in random_number:
            cows += 1

    session['chances'] -= 1
    session['guess_history'].append({"guess": guess_number, "bulls": bulls, "cows": cows})

    if session['chances'] == 0:
        correct_number = session.pop('random_number', None)
        session.pop('chances', None)
        return jsonify({"message": f"Game Over! The correct number was {correct_number}", "gameOver": True, "chances": 0, "history": session['guess_history']})

    return jsonify({"bulls": bulls, "cows": cows, "chances": session['chances'], "history": session['guess_history']})

@app.route('/restart', methods=['POST'])
def restart():
    session['random_number'] = generate_random_number()
    session['chances'] = 8
    session['guess_history'] = []
    return jsonify({"message": "Game restarted!", "chances": session['chances'], "history": session['guess_history']})

if __name__ == '__main__':
    app.run(debug=True)
