from applications import db

class Prizes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prize_value = db.Column(db.Integer)
    no_of_balls = db.Column(db.Integer)
    lightening_ball = db.Column(db.String(3))

    def __repr__(self):
        return ''.join(['Prize:',self.prize_value,'Number of Balls:',self.no_of_balls, 'Lightening Ball:',self.ligtening_ball])


