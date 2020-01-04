from flask import render_template, redirect, request
from application import app, db
from application.models import Deck
from application.forms import StartGame, CardColour, DrawCard

@app.route('/')

@app.route('/home', methods=['GET', 'POST'])
def home():
    form = StartGame()
    if request.method == 'POST':
        return redirect(url_for('page-1'))
    return render_template('home.html', title='Home', form=form)

@app.route('/page-1', methods=['GET', 'POST'])
def card():
    form = CardColour()
    if request.method == 'POST':
        if request.form == 'black_sub':
            return render_template('page-2.html', tite='Page 2')
        elif request.form == 'red_sub':
            return render_template('page-2.html', title='Page 2')
    return render_template('page-1.html', tite='Page 1', form=form)

@app.route('/page-2', methods=['GET', 'POST'])
def draw():
    form = DrawCard()
    if request.form == 'POST':
        return render_template('page-3', title='Page 3', form=form)

@app.route('/page-3')
def prize():
    return render_template('page-3.html', title='Page 3', form=form)
