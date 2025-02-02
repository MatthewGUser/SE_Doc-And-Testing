from .mechanics import mechanics_bp

def register_blueprints(app):
    app.register_blueprint(mechanics_bp)