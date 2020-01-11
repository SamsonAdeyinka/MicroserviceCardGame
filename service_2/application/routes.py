from flask import Flask, request, jsonify
from application.models import Deck
from application import app, db
import random
from os import getenv


def random_int():
    int = random.randint(1, 52)
    return int

@app.route('/service_2', methods=['GET','POST'])
def random_card():
    number = random_int()
    card = Deck.query.filter_by(Points=number).first()
    return {'card':f'{card}'}

