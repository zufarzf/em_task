from flask import Flask
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment
from config import CONFIG




csrf_protect = CSRFProtect()
migrate = Migrate()
socketio = SocketIO()
db = SQLAlchemy()
moment = Moment()




from . import db_models


def create_app(config_type:str):
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_type])

    #Initialization
    db.init_app(app)
    csrf_protect.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app, async_mode='gevent')
    moment.init_app(app)

    #Import a Blueprint
    from .blueprints.admin_module import admin_module
    from .blueprints.main_module import main_module

    #Register a Blueprint
    app.register_blueprint(main_module)
    app.register_blueprint(admin_module, url_prefix="/admin")

    return app