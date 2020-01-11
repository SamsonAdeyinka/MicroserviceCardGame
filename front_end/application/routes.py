from flask import render_template, redirect, request
from application import app #, db
#from application.models import Deck, Prize_gen
from application.forms import DrawCard
import random
import requests

@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/page-1', methods=['GET', 'POST'])
def draw():
    form = DrawCard()

    card = ''
    roll = ''
    prize = ''

    if form.is_submitted()
        serv4 = requests.post("http://service_4:5004/service_4")
        if serv4.status_code == 200:
            prize = serv4.json()['prize']

    return render_template('page-1.html', title='Page 1', form=form, card_des=card, roll=roll, prize=prize)
