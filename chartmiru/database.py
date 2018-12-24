from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy_session import current_session, flask_scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()


class Database:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    @classmethod
    def init_app(cls, app):
        cls.__create_session(app)

    @staticmethod
    def flush():
        current_session.flush()

    @staticmethod
    def commit():
        try:
            current_session.commit()
        except Exception as e:
            current_session.rollback()
            raise e
        finally:
            current_session.close()

    @staticmethod
    def close():
        current_session.close()

    # private

    @staticmethod
    def __create_session(app):
        flask_scoped_session(sessionmaker(
            autocommit=False,
            autoflush=True,
            expire_on_commit=False,
            bind=create_engine(app.config['SQLALCHEMY_DATABASE_URI'], encoding='utf-8')), app)