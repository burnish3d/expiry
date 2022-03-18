from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app(test_config=None):
  app = Flask(__name__)
  app.config.from_object(DevConfig())

  @app.route('/')
  def index():
    return 'AHOY THERE'

  return app