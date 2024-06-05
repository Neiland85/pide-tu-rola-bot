from flask import Flask
from .routes import main
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(main)

    return app

