from flask import Blueprint, request
from init import db
from models.players import Player, PlayerSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

players_bp = Blueprint('players', __name__,url_prefix='/players')

@players_bp.route('/')
# @jwt_required()
def all_players():
    # return 'all_players route'
    # if not authorize():
    #     return {'error': 'You must have an account'}, 401

    stmt = db.select(Player).order_by(Player.team.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)

# @players_bp.route('/<string:name>/')
# # @jwt_required()
# def one_player(name):
#     # return 'all_playerss route'
#     # if not authorize():
#     #     return {'error': 'You must have an account'}, 401

#     stmt = db.select(Player).filter_by(name=name)
#     player = db.session.scalar(stmt)
#     return PlayerSchema.dump(player)

@players_bp.route('most.goals')
# @jwt_required()
def top_scorers():
    # return 'top_scorers route'
    # if not authorize():
    #     return {'error': 'You must have an account'}, 401

    stmt = db.select(Player).order_by(Player.goals.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players) 

@players_bp.route('most.assists')
# @jwt_required()
def most_assists():
    # return 'most_assists route'
    # if not authorize():
    #     return {'error': 'You must have an account'}, 401

    stmt = db.select(Player).order_by(Player.assists.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)

@players_bp.route('most.cleansheets')
# @jwt_required()
def most_cleansheets():
    # return 'most_assists route'
    # if not authorize():
    #     return {'error': 'You must have an account'}, 401

    stmt = db.select(Player).order_by(Player.cleansheets.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players)



#please finish

# Editing players in the database

@players_bp.route('/<int:position>/', methods=['DELETE']) 
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


@players_bp.route('/<int:position>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_team(team):
    stmt = db.select(Table).filter_by(team=team)
    table = db.session.scalar(stmt)
    if table:
        table.position = request.json.get('position') or table.position
        table.team = request.json.get('team') or table.team
        table.MP = request.json.get('MP') or table.MP
        table.W = request.json.get('W') or table.W
        table.D = request.json.get('D') or table.D
        table.L = request.json.get('L') or table.L
        table.Pts = request.json.get('Pts') or table.Pts
        table.GF = request.json.get('GF') or table.GF
        table.GA = request.json.get('GA') or table.GA
        table.GD = request.json.get('GD') or table.GD
        db.session.commit()
        return TableSchema().dump(table)
    else:
        return {'error': f'team not found {team}'}, 404


@players_bp.route('/', methods=['POST'])
@jwt_required()
def add_player():
        # Create a new tema instance
        player = Player(
            position = request.json['position'],
            team = request.json['team'],
            MP = request.json['MP'],
            W = request.json['W'],
            D = request.json['D'],
            L = request.json['L'],
            Pts = request.json['Pts'],
            GF = request.json['GF'],
            GA = request.json['GA'],
            GD = request.json['GD']
        )
        # Add and commit team to DB
        db.session.add(player)
        db.session.commit()
        # Respond to client
        return PlayerSchema().dump(player), 201