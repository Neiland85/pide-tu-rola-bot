# /mnt/data/database.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

def init_db():
    db.create_all()

# Importar modelos para que sean reconocidos por SQLAlchemy
from models import SongRequest, Event

