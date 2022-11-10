from flask import Blueprint, request
from init import db
from models.players import Player, PlayerSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

players_bp = Blueprint('players', __name__,url_prefix='/players')

@players_bp.route('/')
def all_players():
# View all players
    stmt = db.select(Player).order_by(Player.team.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)

@players_bp.route('most.goals')
def top_scorers():
# View top goal scorers
    stmt = db.select(Player).order_by(Player.goals.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)

@players_bp.route('most.assists')
def most_assists():
# View players with the most assists
    stmt = db.select(Player).order_by(Player.assists.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)

@players_bp.route('most.cleansheets')
def most_cleansheets():
# View players with the most cleansheets
    stmt = db.select(Player).order_by(Player.cleansheets.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)

@players_bp.route('/<int:number>/')
def get_one_team(number):
# find one player
    stmt = db.select(Player).filter_by(number=number)
    player = db.session.scalar(stmt)
    if player:
        return PlayerSchema().dump(player)
    else:
        return {'error': f'could not find this player{number}'}, 404
#please finish

# Editing players in the database

@players_bp.route('/<int:number>/', methods=['DELETE'])
@jwt_required()
def delete_one_player(player):
    authorize()

    stmt = db.select(Player).filter_by(player=player)
    table = db.session.scalar(stmt)
    if table:
        db.session.delete(player)
        db.session.commit()
        return {'message': f'Table "{player.name}" deleted successfully'}
    else:
        return {'error': f'player not found with position {player}'}, 404


@players_bp.route('/<int:number>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_team(team):
    # Update one players information
    stmt = db.select(Player).filter_by(team=team)
    player = db.session.scalar(stmt)
    if player:
        player.position = request.json.get('position') or player.position
        player.team = request.json.get('team') or player.team
        player.name = request.json.get('name') or player.name
        player.number = request.json.get('number') or player.number
        player.goals = request.json.get('goals') or player.goals
        player.assists = request.json.get('assists') or player.assists
        player.cleansheets = request.json.get('cleansheets') or player.cleansheets
        player.form = request.json.get('form') or player.form
        player.fitness = request.json.get('fitness') or player.fitness
        db.session.commit()
        return PlayerSchema().dump(player)
    else:
        return {'error': f'team not found {team}'}, 404


@players_bp.route('/', methods=['POST'])
@jwt_required()
def add_player():
        # Create a new player
        player = Player(
            position = request.json['position'],
            team = request.json['team'],
            name = request.json['name'],
            number = request.json['number'],
            goals = request.json['goals'],
            assists = request.json['assists'],
            cleansheets = request.json['cleansheets'],
            form = request.json['form'],
            fitness = request.json['fitness']
        )
        # Add and commit team to DB
        db.session.add(player)
        db.session.commit()
        # Respond to client
        return PlayerSchema().dump(player), 201