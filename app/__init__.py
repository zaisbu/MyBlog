from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.error import bp as error_bp
    app.register_blueprint(error_bp)

    from app.blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from app.kategorie import bp as kategorie_bp
    app.register_blueprint(kategorie_bp)

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    return app


from app import models