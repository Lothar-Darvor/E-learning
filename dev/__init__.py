from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging
from .views import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:25052002@localhost/e-learning'
db = SQLAlchemy(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


from app import views, models

