from flask import Blueprint, request, jsonify
from app.models.customer import Customer
from app.db import db

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers]), 200

@customer_bp.route('/customers/<int:id>', methods=['GET']) 
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_dict()), 200

@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.to_dict()), 201

@customer_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(customer, key, value)
    db.session.commit()
    return jsonify(customer.to_dict()), 200

@customer_bp.route('/customers/<int:id>', methods=['DELETE']) 
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return '', 204