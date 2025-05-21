# repositories
from repositories import UserRepository
# models 
from models import User

class UserService:
    """
    This class is used to manage the user table in the database.
    """
    def __init__(self):
        """
        Initialize the UserService class.
        arguments:
            user_repository: UserRepository
        """
        self._user_repository : UserRepository = UserRepository()

    def add(self, username : str, email : str, password : str, is_active : bool = None):
        """
        Add a new user to the database.
        arguments:
            username: str
            email: str
            password: str
            is_active: bool | None
        """
        new_user = User(username=username, email=email, password=password)
        if is_active is not None:
            new_user.is_active = is_active
        if self._user_repository.add(new_user):
            print(f"👨‍💼 The user {new_user.username} has been added in database. ✅")
    
    def get_all(self):
        """
        Get all users from the database.
        returns:
            list: A list of all users.
        """
        users = self._user_repository.get_all()
        if users:
            return users
        else:
            print(f"👨‍💼 No user(s) 🛑")
    
    def get_by_email(self, email : str):
        """
        Get a user by email from the database.
        arguments:
            email: str
        returns:
            User: The user with the given email.
        """
        user = self._user_repository.get_by_email(email)
        if user:
            return user
        else:
            print(f"👨‍💼 The user with this email : {email} doesn't exist. 🛑")
        
    def update(self, id : int, username : str = None, email : str = None, password : str = None, is_active : bool = None):
        """
        Update a user in the database.
        arguments:
            id: int
            username: str | None
            email: str | None
            password: str | None
            is_active: bool | None
        """
        user = self._user_repository.get_by_id(id)
        if user is None:
            print(f"👨‍💼 The user with this id : {id} doesn't exist. 🛑")
            return False
        update_user = User(
            id=id,
            username=username if username is not None else user.username,
            email=email if email is not None else user.email,
            password=password if password is not None else user.password,
            is_active=is_active if is_active is not None else user.is_active
        )
        updated_user = self._user_repository.update(update_user)
        if update_user:
            print(f"👨‍💼 The user {updated_user.username} has been updated in database. ✅")
            return update_user
        return False
    
    def delete(self, id : int):
        """
        Delete a user from the database.
        arguments:
            id: int
        returns:
            bool: True if the user was deleted successfully, False otherwise.
        """
        user = self._user_repository.get_by_id(id)
        if not user:
            print(f"👨‍💼 The user with this id : {id} doesn't exist. 🛑")
        if self._user_repository.delete(user):
            print(f"👨‍💼 The user {user.username} has been deleted in database. ✅")
            return True