from flask import Flask
application = Flask(__name__)

from app.views import main_blueprint
application.register_blueprint(main_blueprint)
