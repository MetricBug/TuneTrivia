from flask import Flask
from .views import views  # Import views Blueprint
from .models import db, bcrypt  # Import db and bcrypt

def create_app(): 
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'H0Z13R' 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # Register Blueprints
    app.register_blueprint(views, url_prefix='/')  # Views Blueprint (home, about, etc.)

    return app