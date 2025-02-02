from flask import Blueprint, jsonify, request
from ..models.mechanic import Mechanic, mechanic_schema, mechanics_schema
from ..db import db

mechanics_bp = Blueprint('mechanics', __name__, url_prefix='/api/mechanics')

@mechanics_bp.route('/', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return jsonify(mechanics_schema.dump(mechanics)), 200

@mechanics_bp.route('/<int:id>', methods=['GET'])
def get_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    return jsonify(mechanic_schema.dump(mechanic)), 200

@mechanics_bp.route('/', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    if not data or 'email' not in data:
        return jsonify({"message": "Invalid input"}), 400
    
    mechanic = Mechanic(**data)
    db.session.add(mechanic)
    db.session.commit()
    return jsonify(mechanic_schema.dump(mechanic)), 201

@mechanics_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    if not mechanic:
        return jsonify({"message": "Mechanic not found"}), 404
    
    data = request.get_json()
    for key, value in data.items():
        if value:
            setattr(mechanic, key, value)
    
    db.session.commit()
    return jsonify(mechanic_schema.dump(mechanic)), 200

@mechanics_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    if not mechanic:
        return jsonify({"message": "Mechanic not found"}), 404
    
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": "Mechanic deleted"}), 200