from repositories import TaskRepository
from models import Task, User

class TaskService:
    def __init__(self):
        self._task_repository : TaskRepository = TaskRepository()
    
    def add(self, description : str, user : User):
        new_task = Task(description=description, user=user)
        if self._task_repository.add(new_task):
            print(f"🔤 The task {new_task.description} has been added in database. ✅")
    
    def get_all(self) -> list[Task]:
        tasks = self._task_repository.get_all()
        if tasks:
            return tasks
        print(f"🔤 No task(s) 🛑")

    def get_by_user(self, id_user : int) -> User:
        task = self._task_repository.get_by_user(id_user=id_user)
        if task:
            return task
        print(f"🔤 No task(s) 🛑")

    def update(self, id_task : int, description : str = None, user : User = None) -> Task:
        task = self._task_repository.get_by_id(id_task)
        if task is None:
            print(f"🔤 The task with this id : {id} doesn't exist. 🛑")
            return False
        update_task = Task(
            id=id_task,
            description = description if description is not None else task.description,
            user = user if user is not None else task.user
        )
        update_task = self._task_repository.update(update_task)
        if update_task:
            print(f"🔤 The task {update_task.description} has been updated in database. ✅")
            return update_task
        return False
    
    def delete(self, id_task : int):
        task = self._task_repository.get_by_id(id_task)
        if task:
            if self._task_repository.delete(task):
                print(f"🔤 The task {task.id} has been deletetd in database. ✅")
                return True
        print(f"🔤 The task with this id : {id} doesn't exist. 🛑")
