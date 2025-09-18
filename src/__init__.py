import os
from flask import Flask



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "fallback_dev_key")
    app.config['UPLOAD_FOLDER'] = 'static/files'

    from .views import views

    app.register_blueprint(views, url_prefix="/")
    

    return app


