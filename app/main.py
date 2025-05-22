# database
from database import Db
# services
from services import UserService, TaskService

class App:
    """
    Main class for the application.
    
    This class initializes and manages the application's core components.
    """
    def __init__(self):
        self._user_service: UserService = None
        self._task_service: TaskService = None
        self._initialize_app()
        self._testing()

    def _initialize_app(self) -> None:
        """
        Initialize database connection and services
        """
        if not Db.is_connected():
            raise RuntimeError("Failed to connect to database")
        Db.create_tables()
        print("✅ Connection established")
        self._user_service = UserService()
        self._task_service = TaskService()

    def _testing(self) -> None:
        """
        Create sample users for testing
        """
        self._user_service.add("ZekJulien", "julien@gmail.se", "mdp", None)
        self._user_service.add("Tekess", "quentin@gmail.com", "mdp", False)
        users = self._user_service.get_all()
        print([user.__dict__ for user in users])
        self._user_service.delete(users[1].id)
        users = self._user_service.get_all()
        print([user.__dict__ for user in users])
        print(self._user_service.get_by_email("julien@gmail.se").__dict__)
        print(self._user_service.update(users[0].id, username="JulienZek").__dict__)
        self._task_service.add("Ceci est une description", users[0])
        print([task.description for task in self._user_service.get_by_email("julien@gmail.se").tasks])
        self._task_service.add("Ceci est une description 2", users[0])
        tasks = self._task_service.get_all()
        print([task.__dict__ for task in tasks])
        print(self._task_service.get_by_user(users[0].id).__dict__)
        print(self._task_service.update(id_task=tasks[1].id, description="Nouvelle description").__dict__)
        self._task_service.delete(tasks[1].id)




def main():
    try:
        App()
    except Exception as e:
        print(f"Application failed to start: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
