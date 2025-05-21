# sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# models
from models import Base


class Task(Base):
    """
    Task model.

    The task should be assigned to a user.

    Args:
        id: int
        description: str
        id_user: int
        user: User
    """
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="task")