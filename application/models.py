from application import db

# Database for the deck of cards.

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_shape = db.Column(db.String(7), nullable=False)
    card_number = db.Column(db.String(5), nullable=False)
    card_colour = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return ''.join(['card:', self.card_number, 'of', self.card_shape])
