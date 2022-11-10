from flask import Blueprint, request
from init import db
from models.players import Player, PlayerSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

players_bp = Blueprint('players', __name__,url_prefix='/players')

@players_bp.route('/')
# @jwt_required()
def all_players():
    # return 'all_playerss route'
    # if not authorize():
    #     return {'error': 'You must be an admin'}, 401

    stmt = db.select(Player).order_by(Player.team.desc())
    players = db.session.scalars(stmt)
    return PlayerSchema(many=True).dump(players) 