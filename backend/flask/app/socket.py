from flask import session
from flask_login import current_user
from flask_socketio import send, ConnectionRefusedError

from . import socketio
from . import oauth

@socketio.on('connect', namespace='/recognition')
def connect_handler():
    if not current_user.is_authenticated:
        raise ConnectionRefusedError('unauthorized')


@socketio.on('message', namespace='/recognition')
def handle_message(message):
    if current_user.oauth:
        send(message, json=True, broadcast=True, namespace=f'/overlay/{current_user.oauth[0].provider_user_id}')