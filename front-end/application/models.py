from application import db

# Database for the deck of cards.

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Colour = db.Column(db.String(7), nullable=False)
    Shape = db.Column(db.String(10), nullable=False)
    Number = db.Column(db.String(5), nullable=False)
    Description = db.Column(db.String(30), nullable=False)
    Points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join([
            'card:', self.Description, '\r\n',
            'points:', self.Points
            ])
