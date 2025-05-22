# models
from models import Task
# tools
from tools import DbTools
# database
from database import Db

class TaskRepository(DbTools):
    def __init__(self):
        super().__init__(Db.get_session())

    def add(self, task : Task):
        self.session.add(task)
        return self.commit()
    
    def get_all(self):
        return self.session.query(Task).all()
    
    def get_by_user(self, id_user : int):
        return self.session.query(Task).filter_by(id_user=id_user).first()
    
    def get_by_id(self, id_task : int):
        return self.session.query(Task).filter_by(id=id_task).first()
    
    def update(self, task : Task):
        task_update = self.session.merge(task)
        self.commit()
        if task_update:
            return task_update
        return False

    def delete(self, task : Task):
        self.session.delete(task)
        return self.commit()
    
        
    
