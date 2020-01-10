#from service_2 import app
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from random import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.242.157.199/cards_db'
app.config['SECRET_KEY'] = 'Z2XW3CE45VRBT6U8MOP'

db = SQLAlchemy(app)

def random_int():
    int = random.randint(1, 52)
    return int

@app.route('/service_2', methods=['POST'])
def random_card():
    number = random_int()
    card = Deck.query.filter_by(id=number).first()
    return {'card':f'{card}'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
