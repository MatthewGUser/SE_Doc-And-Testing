from .routes import customer_bp

def register_blueprints(app):
    app.register_blueprint(customer_bp)