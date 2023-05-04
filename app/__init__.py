from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY,JWT_TOKEN
from .extensions import db,jwt
from flask_migrate import Migrate

from .api.gpt import GPT
#from .api.login import auth
migrate = Migrate()
  
    
    
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 370
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = SECRET_KEY
    
    app.config["JWT_SECRET_KEY"] = JWT_TOKEN
    
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(GPT)
    #app.register_blueprint(auth)
    
        
    return app