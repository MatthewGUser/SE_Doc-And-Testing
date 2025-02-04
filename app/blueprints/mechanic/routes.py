from flask import Blueprint, request, jsonify
from app.models.mechanic import Mechanic
from app.db import db

mechanic_bp = Blueprint('mechanic', __name__)

@mechanic_bp.route('/mechanics', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return jsonify([mechanic.to_dict() for mechanic in mechanics]), 200

@mechanic_bp.route('/mechanics/<int:id>', methods=['GET'])
def get_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    return jsonify(mechanic.to_dict()), 200

@mechanic_bp.route('/mechanics', methods=['POST'])
def create_mechanic():
    data = request.get_json()
    mechanic = Mechanic(**data)
    db.session.add(mechanic)
    db.session.commit()
    return jsonify(mechanic.to_dict()), 201

@mechanic_bp.route('/mechanics/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(mechanic, key, value)
    db.session.commit()
    return jsonify(mechanic.to_dict()), 200

@mechanic_bp.route('/mechanics/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    db.session.delete(mechanic)
    db.session.commit()
    return '', 204