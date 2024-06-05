# /mnt/data/__init__.py

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Importar las rutas al final para evitar problemas de importación circular
from routes import *

