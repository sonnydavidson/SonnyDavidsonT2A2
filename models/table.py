from init import db, ma 

class Table(db.Model):
    __tablename__ = 'table'

    team = db.Column(db.String(50), primary_key=True)
    MP = db.Column(db.Integer)
    W = db.Column(db.Integer)
    D = db.Column(db.Integer)
    L= db.Column(db.Integer)
    Pts = db.Column(db.Integer)
    GF = db.Column(db.Integer)
    GA = db.Column(db.Integer)
    GD = db.Column(db.Integer)

class TableSchema(ma.Schema):
    class  Meta:
        fields = ('team', 'MP', 'W', 'D', 'L', 'points', 'GF', 'GA', 'GD')
        ordered = True