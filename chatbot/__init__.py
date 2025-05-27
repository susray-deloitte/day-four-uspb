from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import chatbot_bp
    app.register_blueprint(chatbot_bp)
    return app