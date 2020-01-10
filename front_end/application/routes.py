from flask import render_template, redirect, request
from application import app, db
from application.models import Deck
from application.forms import DrawCard
from random import randint

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/page-2', methods=['GET', 'POST'])
def draw():
    form = DrawCard()

    card = ''
    die = ''

    if form.is_submitted():
        r = requests.post("http://service_2:5002/service_2")
        card = response.json()['random_card']
    
    return render_template('page-2.html', tite='Page 2', form=form, card=card, die=die)
