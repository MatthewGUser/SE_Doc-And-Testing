from .routes import mechanic_bp

def register_blueprints(app):
    app.register_blueprint(mechanic_bp)