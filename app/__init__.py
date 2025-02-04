from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from .db import db, ma
import click

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Load config
    if config_name == 'testing':
        app.config.from_object('app.config.TestingConfig')
    else:
        app.config.from_object('app.config.Config')
    
    # Initialize extensions
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
    
    # Register blueprints
    from .blueprints import register_blueprints
    register_blueprints(app)
    
    return app