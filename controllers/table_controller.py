from flask import Blueprint, request
from init import db
from models.table import Table, TableSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

table_bp = Blueprint('table', __name__,url_prefix='/table')

@table_bp.route('/')
def full_table():
# View the full table
    stmt = db.select(Table).order_by(Table.Pts.desc())
    table = db.session.scalars(stmt)
    return TableSchema(many=True).dump(table)
# View one teaam
@table_bp.route('/<string:team>/')
def get_one_team(team):
    stmt = db.select(Table).filter_by(team=team)
    table = db.session.scalar(stmt)
    if table:
        return TableSchema().dump(table)
    else:
        return {'error': f'Team not found with the name  {team}'}, 404


#Editing teams with in the database
@table_bp.route('/<string:team>/', methods=['DELETE'])
@jwt_required()
# Delete a team
def delete_one_team(team):
    authorize()

    stmt = db.select(Table).filter_by(team=team)
    table = db.session.scalar(stmt)
    if table:
        db.session.delete(team)
        db.session.commit()
        return {'message': f'Table "{table.team}" deleted successfully'}
    else:
        return {'error': f'Team not found with position {team}'}, 404


@table_bp.route('/<string:team>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_team(team):
    # Update team information
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


@table_bp.route('/', methods=['POST'])
@jwt_required()
def create_team():
        # Create a new tema instance
        table = Table(
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
        db.session.add(table)
        db.session.commit()
        # Respond to client
        return TableSchema().dump(table), 201