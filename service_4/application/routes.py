from flask import Flask, request
from application import app, db
from application.models import Deck, Prize_gen
import random
import requests

@app.route('/service_4', methods=['POST'])
def result():
    serv2 = requests.post("http://service_2:5002/service_2")
    point = serv2.json()['points']

    # serv21 = requests.post("http://service_2:5002/service_2")
    # card_des = serv21.json()['card']

    serv3 = requests.post("http://service_3:5003/service_3")
    roll = serv3.json()['roll']

    points = int(point) * int(roll)

    if points <= 78:
        query = Prize_gen.filter_by(id=1).first()
        prize = query.Prize
    elif points >= 79 and points <= 156:
        query = Prize_get.filter_by(id=10).first()
        prize = query.Prize
    elif points => 157 and points <= 234:
        query = Prize_get.filter_by(id=20).first()
        prize = query.Prize
    elif points => 235 and points <= 317:
        query = Prize_get.filter_by(id=34).first()
        prize = query.Prize
    elif points == 318:
        query = Prize_get.filter_by(id=40).first()
        prize = query.Prize


    #if points <= 78:
        #prize_num = random.randint(1, 9)
        #query = Prize_gen.query.filter_by(id=prize_num).first()
        #prize = query.Prize

    #elif points >= 79 and points <= 156:
        #prize_num = random.randint(10, 19)
        #query = Prize_gen.query.filter_by(id=prize_num).first()
        #prize = query.Prize

    #elif points >= 157 and points <= 234:
        #prize_num = random.randint(20, 33)
        #query = Prize_gen.query.filter_by(id=prize_num).first()
        #prize = query.Prize

    #elif points >= 235 and points <= 317:
        #prize_num = random.randint(34, 39)
        #query = Prize_gen.query.filter_by(id=prize_num).first()
        #prize = prize = query.Prize

    #elif points == 318:
        #query = Prize_gen.query.filter_by(id=40).first()
        #prize = query.Prize

    return {'prize':'{}'.format(prize)}
