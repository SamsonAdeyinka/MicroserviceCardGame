from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.242.157.199/cards_db'
app.config['SECRET_KEY'] = 'Z2XW3CE45VRBT6U8MOP'

db = SQLAlchemy(app)

from application import routes
