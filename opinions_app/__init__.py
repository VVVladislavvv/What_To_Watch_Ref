from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config


app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import views, models, cli_commands, error_handlers
