# models
from models import Task
# tools
from tools import DbTools
# database
from database import Db

class TaskRepository(DbTools):
    """
    This class is used to manage the task table in the database.
    """
    def __init__(self):
        """
        Initialize the TaskRepository class.
        """
        super().__init__(Db.get_session())

    def add(self, task : Task):
        """
        Add a new task to the database.
        arguments:
            task: Task
        returns:
            bool: True if the task was added successfully, False otherwise.
        """
        self.session.add(task)
        return self.commit()
    
    def get_all(self):
        """
        Get all tasks from the database.
        returns:
            list: A list of all tasks.
        """
        return self.session.query(Task).all()
    
    def get_by_user(self, id_user : int) -> list[Task]:
        """
        Get a list of task by user id from the database.
        arguments:
            id_user: int
        returns:
            Task: The tasks with the given user id.
        """
        return self.session.query(Task).filter_by(id_user=id_user).all()
    
    def get_by_id(self, id_task : int):
        """
        Get a task by id from the database.
        arguments:
            id_task: int
        returns:
            Task: The task with the given id.
        """
        return self.session.query(Task).filter_by(id=id_task).first()
    
    def update(self, task : Task):
        """
        Update a task in the database.
        arguments:
            task: Task
        returns:
            Task: The updated task.
        """
        task_update = self.session.merge(task)
        self.commit()
        if task_update:
            return task_update
        return False

    def delete(self, task : Task):
        """
        Delete a task from the database.
        arguments:
            task: Task
        returns:
            bool: True if the task was deleted successfully, False otherwise.
        """
        self.session.delete(task)
        return self.commit()
    
        
    
