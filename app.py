import os
import random
import requests
from flask import Flask, render_template, request, session, redirect, url_for
from currency_converter import CurrencyConverter
from Utilities.score import add_score
from Utilities.utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'wog-super-secret-key')

GAME_NAMES = {1: "Memory Game", 2: "Guess Game", 3: "Currency Roulette"}
GAME_ICONS = {1: "🧠", 2: "🎯", 3: "💱"}
GAME_DESCRIPTIONS = {
    1: "A sequence of numbers will appear briefly — memorize and type them back.",
    2: "Guess the number the computer is thinking of.",
    3: "Guess the value of a random USD amount in Israeli Shekels."
}


# ── Welcome / username ────────────────────────────────────────────────────────

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            session['username'] = username
            return redirect(url_for('select_game'))
    return render_template('index.html', username=session.get('username', ''))


@app.route('/start-over', methods=['POST'])
def start_over():
    # Keep username but reset the score
    with open(SCORES_FILE_NAME, 'w') as f:
        f.write('')
    return redirect(url_for('select_game'))


@app.route('/new-player')
def new_player():
    # Clear session and score for a completely fresh start
    session.clear()
    with open(SCORES_FILE_NAME, 'w') as f:
        f.write('')
    return redirect(url_for('index'))


# ── Game selection ────────────────────────────────────────────────────────────

@app.route('/select')
def select_game():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('select_game.html',
                           username=session['username'],
                           games=GAME_NAMES,
                           icons=GAME_ICONS,
                           descriptions=GAME_DESCRIPTIONS)


# ── Difficulty selection ──────────────────────────────────────────────────────

@app.route('/game/<int:game_num>', methods=['GET', 'POST'])
def difficulty(game_num):
    if 'username' not in session or game_num not in GAME_NAMES:
        return redirect(url_for('index'))
    if request.method == 'POST':
        diff = int(request.form.get('difficulty', 1))
        if 1 <= diff <= 5:
            session['game_num'] = game_num
            session['difficulty'] = diff
            return redirect(url_for('play', game_num=game_num))
    return render_template('difficulty.html',
                           username=session['username'],
                           game_num=game_num,
                           game_name=GAME_NAMES[game_num],
                           icon=GAME_ICONS[game_num])


# ── Play ──────────────────────────────────────────────────────────────────────

@app.route('/play/<int:game_num>', methods=['GET', 'POST'])
def play(game_num):
    if 'username' not in session or game_num not in GAME_NAMES:
        return redirect(url_for('index'))

    diff = session.get('difficulty', 1)

    # ── GET: generate game state and show play page ───────────────────────────
    if request.method == 'GET':

        if game_num == 1:  # Memory Game
            sequence = [random.randint(1, 100) for _ in range(diff)]
            session['sequence'] = sequence
            display_time = diff + 1   # more numbers → more time to read
            return render_template('play_memory.html',
                                   username=session['username'],
                                   sequence=sequence,
                                   display_time=display_time,
                                   difficulty=diff)

        elif game_num == 2:  # Guess Game
            secret = random.randint(0, diff)
            session['secret_number'] = secret
            return render_template('play_guess.html',
                                   username=session['username'],
                                   difficulty=diff)

        elif game_num == 3:  # Currency Roulette
            usd_rand = random.randint(1, 100)
            interval = 10 - diff
            try:
                api_app_id = '0143356b50534276a2e4de9adef60d8c'
                url = (f'https://openexchangerates.org/api/latest.json'
                       f'?app_id={api_app_id}&symbols=ILS')
                response = requests.get(url, timeout=3)
                if response.status_code == 200:
                    usd_to_ils = response.json()['rates']['ILS']
                else:
                    raise Exception("API error")
            except Exception:
                c = CurrencyConverter()
                usd_to_ils = c.convert(1, 'USD', 'ILS')

            session['usd_rand'] = usd_rand
            session['usd_to_ils'] = usd_to_ils
            session['interval'] = interval
            return render_template('play_currency.html',
                                   username=session['username'],
                                   usd_rand=usd_rand,
                                   difficulty=diff,
                                   interval=interval)

    # ── POST: evaluate the player's answer ────────────────────────────────────
    result = False

    if game_num == 1:
        raw = request.form.get('sequence', '')
        try:
            user_list = [int(x.strip()) for x in raw.split(',')
                         if x.strip().lstrip('-').isdigit()]
        except Exception:
            user_list = []
        result = user_list == session.get('sequence', [])

    elif game_num == 2:
        try:
            user_guess = int(request.form.get('guess', -999))
        except Exception:
            user_guess = -999
        result = (user_guess == session.get('secret_number', -998))

    elif game_num == 3:
        try:
            user_guess = float(request.form.get('guess', -1))
        except Exception:
            user_guess = -1.0
        usd_to_ils = session.get('usd_to_ils', 0)
        usd_rand = session.get('usd_rand', 0)
        interval = session.get('interval', 0)
        ils_calc = usd_to_ils * usd_rand
        result = abs(user_guess - ils_calc) <= interval

    score_earned = 0
    if result:
        score_earned = (diff * 3) + 5
        add_score(diff)

    return render_template('result.html',
                           username=session['username'],
                           result=result,
                           game_name=GAME_NAMES[game_num],
                           game_num=game_num,
                           icon=GAME_ICONS[game_num],
                           difficulty=diff,
                           score_earned=score_earned)


# ── Score board ───────────────────────────────────────────────────────────────

@app.route('/score')
def score():
    score_val = None
    error = False
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as f:
            raw = f.read().strip()
        if raw.isdigit() and int(raw) >= 1:
            score_val = int(raw)
        else:
            error = True
    else:
        error = True

    return render_template('score.html',
                           username=session.get('username', ''),
                           score=score_val,
                           error=error,
                           bad_return=BAD_RETURN_CODE)


# ── Reset score ───────────────────────────────────────────────────────────────

@app.route('/reset-score', methods=['POST'])
def reset_score():
    with open(SCORES_FILE_NAME, 'w') as f:
        f.write('')
    return redirect(url_for('score'))


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
