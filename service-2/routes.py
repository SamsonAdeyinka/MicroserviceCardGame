import random


def random_card():
    number = randint(1, 52)
    data = Deck.query.filter_by(id=number).first()
    return data
