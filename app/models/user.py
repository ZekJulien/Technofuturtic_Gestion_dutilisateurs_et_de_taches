# sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
# models
from models import Base

class User(Base):
    """
    User model.

    The user can have several tasks.

    Args:
        id: int
        username: str
        email: str
        password: str
        is_active: bool
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)

    tasks = relationship("Task", back_populates="user")
