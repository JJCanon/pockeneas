from flask import Flask
from app.routes.info import info_bp
from app.routes.frase import frase_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(info_bp)
    app.register_blueprint(frase_bp)
    return app