from flask import Flask
from .models.all import db
from .routes.benefits import benefits_bp, home_bp
from .routes.policies import policies_bp
from .routes.claims import claims_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(home_bp)
    app.register_blueprint(benefits_bp)
    app.register_blueprint(policies_bp)
    app.register_blueprint(claims_bp)

    return app