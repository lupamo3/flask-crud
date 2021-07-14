
from flask import Flask
from flask_migrate import Migrate

from .config import app_config
from .models import db, bcrypt



def create_app(env_name):
  
  app = Flask(__name__)
#   app initialization

  app.config.from_object(app_config[env_name])
  """ 
  Initialize encryption and db connection
  """
  bcrypt.init_app(app)
  db.init_app(app)

  migrate = Migrate(app, db)

  @app.route('/', methods=['GET'])
  def index():
    """
    test  endpoint
    """
    return 'Congratulations!'

  return app