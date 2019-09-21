from flask import redirect, url_for, session, flash
from flask_login import current_user, login_user, login_required, logout_user
from flask_dance import OAuth2ConsumerBlueprint
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound

from oauthlib.oauth2.rfc6749.errors import TokenExpiredError

from . import app, db, login_manager
from .models import User, OAuth

twitch_blueprint = OAuth2ConsumerBlueprint(
    "twitch",
    __name__,
    client_id=app.config.get("TWITCH_CLIENT_ID"),
    client_secret=app.config.get("TWITCH_CLIENT_SECRET"),
    base_url="https://api.twitch.tv/helix/",
    token_url="https://id.twitch.tv/oauth2/token",
    authorization_url="https://id.twitch.tv/oauth2/authorize",
    redirect_url=app.config.get('SERVER_HOME'),
    token_url_params={"include_client_id": True},
    scope=("user:read:email",),
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
)

app.register_blueprint(twitch_blueprint, url_prefix="/login")

class NotAuthorizedError(Exception):
    pass

login_manager.login_view = "twitch.login"

@oauth_authorized.connect_via(twitch_blueprint)
def twitch_logged_in(blueprint, token):
    if not token:
        flash("로그인을 할 수 없습니다.", category="error")
        return False

    tb_users = blueprint.session.get("users")
    if not tb_users.ok:
        flash("사용자 정보를 가져올 수 없습니다.", category="error")
        return False

    tb_user = tb_users.json().get('data')[0]
    user_id = tb_user.get("id")

    query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=user_id)
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(provider=blueprint.name, provider_user_id=user_id, token=token)

    if not oauth.user:
        user = User(twitch_id=user_id)
        oauth.user = user
        db.session.add_all([user, oauth])
        db.session.commit()
    else:
        oauth.user.twitch_id = user_id
        db.session.commit()

    login_user(oauth.user)
    flash("성공적으로 로그인했습니다.")

    return False

@oauth_error.connect_via(twitch_blueprint)
def twitch_error(blueprint, message, response):
    msg = ("OAuth error from {name}! " "message={message} response={response}").format(
        name=blueprint.name, message=message, response=response
    )
    flash(msg, category="error")

@app.route("/login")
def login():
    return redirect(url_for("twitch.login"))

@app.route("/logout")
@login_required
def logout():
    if twitch_blueprint.token:
        print(twitch_blueprint.token)
        token = twitch_blueprint.token["access_token"]
        try:
            resp = twitch_blueprint.session.post(
                "https://id.twitch.tv/oauth2/revoke",
                params={"client_id": twitch_blueprint.client_id, "token": token}
            )
        except TokenExpiredError:
            pass
        del twitch_blueprint.token
    logout_user()
    return redirect(app.config.get('SERVER_HOME'))

