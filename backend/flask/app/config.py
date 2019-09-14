import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    migration_directory = "migrations"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{os.environ.get("POSTGRES_USER")}:{os.environ.get("POSTGRES_PASSWORD")}@db/{os.environ.get("POSTGRES_DB")}'

    SERVER_PROTOCOL = os.environ.get("SERVER_PROTOCOL")
    SERVER_HOSTNAME = os.environ.get("SERVER_HOSTNAME")

    SERVER_HOME = f"{SERVER_PROTOCOL}://{SERVER_HOSTNAME}/"

    TWITCH_CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
    TWITCH_CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")
