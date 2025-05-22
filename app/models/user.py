# sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
# models
from models import Base

class User(Base):
    """
    User model.

    A user can have zero to multiple tasks (zero-to-many relationship).
    Tasks are optional for a user.

    Attributes:
        id: int - Primary key
        username: str - User's name
        email: str - User's email address
        password: str - User's password
        is_active: bool - User's status (defaults to True)
        tasks: List[Task] - Collection of user's tasks (can be empty)
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="user", cascade="all, delete")

    def __str__(self):
        return f"""
            Username : {self.username}
            Email : {self.email}
            Actif : {"✅" if self.is_active else "❎"}
        """
    
