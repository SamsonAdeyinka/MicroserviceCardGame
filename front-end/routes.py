from flask import render_template, redirect, request
from application import app, db
from application.models import Deck
from application.forms import StartGame, CardColour, DrawCard
from random import random

@app.route('/')

@app.route('/home')
def home():
    form = StartGame()
    #if request.method == 'POST':
    #if form.validate_on_submit():
        #return redirect(url_for('card'))

    return render_template('home.html', title='Home', form=form)

@app.route('/page-1', methods=['GET', 'POST'])
def card():
    form = CardColour()
    # if request.method == 'POST':
    #     if request.form == 'black_sub':
    #         return redirect(url_for('page-2'))
    #     elif request.form == 'red_sub':
    #         return redirect(url_for('page-2'))
    return render_template('page-1.html', tite='Page 1', form=form)

@app.route('/page-2', methods=['GET', 'POST'])
def draw():
    form = DrawCard()
    if request.form == 'POST':
        return render_template('page-2', title='Page 2', form=form)

@app.route('/page-3')
def prize():
    return render_template('page-3.html', title='Page 3', form=form)
