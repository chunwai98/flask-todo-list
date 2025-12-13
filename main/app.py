from flask import Flask,Blueprint
from flask_migrate import Migrate
from main.extensions import db,bcrypt,login_manager
from main.config import Config
from main.main.route import main
from main.auth.route import auth
from main.todos.route import todos

def create_app():
    #Configuration
    app=Flask(__name__,template_folder="templates")
    app.config.from_object(Config)

    #Init
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    migrate=Migrate(app,db)

    #Import blueprint
    app.register_blueprint(main,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/auth")
    app.register_blueprint(todos,url_prefix="/todos")

    with app.app_context():
        db.create_all()

    return app