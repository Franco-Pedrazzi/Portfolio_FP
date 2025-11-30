from flask import Flask, redirect
from flask_cors import CORS
from flask_login import  login_required, logout_user

from dotenv import load_dotenv
load_dotenv()
from py.Rutas import rutas
from py.apis import apis
from py.db import db
from py.LyS import SyL,login_manager
import os

app = Flask(__name__)
CORS(app)
host = os.getenv('MYSQL_ADDON_HOST')
user = os.getenv('MYSQL_ADDON_USER')
passwornd= os.getenv('MYSQL_ADDON_PASSWORD')
name = os.getenv('MYSQL_ADDON_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{passwornd}@{host}/{name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'


db.init_app(app)

app.register_blueprint(rutas)
app.register_blueprint(apis)
app.register_blueprint(SyL)

login_manager.init_app(app)
login_manager.login_view = "login"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)