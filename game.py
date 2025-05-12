from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        difficulty = request.form.get('difficulty')
        difficulty_map = {
            'easy': 20,
            'medium': 50,
            'hard': 100,
            'expert': 500,
            'master': 1000
        }
        max_num = difficulty_map[difficulty]

        session['number_to_guess'] = random.randint(1, max_num)
        session['max_number'] = max_num
        session['attempts'] = 0
        session['previous_guess'] = None

        return redirect(url_for('game'))

    return render_template('index.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    message = ''
    proximity = ''
    hint = ''

    if 'number_to_guess' not in session:
        return redirect(url_for('index'))

    number = session['number_to_guess']
    max_number = session['max_number']

    if request.method == 'POST':
        try:
            guess = int(request.form.get('guess'))
            session['attempts'] += 1
            session['previous_guess'] = guess
            difference = abs(number - guess)
            percentage_diff = (difference / max_number) * 100

            # --- Proximity Phrases Only ---
            if difference == 0:
                message = f"🎉 Correct! You guessed it in {session['attempts']} attempts."
                proximity = ''
            else:
                if percentage_diff <= 1:
                    proximity = "Extremely close!"
                elif percentage_diff <= 3:
                    proximity = "Very close."
                elif percentage_diff <= 7:
                    proximity = "Close."
                elif percentage_diff <= 15:
                    proximity = "Far."
                elif percentage_diff <= 30:
                    proximity = "Very far."
                else:
                    proximity = "Extremely far."

                message = ''  # No "too high" or "too low"

            # --- Hint System ---
            if session['attempts'] == 4:
                hint = "Hint: It's even." if number % 2 == 0 else "Hint: It's odd."
            elif session['attempts'] == 6:
                if number % 10 == 0:
                    hint = "Hint: It's divisible by 10."
                elif number % 5 == 0:
                    hint = "Hint: It's divisible by 5."
                else:
                    hint = "Hint: It's not divisible by 5 or 10."
            elif session['attempts'] == 8:
                if number < 10:
                    hint = "Hint: It's a single-digit number."
                elif number < 100:
                    hint = "Hint: It's a two-digit number."
                elif number < 1000:
                    hint = "Hint: It's a three-digit number."
                else:
                    hint = "Hint: It's a four-digit number."

        except ValueError:
            message = "Please enter a valid number."

    return render_template('game.html',
                           message=message,
                           proximity=proximity,
                           hint=hint,
                           attempts=session['attempts'],
                           max_number=session['max_number'])


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

