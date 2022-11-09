from flask import Blueprint, request
from init import db
from models.table import Table, TableSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

cards_bp = Blueprint('table', __name__,url_prefix='/table')

@cards_bp.route('/')
# @jwt_required()
def table():
    # return 'all_cards route'
    # if not authorize():
    #     return {'error': 'You must have an account'}, 401

    stmt = db.select(Table).order_by(Table.points.desc())
    table = db.session.scalars(stmt)
    return TableSchema(many=True).dump(table)

@cards_bp.route('/<int:team>/', methods=['DELETE'])
@jwt_required()
def delete_one_team(team):
    authorize()

    stmt = db.select(Table).filter_by(team=team)
    card = db.session.scalar(stmt)
    if card:
        db.session.delete(team)
        db.session.commit()
        return {'message': f'Table "{table.team}" deleted successfully'}
    else:
        return {'error': f'Team not found with id {id}'}, 404


@cards_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_cards(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        card.title = request.json.get('title') or card.title
        card.description = request.json.get('description') or card.description
        card.status = request.json.get('status') or card.status
        card.priority = request.json.get('priority') or card.priority
        db.session.commit()
        return CardSchema().dump(card)
    else:
        return {'error': f'Card not found with id {id}'}, 404


@cards_bp.route('/', methods=['POST'])
@jwt_required()
def create_card():
        # Create a new Card model instance
        card = Card(
            title = request.json['title'],
            description = request.json['description'],
            date = date.today(), # date created
            status = request.json['status'],
            priority = request.json['priority']
        )
        # Add and commit card to DB
        db.session.add(card)
        db.session.commit()
        # Respond to client
        return CardSchema().dump(card), 201