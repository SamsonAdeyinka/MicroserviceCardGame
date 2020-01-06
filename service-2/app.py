#from application import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.242.157.199/cards_db'
app.config['SECRET_KEY'] = 'Z2XW3CE45VRBT6U8MOP'

db = SQLAlchemy(app)

#from application import routes


@app.route('/')
@app.route('/page-')
def random_card():
        number = randint(1, 52)
        data = Deck.query.filter_by(id=number).first()
        return data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
