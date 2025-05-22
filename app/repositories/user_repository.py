# tools
from tools import DbTools
# database
from database import Db
# models
from models import User

class UserRepository(DbTools):
    """
    This class is used to manage the user table in the database.
    """
    def __init__(self):
        """
        Initialize the UserRepository class.
        """
        super().__init__(Db.get_session())

    def add(self, user : User):
        """
        Add a new user to the database.
        arguments:
            user: User
        returns:
            bool: True if the user was added successfully, False otherwise.
        """
        self.session.add(user)
        return self.commit()

    def get_all(self):
        """
        Get all users from the database.
        arguments:
            None
        returns:
            list: A list of all users.
        """
        return self.session.query(User).all()
    
    def get_by_email(self, email : str):
        """
        Get a user by email from the database.
        arguments:
            email: str
        returns:
            User: The user with the given email.
        """
        return self.session.query(User).filter_by(email=email).first()
    
    def get_by_id(self, id : int):
        """
        Get a user by id from the database.
        arguments:
            id: int
        returns:
            User: The user with the given id.
        """
        return self.session.query(User).filter_by(id=id).first()
    
    def update(self, user : User):
        """
        Update a user in the database.
        arguments:
            user: User
        returns:
            User: The updated user.
        """
        user_update = self.session.merge(user)
        self.commit()
        if user_update:
            return user_update
        return False

    def delete(self, user : User):
        """
        Delete a user from the database.
        arguments:
            user: User
        returns:
            bool: True if the user was deleted successfully, False otherwise.
        """
        self.session.delete(user)
        return self.commit()