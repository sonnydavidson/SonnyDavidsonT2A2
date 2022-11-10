from init import db, ma

class Player(db.Model):
    __tablename__ = 'players'

    position = db.Column(db.String, nullable=False)
    team = db.Column(db.String(50), foreign_key=True, nullable=False)
    name = db.Column(db.String(50), primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    cleansheets= db.Column(db.Integer)
    form = db.Column(db.String, nullable=False)
    fitness = db.Column(db.String, nullable=False)

class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('position','team', 'name','number', 'goals', 'assists', 'cleansheet', 'form', 'fitness', )
        ordered = True