from flask_wtf import FlaskForm
from wtforms import SubmitField
from application.models import Deck
import re

class StartGame(FlaskForm):
    start = SubmitField('Start Game')

class CardColour(FlaskForm):
    black_sub = SubmitField('Black')
    red_sub = SubmitField('Red')

class DrawCard(FlaskForm):
    draw = SubmitField('Draw Card')
