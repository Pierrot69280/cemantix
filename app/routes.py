from flask import render_template, request
from app import app
from app.game import play_game


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""

    if request.method == 'POST':

        given_word = request.form['given_word']
        message = play_game(given_word)

    return render_template('index.html', message=message)
