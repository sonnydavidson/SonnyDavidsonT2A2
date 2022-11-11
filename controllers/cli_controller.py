from flask import Blueprint
from init import db, bcrypt
from models.table import Table
from models.user import User
from models.players import Player


db_commands = Blueprint('db', __name__)


# Define a custom CLI 
@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='admin@EPLAPP.com',
            password=bcrypt.generate_password_hash('admin').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='Sonny Davidson',
            email='sonny@EPLAPP.com',
            password=bcrypt.generate_password_hash('benny').decode('utf-8'),
        )
    ]

    table = [
        Table(
            position = '1',
            team = 'Arsenal',
            MP = '13',
            W = '11',
            D = '1',
            L = '1',
            Pts = '34',
            GF = '31',
            GA = '11',
            GD = '20'
        ),
        Table(
            position = '2',
            team = 'Man City',
            MP = '13',
            W = '10',
            D = '2',
            L = '1',
            Pts = '32',
            GF = '39',
            GA = '12',
            GD = '27'
        ),
        Table(
            position = '3',
            team = 'Newcastle',
            MP = '14',
            W = '7',
            D = '6',
            L = '1',
            Pts = '27',
            GF = '28',
            GA = '11',
            GD = '17'
        ),
        Table(
            position = '4',
            team = 'Tottenham',
            MP = '14',
            W = '8',
            D = '2',
            L = '4',
            Pts = '26',
            GF = '27',
            GA = '18',
            GD = '9'
        ),
        Table(
            position = '5',
            team = 'Man United',
            MP = '13',
            W = '7',
            D = '2',
            L = '4',
            Pts = '23',
            GF = '18',
            GA = '19',
            GD = '-1'
        ),
        Table(
            position = '6',
            team = 'Brighton',
            MP = '13',
            W = '6',
            D = '3',
            L = '4',
            Pts = '21',
            GF = '22',
            GA = '17',
            GD = '5'
        ),
        Table(
            position = '7',
            team = 'Chelsea',
            MP = '13',
            W = '6',
            D = '3',
            L = '4',
            Pts = '21',
            GF = '17',
            GA = '16',
            GD = '1'
        ),
        Table(
            position = '8',
            team = 'Liverpool',
            MP = '13',
            W = '5',
            D = '4',
            L = '4',
            Pts = '19',
            GF = '25',
            GA = '16',
            GD = '9'
        ),
        Table(
            position = '9',
            team = 'Fulham',
            MP = '14',
            W = '5',
            D = '4',
            L = '5',
            Pts = '19',
            GF = '23',
            GA = '24',
            GD = '-1'
        ),
        Table(
            position = '10',
            team = 'Crystal Palace',
            MP = '13',
            W = '5',
            D = '4',
            L = '4',
            Pts = '19',
            GF = '15',
            GA = '17',
            GD = '-2'
        ),
    ]


    players = [
        Player(
            position = 'RW',
            team = 'Arsenal',
            name = 'Bukayo Saka',
            number = '7',
            goals = '5',
            assists = '5',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'CAM',
            team = 'Arsenal',
            name = 'Martin Odegaard',
            number = '8',
            goals = '3',
            assists = '6',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'CB',
            team = 'Arsenal',
            name = 'William Saliba',
            number = '12',
            goals = '1',
            assists = '1',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'GK',
            team = 'Arsenal',
            name = 'Aaron Ramsdale',
            number = '7',
            goals = '0',
            assists = '0',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'ST',
            team = 'Man City',
            name = 'Erling Haaland',
            number = '9',
            goals = '18',
            assists = '3',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'CAM',
            team = 'Man City',
            name = 'Kevin De Bruyne',
            number = '10',
            goals = '3',
            assists = '9',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'CB',
            team = 'Man City',
            name = 'Ruben Dias',
            number = '3',
            goals = '0',
            assists = '0',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
        Player(
            position = 'GK',
            team = 'Man City',
            name = 'Ederson',
            number = '1',
            goals = '0',
            assists = '0',
            cleansheets = '6',
            form = 'good',
            fitness = 'match fit'
        ),
    ]

    db.session.add_all(table)
    db.session.add_all(users)
    db.session.add_all(players)
    db.session.commit()
    print('Tables seeded')