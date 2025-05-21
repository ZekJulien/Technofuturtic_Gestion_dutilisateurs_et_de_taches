# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
# database
from database import URL_DB
# models
from models import Base

class InitDb:
    """
    Initialize the database connection and create the tables if they don't exist.
    """
    # object initialization
    engine = None
    session = None

    @staticmethod
    def init() -> bool:
        """
        Initialize the database connection and create the tables if they don't exist.
        Return True if the connection is successful.
        Raise an error if the connection fails and return False.
        """
        try:
            # postgreSQL database connection
            engine = create_engine(URL_DB)

            # session initialization
            session = sessionmaker(bind=engine)
            session = session()

            # create tables if they don't exist.
            Base.metadata.create_all(bind=engine)
            print("Connection established")
            return True
        except SQLAlchemyError as e:
            print(f"Error : {e}")
            return False
