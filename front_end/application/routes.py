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
    dice = ''
    prize = ''

    if form.is_submitted():
        #serv2 = requests.get("http://service_2:5002/service_2")
        #print("ok 1")
        #card = serv2.json()['random_card']
        #print("ok 2")

        #serv3 = requests.get("http://service_3:5003/service_3")
        #print("ok 3")
        #die = serv3.json()['roll_dice']
        #print("ok 4")

        serv4 = requests.post("http://service_4:5004/service_4")
        if serv4.status_code == 200:
            prize = serv4.json()['prize']
            card = ser4.json()['card']
            dice = ser4.json()['dice']
        #elif serv4.status_code == 500:
            #print("something wrong------------------------------------------------------------------")
            #app.logger.error(serv4)

    return render_template('page-1.html', title='Page 1', form=form, card=card, dice=dice, prize=prize)
