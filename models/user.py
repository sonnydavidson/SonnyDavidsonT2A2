from init import db, ma

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    favourite_team = db.Column(db.String(50))
    email = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.Integer, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email','phone_number','favourite_team', 'password', 'is_admin')
        ordered = True