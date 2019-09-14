from flask import Flask, render_template, redirect, url_for, request, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager, current_user

from .config import Config


app = Flask(
    __name__,
    static_folder="/frontend",
    template_folder="/frontend",
)
app.config.from_object(Config)

app.debug = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

socketio = SocketIO(
    app,
    async_mode="eventlet",
    cors_allowed_origins="*"
)

from . import models
from . import oauth
from . import socket

@app.route("/")
def index():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return redirect(url_for("recognition"))

@app.route("/recognition")
def recognition():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template("recognition.html")

@app.route("/overlay")
def overlay():
    return render_template("overlay.html")

