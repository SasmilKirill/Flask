from flask import Flask, g
from blog.user import views
from blog.models.database import db
from flask_migrate import Migrate

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app: Flask):
    app.register_blueprint(views.user)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"blog.configs.{cfg_name}")
migrate = Migrate(app, db)