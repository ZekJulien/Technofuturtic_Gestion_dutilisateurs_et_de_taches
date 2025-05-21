# database
from database import Db
# services
from services import UserService

class App:
    """
    Main class for the application.
    
    This class initializes and manages the application's core components.
    """
    def __init__(self):
        self._user_service: UserService = None
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

    def _testing(self) -> None:
        """
        Create sample users for testing
        """
        self._user_service.add("ZekJulien", "julien@paquet.se", "mdp", None)
        self._user_service.add("Tekess", "quentin@gmail.com", "mdp", False)
        users = self._user_service.get_all()
        print([user.__dict__ for user in users])
        self._user_service.delete(users[1].id)
        users = self._user_service.get_all()
        print([user.__dict__ for user in users])
        print(self._user_service.get_by_email("julien@paquet.se").__dict__)
        print(self._user_service.update(users[0].id, username="JulienZek").__dict__)



def main():
    try:
        App()
    except Exception as e:
        print(f"Application failed to start: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
