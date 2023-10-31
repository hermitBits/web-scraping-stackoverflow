import os


class BaseConfig(object):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # SQLITE
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{(os.path.join(PROJECT_ROOT, "example.db"))}'

    # Alembic ini
    ALEMBIC_INI = f'{(os.path.join(PROJECT_ROOT, "alembic.ini"))}'

    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CSRF_ENABLED = True


class TestingConfig(BaseConfig):
    TESTING = True

    # Use in-memory SQLite database for testing
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
