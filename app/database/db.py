# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy.exc import SQLAlchemyError
# database
from database import URL_DB
# models
from models import Base

class Db:
    """
    Initialize the database connection.
    """
    _engine = create_engine(URL_DB)
    _session = sessionmaker(bind=_engine)

    @staticmethod
    def is_connected():
        """
        Check if the database is connected.
        """
        return Db._engine.connect()

    @staticmethod
    def get_session() -> session:
        """
        Returns a new session instance.
        """
        return Db._session()

    @staticmethod
    def create_tables():
        """
        Creates all tables in the database if they don't exist.
        """
        Base.metadata.drop_all(Db._engine)
        Base.metadata.create_all(Db._engine)