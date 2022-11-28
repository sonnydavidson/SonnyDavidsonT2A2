from init import db, ma

class Table(db.Model):
    __tablename__ = 'table'

    position = db.Column(db.Integer, nullable=False)
    team = db.Column(db.String(50), primary_key=True)
    MP = db.Column(db.Integer, nullable=False)
    W = db.Column(db.Integer, nullable=False)
    D = db.Column(db.Integer, nullable=False)
    L= db.Column(db.Integer, nullable=False)
    Pts = db.Column(db.Integer, nullable=False)
    GF = db.Column(db.Integer, nullable=False)
    GA = db.Column(db.Integer, nullable=False)
    GD = db.Column(db.Integer, nullable=False)

    playersteam = db.relationship('Player', back_populates='player_team', cascade='all, delete')

class TableSchema(ma.Schema):
    class Meta:
        fields = ('position','team', 'MP', 'W', 'D', 'L', 'Pts', 'GF', 'GA', 'GD')
        ordered = True
