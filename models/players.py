from init import db, ma

class Player(db.Model):
    __tablename__ = 'players'

    position = db.Column(db.String, nullable=False)
    team = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    cleansheets= db.Column(db.Integer, nullable=False)
    form = db.Column(db.String, nullable=False)
    fitness = db.Column(db.String, nullable=False)

class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('position','team', 'name','number', 'goals', 'assists', 'cleansheet', 'form', 'fitness', )
        ordered = True