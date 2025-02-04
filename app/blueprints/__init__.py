from .mechanic import mechanic_bp
from .customer import customer_bp

def register_blueprints(app):
    """Register all blueprints with the Flask app"""
    app.register_blueprint(mechanic_bp)
    app.register_blueprint(customer_bp)