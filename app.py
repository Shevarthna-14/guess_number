from flask import Flask, render_template, request, session, jsonify
import random

app = Flask(__name__)
app.secret_key = "guessgame_secret_key"

@app.route("/")
def home():
    # Start a new game
    session['number'] = random.randint(1, 100)
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    guess = int(data["guess"])
    number = session.get("number", random.randint(1, 100))

    if guess < number:
        return jsonify(result="Too Low")
    elif guess > number:
        return jsonify(result="Too High")
    else:
        return jsonify(result="Correct! 🎉")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
