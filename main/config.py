import secrets 
import os

class Config():
    SECRET_KEY=secrets.token_hex()
    SQLALCHEMY_DATABASE_URI="sqlite:///Todos_Auth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False