from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from .extensions import db


from .api.gpt import GPT
    
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_SIZE'] = 370
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = SECRET_KEY
    
    #app.config["JWT_SECRET_KEY"]
    
    db.init_app(app)
    

    app.register_blueprint(GPT)
    
        
    return app