from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from .db import db, ma
import click

def create_app(config_name=None):
    app = Flask(__name__)
    
    if config_name == 'testing':
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    ma.init_app(app)
    
    # Register CLI commands
    @app.cli.command("init-db")
    def init_db_command():
        """Initialize the database."""
        try:
            db.create_all()
            click.echo("Database initialized successfully!")
        except Exception as e:
            click.echo(f"Error initializing database: {e}")
    
    from .blueprints.mechanics import mechanics_bp
    app.register_blueprint(mechanics_bp)
    
    return app