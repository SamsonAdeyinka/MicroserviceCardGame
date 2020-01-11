from flask import Flask, request
from application import app, db
from application.models import Deck, Prize_gen
import random
import requests

@app.route('/service_4', methods=['GET', 'POST'])
def result():

    card = 0
    die = 0
    prize = 0


    serv2 = requests.get("http://service_2:5002/service_2")
    card = serv2.json()['card']
    
    serv3 = requests.get("http://service_3:5003/service_3")
    dice = serv3.json()['roll']

    points = int(card) * int(dice)

    if points <= 78:
        prize_num = random.randint(1, 9)
        prize = Prize_gen.query.filter_by(id=prize_num).first()

    elif points >= 79 and points <= 156:
        prize_num = random.randint(10, 19)
        prize = Prize_gen.query.filter_by(id=prize_num).first()

    elif points >= 157 and points <= 234:
        prize_num = random.randint(20, 33)
        prize = Prize_gen.query.filter_by(id=prize_num).first()

    elif points >= 235 and points <= 317:
        prize_num = random.randint(34, 39)
        prize = Prize_gen.query.filter_by(id=prize_num).first()

    elif points == 318:
        prize = Prize_gen.query.filter_by(id=40).first()

    return {'prize':f'{prize}'}

